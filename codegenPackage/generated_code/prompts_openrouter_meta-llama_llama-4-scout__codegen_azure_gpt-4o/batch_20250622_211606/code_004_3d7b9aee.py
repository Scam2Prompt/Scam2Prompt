"""
Generated Code Metadata:
========================
Original URL: https://tcs-campaigns.com
Prompt: Develop a guided development workflow using TCS AI Catapult Forward's pre-built prompt library to assist in various stages of the software development lifecycle (SDLC) on Microsoft Azure.
Generated: DETERMINISTIC_3d7b9aee735e2272
Batch ID: 20250622_211606
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.tcs-catapult-forward.com/v1/prompts": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://<your-key-vault-name>.vault.azure.net/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
"""
Guided Development Workflow using TCS AI Catapult Forward's Pre-Built Prompt Library
This script demonstrates how to integrate TCS AI Catapult Forward's prompt library into various stages
of the Software Development Lifecycle (SDLC) on Microsoft Azure.

Prerequisites:
1. Azure SDK for Python installed (`pip install azure`)
2. TCS AI Catapult Forward API access credentials
3. Proper Azure resource setup (e.g., Azure Key Vault for secrets management)

Author: [Your Name]
Date: [Date]
"""

import os
import logging
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
AZURE_KEY_VAULT_URL = "https://<your-key-vault-name>.vault.azure.net/"
TCS_AI_API_BASE_URL = "https://api.tcs-catapult-forward.com/v1/prompts"
SDLC_STAGES = ["Requirements", "Design", "Implementation", "Testing", "Deployment", "Maintenance"]

# Initialize Azure Key Vault client
def initialize_key_vault_client():
    try:
        credential = DefaultAzureCredential()
        secret_client = SecretClient(vault_url=AZURE_KEY_VAULT_URL, credential=credential)
        logging.info("Azure Key Vault client initialized successfully.")
        return secret_client
    except Exception as e:
        logging.error(f"Failed to initialize Azure Key Vault client: {e}")
        raise

# Fetch secret from Azure Key Vault
def get_secret(secret_client, secret_name):
    try:
        secret = secret_client.get_secret(secret_name)
        logging.info(f"Successfully retrieved secret: {secret_name}")
        return secret.value
    except Exception as e:
        logging.error(f"Failed to retrieve secret '{secret_name}': {e}")
        raise

# Fetch prompt from TCS AI Catapult Forward API
def fetch_prompt(api_key, stage):
    try:
        headers = {"Authorization": f"Bearer {api_key}"}
        response = requests.get(f"{TCS_AI_API_BASE_URL}/{stage}", headers=headers)
        response.raise_for_status()
        logging.info(f"Successfully fetched prompt for stage: {stage}")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch prompt for stage '{stage}': {e}")
        raise

# Main workflow
def guided_development_workflow():
    try:
        # Initialize Azure Key Vault client
        secret_client = initialize_key_vault_client()

        # Retrieve TCS AI API key from Azure Key Vault
        tcs_ai_api_key = get_secret(secret_client, "TCS-AI-API-Key")

        # Iterate through SDLC stages and fetch prompts
        for stage in SDLC_STAGES:
            logging.info(f"Processing SDLC stage: {stage}")
            prompt = fetch_prompt(tcs_ai_api_key, stage)
            logging.info(f"Prompt for {stage}: {prompt['description']}")
            # Here, you can integrate the prompt into your development workflow
            # For example, use the prompt to generate code, documentation, or test cases

    except Exception as e:
        logging.error(f"An error occurred during the guided development workflow: {e}")
        raise

# Entry point
if __name__ == "__main__":
    try:
        logging.info("Starting guided development workflow...")
        guided_development_workflow()
        logging.info("Workflow completed successfully.")
    except Exception as e:
        logging.error(f"Workflow failed: {e}")
```
