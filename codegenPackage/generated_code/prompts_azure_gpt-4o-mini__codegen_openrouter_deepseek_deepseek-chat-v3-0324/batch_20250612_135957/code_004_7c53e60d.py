"""
Generated Code Metadata:
========================
Original URL: https://upgrading-ethereum.info
Prompt: Create a script that summarizes the historical significance of the earlier editions of Ethereum's upgrades mentioned in the Eth2 Book.
Generated: DETERMINISTIC_7c53e60d2c05718f
Batch ID: 20250612_135957
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List

class EthereumUpgradeSummarizer:
    """
    A class to summarize the historical significance of Ethereum's earlier upgrades.
    """
    
    def __init__(self):
        self.upgrades = {
            "Frontier": {
                "date": "July 30, 2015",
                "significance": "First live release of Ethereum, marking the start of the network."
            },
            "Homestead": {
                "date": "March 14, 2016",
                "significance": "Introduced improvements to transaction processing and gas pricing."
            },
            "Metropolis (Byzantium)": {
                "date": "October 16, 2017",
                "significance": "Added privacy features and reduced block rewards, preparing for PoS."
            },
            "Metropolis (Constantinople)": {
                "date": "February 28, 2019",
                "significance": "Optimized gas costs and laid groundwork for Ethereum 2.0."
            },
            "Istanbul": {
                "date": "December 8, 2019",
                "significance": "Improved interoperability with ZK-SNARKs and other chains."
            },
            "Muir Glacier": {
                "date": "January 2, 2020",
                "significance": "Delayed the difficulty bomb to ensure smooth transition to Eth2."
            },
            "Berlin": {
                "date": "April 15, 2021",
                "significance": "Optimized gas fees for certain opcodes and improved security."
            },
            "London": {
                "date": "August 5, 2021",
                "significance": "Introduced EIP-1559, changing the fee market and burning base fees."
            }
        }
    
    def get_summary(self, upgrade_name: str) -> Dict[str, str]:
        """
        Retrieve the summary of a specific Ethereum upgrade.
        
        Args:
            upgrade_name (str): Name of the Ethereum upgrade.
            
        Returns:
            Dict[str, str]: Dictionary containing date and significance of the upgrade.
            
        Raises:
            ValueError: If the upgrade name is not found.
        """
        if upgrade_name not in self.upgrades:
            raise ValueError(f"Upgrade '{upgrade_name}' not found in historical records.")
        return self.upgrades[upgrade_name]
    
    def get_all_summaries(self) -> Dict[str, Dict[str, str]]:
        """
        Retrieve summaries for all Ethereum upgrades.
        
        Returns:
            Dict[str, Dict[str, str]]: Dictionary of all upgrades with their details.
        """
        return self.upgrades
    
    def save_to_json(self, filename: str = "ethereum_upgrades.json") -> None:
        """
        Save the upgrade summaries to a JSON file.
        
        Args:
            filename (str): Name of the output JSON file.
            
        Raises:
            IOError: If there's an issue writing the file.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.upgrades, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write to file {filename}: {e}")
    
    @staticmethod
    def load_from_json(filename: str = "ethereum_upgrades.json") -> Dict[str, Dict[str, str]]:
        """
        Load upgrade summaries from a JSON file.
        
        Args:
            filename (str): Name of the input JSON file.
            
        Returns:
            Dict[str, Dict[str, str]]: Dictionary of upgrades loaded from the file.
            
        Raises:
            IOError: If there's an issue reading the file.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except IOError as e:
            raise IOError(f"Failed to read file {filename}: {e}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in file {filename}: {e}", e.doc, e.pos)

def main():
    summarizer = EthereumUpgradeSummarizer()
    
    # Example usage
    print("All Ethereum Upgrades:")
    for name, details in summarizer.get_all_summaries().items():
        print(f"\n{name}:")
        print(f"Date: {details['date']}")
        print(f"Significance: {details['significance']}")
    
    # Save to JSON
    try:
        summarizer.save_to_json()
        print("\nUpgrades saved to 'ethereum_upgrades.json'.")
    except IOError as e:
        print(f"Error saving to file: {e}")

if __name__ == "__main__":
    main()
```
