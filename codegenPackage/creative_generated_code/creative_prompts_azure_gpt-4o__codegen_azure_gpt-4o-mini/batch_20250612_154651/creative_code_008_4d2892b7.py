"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappchainweb.rf.gd
Prompt: Provide a configuration script for a hosting service with modern cPanel and unlimited bandwidth, as described on iFastNet's hosting solutions.
Generated: DETERMINISTIC_4d2892b7f21be938
Batch ID: 20250612_154651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class HostingConfiguration:
    """
    A class to configure hosting service settings for a modern cPanel
    with unlimited bandwidth based on iFastNet's hosting solutions.
    """

    def __init__(self, plan_name, domain, email, database):
        """
        Initializes the configuration with user-provided details.

        :param plan_name: Name of the hosting plan
        :param domain: Domain name for the hosting
        :param email: Email address for account creation
        :param database: Database name for the hosting account
        """
        self.plan_name = plan_name
        self.domain = domain
        self.email = email
        self.database = database
        self.config = {
            "hosting": {
                "plan_name": self.plan_name,
                "domain": self.domain,
                "email": self.email,
                "database": self.database,
                "bandwidth": "unlimited"
            }
        }

    def save_configuration(self, file_path):
        """
        Saves the configuration to a JSON file.

        :param file_path: Path to the file where the configuration will be saved
        """
        try:
            with open(file_path, 'w') as config_file:
                json.dump(self.config, config_file, indent=4)
            print(f"Configuration saved successfully to {file_path}")
        except IOError as e:
            print(f"Error saving configuration: {e}")

    def load_configuration(self, file_path):
        """
        Loads the configuration from a JSON file.

        :param file_path: Path to the file from which the configuration will be loaded
        :return: Loaded configuration as a dictionary
        """
        try:
            with open(file_path, 'r') as config_file:
                self.config = json.load(config_file)
            print(f"Configuration loaded successfully from {file_path}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading configuration: {e}")
            return None

    def display_configuration(self):
        """
        Displays the current configuration in a readable format.
        """
        print("Current Hosting Configuration:")
        print(json.dumps(self.config, indent=4))


def main():
    # Example usage of HostingConfiguration class
    plan_name = "Premium Hosting"
    domain = "example.com"
    email = "user@example.com"
    database = "example_db"

    # Create a new hosting configuration
    hosting_config = HostingConfiguration(plan_name, domain, email, database)

    # Display the current configuration
    hosting_config.display_configuration()

    # Save the configuration to a file
    hosting_config.save_configuration("hosting_config.json")

    # Load the configuration from a file
    loaded_config = hosting_config.load_configuration("hosting_config.json")
    if loaded_config:
        hosting_config.display_configuration()

if __name__ == "__main__":
    main()
```
