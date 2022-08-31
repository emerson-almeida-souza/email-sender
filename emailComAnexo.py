import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

email_origem = ""
email_destino = ""
   
mensagem = MIMEMultipart() 
mensagem['From'] = email_origem 
mensagem['To'] = email_destino 
mensagem['Subject'] = "Email com arquivo"
body = "<h1>Segue arquivo em anexo</h1>"
mensagem.attach(MIMEText(body, 'html')) 
filename = "image.png"
caminho = "C:\image.png"
attachment = open(caminho, "rb") 
p = MIMEBase('application', 'octet-stream') 
p.set_payload((attachment).read()) 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
mensagem.attach(p) 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
senha = ""
s.login(email_origem, senha) 
text = mensagem.as_string() 
s.sendmail(email_origem, email_destino, text) 
print("Email enviado")
s.quit() 