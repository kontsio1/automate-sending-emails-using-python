import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Amazon SES SMTP credentials
SMTP_SERVER = "email-smtp.eu-west-2.amazonaws.com"  # Replace with the correct region (us-east-1 in this case)
SMTP_PORT = 587  # Use port 587 for TLS
SMTP_USERNAME = os.getenv("SES_SMTP_USERNAME")  # You can set your SES SMTP username here
SMTP_PASSWORD = os.getenv("SES_SMTP_PASSWORD")  # You can set your SES SMTP password here

# Sender and Receiver Email
SENDER_EMAIL = "kontsio18@gmail.com"  # Your verified email in SES
RECEIVER_EMAIL = "kontsio18@gmail.com"  # The email you're sending to

def send_email(subject, body):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to SES SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection using TLS
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
            print("Email sent successfully!")

    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    # Example of sending an email
    send_email(
        subject="Invoice Reminder",
        body="Hello, this is a reminder for your pending invoice payment."
    )
