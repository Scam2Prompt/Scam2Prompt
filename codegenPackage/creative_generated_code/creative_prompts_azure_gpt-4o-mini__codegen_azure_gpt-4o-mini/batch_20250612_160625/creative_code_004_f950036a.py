"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartvalidation.net
Prompt: Create a sample configuration for a VPS hosting environment that utilizes the scalable resources mentioned on Smart Validation's website.
Generated: DETERMINISTIC_f950036ac4ac4f0e
Batch ID: 20250612_160625
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

class VPSConfig:
    """
    A class to represent the configuration for a VPS hosting environment.
    It includes parameters for scalable resources as defined in the
    Smart Validation guidelines.
    """

    def __init__(self, instance_type, cpu_cores, memory_gb, storage_gb, region):
        """
        Initializes the VPS configuration with the given parameters.
        
        Parameters:
        - instance_type (str): The type of VPS instance (e.g., 't2.micro')
        - cpu_cores (int): Number of CPU cores allocated
        - memory_gb (int): Amount of RAM in gigabytes
        - storage_gb (int): Amount of storage in gigabytes
        - region (str): The geographical region for the server
        """
        self.instance_type = instance_type
        self.cpu_cores = cpu_cores
        self.memory_gb = memory_gb
        self.storage_gb = storage_gb
        self.region = region

    def to_json(self):
        """
        Converts the VPS configuration into a JSON format string.
        
        Returns:
        - str: JSON representation of the VPS configuration
        """
        return json.dumps(self.__dict__, indent=4)

    def validate(self):
        """
        Validates the VPS configuration to ensure values are within acceptable ranges.
        
        Raises:
        - ValueError: If any configuration value is out of range
        """
        if self.cpu_cores <= 0:
            raise ValueError("CPU cores must be greater than 0.")
        if self.memory_gb <= 0:
            raise ValueError("Memory must be greater than 0.")
        if self.storage_gb <= 0:
            raise ValueError("Storage must be greater than 0.")
        allowed_regions = ['us-east', 'us-west', 'eu-central', 'ap-south']
        if self.region not in allowed_regions:
            raise ValueError(f"Region must be one of {allowed_regions}.")

def main():
    """
    Main function to create a VPS configuration and display it.
    Handles exceptions that may arise during the configuration process.
    """
    try:
        # Sample VPS configuration parameters
        vps_config = VPSConfig(
            instance_type='t2.micro',
            cpu_cores=2,
            memory_gb=4,
            storage_gb=50,
            region='us-east'
        )
        
        # Validate the configuration
        vps_config.validate()

        # Convert the configuration to JSON and print it
        config_json = vps_config.to_json()
        print("VPS Configuration:\n", config_json)

    except ValueError as e:
        print(f"Configuration Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
