"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumprofit.org
Prompt: Write code to implement a feature that categorizes cryptocurrencies into stablecoins, utility tokens, and payment cryptocurrencies, with details on their use cases, similar to Auto Profit Hub.
Generated: DETERMINISTIC_8c343b2f980f7229
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class Cryptocurrency:
    """
    A class to represent a cryptocurrency with its details.
    """

    def __init__(self, name: str, category: str, use_case: str):
        """
        Initializes a Cryptocurrency instance.

        :param name: The name of the cryptocurrency.
        :param category: The category of the cryptocurrency (stablecoin, utility token, payment).
        :param use_case: A brief description of the cryptocurrency's use case.
        """
        self.name = name
        self.category = category
        self.use_case = use_case

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the Cryptocurrency instance to a dictionary.

        :return: A dictionary representation of the cryptocurrency.
        """
        return {
            "name": self.name,
            "category": self.category,
            "use_case": self.use_case
        }


class CryptoCategorizer:
    """
    A class to categorize a list of cryptocurrencies into stablecoins, utility tokens, and payment cryptocurrencies.
    """

    def __init__(self):
        """
        Initializes the CryptoCategorizer with an empty list of cryptocurrencies.
        """
        self.cryptos: List[Cryptocurrency] = []

    def add_crypto(self, crypto: Cryptocurrency) -> None:
        """
        Adds a Cryptocurrency instance to the list.

        :param crypto: An instance of Cryptocurrency to be added.
        """
        self.cryptos.append(crypto)

    def categorize_cryptos(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Categorizes the cryptocurrencies into different categories.

        :return: A dictionary categorizing cryptocurrencies by their types.
        """
        categorized_cryptos = {
            "stablecoins": [],
            "utility_tokens": [],
            "payment_cryptocurrencies": []
        }

        for crypto in self.cryptos:
            if crypto.category in categorized_cryptos:
                categorized_cryptos[crypto.category].append(crypto.to_dict())
            else:
                raise ValueError(f"Unknown category '{crypto.category}' for cryptocurrency '{crypto.name}'.")

        return categorized_cryptos

    def export_to_json(self, file_path: str) -> None:
        """
        Exports the categorized cryptocurrencies to a JSON file.

        :param file_path: The path where the JSON file will be saved.
        """
        try:
            categorized_data = self.categorize_cryptos()
            with open(file_path, 'w') as json_file:
                json.dump(categorized_data, json_file, indent=4)
        except ValueError as ve:
            print(f"Error during categorization: {ve}")
        except IOError as ioe:
            print(f"Error writing to file {file_path}: {ioe}")


# Example Usage
if __name__ == "__main__":
    categorizer = CryptoCategorizer()
    
    # Adding some cryptocurrencies
    categorizer.add_crypto(Cryptocurrency("Tether", "stablecoins", "Pegged to USD for stability"))
    categorizer.add_crypto(Cryptocurrency("Ethereum", "utility_tokens", "Used for smart contracts and DApps"))
    categorizer.add_crypto(Cryptocurrency("Bitcoin", "payment_cryptocurrencies", "Digital currency for payments"))
    
    # Export categorized cryptocurrencies to JSON
    categorizer.export_to_json("categorized_cryptos.json")
```
