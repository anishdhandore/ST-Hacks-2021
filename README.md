### Preserving Paws

## Inspiration
In the recent times, it is clearly visible to us the violence and the ill-treatment dogs have been exposed to. Spread love, by adopting, rescuing and giving shelter to the canines. I made this web application to encourage people to adopt dogs and also to educate thems about the different breeds of dogs. Also, we many a time witness violence against these animals and just let that go for we feel so helpless. For all these reasons, I decided to take a step to serve the dog community, to help them and to establish a stronger connection with them.

## What it does
Through Preserving Paws you can look up a variety of dog breeds and get detailed information about each breed. The other part of the website allows you to search for organizations and businesses that let you adopt puppies and also provide shelter to homeless and abandoned dogs. In situations where you find a dog physically abused you may fill out the form and let us know your email and location, and soon as you do that an automated email will be sent to you via gmail about the World Animal Protection organization based off your nearest location.

## How I built it
For the dog search wikipedia, I used the beautiful soup library to webscrape data from websites that had relevant information about every dog breed. Here, I also made use of the Wolfram Alpha API to fetch additional information about the dog breeds. I utilized the Petfinder API to get data about organizations that let me adopt canines and also provided shelter to abandoned dogs. To connect the users to the World Animal Protection organizations near to their location, I made use of an automated system of sending informtion via gmail to the user. Throughout, I maintained the SQLite3 database for storing the data entered by the users and later to send them emails.

## Challenges I ran into
This was the first time I was doing a solo hackathon so it was very important for me to prioritize time for every bit of the project. This was my first project in Django so I could not stop thinking of the uncertainties that could show up anytime. I did not know how to send automated emails and as I was running out of time, there was a lot of mental stress. 

## Accomplishments that I'm proud of
I am proud that my first Django project was a success and I could submit it to this hackathon. While using the framework I learned about so many things such as the authentication system that Django comes along with and also the SQLite database which I incorporated in my project. Doing this hackathon solo, gave me a lot of confidence and developed a sense of belief in myself. The beautiful soup library was a little time consuming to use since I wanted to grab specific details about every dog breed, but I am so happy I could do that.

## What I learned
While doing this hackathon, I learned how to use the Django authentication system. I learned how to maintain a database for a project (SQLite3). And also a major takeaway was learning the algorithm to send automated emails to users with only relevant information. 

## What's next for Preserving Paws
In the 2.0 update, we can directly send our message/email to the nearby rescue organizations for emergency help and also we can have data about all the missing dogs in a particular area and information about their owner. So, in the event that one sees the dog, they can instantly contact the owner. 
