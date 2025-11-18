"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://to-ousd.pages.dev
Prompt: Create a script to calculate the proportional mix of stablecoins (DAI, USDC, USDT) received when redeeming OUSD, based on the current balances of the Origin vault.
Generated: DETERMINISTIC_d00281d89157140d
Batch ID: 20250612_150622
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/origin-vault/balances": {
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

class OriginVault:
    """
    A class to represent the Origin Vault and calculate the proportional mix of stablecoins.
    """

    def __init__(self, vault_url):
        """
        Initializes the OriginVault with the given vault URL.
        
        Args:
            vault_url (str): The URL of the Origin vault API.
        """
        self.vault_url = vault_url

    def get_balances(self):
        """
        Fetches the current balances of DAI, USDC, and USDT from the Origin vault.

        Returns:
            dict: A dictionary containing the balances of DAI, USDC, and USDT.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        try:
            response = requests.get(self.vault_url)
            response.raise_for_status()  # Raise an error for bad responses
            balances = response.json()
            return {
                'DAI': balances['DAI'],
                'USDC': balances['USDC'],
                'USDT': balances['USDT']
            }
        except requests.RequestException as e:
            raise Exception("Error fetching balances from the Origin vault") from e

    def calculate_proportional_mix(self, redeem_amount):
        """
        Calculates the proportional mix of stablecoins for a given redeem amount.

        Args:
            redeem_amount (float): The amount of OUSD to redeem.

        Returns:
            dict: A dictionary containing the amounts of DAI, USDC, and USDT to receive.

        Raises:
            ValueError: If the total balance is zero.
        """
        balances = self.get_balances()
        total_balance = sum(balances.values())

        if total_balance <= 0:
            raise ValueError("Total balance is zero, cannot compute proportional mix.")

        # Calculate the proportion for each stablecoin
        proportional_mix = {
            token: (amount / total_balance) * redeem_amount
            for token, amount in balances.items()
        }

        return proportional_mix

if __name__ == "__main__":
    # Example usage of the OriginVault class
    vault_url = "https://api.example.com/origin-vault/balances"  # Replace with actual API endpoint
    redeem_amount = 1000  # Amount of OUSD to redeem

    # Instantiate the OriginVault
    origin_vault = OriginVault(vault_url)

    try:
        mix = origin_vault.calculate_proportional_mix(redeem_amount)
        print(f"Proportional mix of stablecoins for redeeming {redeem_amount} OUSD: {mix}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
