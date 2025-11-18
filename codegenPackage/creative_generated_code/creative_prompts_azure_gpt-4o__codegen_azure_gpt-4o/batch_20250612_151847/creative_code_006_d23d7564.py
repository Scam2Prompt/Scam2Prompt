"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buterin.s3.eu-west-2.amazonaws.com
Prompt: Create a script in Python to check the region of an S3 bucket and update the endpoint configuration dynamically to avoid redirection errors.
Generated: DETERMINISTIC_d23d756419997ef5
Batch ID: 20250612_151847
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
import sys

def get_bucket_region(bucket_name):
    """
    Fetches the region of the specified S3 bucket using boto3.

    Args:
        bucket_name (str): The name of the S3 bucket.

    Returns:
        str: The AWS region of the bucket.

    Raises:
        botocore.exceptions.ClientError: If the bucket does not exist or access is denied.
    """
    try:
        # Create a client with default configurations
        s3_client = boto3.client('s3')
        
        # Get bucket location
        response = s3_client.get_bucket_location(Bucket=bucket_name)
        
        # Region is returned as None for us-east-1
        region = response.get('LocationConstraint', 'us-east-1')
        return region
    except botocore.exceptions.ClientError as e:
        print(f"Error fetching region for bucket '{bucket_name}': {str(e)}")
        sys.exit(1)

def configure_s3_client(bucket_name):
    """
    Configures and returns an S3 client set to the correct region for the specified bucket.

    Args:
        bucket_name (str): The name of the S3 bucket.

    Returns:
        boto3.client: An S3 client configured for the bucket's region.
    """
    try:
        # Get the bucket's region
        bucket_region = get_bucket_region(bucket_name)
        
        # Configure S3 client for the specific region
        s3_client = boto3.client('s3', region_name=bucket_region)
        print(f"S3 client configured for region: {bucket_region}")
        
        return s3_client
    except Exception as e:
        print(f"Error configuring S3 client: {str(e)}")
        sys.exit(1)

def main():
    """
    Main function to demonstrate region detection and dynamic S3 client configuration.

    Prompts the user for a bucket name, fetches its region, and configures the S3 client.
    """
    try:
        # Prompt user for S3 bucket name
        bucket_name = input("Enter the name of the S3 bucket: ").strip()
        
        if not bucket_name:
            print("Bucket name cannot be empty.")
            sys.exit(1)
        
        # Configure an S3 client dynamically based on bucket region
        s3_client = configure_s3_client(bucket_name)
        
        # Example: List objects in the bucket (ensure the bucket exists and is accessible)
        try:
            objects = s3_client.list_objects_v2(Bucket=bucket_name)
            print(f"Objects in bucket '{bucket_name}':")
            for obj in objects.get('Contents', []):
                print(f"- {obj['Key']}")
        except botocore.exceptions.ClientError as e:
            print(f"Error accessing bucket '{bucket_name}': {str(e)}")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\nScript interrupted by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
```
