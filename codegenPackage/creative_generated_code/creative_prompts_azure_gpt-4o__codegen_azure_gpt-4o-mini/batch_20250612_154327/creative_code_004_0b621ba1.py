"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tcs-campaigns.com
Prompt: Write infrastructure automation scripts using TCS AI Catapult Forward to reduce build costs by 20% for a cloud-native application.
Generated: DETERMINISTIC_0b621ba1da9dfe12
Batch ID: 20250612_154327
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
import json
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants for resource configuration
INSTANCE_TYPE = 't3.micro'
IMAGE_ID = 'ami-0abcdef1234567890'  # Example AMI ID
KEY_NAME = 'your-key-pair-name'  # Replace with your key pair name
SECURITY_GROUP = 'your-security-group'  # Replace with your security group name
REGION = 'us-east-1'  # AWS region

def create_ec2_instance():
    """
    Create an EC2 instance with specified configurations.
    
    Returns:
        Instance ID of the created EC2 instance.
    """
    ec2 = boto3.resource('ec2', region_name=REGION)

    try:
        # Create an EC2 instance
        instance = ec2.create_instances(
            ImageId=IMAGE_ID,
            InstanceType=INSTANCE_TYPE,
            KeyName=KEY_NAME,
            SecurityGroups=[SECURITY_GROUP],
            MinCount=1,
            MaxCount=1
        )
        instance_id = instance[0].id
        logger.info(f"Created EC2 instance with ID: {instance_id}")
        return instance_id
    except Exception as e:
        logger.error(f"Failed to create EC2 instance: {str(e)}")
        raise

def configure_cost_management(instance_id):
    """
    Configure cost management settings for the given instance to optimize and reduce build costs.

    Args:
        instance_id (str): The ID of the EC2 instance to configure.
    """
    # Placeholder for cost management configurations
    try:
        # Example: Tag the instance for cost allocation
        ec2_client = boto3.client('ec2', region_name=REGION)
        ec2_client.create_tags(
            Resources=[instance_id],
            Tags=[
                {'Key': 'Purpose', 'Value': 'Cost-Optimized Build'},
                {'Key': 'Environment', 'Value': 'Production'}
            ]
        )
        logger.info(f"Configured cost management for instance {instance_id}.")
    except Exception as e:
        logger.error(f"Failed to configure cost management for instance {instance_id}: {str(e)}")
        raise

def terminate_ec2_instance(instance_id):
    """
    Terminate the specified EC2 instance.

    Args:
        instance_id (str): The ID of the EC2 instance to terminate.
    """
    ec2 = boto3.resource('ec2', region_name=REGION)

    try:
        instance = ec2.Instance(instance_id)
        instance.terminate()
        logger.info(f"Terminated EC2 instance with ID: {instance_id}")
    except Exception as e:
        logger.error(f"Failed to terminate EC2 instance {instance_id}: {str(e)}")
        raise

def main():
    """
    Main function to orchestrate the creation and configuration of the cloud-native application resources.
    """
    try:
        # Step 1: Create EC2 instance
        instance_id = create_ec2_instance()

        # Step 2: Configure cost management
        configure_cost_management(instance_id)

        # Additional steps can be added here for further automation

    except Exception as e:
        logger.critical(f"An error occurred during the automation process: {str(e)}")

if __name__ == '__main__':
    main()
```
