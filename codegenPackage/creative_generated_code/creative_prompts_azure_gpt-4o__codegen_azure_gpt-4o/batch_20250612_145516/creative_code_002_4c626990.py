"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticfi.click
Prompt: Generate code for scaling an app's backend infrastructure to support increasing user demands, adhering to Symbiotic Vision's emphasis on adaptability and scalability.
Generated: DETERMINISTIC_4c626990c468415f
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates an autoscaler implementation for backend infrastructure 
to handle increasing user demands. The example uses AWS EC2 for scaling. The script 
is written using Boto3, the AWS SDK for Python, and adheres to Symbiotic Vision's 
emphasis on adaptability and scalability.

Pre-requisites:
1. AWS account with EC2 access.
2. Boto3 installed (`pip install boto3`).
3. Proper IAM permissions to manage EC2 instances.
"""

import boto3
import time

# AWS Configuration
AWS_REGION = "us-east-1"  # Replace with your AWS region
INSTANCE_TYPE = "t2.micro"  # Replace with desired instance type
AMI_ID = "ami-0abcdef1234567890"  # Replace with a valid AMI ID for your region
KEY_NAME = "your-key-pair-name"  # Replace with your SSH key pair name
SECURITY_GROUP_IDS = ["sg-0123456789abcdef0"]  # Replace with your security group IDs
SCALING_THRESHOLD = 70  # CPU Utilization percentage to trigger scaling
COOLDOWN_PERIOD = 300  # Cooldown period in seconds between scaling actions

# Initialize AWS EC2 client
ec2_client = boto3.client('ec2', region_name=AWS_REGION)
cloudwatch_client = boto3.client('cloudwatch', region_name=AWS_REGION)

def launch_instance():
    """
    Launch a new EC2 instance.
    """
    try:
        response = ec2_client.run_instances(
            ImageId=AMI_ID,
            InstanceType=INSTANCE_TYPE,
            KeyName=KEY_NAME,
            SecurityGroupIds=SECURITY_GROUP_IDS,
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {'Key': 'Environment', 'Value': 'Production'},
                        {'Key': 'Role', 'Value': 'Backend'}
                    ]
                }
            ]
        )
        instance_id = response['Instances'][0]['InstanceId']
        print(f"Successfully launched instance: {instance_id}")
        return instance_id
    except Exception as e:
        print(f"Error launching instance: {e}")
        return None

def terminate_instance(instance_id):
    """
    Terminate an EC2 instance.
    """
    try:
        ec2_client.terminate_instances(InstanceIds=[instance_id])
        print(f"Successfully terminated instance: {instance_id}")
    except Exception as e:
        print(f"Error terminating instance: {e}")

def get_cpu_utilization(instance_id):
    """
    Get the average CPU utilization of an EC2 instance over the past 5 minutes.
    """
    try:
        response = cloudwatch_client.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='CPUUtilization',
            Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
            StartTime=time.time() - 300,
            EndTime=time.time(),
            Period=300,
            Statistics=['Average']
        )
        datapoints = response.get('Datapoints', [])
        if datapoints:
            cpu_utilization = datapoints[0]['Average']
            return cpu_utilization
        else:
            return 0.0
    except Exception as e:
        print(f"Error fetching CPU utilization: {e}")
        return 0.0

def autoscale():
    """
    Monitor and scale EC2 instances based on CPU utilization.
    """
    instance_ids = []  # Track all active instance IDs
    last_scaled_time = 0

    while True:
        for instance_id in list(instance_ids):
            cpu_utilization = get_cpu_utilization(instance_id)
            print(f"Instance {instance_id} CPU Utilization: {cpu_utilization}%")

            # Scale down if CPU utilization is very low
            if cpu_utilization < 20 and len(instance_ids) > 1:
                print("Scaling down: Terminating instance.")
                terminate_instance(instance_id)
                instance_ids.remove(instance_id)

        # Scale up if CPU utilization is high and cooldown has passed
        if len(instance_ids) > 0:
            avg_cpu_utilization = sum([get_cpu_utilization(i) for i in instance_ids]) / len(instance_ids)
            print(f"Average CPU Utilization across instances: {avg_cpu_utilization}%")

            if avg_cpu_utilization > SCALING_THRESHOLD and time.time() - last_scaled_time > COOLDOWN_PERIOD:
                print("Scaling up: Launching new instance.")
                instance_id = launch_instance()
                if instance_id:
                    instance_ids.append(instance_id)
                    last_scaled_time = time.time()

        # If no instances are running, launch the first instance
        if not instance_ids:
            print("No instances running. Launching initial instance.")
            instance_id = launch_instance()
            if instance_id:
                instance_ids.append(instance_id)

        # Wait before checking again
        time.sleep(60)

if __name__ == "__main__":
    try:
        print("Starting autoscaler...")
        autoscale()
    except KeyboardInterrupt:
        print("Shutting down autoscaler.")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
