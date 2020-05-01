import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from']= 'ggopalsawant@gmail.com'
email['to']= "sawantvaishali646@gmail.com"
email['subject']= 'New email using Python'

email.set_content("Learning python")

with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("ggopalsawant@gmail.com", "Gmail@24")
    smtp.send_message(email)
    print("email sent !!!!")
