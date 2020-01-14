from email.mime.multipart import MIMEMultipart
from email.mime.text      import MIMEText
import smtplib

from config import email, password


class EmailModule:

    def __init__(self,_email="",_password=""):
        self.session = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        
        if _email == "" or _password == "":
            self.email = email
            self.session.login(email, password)
        else:
            self.email = _email
            self.session.login(_email,_password)

    def send_email(self,to,sub,body,is_mime=False):
        # Try to send the email, if not return false and the failed email
        try:
            msg = MIMEMultipart()

            msg["From"] = self.email
            if sub:
                msg["Subject"] = sub
            msg["To"] = to
            
            # is_mime means a MIMEText wa ssupplied instead of a string
            if not is_mime:
                msg.attach(MIMEText(body,plain))
            else:
                msg.attach(body)

            session.send_message(msg)
            return (True, to)
        except:
            return (False, to)

    def send_emails(self, emails):
        vals = [self.send_email(**em) for em in emails]
        return vals
    
    def quit(self):
        self.session.quit()
