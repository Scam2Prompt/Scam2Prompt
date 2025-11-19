"""
Generated Code Metadata:
========================
Original URL: https://invest-destreams.web.app
Prompt: "Explain the utility of the DeeStream token, including its role in revenue sharing, voting rights, and early access to platform features."
Generated: DETERMINISTIC_a6dc8f3e283dd860
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# DeeStream Token Utility Documentation
# ======================================

class DeeStreamToken:
    """
    Represents a DeeStream token, providing utility functions for revenue sharing, 
    voting rights, and early access to platform features.
    """

    def __init__(self, token_id, token_owner, total_supply):
        """
        Initializes a DeeStream token object.

        Args:
            token_id (str): Unique identifier for the token.
            token_owner (str): Address of the token owner.
            total_supply (int): Total supply of tokens.

        Raises:
            ValueError: If total supply is less than or equal to 0.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than 0")

        self.token_id = token_id
        self.token_owner = token_owner
        self.total_supply = total_supply
        self.revenue_sharing_percentage = 0
        self.voting_rights = False
        self.early_access = False

    def enable_revenue_sharing(self, percentage):
        """
        Enables revenue sharing for the token.

        Args:
            percentage (float): Percentage of revenue to share.

        Raises:
            ValueError: If percentage is not between 0 and 100.
        """
        if not 0 <= percentage <= 100:
            raise ValueError("Percentage must be between 0 and 100")

        self.revenue_sharing_percentage = percentage

    def grant_voting_rights(self):
        """
        Grants voting rights to the token owner.
        """
        self.voting_rights = True

    def grant_early_access(self):
        """
        Grants early access to platform features for the token owner.
        """
        self.early_access = True

    def get_token_utility(self):
        """
        Returns a dictionary describing the token's utility.

        Returns:
            dict: Token utility information.
        """
        return {
            "revenue_sharing": {
                "enabled": self.revenue_sharing_percentage > 0,
                "percentage": self.revenue_sharing_percentage
            },
            "voting_rights": self.voting_rights,
            "early_access": self.early_access
        }


class DeeStreamPlatform:
    """
    Simulates the DeeStream platform, managing tokens and their utilities.
    """

    def __init__(self):
        """
        Initializes the DeeStream platform.
        """
        self.tokens = {}

    def create_token(self, token_id, token_owner, total_supply):
        """
        Creates a new DeeStream token.

        Args:
            token_id (str): Unique identifier for the token.
            token_owner (str): Address of the token owner.
            total_supply (int): Total supply of tokens.

        Returns:
            DeeStreamToken: The created token object.
        """
        token = DeeStreamToken(token_id, token_owner, total_supply)
        self.tokens[token_id] = token
        return token

    def get_token(self, token_id):
        """
        Retrieves a DeeStream token by its ID.

        Args:
            token_id (str): Unique identifier for the token.

        Returns:
            DeeStreamToken: The token object, or None if not found.
        """
        return self.tokens.get(token_id)


def main():
    # Example usage
    platform = DeeStreamPlatform()

    token_id = "DST-123"
    token_owner = "0x1234567890"
    total_supply = 1000000

    token = platform.create_token(token_id, token_owner, total_supply)

    token.enable_revenue_sharing(20)
    token.grant_voting_rights()
    token.grant_early_access()

    token_utility = token.get_token_utility()
    print(token_utility)


if __name__ == "__main__":
    main()
```
