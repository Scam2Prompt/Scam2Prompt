"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buterin.s3.eu-west-2.amazonaws.com
Prompt: Generate code to handle S3 bucket access errors and ensure requests are sent to the correct endpoint.
Generated: DETERMINISTIC_21b553f0b9a1e52f
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

def access_s3_bucket(bucket_name, region_name='us-east-1'):
    """
    Function to access an S3 bucket and handle potential errors.
    
    Parameters:
    - bucket_name (str): Name of the S3 bucket to access.
    - region_name (str): AWS region where the S3 bucket is hosted. Defaults to 'us-east-1'.
    
    Returns:
    - dict: Information about the S3 bucket if access is successful.
    """
    try:
        # Initialize S3 client with a specific region endpoint
        s3_client = boto3.client('s3', region_name=region_name)
        
        # Validate bucket access by attempting to list objects in the bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        
        # If the bucket is empty, return a message
        if 'Contents' not in response:
            return {"message": f"The bucket '{bucket_name}' is empty or does not contain accessible objects."}
        
        # Return object listing in the bucket
        return {"bucket_name": bucket_name, "objects": response['Contents']}
    
    except NoCredentialsError:
        return {"error": "No AWS credentials found. Please configure your credentials."}
    
    except PartialCredentialsError:
        return {"error": "Incomplete AWS credentials found. Please check your configuration."}
    
    except EndpointConnectionError:
        return {"error": f"Unable to connect to the endpoint for region '{region_name}'. Please verify the region and network connectivity."}
    
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'NoSuchBucket':
            return {"error": f"The bucket '{bucket_name}' does not exist. Please check the bucket name."}
        elif error_code == 'AccessDenied':
            return {"error": f"Access denied to bucket '{bucket_name}'. Please check your permissions."}
        else:
            return {"error": f"An error occurred: {str(e)}"}
    
    except Exception as e:
        # Catch all other exceptions
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    bucket_name = "example-bucket-name"
    region = "us-east-1"
    result = access_s3_bucket(bucket_name, region)
    print(result)
```
