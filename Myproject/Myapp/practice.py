api_key = "VHp4zUhut7FMZhacKfRH9nItMRtR3hrOwkw1UEsJGsKwLA836O"
secret = "YHT9k21iMKy06gKVfrHvi2a4SQUqDaiNkV2K5uSu"
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJWSHA0elVodXQ3Rk1aaGFjS2ZSSDluSXRNUnRSM2hyT3drdzFVRXNKR3NLd0xBODM2TyIsImp0aSI6IjY1ZDRkMGU2NjA3ZjhlOWUzOGI1N2ExMGUzZDZkYjgxZGY2NTgxZjE4NzJjY2VhZDUzYzM5NDMwNzBmZWE4Mjc5NTA5MzQ4YjEwZWI1ZTQzIiwiaWF0IjoxNjEwMjkyNjIzLCJuYmYiOjE2MTAyOTI2MjMsImV4cCI6MTYxMDI5NjIyMywic3ViIjoiIiwic2NvcGVzIjpbXX0.sKNJab4nQqWu2Bzsuk4SC2fUAHjU2dIigpskbCufz-E0aH29iseYSG8nR2zwtKSrp9bBIOQP3ldOTomWtdhKX4_2C7sNSMUEgHQyOah1iYkSOKtfsjn1JxcBsk6dBjV07EOWIlC0Nm0PNDRiIpaRL5cRHFN2Rdu9R26gPSYDUHAOd7s8XXRyhTDih5VtowkFSygOgMk_9i-Re3ae2sbhHOOpnb8JXkIeesyeh4Tk1KpoJovIZC2Ab2oPQTL4RsXoFcK7HTFKyPSFBIP66ulJ4fnPcAXG1R0cev1bHH61-aGEXkF-Zzm7VBF-njiEOAXV32sKg45kMgr-bqEqnQrWtA"

#curl -d "grant_type=client_credentials&client_id=VHp4zUhut7FMZhacKfRH9nItMRtR3hrOwkw1UEsJGsKwLA836O&client_secret=YHT9k21iMKy06gKVfrHvi2a4SQUqDaiNkV2K5uSu" https://api.petfinder.com/v2/oauth2/token

import smtplib
import os

EMAIL_ADDRESS="anish.dhandore@gmail.com"
EMAIL_PASSWORD = "****"

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = "Test Email"
    body = "Hi! This is a test email bro"
    
    msg = f"Subject: {subject}\n\n{body}"
    
    smtp.sendmail(EMAIL_ADDRESS, 'anish.dhandore@gmail.com', msg)




