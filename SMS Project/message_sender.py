from distutils.sysconfig import get_config_h_filename
import email, smtplib, ssl
from providers import PROVIDERS


def send_sms_via_email(
    number: str,
    message: str,
    provider: str,
    sender_cred: tuple,
    subject: str = " Sent using python",
    smtp_server: str = "smtp.gmail.com",
    smpt_port: int = 465,
):
    sender_email, email_password = sender_cred
    sms = PROVIDERS.get(provider).get("sms")
    receiver_email = f"{number}@{sms}"
    
    email_message = f"Subject: {subject}\nTo: {receiver_email}\n{message}"
    
    with smtplib.SMTP_SSL(smtp_server, smpt_port, context=ssl.create_default_context()) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, email_message)

def main():
    number = "4045796624" #henok
    #number = "2039792084"
    #number = "2039793574" - drew
    message = " Yeooo - Tejas via python"
    #provider = "AT&T"
    provider = "T-Mobile"
    sender_cred = ("tejasvermani@gmail.com", "hgjvzhdnutcocuri")
    send_sms_via_email(number, message, provider, sender_cred)
    
if __name__ == "__main__":
    main()