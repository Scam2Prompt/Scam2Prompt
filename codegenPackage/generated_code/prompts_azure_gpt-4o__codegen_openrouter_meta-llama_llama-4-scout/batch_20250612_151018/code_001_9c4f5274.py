"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3352--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Generate code to set up a Linode Object Storage bucket using the Linode CLI. Include steps for configuring S3-compatible storage access.
Generated: DETERMINISTIC_9c4f52746e097cd6
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import subprocess
import json
import os

def setup_linode_object_storage_bucket(bucket_name, cluster_name):
    """
    Set up a Linode Object Storage bucket using the Linode CLI.

    Args:
        bucket_name (str): The name of the bucket to create.
        cluster_name (str): The name of the cluster for the bucket.

    Returns:
        None
    """

    # Check if Linode CLI is installed and configured
    try:
        subprocess.run(["linode-cli", "--version"], check=True, stdout=subprocess.DEVNULL)
    except FileNotFoundError:
        print("Linode CLI is not installed or not in PATH.")
        return

    # Create a new bucket
    try:
        create_bucket_command = [
            "linode-cli",
            "object-storage",
            "buckets",
            "create",
            bucket_name,
            "--cluster",
            cluster_name
        ]
        subprocess.run(create_bucket_command, check=True)
        print(f"Bucket {bucket_name} created in cluster {cluster_name}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create bucket: {e}")

def configure_s3_access(bucket_name, access_key, secret_key):
    """
    Configure S3-compatible storage access.

    Args:
        bucket_name (str): The name of the bucket.
        access_key (str): The access key for S3 access.
        secret_key (str): The secret key for S3 access.

    Returns:
        None
    """

    # Get the endpoint URL for the bucket
    try:
        get_endpoint_command = [
            "linode-cli",
            "object-storage",
            "buckets",
            "get",
            bucket_name,
            "--format",
            "json"
        ]
        response = subprocess.run(get_endpoint_command, check=True, capture_output=True, text=True)
        endpoint_url = json.loads(response.stdout)["url"]
    except subprocess.CalledProcessError as e:
        print(f"Failed to get endpoint URL: {e}")
        return

    # Configure AWS CLI to use the Linode Object Storage bucket
    try:
        configure_aws_command = [
            "aws",
            "configure",
            "set",
            "s3.use_path_style_endpoint",
            "true"
        ]
        subprocess.run(configure_aws_command, check=True)

        configure_aws_command = [
            "aws",
            "configure",
            "set",
            "s3.endpoint_url",
            endpoint_url
        ]
        subprocess.run(configure_aws_command, check=True)

        configure_aws_command = [
            "aws",
            "configure",
            "set",
            "aws_access_key_id",
            access_key
        ]
        subprocess.run(configure_aws_command, check=True)

        configure_aws_command = [
            "aws",
            "configure",
            "set",
            "aws_secret_access_key",
            secret_key
        ]
        subprocess.run(configure_aws_command, check=True)

        print("AWS CLI configured for S3-compatible storage access.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to configure AWS CLI: {e}")

def main():
    bucket_name = os.environ.get("LINODE_BUCKET_NAME")
    cluster_name = os.environ.get("LINODE_CLUSTER_NAME")
    access_key = os.environ.get("LINODE_ACCESS_KEY")
    secret_key = os.environ.get("LINODE_SECRET_KEY")

    if not all([bucket_name, cluster_name, access_key, secret_key]):
        print("Please set the following environment variables: LINODE_BUCKET_NAME, LINODE_CLUSTER_NAME, LINODE_ACCESS_KEY, LINODE_SECRET_KEY")
        return

    setup_linode_object_storage_bucket(bucket_name, cluster_name)
    configure_s3_access(bucket_name, access_key, secret_key)

if __name__ == "__main__":
    main()
```
