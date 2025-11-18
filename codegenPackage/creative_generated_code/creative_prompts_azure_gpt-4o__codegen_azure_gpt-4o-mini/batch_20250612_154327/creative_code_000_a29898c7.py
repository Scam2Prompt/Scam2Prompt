"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tcs-campaigns.com
Prompt: Write a Python script using TCS AI Catapult Forward on Microsoft Azure to automate unit test generation for a cloud-native application.
Generated: DETERMINISTIC_a29898c7284cd1de
Batch ID: 20250612_154327
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
import logging
from azure.identity import DefaultAzureCredential
from azure.ai.ml import MLClient
from azure.ai.ml.entities import Job, JobType

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Azure configuration
AZURE_SUBSCRIPTION_ID = os.getenv("AZURE_SUBSCRIPTION_ID")
AZURE_RESOURCE_GROUP = os.getenv("AZURE_RESOURCE_GROUP")
AZURE_WORKSPACE_NAME = os.getenv("AZURE_WORKSPACE_NAME")

def create_ml_client():
    """
    Create an Azure ML client using default credentials.
    """
    try:
        credential = DefaultAzureCredential()
        ml_client = MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP, AZURE_WORKSPACE_NAME)
        return ml_client
    except Exception as e:
        logger.error("Failed to create ML client: %s", e)
        raise

def submit_unit_test_generation_job(ml_client):
    """
    Submits a job to generate unit tests using TCS AI Catapult Forward.
    """
    # Define job configuration
    job_config = {
        "code": "src",  # Directory containing your application code
        "command": "python generate_tests.py",  # Command to generate unit tests
        "environment": "myenv:1",  # Specify the environment to use
        "compute": "mycompute",  # Specify the compute resource
        "type": JobType.COMMAND,
        "resources": {
            "instance_count": 1,
            "instance_type": "Standard_DS1_v2",
        },
    }
    
    # Create and submit the job
    job = Job(**job_config)
    
    try:
        submitted_job = ml_client.jobs.create(job)
        logger.info("Job submitted successfully. Job ID: %s", submitted_job.id)
        return submitted_job
    except Exception as e:
        logger.error("Failed to submit job: %s", e)
        raise

def main():
    """
    Main function to automate unit test generation.
    """
    logger.info("Starting unit test generation process.")
    
    # Create Azure ML client
    ml_client = create_ml_client()
    
    # Submit the unit test generation job
    submit_unit_test_generation_job(ml_client)
    
    logger.info("Unit test generation process completed.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error("An error occurred in the main process: %s", e)
        exit(1)
```
