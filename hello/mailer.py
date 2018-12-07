
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from hello.models import profile
import time




def sending(currentuser,leadmail, body):
    uconfig = profile.objects.get(User=currentuser).uconfig
    smtp=uconfig['smtp']
    port=uconfig['port']
    emaill=uconfig['emaill']
    passs=uconfig['pass']


    msg = MIMEMultipart()

    msg['From'] = emaill
    msg['To'] = leadmail
    msg['Subject'] = ""

    msg.attach(MIMEText(body, 'html'))

    server = smtplib.SMTP(smtp, port)
    server.starttls()
    server.login(emaill, passs)
    text = msg.as_string()
    server.sendmail(emaill, leadmail, text)
    print('sent')
    print(smtp)
    print(port)
    print(emaill)
    print(passs)
    server.quit()




def startmailer(currentuser):
    while int(currentuser.profile.city) > 0:
        print(int(currentuser.profile.city))
        time.sleep(60)
        sending(currentuser,'shimul929@gmail.com', 'hii')



        if int(currentuser.profile.city) == 0:
            print('loop broke')
            break

    






# def sending2(leadmail, body):  # mail sender function
#     fromaddr = "openislam88@gmail.com"

#     msg = MIMEMultipart()

#     msg['From'] = fromaddr
#     msg['To'] = leadmail
#     msg['Subject'] = ""

#     msg.attach(MIMEText(body, 'html'))

#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(fromaddr, "rosaria08")
#     text = msg.as_string()
#     server.sendmail(fromaddr, leadmail, text)
#     server.quit()

