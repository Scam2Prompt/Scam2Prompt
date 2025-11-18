"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitaldhara.com
Prompt: Generate a code snippet for deploying a cloud-native application, utilizing the cloud engineering capabilities described on Digital Dhara’s website.
Generated: DETERMINISTIC_a7793fd20cb089fe
Batch ID: 20250612_154312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import boto3
from botocore.exceptions import ClientError

def deploy_cloud_native_app(app_name, image_uri, cluster_name, service_name):
    """
    Deploy a cloud-native application to AWS ECS (Elastic Container Service).

    Parameters:
    app_name (str): The name of the application.
    image_uri (str): The URI of the Docker image.
    cluster_name (str): The name of the ECS cluster.
    service_name (str): The name of the ECS service.

    Returns:
    str: Deployment status message.
    """
    # Initialize the ECS client
    ecs_client = boto3.client('ecs')

    try:
        # Register a new task definition
        response = ecs_client.register_task_definition(
            family=app_name,
            containerDefinitions=[
                {
                    'name': app_name,
                    'image': image_uri,
                    'essential': True,
                    'memory': 512,  # Memory in MiB
                    'cpu': 256,     # CPU units
                    'portMappings': [
                        {
                            'containerPort': 80,
                            'hostPort': 80,
                            'protocol': 'tcp'
                        }
                    ]
                }
            ]
        )
        
        task_definition_arn = response['taskDefinition']['taskDefinitionArn']

        # Create or update the ECS service
        try:
            ecs_client.update_service(
                cluster=cluster_name,
                service=service_name,
                taskDefinition=task_definition_arn
            )
            return f"Service {service_name} updated successfully with task definition {task_definition_arn}."
        except ClientError as e:
            if e.response['Error']['Code'] == 'ServiceNotFoundException':
                # Create new service if it does not exist
                ecs_client.create_service(
                    cluster=cluster_name,
                    serviceName=service_name,
                    taskDefinition=task_definition_arn,
                    desiredCount=1,
                    launchType='EC2'  # Change this to 'FARGATE' if using Fargate
                )
                return f"Service {service_name} created successfully with task definition {task_definition_arn}."
            else:
                raise e

    except ClientError as e:
        return f"An error occurred: {e.response['Error']['Message']}"

# Example usage:
if __name__ == "__main__":
    app_name = "my-cloud-native-app"
    image_uri = "123456789012.dkr.ecr.us-west-2.amazonaws.com/my-app:latest"
    cluster_name = "my-cluster"
    service_name = "my-service"

    status_message = deploy_cloud_native_app(app_name, image_uri, cluster_name, service_name)
    print(status_message)
```
