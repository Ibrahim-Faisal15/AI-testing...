from text_gen import text_generation
import smtplib


mail_topic = input("Enter Your topic:" )

AI_response = text_generation(mail_topic)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('bhattikids82@gmail.com', 'yoow fcuk nuli tbgr')
server.sendmail( 'bhattikids82@gmail.com', 'hyibrahimfaisal@gmail.com', AI_response.encode('utf-8'))
print("Email Sent...")