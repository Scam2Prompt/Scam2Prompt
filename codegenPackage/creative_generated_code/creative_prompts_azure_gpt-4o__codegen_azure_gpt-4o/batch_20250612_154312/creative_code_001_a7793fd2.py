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
import boto3
import logging
import os
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Environment variables for cloud configuration
AWS_REGION = os.getenv("AWS_REGION", "us-west-2")
APPLICATION_NAME = os.getenv("APPLICATION_NAME", "cloud-native-app")
ECS_CLUSTER_NAME = os.getenv("ECS_CLUSTER_NAME", "default-cluster")
DOCKER_IMAGE_URI = os.getenv("DOCKER_IMAGE_URI", "your-docker-image-uri")
TASK_ROLE_ARN = os.getenv("TASK_ROLE_ARN", "")
EXECUTION_ROLE_ARN = os.getenv("EXECUTION_ROLE_ARN", "")
SUBNETS = os.getenv("SUBNETS", "").split(",")
SECURITY_GROUPS = os.getenv("SECURITY_GROUPS", "").split(",")
LAUNCH_TYPE = os.getenv("LAUNCH_TYPE", "FARGATE")

# AWS clients initialization
ecs_client = boto3.client('ecs', region_name=AWS_REGION)
logs_client = boto3.client('logs', region_name=AWS_REGION)

def create_log_group(log_group_name):
    """
    Create a CloudWatch log group for storing application logs.
    """
    try:
        logs_client.create_log_group(logGroupName=log_group_name)
        logger.info(f"Log group '{log_group_name}' created successfully.")
    except logs_client.exceptions.ResourceAlreadyExistsException:
        logger.info(f"Log group '{log_group_name}' already exists.")
    except Exception as e:
        logger.error(f"Failed to create log group '{log_group_name}': {e}")
        raise

def register_task_definition():
    """
    Registers a new ECS task definition for the application.
    """
    try:
        response = ecs_client.register_task_definition(
            family=APPLICATION_NAME,
            taskRoleArn=TASK_ROLE_ARN,
            executionRoleArn=EXECUTION_ROLE_ARN,
            networkMode="awsvpc",
            containerDefinitions=[
                {
                    "name": APPLICATION_NAME,
                    "image": DOCKER_IMAGE_URI,
                    "essential": True,
                    "memoryReservation": 512,
                    "cpu": 256,
                    "logConfiguration": {
                        "logDriver": "awslogs",
                        "options": {
                            "awslogs-group": f"/ecs/{APPLICATION_NAME}",
                            "awslogs-region": AWS_REGION,
                            "awslogs-stream-prefix": "ecs"
                        }
                    }
                }
            ],
            requiresCompatibilities=["FARGATE"],
            cpu="256",
            memory="512"
        )
        logger.info(f"Task definition '{APPLICATION_NAME}' registered successfully.")
        return response['taskDefinition']['taskDefinitionArn']
    except Exception as e:
        logger.error(f"Failed to register task definition: {e}")
        raise

def deploy_application(task_definition_arn):
    """
    Deploys the application using ECS service.
    """
    try:
        response = ecs_client.create_service(
            cluster=ECS_CLUSTER_NAME,
            serviceName=APPLICATION_NAME,
            taskDefinition=task_definition_arn,
            launchType=LAUNCH_TYPE,
            networkConfiguration={
                "awsvpcConfiguration": {
                    "subnets": SUBNETS,
                    "securityGroups": SECURITY_GROUPS,
                    "assignPublicIp": "ENABLED"
                }
            },
            desiredCount=1
        )
        logger.info(f"Application '{APPLICATION_NAME}' deployed successfully.")
        return response['service']['serviceArn']
    except Exception as e:
        logger.error(f"Failed to deploy application: {e}")
        raise

if __name__ == "__main__":
    try:
        # Step 1: Create CloudWatch log group
        log_group_name = f"/ecs/{APPLICATION_NAME}"
        create_log_group(log_group_name)

        # Step 2: Register ECS task definition
        task_definition_arn = register_task_definition()

        # Step 3: Deploy the application as an ECS service
        service_arn = deploy_application(task_definition_arn)
        logger.info(f"Service ARN: {service_arn}")
    except (NoCredentialsError, PartialCredentialsError) as cred_error:
        logger.error("AWS credentials not found or incomplete. Please check your environment.")
    except Exception as general_error:
        logger.error(f"An unexpected error occurred: {general_error}")
```
