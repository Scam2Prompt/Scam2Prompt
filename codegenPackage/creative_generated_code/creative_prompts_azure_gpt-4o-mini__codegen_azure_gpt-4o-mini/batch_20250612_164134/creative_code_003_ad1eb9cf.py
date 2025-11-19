"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maindapps.42web.io
Prompt: Create a configuration file for a web application hosted on iFastNet that takes advantage of unlimited disk space and multiple email accounts.
Generated: DETERMINISTIC_ad1eb9cf76400681
Batch ID: 20250612_164134
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

class WebAppConfig:
    """Configuration class for a web application hosted on iFastNet."""

    def __init__(self, app_name, disk_space, email_accounts):
        """
        Initializes the configuration for the web application.

        :param app_name: Name of the web application
        :param disk_space: Description of the disk space allocation
        :param email_accounts: A list of email accounts for the application
        """
        self.app_name = app_name
        self.disk_space = disk_space
        self.email_accounts = email_accounts

    def to_dict(self):
        """Converts the configuration to a dictionary for easy serialization."""
        return {
            'app_name': self.app_name,
            'disk_space': self.disk_space,
            'email_accounts': self.email_accounts
        }

    def save_to_file(self, file_path):
        """Saves the configuration to a JSON file.

        :param file_path: Path to the file where the configuration will be saved
        """
        try:
            with open(file_path, 'w') as config_file:
                json.dump(self.to_dict(), config_file, indent=4)
            print(f"Configuration saved successfully to {file_path}")
        except IOError as e:
            print(f"Error saving configuration to file: {e}")

def main():
    """Main function to create and save the web application configuration."""
    # Configuration parameters
    app_name = "MyWebApp"
    disk_space = "Unlimited disk space provided by iFastNet"
    email_accounts = ["admin@mywebapp.com", "support@mywebapp.com", "info@mywebapp.com"]

    # Create a configuration instance
    config = WebAppConfig(app_name, disk_space, email_accounts)

    # Define the configuration file path
    config_file_path = os.path.join(os.getcwd(), 'webapp_config.json')

    # Save the configuration to the file
    config.save_to_file(config_file_path)

if __name__ == "__main__":
    main()
```
