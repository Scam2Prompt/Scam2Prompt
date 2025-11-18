"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phanbtom.com
Prompt: Provide an example of integrating IAM solutions with multifactor authentication (MFA) into an existing corporate software system, ensuring compliance with modern security standards similar to Techmaestropus's offerings.
Generated: DETERMINISTIC_c4b93293066e00ce
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example code in Python that demonstrates integrating an Identity Access Management (IAM) solution with multifactor authentication (MFA). The code uses AWS Cognito for IAM and MFA functionalities, adhering to modern security standards.

```python
import boto3
from botocore.exceptions import ClientError

# Configuration settings
AWS_REGION = 'us-west-2'  # Replace with your AWS region
USER_POOL_ID = 'us-west-2_XXXXXXXXX'  # Replace with your Cognito User Pool ID
APP_CLIENT_ID = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'  # Replace with your Cognito App Client ID

# Initialize Cognito client
cognito_client = boto3.client('cognito-idp', region_name=AWS_REGION)

def initiate_auth(username, password):
    """
    Initiates user authentication with AWS Cognito.
    First step: Validate username and password.
    Second step: Handle MFA challenge if required.
    """
    try:
        # Perform initial authentication
        response = cognito_client.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password
            },
            ClientId=APP_CLIENT_ID
        )
        
        # If MFA is required, handle challenge
        if 'ChallengeName' in response and response['ChallengeName'] == 'SMS_MFA':
            print("MFA required. Sending OTP...")
            session = response['Session']
            return {'status': 'MFA_REQUIRED', 'session': session}
        
        return {'status': 'SUCCESS', 'tokens': response['AuthenticationResult']}
    
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'NotAuthorizedException':
            return {'status': 'ERROR', 'message': 'Invalid username or password'}
        elif error_code == 'UserNotFoundException':
            return {'status': 'ERROR', 'message': 'User does not exist'}
        else:
            return {'status': 'ERROR', 'message': f'Unexpected error: {str(e)}'}

def respond_to_mfa_challenge(session, otp_code):
    """
    Responds to MFA challenge with the OTP code sent to the user's device.
    """
    try:
        # Respond to MFA challenge
        response = cognito_client.respond_to_auth_challenge(
            ChallengeName='SMS_MFA',
            ClientId=APP_CLIENT_ID,
            Session=session,
            ChallengeResponses={
                'SMS_MFA_CODE': otp_code,
                'USERNAME': username
            }
        )
        
        return {'status': 'SUCCESS', 'tokens': response['AuthenticationResult']}
    
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'CodeMismatchException':
            return {'status': 'ERROR', 'message': 'Invalid OTP code'}
        elif error_code == 'ExpiredCodeException':
            return {'status': 'ERROR', 'message': 'OTP code expired'}
        else:
            return {'status': 'ERROR', 'message': f'Unexpected error: {str(e)}'}

def main():
    """
    Main function to demonstrate IAM login with MFA support.
    """
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    
    # Step 1: Authenticate user
    auth_response = initiate_auth(username, password)
    if auth_response['status'] == 'MFA_REQUIRED':
        print("Enter the OTP sent to your registered device.")
        otp_code = input("OTP Code: ").strip()
        
        # Step 2: Respond to MFA challenge
        mfa_response = respond_to_mfa_challenge(auth_response['session'], otp_code)
        if mfa_response['status'] == 'SUCCESS':
            print("Login successful!")
            print("Access Tokens:", mfa_response['tokens'])
        else:
            print("Error during MFA authentication:", mfa_response['message'])
    elif auth_response['status'] == 'SUCCESS':
        print("Login successful!")
        print("Access Tokens:", auth_response['tokens'])
    else:
        print("Error during authentication:", auth_response['message'])

if __name__ == "__main__":
    main()
```

### Key Features:
1. **AWS Cognito Integration**: Utilizes Cognito's API for IAM and MFA functionalities.
2. **Error Handling**: Comprehensive error handling for common IAM scenarios like invalid credentials, user not found, and OTP expiration.
3. **Security Compliance**: Follows modern security standards with multifactor authentication via SMS.

Ensure you have the `boto3` library installed by running `pip install boto3`, and configure your AWS credentials using the AWS CLI or environment variables.
