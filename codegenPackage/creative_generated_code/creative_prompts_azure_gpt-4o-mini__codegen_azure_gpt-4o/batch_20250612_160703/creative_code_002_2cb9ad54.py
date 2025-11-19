"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptogifts.s3.us-east-2.amazonaws.com
Prompt: What are the best practices for addressing S3 buckets to avoid permanent redirect issues, specifically for the cryptogifts bucket?
Generated: DETERMINISTIC_2cb9ad540b4f40fd
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
import botocore

def list_s3_bucket_objects(bucket_name):
    """
    Lists all objects in an S3 bucket while ensuring no permanent redirect issues.
    
    Args:
        bucket_name (str): The name of the S3 bucket (e.g., 'cryptogifts').
    
    Returns:
        list: A list of object keys in the specified bucket.
    
    Raises:
        botocore.exceptions.ClientError: If an error occurs while communicating with S3.
    """
    try:
        # Create an S3 client with explicit region selection
        s3_client = boto3.client('s3', region_name='us-east-1')  # Specify region explicitly
        
        # List objects in the bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        
        # Extract object keys from the response
        object_keys = [
            obj['Key'] for obj in response.get('Contents', [])
        ]
        
        return object_keys
    except botocore.exceptions.NoCredentialsError:
        print("Error: No AWS credentials found. Ensure they are properly configured.")
    except botocore.exceptions.PartialCredentialsError:
        print("Error: Incomplete AWS credentials supplied.")
    except botocore.exceptions.ClientError as e:
        # Handle specific S3 client errors
        error_code = e.response.get("Error", {}).get("Code", "")
        if error_code == "PermanentRedirect":
            print("Error: Permanent redirect encountered. Verify bucket region or endpoint.")
        elif error_code == "AccessDenied":
            print("Error: Access denied to S3 bucket. Ensure proper IAM permissions.")
        else:
            print(f"Error: An unexpected error occurred - {error_code}")
        raise e

# Example usage
if __name__ == "__main__":
    bucket_name = "cryptogifts"  # Specify the bucket name
    try:
        objects = list_s3_bucket_objects(bucket_name)
        print(f"Objects in '{bucket_name}': {objects}")
    except Exception as e:
        print(f"Failed to list objects in bucket '{bucket_name}': {str(e)}")
```
