"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tcs-campaigns.com
Prompt: Write infrastructure automation scripts using TCS AI Catapult Forward to reduce build costs by 20% for a cloud-native application.
Generated: DETERMINISTIC_0b621ba1da9dfe12
Batch ID: 20250612_154327
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tcs-catapult-forward.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
"""
Infrastructure Automation Script
Automates cloud-native application infrastructure deployment using TCS AI Catapult Forward
to optimize resource allocation and reduce build costs by 20%.

Assumptions:
- TCS AI Catapult Forward API key is required for authentication.
- The script targets a cloud-native deployment with compute and storage resources.
- Build cost optimizations are applied via AI-driven resource recommendations.

Prerequisites:
- Install 'requests' library: pip install requests
"""

import requests
import json
import os

# Constants
API_BASE_URL = "https://api.tcs-catapult-forward.com/v1"
API_KEY = os.getenv("TCS_CATAPULT_API_KEY")  # Set your API key as environment variable
TARGET_REDUCTION_PERCENTAGE = 20  # Cost reduction target

# Error classes
class APIError(Exception):
    """Custom exception for API errors."""
    pass

class ConfigurationError(Exception):
    """Custom exception for configuration errors."""
    pass

# Function to authenticate with TCS AI Catapult Forward API
def authenticate(api_key):
    """
    Authenticate to TCS AI Catapult Forward API.

    Args:
        api_key (str): API key for authentication.

    Returns:
        str: Access token.
    """
    endpoint = f"{API_BASE_URL}/auth"
    payload = {"apiKey": api_key}
    try:
        response = requests.post(endpoint, json=payload)
        response.raise_for_status()
        return response.json().get("accessToken")
    except requests.exceptions.RequestException as e:
        raise APIError(f"Failed to authenticate: {e}")

# Function to analyze and optimize infrastructure costs
def optimize_infrastructure(access_token, application_id):
    """
    Analyze current infrastructure and apply cost optimizations.

    Args:
        access_token (str): Access token for API authorization.
        application_id (str): ID of the cloud-native application.

    Returns:
        dict: Optimization summary.
    """
    endpoint = f"{API_BASE_URL}/optimize"
    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {
        "applicationId": application_id,
        "targetReductionPercentage": TARGET_REDUCTION_PERCENTAGE,
    }
    try:
        response = requests.post(endpoint, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise APIError(f"Failed to optimize infrastructure: {e}")

# Function to apply optimized configuration
def apply_optimized_config(access_token, optimization_id):
    """
    Apply the optimized infrastructure configuration.

    Args:
        access_token (str): Access token for API authorization.
        optimization_id (str): ID of the optimization result.

    Returns:
        dict: Application deployment status.
    """
    endpoint = f"{API_BASE_URL}/deploy"
    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {"optimizationId": optimization_id}
    try:
        response = requests.post(endpoint, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise APIError(f"Failed to apply optimized configuration: {e}")

# Main function
def main(application_id):
    """
    Main function to execute infrastructure automation.

    Args:
        application_id (str): ID of the cloud-native application.
    """
    try:
        # Ensure API key is configured
        if not API_KEY:
            raise ConfigurationError("API key is not configured in environment variables.")

        print("Authenticating with TCS AI Catapult Forward...")
        access_token = authenticate(API_KEY)

        print("Optimizing infrastructure costs...")
        optimization_result = optimize_infrastructure(access_token, application_id)
        optimization_id = optimization_result.get("optimizationId")
        print(f"Optimization ID: {optimization_id}, Details: {optimization_result}")

        print("Applying optimized configuration...")
        deployment_status = apply_optimized_config(access_token, optimization_id)
        print(f"Deployment Status: {deployment_status}")

    except (APIError, ConfigurationError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point
if __name__ == "__main__":
    # Replace with your application ID
    APPLICATION_ID = "your-cloud-native-app-id"
    main(APPLICATION_ID)
```
