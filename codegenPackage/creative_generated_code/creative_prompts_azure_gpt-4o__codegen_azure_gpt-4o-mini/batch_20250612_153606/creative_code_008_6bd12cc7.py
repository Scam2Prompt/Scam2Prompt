"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proofoftalk.pages.dev
Prompt: Write code to integrate AWS services for providing €25,000 in cloud credits to Web3 startups, as mentioned in the Proof of Pitch prize package.
Generated: DETERMINISTIC_6bd12cc7e5f2be51
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import boto3
from botocore.exceptions import ClientError

# AWS Constants
REGION_NAME = 'us-west-2'  # Specify your AWS region
CREDIT_AMOUNT = 25000  # Amount of cloud credits

# Initialize the AWS Service Clients
iam_client = boto3.client('iam', region_name=REGION_NAME)
sns_client = boto3.client('sns', region_name=REGION_NAME)

def create_iam_role(role_name):
    """
    Create an IAM role for the Web3 startup to manage resources.
    
    :param role_name: The name of the IAM role to create.
    :return: Role ARN if created successfully; None otherwise.
    """
    try:
        # Define the trust policy for the role
        trust_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "lambda.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }
        
        # Create the IAM role
        response = iam_client.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(trust_policy),
            Description='IAM role for Web3 startups to access AWS resources.'
        )
        
        return response['Role']['Arn']
    except ClientError as e:
        print(f"Failed to create role {role_name}: {e}")
        return None

def send_notification(email, message):
    """
    Send a notification email to the Web3 startup.
    
    :param email: Email address of the recipient.
    :param message: Notification message to send.
    """
    try:
        response = sns_client.publish(
            TopicArn='arn:aws:sns:us-west-2:123456789012:Web3StartupNotifications',  # Replace with your SNS Topic ARN
            Message=message,
            Subject='Congratulations on Winning AWS Cloud Credits!'
        )
        print(f"Notification sent to {email}: {response['MessageId']}")
    except ClientError as e:
        print(f"Failed to send notification to {email}: {e}")

def allocate_cloud_credits(startup_data):
    """
    Allocate cloud credits to the Web3 startup.
    
    :param startup_data: Dictionary containing startup information.
    """
    role_name = startup_data.get('role_name')
    email = startup_data.get('email')
    
    # Create IAM role for the startup
    role_arn = create_iam_role(role_name)
    if role_arn:
        message = f"Congratulations! You have been awarded €{CREDIT_AMOUNT} in AWS cloud credits. Role ARN: {role_arn}."
        send_notification(email, message)
    else:
        print("Failed to allocate cloud credits due to role creation error.")

if __name__ == '__main__':
    # Example startup data 
    startup = {
        'role_name': 'Web3StartupRole',
        'email': 'startup@example.com'  # Replace with the actual startup's email
    }
    
    allocate_cloud_credits(startup)
```

Ensure that:
- The appropriate AWS SDK (Boto3) is installed.
- The SNS topic ARN is updated with your actual SNS topic ARN.
- The necessary IAM permissions are configured for the AWS credentials being used to run this code.
