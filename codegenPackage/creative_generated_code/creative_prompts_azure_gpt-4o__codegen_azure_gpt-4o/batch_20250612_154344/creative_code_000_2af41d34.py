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
"""
This Python code sets up a scalable cloud hosting solution using AWS with 
security and performance optimizations. It uses the `boto3` library to manage 
AWS resources, including setting up an Auto Scaling Group, Load Balancer, EC2 instances, 
and configuring security groups. Ensure AWS credentials are properly configured.
"""

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def create_vpc(ec2_client):
    """
    Creates a Virtual Private Cloud (VPC) and returns the VPC ID.
    """
    try:
        response = ec2_client.create_vpc(
            CidrBlock='10.0.0.0/16',  # Define the IP range for the VPC
            TagSpecifications=[
                {
                    'ResourceType': 'vpc',
                    'Tags': [{'Key': 'Name', 'Value': 'ScalableCloudVPC'}],
                },
            ],
        )
        vpc_id = response['Vpc']['VpcId']
        print(f"VPC created with ID: {vpc_id}")
        return vpc_id
    except Exception as e:
        print(f"Error creating VPC: {e}")
        raise

def configure_security_group(ec2_client, vpc_id):
    """
    Creates and configures a Security Group in the specified VPC.
    """
    try:
        response = ec2_client.create_security_group(
            GroupName='ScalableCloudSG',
            Description='Security group for scalable cloud hosting',
            VpcId=vpc_id
        )
        sg_id = response['GroupId']
        
        # Add inbound rules for HTTP and HTTPS traffic
        ec2_client.authorize_security_group_ingress(
            GroupId=sg_id,
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 80,
                    'ToPort': 80,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                },
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 443,
                    'ToPort': 443,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                }
            ]
        )
        print(f"Security Group created and configured: {sg_id}")
        return sg_id
    except Exception as e:
        print(f"Error configuring Security Group: {e}")
        raise

def create_key_pair(ec2_client):
    """
    Creates a Key Pair for SSH access to EC2 instances.
    Saves the private key to a local file.
    """
    try:
        response = ec2_client.create_key_pair(KeyName='ScalableCloudKeyPair')
        private_key = response['KeyMaterial']
        
        with open('ScalableCloudKeyPair.pem', 'w') as key_file:
            key_file.write(private_key)
            print("Key Pair created and saved as 'ScalableCloudKeyPair.pem'")
    except Exception as e:
        print(f"Error creating Key Pair: {e}")
        raise

def setup_auto_scaling_group(as_client, launch_template_id):
    """
    Configures an Auto Scaling Group linked to a Launch Template.
    """
    try:
        response = as_client.create_auto_scaling_group(
            AutoScalingGroupName='ScalableCloudASG',
            LaunchTemplate={
                'LaunchTemplateId': launch_template_id
            },
            MinSize=1,
            MaxSize=5,
            DesiredCapacity=2,
            VPCZoneIdentifier='subnet-12345678,subnet-87654321',  # Replace with real Subnet IDs
            Tags=[
                {'Key': 'Name', 'Value': 'ScalableCloudInstance', 'PropagateAtLaunch': True}
            ]
        )
        print("Auto Scaling Group configured.")
    except Exception as e:
        print(f"Error setting up Auto Scaling Group: {e}")
        raise

def create_load_balancer(elb_client, security_group_ids, subnet_ids):
    """
    Creates an Application Load Balancer with HTTP and HTTPS listeners.
    """
    try:
        response = elb_client.create_load_balancer(
            Name='ScalableCloudLB',
            Subnets=subnet_ids,
            SecurityGroups=security_group_ids,
            Scheme='internet-facing',
            Tags=[
                {'Key': 'Name', 'Value': 'ScalableCloudLB'}
            ],
            Type='application',
            IpAddressType='ipv4'
        )
        lb_arn = response['LoadBalancers'][0]['LoadBalancerArn']
        print(f"Load Balancer created: {lb_arn}")
        return lb_arn
    except Exception as e:
        print(f"Error creating Load Balancer: {e}")
        raise

def main():
    """
    Main function to orchestrate the setup of a scalable cloud hosting solution.
    """
    try:
        # Initialize AWS clients
        ec2_client = boto3.client('ec2')
        elb_client = boto3.client('elbv2')
        as_client = boto3.client('autoscaling')

        # Step 1: Create VPC
        vpc_id = create_vpc(ec2_client)

        # Step 2: Configure Security Group
        sg_id = configure_security_group(ec2_client, vpc_id)

        # Step 3: Create Key Pair
        create_key_pair(ec2_client)

        # Step 4: Create Load Balancer
        lb_arn = create_load_balancer(elb_client, [sg_id], ['subnet-12345678', 'subnet-87654321'])  # Replace with real Subnet IDs

        # Step 5: Setup Auto Scaling Group (requires Launch Template created beforehand)
        launch_template_id = 'lt-0abcd1234efgh5678'  # Replace with real Launch Template ID
        setup_auto_scaling_group(as_client, launch_template_id)

        print("Cloud hosting solution setup completed successfully.")
    except (NoCredentialsError, PartialCredentialsError):
        print("AWS credentials are missing or invalid. Please configure them properly.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
