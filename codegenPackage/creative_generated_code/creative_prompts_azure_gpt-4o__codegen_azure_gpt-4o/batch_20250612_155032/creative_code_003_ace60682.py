"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nbnm.pages.dev
Prompt: Create a detailed deployment script for launching a protocol on the Sonic testnet and transitioning it to the Sonic mainnet within the required 7-day window.
Generated: DETERMINISTIC_ace606827addf2a2
Batch ID: 20250612_155032
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
#!/usr/bin/env python3

"""
Deployment Script for Protocol Launch on Sonic Testnet and Mainnet

This script automates the deployment of a protocol to the Sonic testnet 
followed by transitioning it to the Sonic mainnet within a 7-day window.

Requirements:
- Python 3.x
- Sonic SDK (installed via pip)
- Configuration files for testnet and mainnet

Usage:
Run `python deploy_protocol.py` to execute the deployment process.

Author: Expert Programmer
"""

import sys
import time
import logging
from sonic_sdk import SonicClient, DeploymentError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constants
TESTNET_CONFIG_PATH = "config/testnet_config.json"
MAINNET_CONFIG_PATH = "config/mainnet_config.json"
DEPLOYMENT_TIMEOUT = 7 * 24 * 60 * 60  # 7 days in seconds

# Functions
def load_config(config_path):
    """
    Loads a JSON configuration file.

    Args:
        config_path (str): Path to the configuration file.

    Returns:
        dict: Parsed configuration data.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file contents are invalid JSON.
    """
    try:
        with open(config_path, 'r') as file:
            import json
            return json.load(file)
    except FileNotFoundError as e:
        logging.error(f"Configuration file not found: {config_path}")
        raise e
    except ValueError as e:
        logging.error(f"Invalid JSON in configuration file: {config_path}")
        raise e


def deploy_to_testnet(client, config):
    """
    Deploys protocol to Sonic testnet.

    Args:
        client (SonicClient): Sonic SDK client instance.
        config (dict): Configuration for testnet deployment.

    Returns:
        str: Deployment ID for the testnet deployment.

    Raises:
        DeploymentError: If the deployment fails.
    """
    try:
        logging.info("Starting deployment to testnet...")
        deployment_id = client.deploy(config)
        logging.info(f"Testnet deployment successful. Deployment ID: {deployment_id}")
        return deployment_id
    except DeploymentError as e:
        logging.error(f"Testnet deployment failed: {e}")
        raise e


def transition_to_mainnet(client, config, testnet_deployment_id):
    """
    Transitions protocol from Sonic testnet to mainnet.

    Args:
        client (SonicClient): Sonic SDK client instance.
        config (dict): Configuration for mainnet deployment.
        testnet_deployment_id (str): Deployment ID from testnet.

    Returns:
        str: Deployment ID for the mainnet deployment.

    Raises:
        DeploymentError: If the transition fails.
    """
    try:
        logging.info("Starting transition from testnet to mainnet...")
        deployment_id = client.transition(testnet_deployment_id, config)
        logging.info(f"Mainnet transition successful. Deployment ID: {deployment_id}")
        return deployment_id
    except DeploymentError as e:
        logging.error(f"Mainnet transition failed: {e}")
        raise e


def main():
    """
    Main function to execute the deployment process.
    """
    try:
        # Load configurations
        logging.info("Loading testnet configuration...")
        testnet_config = load_config(TESTNET_CONFIG_PATH)
        
        logging.info("Loading mainnet configuration...")
        mainnet_config = load_config(MAINNET_CONFIG_PATH)

        # Initialize Sonic SDK client
        logging.info("Initializing Sonic SDK client...")
        client = SonicClient()

        # Deploy to testnet
        testnet_deployment_id = deploy_to_testnet(client, testnet_config)

        # Wait for the required 7-day window before transitioning
        logging.info(f"Waiting for the 7-day window before transitioning to mainnet...")
        time.sleep(DEPLOYMENT_TIMEOUT)

        # Transition to mainnet
        mainnet_deployment_id = transition_to_mainnet(client, mainnet_config, testnet_deployment_id)

        logging.info(f"Deployment to mainnet completed successfully. Mainnet Deployment ID: {mainnet_deployment_id}")

    except Exception as e:
        logging.error(f"Deployment process encountered an error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
