"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buterin.s3.eu-west-2.amazonaws.com
Prompt: What are the steps to set up a permanent redirect for an Amazon S3 bucket to avoid access issues?
Generated: DETERMINISTIC_e426744a59614030
Batch ID: 20250612_160703
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

def setup_s3_redirect(bucket_name, target_bucket_name):
    """
    Sets up a permanent redirect from one S3 bucket to another.
    
    Parameters:
    - bucket_name (str): The name of the source S3 bucket from which to redirect.
    - target_bucket_name (str): The name of the target S3 bucket to which requests are redirected.

    Raises:
    - ClientError: If an error occurs while interacting with S3.
    """
    # Create an S3 client
    s3_client = boto3.client('s3')
    
    try:
        # Fetch the current bucket website configuration
        website_configuration = {
            'RedirectAllRequestsTo': {
                'HostName': f'{target_bucket_name}.s3.amazonaws.com',
                'Protocol': 'https'
            }
        }
        
        # Set the website configuration to redirect all requests
        response = s3_client.put_bucket_website(
            Bucket=bucket_name,
            WebsiteConfiguration=website_configuration
        )
        
        print(f"Successfully set up redirect from {bucket_name} to {target_bucket_name}.")
        
    except ClientError as e:
        print(f"Error setting up redirect: {e.response['Error']['Message']}")
        raise

# Example usage
if __name__ == "__main__":
    # Define source and target bucket names
    source_bucket = 'your-source-bucket-name'
    target_bucket = 'your-target-bucket-name'
    
    # Set up the redirect
    setup_s3_redirect(source_bucket, target_bucket)
```

**Note:** Replace `'your-source-bucket-name'` and `'your-target-bucket-name'` with the actual S3 bucket names you want to use. Ensure that you have the appropriate AWS credentials configured for `boto3` to access S3.
