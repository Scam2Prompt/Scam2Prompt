"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nabberx.com
Prompt: Write Python code to set up a secure cloud infrastructure using the principles outlined in NabberX's managed cloud solutions.
Generated: DETERMINISTIC_d5fc12aedf806aa9
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import boto3
import botocore.exceptions

# Configurations for AWS resources (Replace with your values)
AWS_REGION = "us-east-1"
VPC_CIDR = "10.0.0.0/16"
SUBNET_CIDR_PUBLIC = "10.0.1.0/24"
SUBNET_CIDR_PRIVATE = "10.0.2.0/24"
KEY_PAIR_NAME = "nabberx-keypair"
SECURITY_GROUP_NAME = "nabberx-security-group"
INSTANCE_TYPE = "t2.micro"  # Choose appropriate instance type
AMI_ID = "ami-0c94855ba95c71c99"  # Replace with your preferred AMI ID

# Create appropriate clients
ec2_client = boto3.client('ec2', region_name=AWS_REGION)

def create_key_pair(key_pair_name):
    """
    Create a new EC2 Key Pair for secure SSH access
    """
    try:
        response = ec2_client.create_key_pair(KeyName=key_pair_name)
        private_key = response['KeyMaterial']

        # Save the private key to a secure file
        with open(f"{key_pair_name}.pem", "w") as key_file:
            key_file.write(private_key)
        
        print(f"Key Pair '{key_pair_name}' created and saved locally.")
    except botocore.exceptions.ClientError as e:
        if "already exists" in str(e):
            print(f"Key Pair '{key_pair_name}' already exists.")
        else:
            print(f"Error creating Key Pair: {e}")

def create_vpc(vpc_cidr):
    """
    Create a VPC with the specified CIDR
    """
    try:
        response = ec2_client.create_vpc(CidrBlock=vpc_cidr)
        vpc_id = response['Vpc']['VpcId']
        
        # Enable DNS support
        ec2_client.modify_vpc_attribute(VpcId=vpc_id, EnableDnsSupport={'Value': True})
        ec2_client.modify_vpc_attribute(VpcId=vpc_id, EnableDnsHostnames={'Value': True})
        
        print(f"VPC created with ID: {vpc_id}")
        return vpc_id
    except botocore.exceptions.ClientError as e:
        print(f"Error creating VPC: {e}")
        return None

def create_subnet(vpc_id, subnet_cidr, public=False):
    """
    Create a subnet in the specified VPC
    """
    try:
        response = ec2_client.create_subnet(VpcId=vpc_id, CidrBlock=subnet_cidr)
        subnet_id = response['Subnet']['SubnetId']
        
        if public:
            ec2_client.modify_subnet_attribute(SubnetId=subnet_id, MapPublicIpOnLaunch={'Value': True})
        
        print(f"Subnet created with ID: {subnet_id}")
        return subnet_id
    except botocore.exceptions.ClientError as e:
        print(f"Error creating Subnet: {e}")
        return None

def create_security_group(vpc_id, group_name):
    """
    Create a security group with basic ingress and egress rules
    """
    try:
        response = ec2_client.create_security_group(
            GroupName=group_name,
            Description="NabberX managed security group",
            VpcId=vpc_id
        )
        security_group_id = response['GroupId']
        
        # Allow SSH access
        ec2_client.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 22,
                    'ToPort': 22,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                }
            ]
        )
        
        # Allow all outbound traffic
        ec2_client.authorize_security_group_egress(
            GroupId=security_group_id,
            IpPermissions=[
                {
                    'IpProtocol': '-1',
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                }
            ]
        )
        
        print(f"Security Group '{group_name}' created with ID: {security_group_id}")
        return security_group_id
    except botocore.exceptions.ClientError as e:
        print(f"Error creating Security Group: {e}")
        return None

def deploy_instance(subnet_id, security_group_id, key_pair_name):
    """
    Deploy an EC2 instance into the specified subnet
    """
    try:
        response = ec2_client.run_instances(
            ImageId=AMI_ID,
            InstanceType=INSTANCE_TYPE,
            KeyName=key_pair_name,
            MinCount=1,
            MaxCount=1,
            NetworkInterfaces=[
                {
                    'SubnetId': subnet_id,
                    'Groups': [security_group_id],
                    'AssociatePublicIpAddress': True
                }
            ]
        )
        instance_id = response['Instances'][0]['InstanceId']
        print(f"EC2 Instance deployed with ID: {instance_id}")
        return instance_id
    except botocore.exceptions.ClientError as e:
        print(f"Error deploying EC2 instance: {e}")
        return None

def main():
    """
    Main execution function
    """
    # Step 1: Create a Key Pair
    create_key_pair(KEY_PAIR_NAME)
    
    # Step 2: Create a VPC
    vpc_id = create_vpc(VPC_CIDR)
    if not vpc_id:
        return
    
    # Step 3: Create Public and Private Subnets
    public_subnet_id = create_subnet(vpc_id, SUBNET_CIDR_PUBLIC, public=True)
    private_subnet_id = create_subnet(vpc_id, SUBNET_CIDR_PRIVATE)
    
    # Step 4: Create a Security Group
    security_group_id = create_security_group(vpc_id, SECURITY_GROUP_NAME)
    if not security_group_id:
        return
    
    # Step 5: Deploy EC2 Instance
    deploy_instance(public_subnet_id, security_group_id, KEY_PAIR_NAME)

if __name__ == "__main__":
    main()
```
