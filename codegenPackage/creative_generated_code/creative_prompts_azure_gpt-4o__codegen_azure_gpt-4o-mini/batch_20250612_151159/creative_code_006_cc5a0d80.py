"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogem.life
Prompt: Generate code using the `boto3` library to check the configuration of an AWS-hosted website and ensure it is properly set up.
Generated: DETERMINISTIC_cc5a0d8087ff62b9
Batch ID: 20250612_151159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import boto3
import botocore

def check_website_configuration(bucket_name):
    """
    Check the configuration of an AWS-hosted website on S3.

    Parameters:
    bucket_name (str): The name of the S3 bucket hosting the website.

    Returns:
    dict: A dictionary containing the website configuration and any errors encountered.
    """
    s3 = boto3.client('s3')
    result = {
        'bucket_name': bucket_name,
        'website_configuration': None,
        'error': None
    }

    try:
        # Attempt to retrieve the website configuration for the specified bucket
        response = s3.get_bucket_website(Bucket=bucket_name)
        result['website_configuration'] = response
    except botocore.exceptions.ClientError as e:
        # Handle errors, such as bucket not found or website not configured
        result['error'] = str(e)

    return result

if __name__ == "__main__":
    # Example usage
    bucket_name = 'your-s3-bucket-name'  # Replace with your actual bucket name
    config = check_website_configuration(bucket_name)

    if config['error']:
        print(f"Error checking configuration for bucket '{bucket_name}': {config['error']}")
    else:
        print(f"Website configuration for bucket '{bucket_name}': {config['website_configuration']}")
```
