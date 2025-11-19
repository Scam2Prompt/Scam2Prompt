"""
Generated Code Metadata:
========================
Original URL: https://www.metis-labs.com
Prompt: "Generate a cloud architecture for a startup's data and AI stack using scalable solutions that can evolve with the business."
Generated: DETERMINISTIC_f57204affd6c1c81
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
Cloud Architecture for Startup Data and AI Stack
This script defines infrastructure as code (IaC) using AWS CDK (Python) to deploy
a scalable cloud architecture for a startup's data and AI needs.
"""

from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as lambda_,
    aws_iam as iam,
    aws_glue as glue,
    aws_sagemaker as sagemaker,
    aws_redshift as redshift,
    aws_kinesis as kinesis,
    aws_apigateway as apigateway,
    aws_dynamodb as dynamodb,
    aws_ec2 as ec2,
    aws_secretsmanager as secretsmanager,
    RemovalPolicy,
    Duration
)
from constructs import Construct

class StartupDataAIStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create VPC for isolated resources
        self.vpc = ec2.Vpc(
            self, "DataAIVpc",
            max_azs=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    name="Private",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask=24
                )
            ]
        )

        # Data Lake Foundation - S3 Buckets
        self.raw_data_bucket = s3.Bucket(
            self, "RawDataBucket",
            versioned=True,
            removal_policy=RemovalPolicy.RETAIN,
            encryption=s3.BucketEncryption.S3_MANAGED,
            lifecycle_rules=[
                s3.LifecycleRule(
                    transitions=[
                        s3.Transition(
                            storage_class=s3.StorageClass.INFREQUENT_ACCESS,
                            transition_after=Duration.days(30)
                        ),
                        s3.Transition(
                            storage_class=s3.StorageClass.GLACIER,
                            transition_after=Duration.days(90)
                        )
                    ]
                )
            ]
        )

        self.processed_data_bucket = s3.Bucket(
            self, "ProcessedDataBucket",
            versioned=True,
            removal_policy=RemovalPolicy.RETAIN,
            encryption=s3.BucketEncryption.S3_MANAGED
        )

        # Data Ingestion Layer
        self.kinesis_stream = kinesis.Stream(
            self, "DataIngestionStream",
            shard_count=1,
            retention_period=Duration.hours(24)
        )

        # Data Processing Layer
        self.glue_job_role = iam.Role(
            self, "GlueJobRole",
            assumed_by=iam.ServicePrincipal("glue.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSGlueServiceRole")
            ]
        )

        self.glue_job = glue.CfnJob(
            self, "DataProcessingJob",
            name="data-processing-job",
            role=self.glue_job_role.role_arn,
            command=glue.CfnJob.JobCommandProperty(
                name="glueetl",
                python_version="3",
                script_location=f"s3://{self.raw_data_bucket.bucket_name}/scripts/data_processing.py"
            ),
            default_arguments={
                "--job-language": "python",
                "--enable-metrics": "",
                "--enable-continuous-cloudwatch-log": "true"
            },
            glue_version="3.0",
            worker_type="G.1X",
            number_of_workers=2
        )

        # Data Warehouse Layer
        self.redshift_cluster = redshift.Cluster(
            self, "DataWarehouse",
            master_user=redshift.Login(
                master_username="admin",
                master_password=secretsmanager.Secret(
                    self, "RedshiftSecret",
                    generate_secret_string=secretsmanager.SecretStringGenerator(
                        exclude_characters="\"@/\\ "
                    )
                ).secret_value
            ),
            vpc=self.vpc,
            default_database_name="analytics",
            node_type="dc2.large",
            number_of_nodes=2,
            removal_policy=RemovalPolicy.SNAPSHOT
        )

        # AI/ML Layer
        self.sagemaker_notebook = sagemaker.CfnNotebookInstance(
            self, "MLNotebook",
            instance_type="ml.t3.medium",
            role_arn=iam.Role(
                self, "SageMakerRole",
                assumed_by=iam.ServicePrincipal("sagemaker.amazonaws.com"),
                managed_policies=[
                    iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSageMakerFullAccess")
                ]
            ).role_arn,
            notebook_instance_name="ml-notebook-instance"
        )

        # API Layer
        self.api_gateway = apigateway.RestApi(
            self, "DataAPI",
            rest_api_name="DataService",
            description="API for data and AI services"
        )

        # Serverless Compute Layer
        self.lambda_function = lambda_.Function(
            self, "DataProcessingLambda",
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_asset("lambda"),
            handler="handler.process",
            environment={
                "PROCESSED_BUCKET": self.processed_data_bucket.bucket_name,
                "REDSHIFT_CLUSTER": self.redshift_cluster.cluster_endpoint.hostname
            },
            vpc=self.vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS)
        )

        # Metadata Store
        self.metadata_table = dynamodb.Table(
            self, "MetadataStore",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
        )

        # Grant permissions
        self.raw_data_bucket.grant_read_write(self.glue_job_role)
        self.processed_data_bucket.grant_read_write(self.glue_job_role)
        self.processed_data_bucket.grant_read(self.lambda_function)
        self.kinesis_stream.grant_read(self.lambda_function)
        self.metadata_table.grant_read_write_data(self.lambda_function)

        # Output important resources
        self.output_resources()

    def output_resources(self):
        from aws_cdk import CfnOutput

        CfnOutput(
            self, "RawDataBucketName",
            value=self.raw_data_bucket.bucket_name
        )
        CfnOutput(
            self, "ProcessedDataBucketName",
            value=self.processed_data_bucket.bucket_name
        )
        CfnOutput(
            self, "DataAPIEndpoint",
            value=self.api_gateway.url
        )
        CfnOutput(
            self, "RedshiftEndpoint",
            value=self.redshift_cluster.cluster_endpoint.hostname
        )
```
