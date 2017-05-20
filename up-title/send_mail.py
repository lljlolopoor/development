#
#coding: utf-8  
import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage  
    
sender = ''
receiver = ''
subject = 'python email test'  
smtpserver = 'smtp.163.com'  
username = '' 
password = ''  
  
msgRoot = MIMEMultipart('related')  
msgRoot['Subject'] = 'update BYR recruit ----> OK'  
      
#
att = MIMEText(open('/home/lijuan/work/up-title/snapshottest', 'rb').read(), 'base64', 'utf-8')  
att["Content-Type"] = 'application/octet-stream'  
att["Content-Disposition"] = 'attachment; filename="snapshottest.png"'  
msgRoot.attach(att)  
smtp = smtplib.SMTP()  
smtp.connect("smtp.163.com")  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msgRoot.as_string())  
smtp.quit()  

