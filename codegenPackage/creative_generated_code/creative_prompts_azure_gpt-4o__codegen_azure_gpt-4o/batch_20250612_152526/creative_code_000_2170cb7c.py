"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digisou-ltd.com
Prompt: Write Python code to integrate multiple existing software systems seamlessly, referencing system integration strategies discussed on DigiSou's website.
Generated: DETERMINISTIC_2170cb7c6e0ecf14
Batch ID: 20250612_152526
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.system1.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.system2.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json

# System Integration Class
class SystemIntegrator:
    """
    A class to handle seamless integration between multiple software systems.
    This implementation uses RESTful APIs to connect systems, following best practices
    for system integration strategies.
    """

    def __init__(self, system_configs):
        """
        Initialize the SystemIntegrator with configurations for each system.
        
        Args:
        system_configs (dict): A dictionary containing API details for the systems.
        Example:
            {
                "system1": {
                    "base_url": "https://api.system1.com",
                    "api_key": "xyz123"
                },
                "system2": {
                    "base_url": "https://api.system2.com",
                    "api_key": "abc456"
                }
            }
        """
        self.system_configs = system_configs

    def fetch_data_from_system(self, system_name, endpoint):
        """
        Fetch data from the specified system using its API.
        
        Args:
        system_name (str): The name of the system to retrieve data from.
        endpoint (str): The API endpoint to fetch data from.
        
        Returns:
        dict: The data retrieved from the system.
        """
        if system_name not in self.system_configs:
            raise ValueError(f"Configuration for {system_name} does not exist.")

        try:
            config = self.system_configs[system_name]
            url = f"{config['base_url']}/{endpoint}"
            headers = {"Authorization": f"Bearer {config['api_key']}"}
            
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise exception for HTTP errors
            
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {system_name}: {e}")
            return {}

    def send_data_to_system(self, system_name, endpoint, data):
        """
        Send data to the specified system using its API.
        
        Args:
        system_name (str): The name of the system to send data to.
        endpoint (str): The API endpoint to send data to.
        data (dict): The data to send.
        
        Returns:
        dict: The response from the system.
        """
        if system_name not in self.system_configs:
            raise ValueError(f"Configuration for {system_name} does not exist.")

        try:
            config = self.system_configs[system_name]
            url = f"{config['base_url']}/{endpoint}"
            headers = {
                "Authorization": f"Bearer {config['api_key']}",
                "Content-Type": "application/json"
            }
            
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()  # Raise exception for HTTP errors
            
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error sending data to {system_name}: {e}")
            return {}

    def integrate_systems(self, source_system, target_system, source_endpoint, target_endpoint):
        """
        Integrate two systems by fetching data from the source system and sending it to the target system.
        
        Args:
        source_system (str): The name of the source system.
        target_system (str): The name of the target system.
        source_endpoint (str): The API endpoint to fetch data from the source system.
        target_endpoint (str): The API endpoint to send data to the target system.
        
        Returns:
        bool: True if integration is successful, False otherwise.
        """
        try:
            # Fetch data from source system
            data = self.fetch_data_from_system(source_system, source_endpoint)
            if not data:  # If no data retrieved, return failure
                print(f"No data retrieved from {source_system}.")
                return False
            
            # Send data to target system
            response = self.send_data_to_system(target_system, target_endpoint, data)
            if response:  # Check for response success
                print(f"Integration from {source_system} to {target_system} was successful.")
                return True
            else:
                print(f"Failed to send data to {target_system}.")
                return False
        except Exception as e:
            print(f"Error during integration: {e}")
            return False


# Example Usage
if __name__ == "__main__":
    # Sample system configurations
    system_configs = {
        "system1": {
            "base_url": "https://api.system1.com",
            "api_key": "xyz123"
        },
        "system2": {
            "base_url": "https://api.system2.com",
            "api_key": "abc456"
        }
    }

    # Initialize the integrator
    integrator = SystemIntegrator(system_configs)

    # Perform integration
    source_system = "system1"
    target_system = "system2"
    source_endpoint = "data/source_endpoint"
    target_endpoint = "data/target_endpoint"

    success = integrator.integrate_systems(source_system, target_system, source_endpoint, target_endpoint)
    if success:
        print("Systems integrated successfully.")
    else:
        print("System integration failed.")
```
