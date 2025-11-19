"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptogifts.s3.us-east-2.amazonaws.com
Prompt: Explain how to troubleshoot S3 bucket access issues related to endpoint misconfigurations, using the cryptogifts example.
Generated: DETERMINISTIC_ce2439d6560a533a
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
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, EndpointConnectionError, ClientError

def troubleshoot_s3_access(bucket_name: str, endpoint_url: str = None):
    """
    Troubleshoot S3 bucket access issues related to endpoint misconfigurations.

    :param bucket_name: Name of the S3 bucket to test access to.
    :param endpoint_url: Custom S3 endpoint URL (optional), often used for non-standard regions or S3-compatible services.
    """
    try:
        # Initialize the S3 client with optional custom endpoint URL
        s3_client = boto3.client('s3', endpoint_url=endpoint_url) if endpoint_url else boto3.client('s3')

        # Test bucket connectivity by listing objects
        print(f"Testing access to bucket '{bucket_name}'...")
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        
        # If the response contains 'Contents', bucket access is confirmed
        if 'Contents' in response:
            print(f"Bucket '{bucket_name}' is accessible. Objects:")
            for obj in response['Contents']:
                print(f" - {obj['Key']}")
        else:
            print(f"Bucket '{bucket_name}' is accessible, but it is empty.")

    except NoCredentialsError:
        # Handle missing AWS credentials
        print("Error: No AWS credentials found. Please configure your credentials.")
    except PartialCredentialsError:
        # Handle incomplete credentials (e.g., missing access/secret keys)
        print("Error: Incomplete AWS credentials. Please check your configuration.")
    except EndpointConnectionError:
        # Handle incorrect or unreachable endpoint URL
        print(f"Error: Unable to connect to the endpoint '{endpoint_url}'. Please verify the URL.")
    except ClientError as e:
        # Handle other client errors (e.g., bucket not found, permission issues)
        error_code = e.response['Error']['Code']
        if error_code == 'NoSuchBucket':
            print(f"Error: The bucket '{bucket_name}' does not exist.")
        elif error_code == 'AccessDenied':
            print(f"Error: Access denied to bucket '{bucket_name}'. Please check your permissions.")
        else:
            print(f"Client error occurred: {e.response['Error']['Message']}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    # Example usage for troubleshooting S3 bucket access
    bucket_name = "cryptogifts-example-bucket"  # Replace with your bucket name
    endpoint_url = None  # Replace with an endpoint URL if using a custom S3-compatible service
    troubleshoot_s3_access(bucket_name, endpoint_url)
```
