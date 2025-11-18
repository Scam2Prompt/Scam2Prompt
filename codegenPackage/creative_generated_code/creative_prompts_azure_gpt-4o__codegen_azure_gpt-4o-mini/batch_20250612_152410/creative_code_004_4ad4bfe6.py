"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genesis-dymnesion.pages.dev
Prompt: Create a step-by-step guide for deploying a RollApp with maximum flexibility and minimum overhead using Dymension's tools.
Generated: DETERMINISTIC_4ad4bfe6bae825a1
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import os
import subprocess
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_command_success(command):
    """Check if a command executed successfully."""
    try:
        subprocess.check_call(command, shell=True)
        logging.info(f"Command executed successfully: {command}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {command}\nError: {e}")
        raise

def deploy_rollapp(rollapp_name, configuration):
    """
    Deploy a RollApp using Dymension's tools.

    Parameters:
    rollapp_name (str): Name of the RollApp to deploy.
    configuration (dict): Configuration settings for the deployment.

    Raises:
    Exception: If the deployment fails at any step.
    """
    
    # Step 1: Set up environment variables
    os.environ['ROLLAPP_NAME'] = rollapp_name
    logging.info(f"Environment variable ROLLAPP_NAME set to {rollapp_name}")

    # Step 2: Initialize the RollApp
    command_init = f"dymension init {rollapp_name}"
    check_command_success(command_init)

    # Step 3: Configure RollApp
    config_file_path = f"{rollapp_name}/config.json"
    
    # Create config.json using the provided configuration dict
    with open(config_file_path, 'w') as config_file:
        json.dump(configuration, config_file)
        logging.info(f"Configuration file created at {config_file_path}")

    # Step 4: Build the RollApp
    command_build = f"dymension build {rollapp_name}"
    check_command_success(command_build)

    # Step 5: Deploy the RollApp
    command_deploy = f"dymension deploy {rollapp_name}"
    check_command_success(command_deploy)

    logging.info(f"RollApp '{rollapp_name}' deployed successfully!")

if __name__ == "__main__":
    # Example configuration for deployment
    example_configuration = {
        "version": "1.0",
        "settings": {
            "max_connections": 100,
            "timeout": 30,
        }
    }

    try:
        # Deploy the RollApp with the example configuration
        deploy_rollapp("example_rollapp", example_configuration)
    except Exception as e:
        logging.error(f"Deployment failed: {e}")
```
