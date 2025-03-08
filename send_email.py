import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()
# SES SMTP credentials
SMTP_SERVER = os.getenv("SMTP_SERVER")  # SES SMTP server endpoint
SMTP_PORT = 587  # Port 587 for TLS
SMTP_USERNAME = os.getenv("SES_SMTP_USERNAME")  # SES SMTP username
SMTP_PASSWORD = os.getenv("SES_SMTP_PASSWORD")  # SES SMTP password
SENDER_EMAIL = os.getenv("SENDER_EMAIL")  # Replace with your verified email in SES

if not SMTP_USERNAME or not SMTP_PASSWORD:
    print("Error: SES_SMTP_USERNAME or SES_SMTP_PASSWORD not set correctly")
else:
    print("SES credentials loaded successfully")

class UserEmailDto:
    def __init__(self, email: str, name: str, subject: str):
        self.email = email  
        self.name = name,
        self.subject = subject

# Load the HTML template from an external file
def load_html_template()-> str:
    template_path = "automate-sending-emails-using-python\email_template.json"
    print(f"Looking for template at: {template_path}")
    try:
        with open(template_path, "r") as file:
            data = json.load(file)
            return data["html_template"]
    except FileNotFoundError:
        print(f"HTML template file not found at {template_path}")
        return ""

# List of recipients and details
users: list[UserEmailDto] = [
    UserEmailDto("kontsio18@gmail.com","Konstantinos","BEEP BEEP MAIL GIA TO MIKRO MOU CAPYBARA"),
    # UserEmailDto("katerina.ant20@gmail.com","Katerina","BEEP BEEP MAIL GIA TO MIKRO MOU CAPYBARA"),
]

def send_email_to_multiple_users(targetUsers: list[UserEmailDto]):
    html_template: str = load_html_template()

    for user in targetUsers:

        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = user.email
        msg['Subject'] = user.subject

        # Attach the HTML content
        msg.attach(MIMEText(html_template, 'html'))

        try:
            # Send the email
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.set_debuglevel(1)  # Enable debugging to see SMTP communication
                server.starttls()  # Start TLS encryption
                server.login(SMTP_USERNAME, SMTP_PASSWORD)  # Login with SES SMTP credentials
                server.sendmail(SENDER_EMAIL, user.email, msg.as_string())  # Send email
                print(f"Email sent to {user.email}")

        except Exception as e:
            print(f"Error sending email to {user.email}: {e}")

if __name__ == "__main__":
    send_email_to_multiple_users(users)
