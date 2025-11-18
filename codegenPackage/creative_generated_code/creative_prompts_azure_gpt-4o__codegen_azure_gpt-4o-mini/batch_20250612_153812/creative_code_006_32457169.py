"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-doublezero.com
Prompt: Provide a step-by-step guide for setting up a testnet beta for a blockchain system using DoubleZero's high-performance networking principles.
Generated: DETERMINISTIC_32457169ebc79a5e
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestnetSetup:
    def __init__(self, network_name, config_file):
        """
        Initialize the TestnetSetup with a network name and configuration file.

        Args:
            network_name (str): The name of the testnet network to be set up.
            config_file (str): The path to the configuration file for the network.
        """
        self.network_name = network_name
        self.config_file = config_file
        self.validate_config()

    def validate_config(self):
        """Validate the provided configuration file."""
        if not os.path.isfile(self.config_file):
            logging.error(f"Configuration file {self.config_file} not found.")
            sys.exit(1)

    def start_network(self):
        """Start the blockchain testnet based on the configuration."""
        try:
            logging.info(f"Starting testnet: {self.network_name} using config: {self.config_file}")
            subprocess.run(["blockchain-node", "start", "--config", self.config_file], check=True)
            logging.info("Testnet started successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to start the testnet: {e}")
            sys.exit(1)

    def stop_network(self):
        """Stop the blockchain testnet."""
        try:
            logging.info(f"Stopping testnet: {self.network_name}")
            subprocess.run(["blockchain-node", "stop"], check=True)
            logging.info("Testnet stopped successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to stop the testnet: {e}")
            sys.exit(1)

def main():
    """Main function to execute the testnet setup."""
    NETWORK_NAME = "DoubleZeroTestNet"
    CONFIG_FILE = "testnet_config.yaml"

    # Create a TestnetSetup instance
    testnet = TestnetSetup(NETWORK_NAME, CONFIG_FILE)

    # Start the testnet
    testnet.start_network()

    # Here you would typically run the network for a while
    # For demonstration, we'll just print a message to simulate running
    try:
        logging.info("Testnet is running. Press Ctrl+C to stop.")
        while True:
            pass  # Keep the testnet running
    except KeyboardInterrupt:
        logging.info("Stopping the testnet...")
        testnet.stop_network()

if __name__ == "__main__":
    main()
```
