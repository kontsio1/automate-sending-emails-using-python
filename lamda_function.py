import json
from send_email import UserEmailDto, send_email_to_multiple_users

# Lambda Handler (entry point for the Lambda function)
def lambda_handler(event, context):
    users = [
        UserEmailDto("kontsio18@gmail.com", "Konstantinos", "BEEP BEEP MAIL GIA TO MIKRO MOU CAPYBARA"),
    ]
    send_email_to_multiple_users(users)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Emails sent successfully!')
    }