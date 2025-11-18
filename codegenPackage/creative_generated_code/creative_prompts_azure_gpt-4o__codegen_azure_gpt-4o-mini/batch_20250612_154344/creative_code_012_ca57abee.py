"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imts.com.pk
Prompt: Write a script to set up and manage virtual private servers (VPS) for a growing business, inspired by the VPS hosting services provided by IMTS.
Generated: DETERMINISTIC_ca57abee263d9d08
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VPSManager:
    def __init__(self, config_file):
        """Initialize the VPS Manager with the configuration file."""
        self.config_file = config_file
        self.load_config()
    
    def load_config(self):
        """Load the VPS configuration from a JSON file."""
        try:
            with open(self.config_file, 'r') as file:
                self.config = json.load(file)
                logging.info("Configuration loaded successfully.")
        except FileNotFoundError:
            logging.error("Configuration file not found.")
            raise
        except json.JSONDecodeError:
            logging.error("Error decoding JSON configuration.")
            raise

    def create_vps(self, vps_name):
        """Create a new Virtual Private Server."""
        try:
            if vps_name in self.config['vps']:
                logging.warning(f"VPS '{vps_name}' already exists.")
                return
            
            # Simulate VPS creation command
            subprocess.run(['vps-create', vps_name], check=True)
            self.config['vps'][vps_name] = {'status': 'running'}
            logging.info(f"VPS '{vps_name}' created successfully.")
            self.save_config()
        except subprocess.CalledProcessError as e:
            logging.error(f"Error creating VPS: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

    def delete_vps(self, vps_name):
        """Delete an existing Virtual Private Server."""
        try:
            if vps_name not in self.config['vps']:
                logging.warning(f"VPS '{vps_name}' does not exist.")
                return
            
            # Simulate VPS deletion command
            subprocess.run(['vps-delete', vps_name], check=True)
            del self.config['vps'][vps_name]
            logging.info(f"VPS '{vps_name}' deleted successfully.")
            self.save_config()
        except subprocess.CalledProcessError as e:
            logging.error(f"Error deleting VPS: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

    def save_config(self):
        """Save the current configuration back to the JSON file."""
        try:
            with open(self.config_file, 'w') as file:
                json.dump(self.config, file, indent=4)
                logging.info("Configuration saved successfully.")
        except Exception as e:
            logging.error(f"Error saving configuration: {e}")

    def list_vps(self):
        """List all existing Virtual Private Servers."""
        if not self.config['vps']:
            logging.info("No VPS instances found.")
            return
        
        logging.info("Current VPS instances:")
        for vps_name, details in self.config['vps'].items():
            logging.info(f" - {vps_name}: Status: {details['status']}")

if __name__ == "__main__":
    # Example usage
    vps_manager = VPSManager('vps_config.json')
    
    # VPS Management Operations
    vps_manager.create_vps('example-vps-1')
    vps_manager.list_vps()
    vps_manager.delete_vps('example-vps-1')
    vps_manager.list_vps()
```
