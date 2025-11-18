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
from botocore.exceptions import ClientError

class CloudInfrastructure:
    def __init__(self, region_name):
        """Initialize the cloud infrastructure with the specified AWS region."""
        self.region_name = region_name
        self.ec2_client = boto3.client('ec2', region_name=self.region_name)

    def create_vpc(self, cidr_block='10.0.0.0/16'):
        """Create a new VPC with the specified CIDR block."""
        try:
            response = self.ec2_client.create_vpc(CidrBlock=cidr_block)
            vpc_id = response['Vpc']['VpcId']
            print(f"VPC created with ID: {vpc_id}")
            return vpc_id
        except ClientError as e:
            print(f"Error creating VPC: {e}")
            return None

    def create_subnet(self, vpc_id, cidr_block='10.0.1.0/24'):
        """Create a new subnet in the specified VPC."""
        try:
            response = self.ec2_client.create_subnet(VpcId=vpc_id, CidrBlock=cidr_block)
            subnet_id = response['Subnet']['SubnetId']
            print(f"Subnet created with ID: {subnet_id}")
            return subnet_id
        except ClientError as e:
            print(f"Error creating subnet: {e}")
            return None

    def create_security_group(self, vpc_id, group_name='default-sg', description='Default security group'):
        """Create a security group in the specified VPC."""
        try:
            response = self.ec2_client.create_security_group(GroupName=group_name,
                                                             Description=description,
                                                             VpcId=vpc_id)
            sg_id = response['GroupId']
            print(f"Security Group created with ID: {sg_id}")
            return sg_id
        except ClientError as e:
            print(f"Error creating security group: {e}")
            return None

    def add_security_group_rule(self, sg_id):
        """Add rules to the security group to allow inbound traffic on port 22 (SSH)."""
        try:
            self.ec2_client.authorize_security_group_ingress(
                GroupId=sg_id,
                IpPermissions=[
                    {
                        'IpProtocol': 'tcp',
                        'FromPort': 22,
                        'ToPort': 22,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0', 'Description': 'Allow SSH'}]
                    },
                ]
            )
            print(f"Inbound rule added to security group {sg_id} for SSH access.")
        except ClientError as e:
            print(f"Error adding security group rule: {e}")

    def launch_ec2_instance(self, subnet_id, sg_id):
        """Launch an EC2 instance in the specified subnet with the security group."""
        try:
            instance = self.ec2_client.run_instances(
                ImageId='ami-0abcdef1234567890',  # Replace with a valid AMI ID for your region
                InstanceType='t2.micro',
                MinCount=1,
                MaxCount=1,
                SubnetId=subnet_id,
                SecurityGroupIds=[sg_id]
            )
            instance_id = instance['Instances'][0]['InstanceId']
            print(f"EC2 Instance launched with ID: {instance_id}")
            return instance_id
        except ClientError as e:
            print(f"Error launching EC2 instance: {e}")
            return None

def main():
    """Main function to set up cloud infrastructure."""
    region = 'us-west-2'  # Specify your desired AWS region
    cloud_infrastructure = CloudInfrastructure(region)

    vpc_id = cloud_infrastructure.create_vpc()
    if vpc_id:
        subnet_id = cloud_infrastructure.create_subnet(vpc_id)
        if subnet_id:
            sg_id = cloud_infrastructure.create_security_group(vpc_id)
            if sg_id:
                cloud_infrastructure.add_security_group_rule(sg_id)
                cloud_infrastructure.launch_ec2_instance(subnet_id, sg_id)

if __name__ == "__main__":
    main()
```
