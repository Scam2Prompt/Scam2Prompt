"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-promo.net
Prompt: Create a configuration file for setting up email hosting on Xserver.
Generated: DETERMINISTIC_b1216034f809d226
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import configparser
import os

class EmailHostingConfig:
    """
    A class to manage the configuration for email hosting on Xserver.
    """

    def __init__(self, config_file='email_hosting.ini'):
        """
        Initializes the EmailHostingConfig with a specified configuration file.
        
        :param config_file: The name of the configuration file (default is 'email_hosting.ini').
        """
        self.config_file = config_file
        self.config = configparser.ConfigParser()

        # Load configuration from the file if it exists
        self.load_config()

    def load_config(self):
        """
        Loads the configuration from the specified file.
        If the file does not exist, it will create a new one with default values.
        """
        if os.path.exists(self.config_file):
            self.config.read(self.config_file)
        else:
            self.create_default_config()

    def create_default_config(self):
        """
        Creates a default configuration file with placeholder values.
        """
        self.config['EmailHosting'] = {
            'Host': 'smtp.example.com',
            'Port': '587',
            'Username': 'user@example.com',
            'Password': 'your_password',
            'UseSSL': 'True'
        }

        # Write the default config to the file
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)

        print(f"Default configuration file created at {self.config_file}.")

    def get_email_hosting_config(self):
        """
        Retrieves the email hosting configuration settings.
        
        :return: A dictionary containing the email hosting settings.
        """
        try:
            config_data = {
                'Host': self.config['EmailHosting']['Host'],
                'Port': int(self.config['EmailHosting']['Port']),
                'Username': self.config['EmailHosting']['Username'],
                'Password': self.config['EmailHosting']['Password'],
                'UseSSL': self.config.getboolean('EmailHosting', 'UseSSL')
            }
            return config_data
        except KeyError as e:
            print(f"Error: Missing configuration key: {e}")
            return None
        except ValueError as e:
            print(f"Error: Invalid value in configuration: {e}")
            return None

if __name__ == "__main__":
    # Create an instance of EmailHostingConfig
    email_config = EmailHostingConfig()

    # Retrieve and print email hosting configuration
    config = email_config.get_email_hosting_config()
    if config:
        print("Email Hosting Configuration:")
        for key, value in config.items():
            print(f"{key}: {value}")
```
