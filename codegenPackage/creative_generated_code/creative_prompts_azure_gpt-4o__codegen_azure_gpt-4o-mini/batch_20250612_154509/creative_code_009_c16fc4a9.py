"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rtspos.net
Prompt: Provide a solution for implementing enterprise features in phone systems at an affordable cost, referencing the IP-PBX systems offered by Retail Tech Solutions.
Generated: DETERMINISTIC_c16fc4a9804d9042
Batch ID: 20250612_154509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import Dict, Any

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class IPPBXSystem:
    """
    Class representing an IP-PBX System offered by Retail Tech Solutions.
    This class encapsulates methods to manage enterprise features in phone systems.
    """

    def __init__(self, system_name: str, cost: float):
        """
        Initializes an instance of the IPPBXSystem.
        
        :param system_name: Name of the IP-PBX system
        :param cost: Cost of the IP-PBX system
        """
        self.system_name = system_name
        self.cost = cost
        self.features = {}

    def add_feature(self, feature_name: str, feature_details: Dict[str, Any]) -> None:
        """
        Adds a new feature to the IP-PBX system.
        
        :param feature_name: The name of the feature
        :param feature_details: A dictionary containing details of the feature
        """
        self.features[feature_name] = feature_details
        logging.info(f"Feature '{feature_name}' added to {self.system_name}.")

    def remove_feature(self, feature_name: str) -> None:
        """
        Removes a feature from the IP-PBX system.
        
        :param feature_name: The name of the feature to be removed
        """
        if feature_name in self.features:
            del self.features[feature_name]
            logging.info(f"Feature '{feature_name}' removed from {self.system_name}.")
        else:
            logging.error(f"Feature '{feature_name}' not found in {self.system_name}.")

    def get_features(self) -> Dict[str, Any]:
        """
        Returns the list of features in the IP-PBX system.
        
        :return: A dictionary of features
        """
        return self.features

    def to_json(self) -> str:
        """
        Serializes the IP-PBX system to a JSON string.
        
        :return: JSON string representation of the IP-PBX system
        """
        try:
            return json.dumps({
                'system_name': self.system_name,
                'cost': self.cost,
                'features': self.features
            }, indent=4)
        except (TypeError, ValueError) as e:
            logging.error(f"Error serializing to JSON: {e}")
            return '{}'

def main():
    """
    Main function to demonstrate the usage of the IPPBXSystem class.
    """
    try:
        # Creating an instance of IPPBXSystem
        ip_pbx = IPPBXSystem(system_name='Retail Tech IP-PBX', cost=499.99)

        # Adding features
        ip_pbx.add_feature('Voicemail', {'storage': '50 messages', 'notifications': 'Email'})
        ip_pbx.add_feature('Call Forwarding', {'type': 'Immediate', 'conditions': 'All calls'})

        # Getting features
        features = ip_pbx.get_features()
        logging.info(f"Current features: {features}")

        # Serializing to JSON
        json_output = ip_pbx.to_json()
        logging.info(f"IP-PBX System JSON: {json_output}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
