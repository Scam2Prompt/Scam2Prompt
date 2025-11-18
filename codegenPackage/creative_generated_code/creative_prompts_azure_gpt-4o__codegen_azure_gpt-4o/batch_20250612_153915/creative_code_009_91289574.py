"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-foundation.com
Prompt: Write a tutorial for setting up a TON node and connecting it to the blockchain network programmatically.
Generated: DETERMINISTIC_91289574eecf2fc9
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script sets up a TON (The Open Network) node and connects it to the blockchain network.
It demonstrates how to programmatically interact with the TON blockchain using the tonlib library.
Ensure you have tonlib installed and the required dependencies before running this script.
"""

import os
import json
import subprocess
import logging
from pathlib import Path

# Configure logging for the script
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Paths to TON binaries and files
TON_BIN_PATH = "/path/to/ton/bin"
TON_CONFIG_PATH = "/path/to/config.json"
TON_KEY_PATH = "/path/to/ton-private-key.json"
TON_WORK_DIR = "/path/to/ton/workdir"

# Ensure paths exist
Path(TON_WORK_DIR).mkdir(parents=True, exist_ok=True)

# Function to load the TON configuration
def load_config():
    try:
        with open(TON_CONFIG_PATH, 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        logging.error(f"TON configuration file not found: {TON_CONFIG_PATH}")
        raise
    except json.JSONDecodeError:
        logging.error("Failed to parse TON configuration file.")
        raise

# Function to create the private key for the node
def generate_ton_key():
    try:
        logging.info("Generating TON private key...")
        subprocess.run(
            [os.path.join(TON_BIN_PATH, "generate-random-id"), "-m", "4096"],
            check=True
        )
        logging.info(f"TON private key generated at {TON_KEY_PATH}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error during key generation: {e}")
        raise

# Function to start the TON node
def start_ton_node():
    try:
        logging.info("Starting TON node...")
        subprocess.run(
            [
                os.path.join(TON_BIN_PATH, "lite-client"),
                "-C", TON_CONFIG_PATH,
                "-k", TON_KEY_PATH,
                "-w", TON_WORK_DIR
            ],
            check=True
        )
        logging.info("TON node started successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error while starting TON node: {e}")
        raise

# Function to test connection to the TON blockchain
def test_ton_connection():
    try:
        logging.info("Testing TON node connection...")
        subprocess.run(
            [
                os.path.join(TON_BIN_PATH, "lite-client"),
                "-C", TON_CONFIG_PATH,
                "-k", TON_KEY_PATH,
                "-w", TON_WORK_DIR,
                "-c", "getconfig 1"
            ],
            check=True
        )
        logging.info("TON node successfully connected to the blockchain.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error while testing TON node connection: {e}")
        raise

# Main function
def main():
    """
    Main entry point for the script. Sets up a TON node and connects it to the blockchain network.
    """
    try:
        # Load the TON configuration
        config = load_config()
        logging.info("TON configuration loaded successfully.")
        
        # Generate TON private key
        if not Path(TON_KEY_PATH).exists():
            generate_ton_key()
        else:
            logging.info(f"TON private key already exists at {TON_KEY_PATH}")
        
        # Start the TON node
        start_ton_node()
        
        # Test connection to the TON blockchain
        test_ton_connection()
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

# Run the script
if __name__ == "__main__":
    main()
```

### Notes:
- Replace `/path/to/...` with the actual paths to the TON binaries, configuration file, and working directories.
- Ensure you have TON binaries and tonlib installed on your system before running this script.
- Make sure to run the script with the necessary permissions to manage files and processes.
