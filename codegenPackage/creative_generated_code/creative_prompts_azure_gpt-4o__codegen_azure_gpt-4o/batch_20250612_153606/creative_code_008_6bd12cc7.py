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
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

class AWSCloudCreditsManager:
    """
    A class to manage AWS cloud credits allocation for Web3 startups.
    This script uses AWS SDK (boto3) to create and manage AWS resource credits.
    """

    def __init__(self, aws_access_key, aws_secret_key, region_name="us-east-1"):
        """
        Initialize the AWSCloudCreditsManager with provided credentials.
        
        :param aws_access_key: AWS access key ID
        :param aws_secret_key: AWS secret access key
        :param region_name: AWS region to operate in, default is 'us-east-1'
        """
        try:
            self.session = boto3.Session(
                aws_access_key_id=aws_access_key,
                aws_secret_access_key=aws_secret_key,
                region_name=region_name
            )
            self.billing_client = self.session.client('billing')
            self.iam_client = self.session.client('iam')
        except (NoCredentialsError, PartialCredentialsError) as e:
            raise ValueError("Error initializing AWS session: Invalid credentials provided.") from e
        except Exception as e:
            raise RuntimeError("Error initializing AWS session.") from e

    def allocate_cloud_credits(self, startup_name, credits_amount):
        """
        Allocate cloud credits to a Web3 startup.
        
        :param startup_name: Name of the Web3 startup
        :param credits_amount: Amount of cloud credits to allocate
        :return: Confirmation message
        """
        if credits_amount <= 0:
            raise ValueError("Credits amount must be greater than zero.")
        
        # For demonstration purposes, we simulate an allocation process.
        # In reality, AWS credits allocation happens outside of boto3 API and involves agreements with AWS.
        try:
            # Simulate allocation logic
            print(f"Allocating €{credits_amount} in cloud credits to the startup '{startup_name}'.")
            
            # Log the allocation details (In production, this would involve storing details in a database.)
            allocation_details = {
                "StartupName": startup_name,
                "CreditsAmount": credits_amount,
                "Status": "Success"
            }
            # Return a success message
            return f"Successfully allocated €{credits_amount} in cloud credits to '{startup_name}'."
        except Exception as e:
            # Handle generic errors
            raise RuntimeError("Failed to allocate cloud credits.") from e

    def list_iam_users(self):
        """
        List IAM users associated with the account.
        
        :return: List of IAM users
        """
        try:
            response = self.iam_client.list_users()
            users = response.get('Users', [])
            return [user['UserName'] for user in users]
        except Exception as e:
            raise RuntimeError("Failed to list IAM users.") from e


if __name__ == "__main__":
    # Replace with your actual AWS credentials
    AWS_ACCESS_KEY = "your_aws_access_key"
    AWS_SECRET_KEY = "your_aws_secret_key"
    
    try:
        # Initialize the manager
        aws_manager = AWSCloudCreditsManager(AWS_ACCESS_KEY, AWS_SECRET_KEY)

        # Allocate cloud credits to a Web3 startup
        startup_name = "Web3Innovators"
        credits_amount = 25000
        allocation_result = aws_manager.allocate_cloud_credits(startup_name, credits_amount)
        print(allocation_result)

        # List IAM users
        iam_users = aws_manager.list_iam_users()
        print("IAM Users in your account:", iam_users)
    except ValueError as ve:
        print(f"Validation Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
