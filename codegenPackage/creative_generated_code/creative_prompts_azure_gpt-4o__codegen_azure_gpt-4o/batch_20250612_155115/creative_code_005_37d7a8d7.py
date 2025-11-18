"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cliniquerobinpaul.ca
Prompt: Create a guide for integrating Hostinger's hosting plans with a custom website deployment script.
Generated: DETERMINISTIC_37d7a8d7525a9d3c
Batch ID: 20250612_155115
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hostinger.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here is the Python code for integrating Hostinger's hosting plans with a custom website deployment script:

```python
import requests
import json
import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Environment variables for Hostinger API authentication
HOSTINGER_API_KEY = os.getenv("HOSTINGER_API_KEY")
HOSTINGER_BASE_URL = "https://api.hostinger.com"

# Define constants
HEADERS = {
    "Authorization": f"Bearer {HOSTINGER_API_KEY}",
    "Content-Type": "application/json",
}

def list_hosting_plans():
    """
    Fetch and list available hosting plans from Hostinger.

    Returns:
        list: A list of hosting plans.
    """
    endpoint = f"{HOSTINGER_BASE_URL}/v1/plans/hosting"
    try:
        response = requests.get(endpoint, headers=HEADERS)
        response.raise_for_status()
        plans = response.json()
        logging.info("Successfully fetched hosting plans.")
        return plans
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching hosting plans: {e}")
        return []

def deploy_website(domain_name, hosting_plan_id):
    """
    Deploy a custom website to Hostinger under a specific hosting plan.

    Args:
        domain_name (str): The domain name for the deployment.
        hosting_plan_id (str): The ID of the selected hosting plan.

    Returns:
        dict: Deployment status and information.
    """
    endpoint = f"{HOSTINGER_BASE_URL}/v1/websites"
    payload = {
        "domain": domain_name,
        "hosting_plan_id": hosting_plan_id,
    }
    
    try:
        response = requests.post(endpoint, headers=HEADERS, json=payload)
        response.raise_for_status()
        deployment_info = response.json()
        logging.info(f"Website successfully deployed to {domain_name}.")
        return deployment_info
    except requests.exceptions.RequestException as e:
        logging.error(f"Error deploying website: {e}")
        return {}

def main():
    """
    Main function to interact with Hostinger API and deploy websites.
    """
    try:
        # List available hosting plans
        plans = list_hosting_plans()
        if not plans:
            logging.error("No hosting plans available. Exiting.")
            return

        logging.info("Available Hosting Plans:")
        for idx, plan in enumerate(plans, start=1):
            logging.info(f"{idx}: {plan['name']} - {plan['price']}")

        # User input for domain and plan selection
        domain_name = input("Enter the domain name for deployment: ")
        plan_idx = int(input("Choose a hosting plan by entering its number: ")) - 1

        # Validate user selection
        if plan_idx < 0 or plan_idx >= len(plans):
            logging.error("Invalid hosting plan selection. Exiting.")
            return

        selected_plan = plans[plan_idx]
        hosting_plan_id = selected_plan['id']

        # Deploy the website
        deployment_result = deploy_website(domain_name, hosting_plan_id)
        if deployment_result:
            logging.info(f"Deployment Result: {json.dumps(deployment_result, indent=2)}")
        else:
            logging.error("Deployment failed.")

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Instructions
1. Create a `.env` file and add your Hostinger API key:
   ```
   HOSTINGER_API_KEY=your_api_key_here
   ```
2. Install required dependencies:
   ```bash
   pip install requests python-dotenv
   ```
3. Run the script:
   ```bash
   python hostinger_deployment.py
   ```
