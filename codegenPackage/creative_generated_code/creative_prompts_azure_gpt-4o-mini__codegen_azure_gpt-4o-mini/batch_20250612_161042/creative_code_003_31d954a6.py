"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sollfare.com
Prompt: Provide an example of how to set up access monitoring tools in a cloud environment to track user activity, based on Techmaestropus guidelines.
Generated: DETERMINISTIC_31d954a6c99e5844
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import boto3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for AWS configuration
AWS_REGION = 'us-west-2'  # Change to your desired region
CLOUD_TRAIL_NAME = 'UserActivityTrail'
S3_BUCKET_NAME = 'your-s3-bucket-for-logs'  # Change to your S3 bucket name

def create_cloud_trail():
    """
    Create an AWS CloudTrail to monitor user activity in the specified region.
    """
    try:
        cloudtrail_client = boto3.client('cloudtrail', region_name=AWS_REGION)
        
        # Create CloudTrail
        response = cloudtrail_client.create_trail(
            Name=CLOUD_TRAIL_NAME,
            S3BucketName=S3_BUCKET_NAME,
            IsMultiRegionTrail=True,
            EnableLogFileValidation=True,
            IncludeGlobalServiceEvents=True
        )
        logging.info(f"CloudTrail created: {response['TrailARN']}")
    except Exception as e:
        logging.error(f"Failed to create CloudTrail: {e}")
        raise

def start_logging():
    """
    Start logging for the created CloudTrail.
    """
    try:
        cloudtrail_client = boto3.client('cloudtrail', region_name=AWS_REGION)
        
        # Start logging
        response = cloudtrail_client.start_logging(Name=CLOUD_TRAIL_NAME)
        logging.info("Logging started successfully.")
    except Exception as e:
        logging.error(f"Failed to start logging: {e}")
        raise

def main():
    """
    Main function to set up access monitoring tools in a cloud environment.
    """
    try:
        create_cloud_trail()
        start_logging()
        logging.info("Access monitoring setup completed successfully.")
    except Exception as e:
        logging.critical(f"An error occurred during setup: {e}")

if __name__ == "__main__":
    main()
```
