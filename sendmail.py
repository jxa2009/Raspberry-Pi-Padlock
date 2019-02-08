import smtplib

MY_ADDRESS = 'Enter email here'
password = 'enter password here'

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(MY_ADDRESS,password)
    msg = "The passcode was entered successfully"
    server.sendmail(MY_ADDRESS,MY_ADDRESS,msg)
    server.quit()