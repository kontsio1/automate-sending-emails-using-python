import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# SES SMTP credentials
SMTP_SERVER = "email-smtp.eu-west-2.amazonaws.com"  # SES SMTP server endpoint
SMTP_PORT = 587  # Port 587 for TLS
SMTP_USERNAME = os.getenv("SES_SMTP_USERNAME")  # SES SMTP username
SMTP_PASSWORD = os.getenv("SES_SMTP_PASSWORD")  # SES SMTP password

SENDER_EMAIL = "kontsio18@gmail.com"  # Replace with your verified email in SES

# Load the HTML template from an external file
def load_html_template():
    template_path = "automate-sending-emails-using-python\email_template.json"
    print(f"Looking for template at: {template_path}")
    try:
        with open(template_path, "r") as file:
            data = json.load(file)
            return data["html_template"]
    except FileNotFoundError:
        print(f"HTML template file not found at {template_path}")
        return None

# List of recipients and their dynamic details
users = [
    {"email": "kontsio18@gmail.com", "name": "Konstantinos"},
    {"email": "katerina.ant20@gmail.com", "name": "Katerina"},
]

def send_email_to_multiple_users():
    html_template = load_html_template() 
    if html_template is None:
        return 

    for user in users:
        template_data = html_template

        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = user["email"]
        msg['Subject'] = f"BEEP BEEP MAIL GIA TO MIKRO MOU CAPYBARA"

        # Attach the HTML content
        msg.attach(MIMEText(template_data, 'html'))

        try:
            # Send the email
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.set_debuglevel(1)  # Enable debugging to see SMTP communication
                server.starttls()  # Start TLS encryption
                server.login(SMTP_USERNAME, SMTP_PASSWORD)  # Login with SES SMTP credentials
                server.sendmail(SENDER_EMAIL, user["email"], msg.as_string())  # Send email
                print(f"Email sent to {user['email']}")

        except Exception as e:
            print(f"Error sending email to {user['email']}: {e}")

if __name__ == "__main__":
    send_email_to_multiple_users()
