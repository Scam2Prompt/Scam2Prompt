"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophon.pages.dev
Prompt: Generate code for setting up a Sui Full Node and validator selection process, incorporating insights from the SophonLabs article "Sui Full Node & Validator Selection Announcement."
Generated: DETERMINISTIC_82c327d6eceb863d
Batch ID: 20250612_145455
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
import json
import logging

# Setting up logging configuration
logging.basicConfig(level=logging.INFO)

class SuiFullNode:
    def __init__(self, node_dir, config_file):
        """
        Initializes the Sui Full Node instance.

        :param node_dir: Directory where the full node will be set up
        :param config_file: Path to the configuration file
        """
        self.node_dir = node_dir
        self.config_file = config_file

    def setup_node(self):
        """
        Sets up the Sui full node by initializing the required directory 
        and copying the necessary configuration file.
        """
        try:
            # Create the node directory if it doesn't exist
            if not os.path.exists(self.node_dir):
                os.makedirs(self.node_dir)
                logging.info(f"Node directory created at {self.node_dir}")

            # Copy configuration file to node directory
            self._copy_config_file()
            logging.info("Node setup completed successfully.")
        except Exception as e:
            logging.error(f"Error setting up node: {str(e)}")
            raise

    def _copy_config_file(self):
        """ Copies the configuration file to the node directory. """
        if os.path.exists(self.config_file):
            config_destination = os.path.join(self.node_dir, 'sui_config.json')
            with open(self.config_file, 'r') as src, open(config_destination, 'w') as dst:
                dst.write(src.read())
            logging.info(f"Configuration file copied to {config_destination}")
        else:
            raise FileNotFoundError(f"Configuration file not found: {self.config_file}")

    def start_node(self):
        """
        Starts the Sui full node using a subprocess.
        """
        try:
            command = ["sui", "start", "--config", os.path.join(self.node_dir, 'sui_config.json')]
            logging.info("Starting the Sui full node...")
            subprocess.run(command, check=True)
            logging.info("Sui full node started successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to start Sui full node: {str(e)}")
            raise

class ValidatorSelection:
    def __init__(self, validators_file):
        """
        Initializes the Validator Selection process.

        :param validators_file: Path to the file containing the list of validators
        """
        self.validators_file = validators_file

    def select_validators(self):
        """
        Reads the list of validators and selects a subset based on some criteria.
        Here, we assume a simple selection process based on availability.
        """
        try:
            with open(self.validators_file, 'r') as f:
                validators = json.load(f)

            # Selecting active validators (for this example, we assume a simple boolean flag)
            selected_validators = [v for v in validators if v.get('is_active', False)]
            logging.info(f"Selected {len(selected_validators)} active validators.")
            return selected_validators
        except FileNotFoundError:
            logging.error(f"Validators file not found: {self.validators_file}")
            raise
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from validators file.")
            raise

if __name__ == "__main__":
    # Define paths for the node directory and configuration file
    NODE_DIRECTORY = "./sui_node"
    CONFIG_FILE_PATH = "./sui_config.json"
    VALIDATORS_FILE_PATH = "./validators.json"

    # Setting up the Sui full node
    node = SuiFullNode(NODE_DIRECTORY, CONFIG_FILE_PATH)
    node.setup_node()
    node.start_node()

    # Selecting validators
    validator_selection = ValidatorSelection(VALIDATORS_FILE_PATH)
    active_validators = validator_selection.select_validators()
```
