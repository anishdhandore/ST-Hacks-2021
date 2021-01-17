from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import RegisterForm
import bs4, requests
from .keys import *
from .models import Help
from django.contrib import messages
from .api import *
import smtplib
import wolframalpha

# Create your views here.
def home(request):
    if request.user.is_anonymous:
        return redirect('/accounts/login/')
    return render(request, 'home.html')

def search(request):
    if request.user.is_anonymous:
        return redirect('/accounts/login/')
    elif request.method=="POST":
        breed = request.POST.get('breed')

        # web scraper for collecting the names of all breeds of dogs
        url = "https://dogtime.com/dog-breeds/profiles"
        req = requests.get(url)
        soup = bs4.BeautifulSoup(req.text, "lxml")
        data = soup.select(".list-item-title")

        all_breeds= []
        for item in data:
            all_breeds.append(item.text)

        # checking if the entered breed is in the list
        if breed in all_breeds:
            sm = breed.lower()
            formatted_breed1 = sm.replace(" ", "-")
            breed_url = f"https://dogtime.com/dog-breeds/{formatted_breed1}"
            breed_info = requests.get(breed_url)
            breed_soup = bs4.BeautifulSoup(breed_info.text, "lxml")
            newsoup= breed_soup.select(".breeds-single-intro p")

            # storing general information on breed in a variable string
            backg_info = ""
            for x in newsoup:
                backg_info += x.text
            
            # storing the image url of each breed 
            img_soup = breed_soup.select(".breeds-single-intro img")[0]
            img_url = img_soup.attrs['src']
            print(img_url)

            # wikipedia info for each breed
            formatted_breed2 = breed.replace(" ", "_")
            req2 = requests.get(f"https://en.wikipedia.org/wiki/{formatted_breed2}")
            soup2 = bs4.BeautifulSoup(req2.text, "lxml")
            newsoup2 = soup2.select("p")[1]

            # facts about breeds
            newsoup3 = breed_soup.select(".breed-data-item-content ul li")[0]
            newsoup4 = breed_soup.select(".breed-data-item-content ul li")[1]

            # data from wolfram api
            #inp = input("Question: ")
            app_id = "THLPVT-K87YAXLUWE"
            client = wolframalpha.Client(app_id)

            res = client.query(breed)
            answer = next(res.results)
            image2 = answer['subpod']['img']['@src']

            params = {'image1': img_url,
                    'image2': image2,
                    'breed': breed,
                    'backg_info': backg_info,
                    'wiki_info': newsoup2.text,
                    'fact1': newsoup3.text,
                    'fact2': newsoup4.text,
                    'statement1': 'Background Information:',
                    'statement2': 'More about the breed...'}
            return render(request, 'search.html', params)

        else:
            params = {'alert': 'HINT: Oops not a breed! Try writing the complete name'}
            return render(request, 'search.html', params)
    return render(request, 'search.html')

def adopt(request):
    if request.user.is_anonymous:
        return redirect('/accounts/login/')

    # if form is submitted
    elif request.method == "POST":
        user_city = request.POST.get('city')
        user_state = request.POST.get('state')
        distance = request.POST.get('distance')

        # checking if any of the field is submitted empty
        if user_city == "" or user_state=="" or distance=="":
            return redirect('/adopt/')

        # using the petfinder api to determine locations of nearby rescue and adoptions centers
        url = "https://api.petfinder.com/v2/organizations"
        headers = {'Authorization': f'Bearer {access_token}'}
        parameters = {'location': f'{user_city}, {user_state}', 'distance':distance, 'limit':10}
        req = requests.get(url, headers=headers, params=parameters)
        data = req.json()
        my_data = []
        
        for item in data["organizations"]:
            name = item["name"]
            city = item["address"]["city"]
            pincode = item["address"]["postcode"]
            email = item["email"]
            phone = item["phone"]
            photo = item["photos"]
            policy = item["adoption"]["policy"]
            url = item["url"]

            if photo != []:
                photo = item["photos"][0]["medium"]
            else:
                photo = "/static/images/no_image.jpg"

            required_data = {
                'name': name,
                'city': city,
                'pincode': pincode,
                'email': email,
                'phone': phone,
                'photo': photo,
                'policy': policy,
                'url': url
            }
            my_data.append(required_data)
        statement = "Results:"
        context = {"complete_data": my_data, "statement": statement}
        return render(request, 'adopt.html', context)

    return render(request, 'adopt.html')

def register(request):
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/accounts/login/")
    else:
        form = RegisterForm()

    params = {'form': form}
    return render(request, 'register.html', params)

def login(request):
    if request.method=="POST":
        return redirect("/")
    return render(request, 'login.html')

def logout(request):
    logout()
    return render(request, 'login.html')

def help(request):
    if request.user.is_anonymous:
        return redirect('/accounts/login/')

    elif request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        country = request.POST.get('country')
        zip = request.POST.get('zip')

        help = Help(
            firstname=firstname,
            lastname=lastname,
            email=email,
            country=country,
            zip=zip
        )
        help.save()
        

        # now connecting this data with api.py
        for i in range(len(api)):
            if api[i]['country']==country:
                api_data = {
                    'address':api[i]['address'],
                    'phone1':api[i]['phone1'],
                    'phone2':api[i]['phone2'],
                    'email1':api[i]['email1'],
                    'email2':api[i]['email2'],
                }
                #return api_data

                # automated email sending from here

                with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.ehlo()

                    smtp.login(email_address, email_password)
                    
                    msg = f'''Subject: Emergency  help\n\n
                    
                    Address: {api_data['address']}\n
                    Call here: {api_data['phone1']}\n
                    Alternate phone: {api_data['phone2']}\n
                    Email: {api_data['email1']}\n
                    Alternate email: {api_data['email2']}\n
                    '''.encode('utf-8')
                    
                    smtp.sendmail(email_address, email, msg)

        messages.success(request, 'Thank you! Your message has been received, kindly check your gmail!')

            #return("Country not listed")
        

    return render(request, 'help.html')


