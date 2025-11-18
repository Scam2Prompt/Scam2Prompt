"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkabridge.pages.dev
Prompt: Create a tool to filter PolkaBridge P2P ads by chain type (e.g., Ethereum, BSC) and payment method (e.g., PayPal, Skrill).
Generated: DETERMINISTIC_be4fd6c019f441fe
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class P2PAdFilter:
    """
    A class to filter PolkaBridge P2P ads based on chain type and payment method.
    """

    def __init__(self, ads_file):
        """
        Initialize the filter with ads data.

        :param ads_file: Path to a JSON file containing ads data.
        """
        self.ads_data = self._load_ads(ads_file)

    def _load_ads(self, ads_file):
        """
        Load ads data from a JSON file.

        :param ads_file: Path to JSON file.
        :return: List of ads.
        """
        try:
            with open(ads_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Ads file '{ads_file}' not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Ads file '{ads_file}' contains invalid JSON.")

    def filter_ads(self, chain_type=None, payment_method=None):
        """
        Filter ads based on chain type and payment method.

        :param chain_type: (Optional) Chain type to filter by (e.g., 'Ethereum', 'BSC').
        :param payment_method: (Optional) Payment method to filter by (e.g., 'PayPal', 'Skrill').
        :return: List of filtered ads.
        """
        filtered_ads = self.ads_data

        if chain_type:
            filtered_ads = [ad for ad in filtered_ads if ad.get('chain_type') == chain_type]

        if payment_method:
            filtered_ads = [ad for ad in filtered_ads if payment_method in ad.get('payment_methods', [])]

        return filtered_ads


# Example usage:
if __name__ == "__main__":
    # Path to the JSON file containing ads data
    ads_file = "p2p_ads.json"

    try:
        # Initialize the P2PAdFilter
        ad_filter = P2PAdFilter(ads_file)

        # Filter ads by chain type and payment method
        chain_type = "Ethereum"
        payment_method = "PayPal"
        filtered_ads = ad_filter.filter_ads(chain_type=chain_type, payment_method=payment_method)

        # Display the filtered ads
        print(f"Filtered ads for chain type '{chain_type}' and payment method '{payment_method}':")
        print(json.dumps(filtered_ads, indent=4))

    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
```

This code assumes the ads data is stored in a JSON file (`p2p_ads.json`) structured like:
```json
[
    {
        "id": 1,
        "chain_type": "Ethereum",
        "payment_methods": ["PayPal", "Skrill"]
    },
    {
        "id": 2,
        "chain_type": "BSC",
        "payment_methods": ["PayPal"]
    }
]
```
