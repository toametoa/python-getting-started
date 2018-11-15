from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pickle





def sending(leadmail, body):  # mail sender function
    fromaddr = "openislam88@gmail.com"

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = leadmail
    msg['Subject'] = ""

    msg.attach(MIMEText(body, 'html'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "rosaria08")
    text = msg.as_string()
    server.sendmail(fromaddr, leadmail, text)
    server.quit()








# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    leadmail='shimul929@gmail.com'
    msg_1 = "helloooooooooooooooooo"
    sending(leadmail, msg_1)
    return render(request, "index.html")

    



def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


