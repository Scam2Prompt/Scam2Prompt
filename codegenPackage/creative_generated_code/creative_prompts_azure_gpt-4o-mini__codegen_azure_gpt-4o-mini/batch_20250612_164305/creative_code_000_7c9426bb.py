"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeietwjvabsmhbvmmsq4y65nxgb5jhh4qwhskqdgyp7gmcpuwjsyayu.ipfs.dweb.link
Prompt: How can I implement a token launch campaign using Honeypot Finance's DreamPad features to ensure fair pricing and prevent rug pulls?
Generated: DETERMINISTIC_7c9426bb2e95c343
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import json

class TokenLaunchCampaign:
    def __init__(self, token_name, token_symbol, initial_price, total_supply):
        """
        Initialize a new Token Launch Campaign.

        :param token_name: The name of the token being launched.
        :param token_symbol: The symbol of the token being launched.
        :param initial_price: The initial price of the token in USD.
        :param total_supply: The total supply of the token.
        """
        self.token_name = token_name
        self.token_symbol = token_symbol
        self.initial_price = initial_price
        self.total_supply = total_supply
        self.funds_raised = 0
        self.is_launched = False

    def validate_campaign(self):
        """
        Validate campaign parameters to ensure they're within acceptable ranges.

        :raises ValueError: If any parameter is invalid.
        """
        if self.initial_price <= 0:
            raise ValueError("Initial price must be greater than zero.")
        if self.total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        
    def launch(self):
        """
        Launch the token campaign after validation.

        :raises Exception: If the campaign is already launched.
        """
        if self.is_launched:
            raise Exception("Token launch campaign has already been launched.")
        
        self.validate_campaign()
        self.is_launched = True
        print(f"Launched {self.token_name} ({self.token_symbol}) at ${self.initial_price}.")

    def contribute(self, amount):
        """
        Contribute funds to the token launch campaign.

        :param amount: Amount in USD to contribute.
        :raises ValueError: If the amount is invalid.
        """
        if amount <= 0:
            raise ValueError("Contribution amount must be greater than zero.")
        
        if not self.is_launched:
            raise Exception("Campaign not launched yet. Please launch the campaign before contributing.")

        self.funds_raised += amount
        print(f"Raised ${self.funds_raised} for {self.token_name}.")

    def get_status(self):
        """
        Get the current status of the token launch campaign.

        :return: A dictionary containing campaign status.
        """
        return {
            'Token Name': self.token_name,
            'Token Symbol': self.token_symbol,
            'Initial Price': self.initial_price,
            'Total Supply': self.total_supply,
            'Funds Raised': self.funds_raised,
            'Is Launched': self.is_launched
        }

# Example Usage
if __name__ == "__main__":
    try:
        campaign = TokenLaunchCampaign("ExampleToken", "ETK", 0.1, 1000000)
        campaign.launch()
        campaign.contribute(50)
        print(json.dumps(campaign.get_status(), indent=4))
    except Exception as e:
        print(f"Error: {e}")
```
