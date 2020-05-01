import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('ContentFile.html').read_text())
email = EmailMessage()

email['from'] = 'Gopal Sawant'
email['to'] = 'ggopalsawant@mail.com'
email['subject'] = 'Multiple user email'
email.set_content(html.substitute({'name': 'Gopal'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port='587') as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("ggopalsawant@gmail.com", 'Gmail@24')
    smtp.send_message(email)
    print('email sent!!!!')
