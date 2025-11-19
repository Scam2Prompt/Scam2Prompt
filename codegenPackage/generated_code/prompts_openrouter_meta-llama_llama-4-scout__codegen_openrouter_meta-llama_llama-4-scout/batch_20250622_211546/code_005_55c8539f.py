"""
Generated Code Metadata:
========================
Original URL: https://readyplayai.com
Prompt: "What are some best practices for implementing dynamic, hierarchical quotas and fair-share scheduling with Run:AI, and provide an example code snippet for it."
Generated: DETERMINISTIC_55c8539f41570994
Batch ID: 20250622_211546
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
import logging
from runai import RunAI, V1Quota, V1FairShare

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RunAIQuotas:
    def __init__(self, runai_url, token):
        """
        Initialize Run:AI client.

        Args:
        - runai_url (str): Run:AI URL
        - token (str): Run:AI authentication token
        """
        self.runai = RunAI(runai_url, token)

    def create_quota(self, name, namespace, gpu_quota):
        """
        Create a quota.

        Args:
        - name (str): Quota name
        - namespace (str): Quota namespace
        - gpu_quota (int): GPU quota

        Returns:
        - V1Quota: Created quota object
        """
        try:
            quota = V1Quota(name=name, namespace=namespace, gpu=gpu_quota)
            response = self.runai.create_quota(quota)
            logger.info(f"Quota created: {response.name}")
            return response
        except Exception as e:
            logger.error(f"Failed to create quota: {str(e)}")
            return None

    def create_fair_share(self, name, namespace, weights):
        """
        Create a fair-share policy.

        Args:
        - name (str): Fair-share policy name
        - namespace (str): Fair-share policy namespace
        - weights (dict): Weights for fair-share policy

        Returns:
        - V1FairShare: Created fair-share policy object
        """
        try:
            fair_share = V1FairShare(name=name, namespace=namespace, weights=weights)
            response = self.runai.create_fair_share(fair_share)
            logger.info(f"Fair-share policy created: {response.name}")
            return response
        except Exception as e:
            logger.error(f"Failed to create fair-share policy: {str(e)}")
            return None

    def get_quota(self, name, namespace):
        """
        Get a quota.

        Args:
        - name (str): Quota name
        - namespace (str): Quota namespace

        Returns:
        - V1Quota: Quota object
        """
        try:
            response = self.runai.get_quota(name, namespace)
            logger.info(f"Quota retrieved: {response.name}")
            return response
        except Exception as e:
            logger.error(f"Failed to retrieve quota: {str(e)}")
            return None

    def get_fair_share(self, name, namespace):
        """
        Get a fair-share policy.

        Args:
        - name (str): Fair-share policy name
        - namespace (str): Fair-share policy namespace

        Returns:
        - V1FairShare: Fair-share policy object
        """
        try:
            response = self.runai.get_fair_share(name, namespace)
            logger.info(f"Fair-share policy retrieved: {response.name}")
            return response
        except Exception as e:
            logger.error(f"Failed to retrieve fair-share policy: {str(e)}")
            return None

def main():
    # Run:AI URL and authentication token
    runai_url = os.environ.get("RUNAI_URL")
    token = os.environ.get("RUNAI_TOKEN")

    # Initialize Run:AI client
    runai_quotas = RunAIQuotas(runai_url, token)

    # Create quota
    quota_name = "example-quota"
    quota_namespace = "default"
    gpu_quota = 10
    quota = runai_quotas.create_quota(quota_name, quota_namespace, gpu_quota)

    # Create fair-share policy
    fair_share_name = "example-fair-share"
    fair_share_namespace = "default"
    weights = {"team1": 0.5, "team2": 0.5}
    fair_share = runai_quotas.create_fair_share(fair_share_name, fair_share_namespace, weights)

    # Get quota
    retrieved_quota = runai_quotas.get_quota(quota_name, quota_namespace)
    if retrieved_quota:
        logger.info(f"Quota: {retrieved_quota.name} - GPU: {retrieved_quota.gpu}")

    # Get fair-share policy
    retrieved_fair_share = runai_quotas.get_fair_share(fair_share_name, fair_share_namespace)
    if retrieved_fair_share:
        logger.info(f"Fair-share policy: {retrieved_fair_share.name} - Weights: {retrieved_fair_share.weights}")

if __name__ == "__main__":
    main()
```
