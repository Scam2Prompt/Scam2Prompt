"""
Generated Code Metadata:
========================
Original URL: https://www.metis-labs.com
Prompt: "Create a cloud-based data and AI stack for a business, using a collaborative approach and strategic guidance from a cloud engineering expert."
Generated: DETERMINISTIC_0714231ef99b4003
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Cloud-based Data and AI Stack Implementation

This script sets up a cloud-based data and AI infrastructure using AWS services.
It includes data storage, processing pipelines, and AI model deployment capabilities.
"""

import boto3
from botocore.exceptions import ClientError
import json
import logging
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CloudDataAIStack:
    """
    Main class for managing the cloud data and AI stack.
    """
    
    def __init__(self, region_name: str = 'us-east-1'):
        """
        Initialize AWS clients and resources.
        
        Args:
            region_name: AWS region to deploy resources
        """
        self.region = region_name
        self.s3 = boto3.client('s3', region_name=region_name)
        self.glue = boto3.client('glue', region_name=region_name)
        self.sagemaker = boto3.client('sagemaker', region_name=region_name)
        self.iam = boto3.client('iam', region_name=region_name)
        self.lambda_client = boto3.client('lambda', region_name=region_name)
        
    def create_data_lake(self, bucket_name: str) -> bool:
        """
        Create an S3 bucket for data lake storage.
        
        Args:
            bucket_name: Name of the S3 bucket to create
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint': self.region
                }
            )
            logger.info(f"Created S3 bucket: {bucket_name}")
            return True
        except ClientError as e:
            logger.error(f"Error creating bucket {bucket_name}: {e}")
            return False
    
    def setup_glue_catalog(self, database_name: str, table_name: str, 
                          s3_location: str, schema: List[Dict]) -> bool:
        """
        Set up AWS Glue catalog for data processing.
        
        Args:
            database_name: Glue database name
            table_name: Glue table name
            s3_location: S3 path for the data
            schema: List of column definitions
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Create database if it doesn't exist
            try:
                self.glue.create_database(
                    DatabaseInput={
                        'Name': database_name
                    }
                )
            except self.glue.exceptions.AlreadyExistsException:
                pass
            
            # Create table
            self.glue.create_table(
                DatabaseName=database_name,
                TableInput={
                    'Name': table_name,
                    'StorageDescriptor': {
                        'Columns': schema,
                        'Location': s3_location,
                        'InputFormat': 'org.apache.hadoop.mapred.TextInputFormat',
                        'OutputFormat': 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat',
                        'SerdeInfo': {
                            'SerializationLibrary': 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
                        }
                    },
                    'TableType': 'EXTERNAL_TABLE'
                }
            )
            logger.info(f"Created Glue table {table_name} in database {database_name}")
            return True
        except ClientError as e:
            logger.error(f"Error setting up Glue catalog: {e}")
            return False
    
    def deploy_sagemaker_model(self, model_name: str, 
                             model_data: str, 
                             instance_type: str = 'ml.m5.large',
                             role_arn: Optional[str] = None) -> Optional[str]:
        """
        Deploy a model to SageMaker.
        
        Args:
            model_name: Name for the model
            model_data: S3 path to model artifacts
            instance_type: Instance type for hosting
            role_arn: IAM role ARN for SageMaker
            
        Returns:
            str: Endpoint name if successful, None otherwise
        """
        try:
            if not role_arn:
                role_arn = self._create_sagemaker_role()
                
            # Create model
            self.sagemaker.create_model(
                ModelName=model_name,
                ExecutionRoleArn=role_arn,
                PrimaryContainer={
                    'Image': '763104351884.dkr.ecr.us-east-1.amazonaws.com/pytorch-inference:1.8.1-cpu-py36-ubuntu18.04',
                    'ModelDataUrl': model_data
                }
            )
            
            # Create endpoint config
            endpoint_config_name = f"{model_name}-config"
            self.sagemaker.create_endpoint_config(
                EndpointConfigName=endpoint_config_name,
                ProductionVariants=[
                    {
                        'VariantName': 'AllTraffic',
                        'ModelName': model_name,
                        'InitialInstanceCount': 1,
                        'InstanceType': instance_type
                    }
                ]
            )
            
            # Create endpoint
            endpoint_name = f"{model_name}-endpoint"
            self.sagemaker.create_endpoint(
                EndpointName=endpoint_name,
                EndpointConfigName=endpoint_config_name
            )
            
            logger.info(f"Deployed SageMaker model {model_name} to endpoint {endpoint_name}")
            return endpoint_name
        except ClientError as e:
            logger.error(f"Error deploying SageMaker model: {e}")
            return None
    
    def _create_sagemaker_role(self) -> str:
        """
        Create IAM role for SageMaker if it doesn't exist.
        
        Returns:
            str: Role ARN
        """
        role_name = 'AmazonSageMaker-ExecutionRole'
        policy_arn = 'arn:aws:iam::aws:policy/AmazonSageMakerFullAccess'
        
        try:
            response = self.iam.create_role(
                RoleName=role_name,
                AssumeRolePolicyDocument=json.dumps({
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": "sagemaker.amazonaws.com"
                            },
                            "Action": "sts:AssumeRole"
                        }
                    ]
                }),
                Description='Allows SageMaker to call AWS services on your behalf'
            )
            
            self.iam.attach_role_policy(
                RoleName=role_name,
                PolicyArn=policy_arn
            )
            
            return response['Role']['Arn']
        except self.iam.exceptions.EntityAlreadyExistsException:
            return self.iam.get_role(RoleName=role_name)['Role']['Arn']
        except ClientError as e:
            logger.error(f"Error creating SageMaker role: {e}")
            raise
    
    def create_data_processing_lambda(self, function_name: str, 
                                    bucket_name: str, 
                                    handler: str = 'lambda_function.lambda_handler') -> bool:
        """
        Create a Lambda function for data processing.
        
        Args:
            function_name: Name of the Lambda function
            bucket_name: S3 bucket to trigger the Lambda
            handler: Lambda handler function
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Basic Lambda function with S3 trigger
            response = self.lambda_client.create_function(
                FunctionName=function_name,
                Runtime='python3.8',
                Role=self._create_lambda_role(),
                Handler=handler,
                Code={
                    'S3Bucket': 'lambda-functions',
                    'S3Key': 'data-processing.zip'
                },
                Environment={
                    'Variables': {
                        'DATA_BUCKET': bucket_name
                    }
                },
                Timeout=30,
                MemorySize=128
            )
            
            # Add S3 trigger
            self.lambda_client.add_permission(
                FunctionName=function_name,
                StatementId='s3-trigger',
                Action='lambda:InvokeFunction',
                Principal='s3.amazonaws.com',
                SourceArn=f'arn:aws:s3:::{bucket_name}'
            )
            
            self.s3.put_bucket_notification_configuration(
                Bucket=bucket_name,
                NotificationConfiguration={
                    'LambdaFunctionConfigurations': [
                        {
                            'LambdaFunctionArn': response['FunctionArn'],
                            'Events': ['s3:ObjectCreated:*']
                        }
                    ]
                }
            )
            
            logger.info(f"Created Lambda function {function_name} with S3 trigger")
            return True
        except ClientError as e:
            logger.error(f"Error creating Lambda function: {e}")
            return False
    
    def _create_lambda_role(self) -> str:
        """
        Create IAM role for Lambda if it doesn't exist.
        
        Returns:
            str: Role ARN
        """
        role_name = 'LambdaBasicExecutionRole'
        policy_arn = 'arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'
        
        try:
            response = self.iam.create_role(
                RoleName=role_name,
                AssumeRolePolicyDocument=json.dumps({
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": "lambda.amazon
