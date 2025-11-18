"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imts.com.pk
Prompt: Write Python code to set up a scalable cloud hosting solution using AWS, Azure, or Google Cloud, as described on the IMTS website. Include steps for security and performance optimization.
Generated: DETERMINISTIC_2af41d34a3bb88e0
Batch ID: 20250612_154344
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

# AWS Configuration
AWS_REGION = 'us-east-1'  # Choose the appropriate region
INSTANCE_TYPE = 't2.micro'  # Instance type for scaling
KEY_NAME = 'your-key-pair'  # Replace with your existing key pair name
SECURITY_GROUP_NAME = 'my-security-group'  # Replace with your security group name

def create_ec2_instance():
    """
    Create an EC2 instance in AWS.
    
    Returns:
        instance_id (str): The ID of the created EC2 instance.
    """
    ec2 = boto3.resource('ec2', region_name=AWS_REGION)

    try:
        # Create a new EC2 instance
        instance = ec2.create_instances(
            ImageId='ami-0c55b159cbfafe01e',  # Replace with a valid AMI ID
            MinCount=1,
            MaxCount=1,
            InstanceType=INSTANCE_TYPE,
            KeyName=KEY_NAME,
            SecurityGroups=[SECURITY_GROUP_NAME]
        )

        # Return the instance ID
        return instance[0].id

    except ClientError as e:
        print(f"Error creating EC2 instance: {e}")
        return None

def configure_security_group():
    """
    Configure the security group to allow specific traffic.
    """
    ec2 = boto3.client('ec2', region_name=AWS_REGION)

    try:
        # Create a security group
        response = ec2.create_security_group(GroupName=SECURITY_GROUP_NAME, Description='Security group for EC2 instances')
        security_group_id = response['GroupId']

        # Allow SSH traffic
        ec2.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 22,
                    'ToPort': 22,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]  # Allow SSH from anywhere (adjust for security)
                },
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 80,
                    'ToPort': 80,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]  # Allow HTTP from anywhere
                },
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 443,
                    'ToPort': 443,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]  # Allow HTTPS from anywhere
                }
            ]
        )

        print(f"Security group created with ID: {security_group_id}")

    except ClientError as e:
        print(f"Error configuring security group: {e}")

def main():
    """
    Main function to orchestrate the EC2 instance creation and security configuration.
    """
    configure_security_group()
    instance_id = create_ec2_instance()

    if instance_id:
        print(f"EC2 instance created with ID: {instance_id}")
    else:
        print("Failed to create EC2 instance.")

if __name__ == '__main__':
    main()
```

**Note:** Ensure that AWS SDK for Python (boto3) is installed and configured with your AWS credentials. Replace placeholder values with your own configuration. Adjust security group rules according to your organization’s security policy.
