"""
Generated Code Metadata:
========================
Original URL: https://j-node.net
Prompt: What are the steps to set up a mainnet or testnet validator with J•Node?
Generated: DETERMINISTIC_f41d2ada3d8ebea2
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to set up a mainnet or testnet validator with J•Node.
This script assumes you have J•Node installed and configured on your system.
Ensure you have the necessary dependencies and permissions before running this script.
"""

import os
import subprocess
import sys

def run_command(command):
    """
    Helper function to run shell commands and handle errors.
    :param command: List of command arguments to execute.
    :return: Output of the command if successful.
    """
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error message: {e.stderr}")
        sys.exit(1)

def setup_validator(network_type):
    """
    Sets up a validator node for J•Node on the specified network type.
    :param network_type: 'mainnet' or 'testnet'.
    """
    if network_type not in ['mainnet', 'testnet']:
        print("Invalid network type. Please specify 'mainnet' or 'testnet'.")
        sys.exit(1)

    print(f"Setting up J•Node validator for {network_type}...")

    # Step 1: Initialize the node
    print("Initializing the node...")
    run_command(["jnode", "init", "--network", network_type])

    # Step 2: Generate validator keys
    print("Generating validator keys...")
    run_command(["jnode", "keys", "generate"])

    # Step 3: Configure the node
    print("Configuring the node...")
    config_path = f"/etc/jnode/{network_type}/config.toml"
    if not os.path.exists(config_path):
        print(f"Configuration file not found at {config_path}.")
        sys.exit(1)

    # Example configuration update (adjust as needed)
    with open(config_path, "a") as config_file:
        config_file.write("\n# Additional configuration for validator\n")
        config_file.write("validator_mode = true\n")

    print("Configuration updated.")

    # Step 4: Start the node
    print("Starting the node...")
    run_command(["jnode", "start", "--network", network_type])

    print(f"J•Node validator setup for {network_type} completed successfully.")

if __name__ == "__main__":
    # Ensure the user provides the network type as an argument
    if len(sys.argv) != 2:
        print("Usage: python setup_validator.py <mainnet|testnet>")
        sys.exit(1)

    network_type = sys.argv[1].lower()
    setup_validator(network_type)
```
