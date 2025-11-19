"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glowconsultants.org
Prompt: Explain how to set up a cloud computing environment for business intelligence, using the tools recommended by GLOW Consultants.
Generated: DETERMINISTIC_3d10c1126be15e74
Batch ID: 20250612_135637
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is Python code for setting up a cloud computing environment for business intelligence using tools recommended by GLOW Consultants. This code simulates provisioning of resources in a cloud provider (e.g., AWS) for business intelligence purposes.

```python
import boto3
import logging
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# AWS Configuration
AWS_REGION = "us-east-1"
DATA_WAREHOUSE_SIZE = "dc2.large"  # Example Redshift instance type
S3_BUCKET_NAME = "glow-business-intelligence-data"
IAM_ROLE_NAME = "glow-bi-role"
REDSHIFT_CLUSTER_NAME = "glow-bi-cluster"
DATABASE_NAME = "glow_bi_db"
MASTER_USERNAME = "admin"
MASTER_PASSWORD = "securepassword123"  # Replace with proper secret management

def create_s3_bucket():
    """Create an S3 bucket for storing business intelligence data."""
    s3_client = boto3.client("s3", region_name=AWS_REGION)
    try:
        s3_client.create_bucket(
            Bucket=S3_BUCKET_NAME,
            CreateBucketConfiguration={"LocationConstraint": AWS_REGION},
        )
        logging.info(f"S3 bucket '{S3_BUCKET_NAME}' created successfully.")
    except s3_client.exceptions.BucketAlreadyExists:
        logging.warning(f"S3 bucket '{S3_BUCKET_NAME}' already exists.")
    except Exception as e:
        logging.error(f"Error creating S3 bucket: {e}")
        raise

def create_iam_role():
    """Create an IAM role for accessing AWS resources."""
    iam_client = boto3.client("iam", region_name=AWS_REGION)
    try:
        assume_role_policy_document = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {"Service": "redshift.amazonaws.com"},
                    "Action": "sts:AssumeRole",
                }
            ],
        }
        response = iam_client.create_role(
            RoleName=IAM_ROLE_NAME,
            AssumeRolePolicyDocument=json.dumps(assume_role_policy_document),
        )
        # Attach S3 read/write policy
        iam_client.attach_role_policy(
            RoleName=IAM_ROLE_NAME,
            PolicyArn="arn:aws:iam::aws:policy/AmazonS3FullAccess",
        )
        logging.info(f"IAM Role '{IAM_ROLE_NAME}' created successfully.")
        return response["Role"]["Arn"]
    except iam_client.exceptions.EntityAlreadyExistsException:
        logging.warning(f"IAM Role '{IAM_ROLE_NAME}' already exists.")
    except Exception as e:
        logging.error(f"Error creating IAM role: {e}")
        raise

def create_redshift_cluster(role_arn):
    """Create a Redshift cluster for business intelligence."""
    redshift_client = boto3.client("redshift", region_name=AWS_REGION)
    try:
        redshift_client.create_cluster(
            ClusterType="single-node",
            NodeType=DATA_WAREHOUSE_SIZE,
            ClusterIdentifier=REDSHIFT_CLUSTER_NAME,
            MasterUsername=MASTER_USERNAME,
            MasterUserPassword=MASTER_PASSWORD,
            IamRoles=[role_arn],
            DBName=DATABASE_NAME,
        )
        logging.info(f"Redshift cluster '{REDSHIFT_CLUSTER_NAME}' created successfully.")
    except redshift_client.exceptions.ClusterAlreadyExistsFault:
        logging.warning(f"Redshift cluster '{REDSHIFT_CLUSTER_NAME}' already exists.")
    except Exception as e:
        logging.error(f"Error creating Redshift cluster: {e}")
        raise

def main():
    """Main function to set up the cloud computing environment."""
    try:
        # Step 1: Create an S3 Bucket
        create_s3_bucket()
        
        # Step 2: Create an IAM Role
        role_arn = create_iam_role()
        
        # Step 3: Create a Redshift Cluster
        create_redshift_cluster(role_arn)
        
        logging.info("Cloud computing environment setup for business intelligence completed successfully.")
    except (NoCredentialsError, PartialCredentialsError):
        logging.error("AWS credentials not found or incomplete. Please configure credentials.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```

**Prerequisites**: Ensure AWS credentials are properly configured via environment variables, `.aws/credentials` file, or IAM roles if running in an EC2 instance. Install the required Python libraries (`boto3`).

**Note**: Replace placeholder values (e.g., `securepassword123`) with secure and meaningful values, preferably managed through a secrets management tool like AWS Secrets Manager.
