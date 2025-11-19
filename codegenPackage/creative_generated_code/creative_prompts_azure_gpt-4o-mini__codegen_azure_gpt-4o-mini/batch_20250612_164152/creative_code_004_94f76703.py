"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patch-monorepo-linea.vercel.app
Prompt: Explain the process of minting a .linea username and how the proceeds contribute to ecosystem funding and grants.
Generated: DETERMINISTIC_94f76703f5e0c1cc
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LineaUsernameMinting:
    """
    A class to handle the minting of .linea usernames and the associated funding process.
    """

    def __init__(self):
        self.minted_usernames = set()
        self.funding_pool = 0.0  # Total funds raised from username minting
        self.grants = []

    def mint_username(self, username: str, fee: float) -> str:
        """
        Mints a .linea username if it is available and processes the fee.

        Parameters:
            username (str): The desired username without the .linea extension.
            fee (float): The fee for minting the username.

        Returns:
            str: Confirmation message if minting is successful.
        
        Raises:
            ValueError: If the username already exists or fee is negative.
        """
        # Validate input
        if not username.isalnum() or len(username) < 3:
            raise ValueError("Username must be alphanumeric and at least 3 characters long.")

        if username in self.minted_usernames:
            raise ValueError("This username is already taken.")

        if fee < 0:
            raise ValueError("Fee must be a non-negative value.")

        # Mint the username
        self.minted_usernames.add(username)
        self.funding_pool += fee  # Add fee to the funding pool
        return f"Username {username}.linea minted successfully!"

    def distribute_grant(self, amount: float, recipient: str) -> str:
        """
        Distributes a grant from the funding pool to a recipient.

        Parameters:
            amount (float): The amount to grant.
            recipient (str): The recipient of the grant.

        Returns:
            str: Confirmation message if the grant is successfully distributed.

        Raises:
            ValueError: If the amount exceeds available funding or is negative.
        """
        if amount < 0:
            raise ValueError("Grant amount must be a non-negative value.")
        
        if amount > self.funding_pool:
            raise ValueError("Insufficient funds in the funding pool for this grant.")

        # Distribute the grant
        self.funding_pool -= amount
        self.grants.append({'recipient': recipient, 'amount': amount})
        return f"Grant of {amount} distributed to {recipient} successfully!"

    def get_funding_status(self) -> dict:
        """
        Returns the current funding pool status and grants distributed.

        Returns:
            dict: A dictionary containing the funding pool and grant information.
        """
        return {
            'funding_pool': self.funding_pool,
            'grants_distributed': self.grants
        }


# Example usage:
if __name__ == "__main__":
    try:
        minting_system = LineaUsernameMinting()
        print(minting_system.mint_username("exampleUser", 10.0))
        print(minting_system.distribute_grant(5.0, "Project A"))
        print(minting_system.get_funding_status())
    except Exception as e:
        print(f"Error: {e}")
```
