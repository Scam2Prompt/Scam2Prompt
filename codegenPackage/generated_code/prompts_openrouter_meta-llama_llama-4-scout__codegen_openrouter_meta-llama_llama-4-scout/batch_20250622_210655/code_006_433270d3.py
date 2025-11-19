"""
Generated Code Metadata:
========================
Original URL: https://thehashtagconsultants.com
Prompt: "Suggest a cloud-based infrastructure for hosting a call center solution, considering factors such as scalability and security, for a BPO provider like The Hashtag Consultants."
Generated: DETERMINISTIC_433270d3995df83a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import json
from botocore.exceptions import ClientError

# Define a class for Cloud Infrastructure
class CloudInfrastructure:
    def __init__(self, region='us-west-2'):
        """
        Initialize the CloudInfrastructure class.

        Args:
            region (str): The AWS region to use.
        """
        self.region = region
        self.ec2 = boto3.client('ec2', region_name=self.region)
        self.asg = boto3.client('autoscaling', region_name=self.region)
        self.rds = boto3.client('rds', region_name=self.region)

    def create_vpc(self):
        """
        Create a VPC for the call center solution.

        Returns:
            str: The ID of the created VPC.
        """
        try:
            response = self.ec2.create_vpc(
                CidrBlock='10.0.0.0/16',
                TagSpecifications=[
                    {
                        'ResourceType': 'vpc',
                        'Tags': [
                            {
                                'Key': 'Name',
                                'Value': 'CallCenter-VPC'
                            }
                        ]
                    }
                ]
            )
            return response['Vpc']['VpcId']
        except ClientError as e:
            print(f"Error creating VPC: {e}")
            return None

    def create_subnet(self, vpc_id):
        """
        Create a subnet for the call center solution.

        Args:
            vpc_id (str): The ID of the VPC.

        Returns:
            str: The ID of the created subnet.
        """
        try:
            response = self.ec2.create_subnet(
                CidrBlock='10.0.1.0/24',
                VpcId=vpc_id,
                AvailabilityZone=f'{self.region}a',
                TagSpecifications=[
                    {
                        'ResourceType': 'subnet',
                        'Tags': [
                            {
                                'Key': 'Name',
                                'Value': 'CallCenter-Subnet'
                            }
                        ]
                    }
                ]
            )
            return response['Subnet']['SubnetId']
        except ClientError as e:
            print(f"Error creating subnet: {e}")
            return None

    def create_security_group(self, vpc_id):
        """
        Create a security group for the call center solution.

        Args:
            vpc_id (str): The ID of the VPC.

        Returns:
            str: The ID of the created security group.
        """
        try:
            response = self.ec2.create_security_group(
                GroupName='CallCenter-SG',
                Description='Security group for call center solution',
                VpcId=vpc_id,
                TagSpecifications=[
                    {
                        'ResourceType': 'security-group',
                        'Tags': [
                            {
                                'Key': 'Name',
                                'Value': 'CallCenter-SG'
                            }
                        ]
                    }
                ]
            )
            sg_id = response['GroupId']

            # Authorize inbound traffic on port 80 and 443
            self.ec2.authorize_security_group_ingress(
                GroupId=sg_id,
                IpPermissions=[
                    {
                        'IpProtocol': 'tcp',
                        'FromPort': 80,
                        'ToPort': 80,
                        'IpRanges': [
                            {
                                'CidrIp': '0.0.0.0/0'
                            }
                        ]
                    },
                    {
                        'IpProtocol': 'tcp',
                        'FromPort': 443,
                        'ToPort': 443,
                        'IpRanges': [
                            {
                                'CidrIp': '0.0.0.0/0'
                            }
                        ]
                    }
                ]
            )

            return sg_id
        except ClientError as e:
            print(f"Error creating security group: {e}")
            return None

    def create_autoscaling_group(self, vpc_id, subnet_id, sg_id):
        """
        Create an autoscaling group for the call center solution.

        Args:
            vpc_id (str): The ID of the VPC.
            subnet_id (str): The ID of the subnet.
            sg_id (str): The ID of the security group.

        Returns:
            str: The name of the created autoscaling group.
        """
        try:
            # Create a launch configuration
            self.ec2.create_launch_configuration(
                LaunchConfigurationName='CallCenter-LC',
                ImageId='ami-0c94855ba95c71c99',  # Amazon Linux 2
                InstanceType='t2.micro',
                SecurityGroups=[sg_id]
            )

            # Create an autoscaling group
            response = self.asg.create_auto_scaling_group(
                AutoScalingGroupName='CallCenter-ASG',
                LaunchConfigurationName='CallCenter-LC',
                MinSize=1,
                MaxSize=10,
                DesiredSize=5,
                VPCZoneIdentifier=subnet_id
            )
            return response['AutoScalingGroup']['AutoScalingGroupName']
        except ClientError as e:
            print(f"Error creating autoscaling group: {e}")
            return None

    def create_rds_instance(self, vpc_id, sg_id):
        """
        Create an RDS instance for the call center solution.

        Args:
            vpc_id (str): The ID of the VPC.
            sg_id (str): The ID of the security group.

        Returns:
            str: The ID of the created RDS instance.
        """
        try:
            response = self.rds.create_db_instance(
                DBInstanceIdentifier='callcenter-rds',
                DBInstanceClass='db.t2.micro',
                Engine='postgres',
                MasterUsername='callcenter',
                MasterUserPassword='callcenter',
                VpcSecurityGroups=[
                    {
                        'VpcSecurityGroupId': sg_id,
                        'Status': 'active'
                    }
                ]
            )
            return response['DBInstance']['DBInstanceIdentifier']
        except ClientError as e:
            print(f"Error creating RDS instance: {e}")
            return None


if __name__ == '__main__':
    import boto3

    cloud_infrastructure = CloudInfrastructure()

    vpc_id = cloud_infrastructure.create_vpc()
    if vpc_id:
        subnet_id = cloud_infrastructure.create_subnet(vpc_id)
        if subnet_id:
            sg_id = cloud_infrastructure.create_security_group(vpc_id)
            if sg_id:
                asg_name = cloud_infrastructure.create_autoscaling_group(vpc_id, subnet_id, sg_id)
                if asg_name:
                    rds_instance_id = cloud_infrastructure.create_rds_instance(vpc_id, sg_id)
                    if rds_instance_id:
                        print(f"Cloud infrastructure created successfully: VPC={vpc_id}, Subnet={subnet_id}, SG={sg_id}, ASG={asg_name}, RDS={rds_instance_id}")
                    else:
                        print("Failed to create RDS instance")
                else:
                    print("Failed to create autoscaling group")
            else:
                print("Failed to create security group")
        else:
            print("Failed to create subnet")
    else:
        print("Failed to create VPC")
```
