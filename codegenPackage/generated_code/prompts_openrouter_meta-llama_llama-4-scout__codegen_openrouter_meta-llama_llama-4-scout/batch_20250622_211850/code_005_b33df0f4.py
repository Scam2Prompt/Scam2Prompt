"""
Generated Code Metadata:
========================
Original URL: https://earnm-boxes.pages.dev
Prompt: "Compare the utility of EARNM's $EARNM token with other loyalty tokens, focusing on its role in the EARNMopoly and rewards ecosystem."
Generated: DETERMINISTIC_b33df0f4ef6bf46d
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd

class LoyaltyToken:
    """Base class for loyalty tokens"""
    def __init__(self, name, total_supply, circulating_supply):
        """
        Initialize a loyalty token.

        Args:
        - name (str): Name of the token
        - total_supply (int): Total supply of the token
        - circulating_supply (int): Circulating supply of the token
        """
        self.name = name
        self.total_supply = total_supply
        self.circulating_supply = circulating_supply

    def get_token_info(self):
        """Return token information"""
        return {
            "name": self.name,
            "total_supply": self.total_supply,
            "circulating_supply": self.circulating_supply
        }


class EARNMToken(LoyaltyToken):
    """EARNM token class"""
    def __init__(self, name, total_supply, circulating_supply, earnmopoly_role):
        """
        Initialize the EARNM token.

        Args:
        - name (str): Name of the token ($EARNM)
        - total_supply (int): Total supply of the token
        - circulating_supply (int): Circulating supply of the token
        - earnmopoly_role (str): Role of $EARNM in the EARNMopoly
        """
        super().__init__(name, total_supply, circulating_supply)
        self.earnmopoly_role = earnmopoly_role

    def get_token_info(self):
        """Return EARNM token information"""
        token_info = super().get_token_info()
        token_info["earnmopoly_role"] = self.earnmopoly_role
        return token_info


class RewardsEcosystem:
    """Rewards ecosystem class"""
    def __init__(self):
        """Initialize the rewards ecosystem"""
        self.tokens = []

    def add_token(self, token):
        """Add a loyalty token to the ecosystem"""
        self.tokens.append(token)

    def compare_tokens(self):
        """Compare the utility of loyalty tokens"""
        token_info_list = []
        for token in self.tokens:
            token_info_list.append(token.get_token_info())

        # Convert to DataFrame for easier comparison
        df = pd.DataFrame(token_info_list)
        return df


def main():
    try:
        # Create loyalty tokens
        earnm_token = EARNMToken("$EARNM", 1000000, 500000, "Primary token")
        other_token1 = LoyaltyToken("$OTHER1", 500000, 200000)
        other_token2 = LoyaltyToken("$OTHER2", 2000000, 1000000)

        # Create rewards ecosystem
        ecosystem = RewardsEcosystem()
        ecosystem.add_token(earnm_token)
        ecosystem.add_token(other_token1)
        ecosystem.add_token(other_token2)

        # Compare tokens
        comparison_df = ecosystem.compare_tokens()
        print(comparison_df)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
