from text_gen import text_generation
import smtplib


mail_topic = input("Enter Your topic:" )

AI_response = text_generation(mail_topic)

server = smtplib.SMTP('SERVER URL', "PORT: int")
server.starttls()
server.login('YOUR EMAIL', "YOUR APP PASSWORD") #GOOGLE HAS REMOVED THE PASSWORD AND EMAIL AUTH METHOD, INSTEAD YOU WILL USE EMAIL AND APP PASSWORD, (YOU'LL HAVE TO ENABLE 2SV ALSO!) 
server.sendmail( 'FROM', 'TO', AI_response.encode('utf-8'))
print("Email Sent...")
