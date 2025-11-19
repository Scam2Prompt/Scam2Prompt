"""
Generated Code Metadata:
========================
Original URL: https://upgrading-ethereum.info
Prompt: What are the key differences between the Capella, Bellatrix, and Altair editions of Ethereum's consensus layer upgrades as outlined in the Upgrading Ethereum documentation?
Generated: DETERMINISTIC_8082f65f55adf1e2
Batch ID: 20250612_135957
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests

class EthereumUpgrade:
    """
    A class to represent Ethereum's consensus layer upgrades.
    """

    def __init__(self):
        """
        Initializes the EthereumUpgrade class with the upgrade data.
        """
        self.upgrades = {
            "Capella": {
                "description": "Capella is the first upgrade of the consensus layer, focusing on the transition to proof-of-stake.",
                "key_features": [
                    "Introduction of the Beacon Chain.",
                    "Transition from proof-of-work to proof-of-stake.",
                    "Improved security and scalability."
                ]
            },
            "Bellatrix": {
                "description": "Bellatrix is the second upgrade, enhancing the capabilities of the proof-of-stake mechanism.",
                "key_features": [
                    "Improvements to validator performance.",
                    "Enhanced network efficiency.",
                    "Support for shard chains."
                ]
            },
            "Altair": {
                "description": "Altair is the third upgrade, which introduces several optimizations and improvements.",
                "key_features": [
                    "Increased rewards for validators.",
                    "Penalties for inactivity.",
                    "Improvements to the overall user experience."
                ]
            }
        }

    def get_upgrade_info(self, upgrade_name):
        """
        Retrieves information about a specific Ethereum upgrade.

        Parameters:
        upgrade_name (str): The name of the upgrade to retrieve information for.

        Returns:
        dict: A dictionary containing the upgrade's description and key features.
        """
        try:
            upgrade_info = self.upgrades.get(upgrade_name)
            if upgrade_info is None:
                raise ValueError(f"Upgrade '{upgrade_name}' not found.")
            return upgrade_info
        except Exception as e:
            print(f"Error retrieving upgrade info: {e}")
            return None

    def display_upgrade_info(self, upgrade_name):
        """
        Displays the information of a specific Ethereum upgrade.

        Parameters:
        upgrade_name (str): The name of the upgrade to display information for.
        """
        upgrade_info = self.get_upgrade_info(upgrade_name)
        if upgrade_info:
            print(f"Upgrade: {upgrade_name}")
            print(f"Description: {upgrade_info['description']}")
            print("Key Features:")
            for feature in upgrade_info['key_features']:
                print(f"- {feature}")
        else:
            print("No information available.")

if __name__ == "__main__":
    # Create an instance of the EthereumUpgrade class
    ethereum_upgrade = EthereumUpgrade()

    # Display information for each upgrade
    for upgrade in ethereum_upgrade.upgrades.keys():
        ethereum_upgrade.display_upgrade_info(upgrade)
```
