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

# local development
if __name__ == "__main__":
    # Event can be anything you'd typically send in AWS Lambda, here it's just an empty dict
    mock_event = {}
    mock_context = {}

    # Call the lambda_handler function locally
    response = lambda_handler(mock_event, mock_context)
    print(response)  # Print the result to see the output