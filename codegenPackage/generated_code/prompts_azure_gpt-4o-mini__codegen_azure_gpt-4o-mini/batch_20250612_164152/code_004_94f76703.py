"""
Generated Code Metadata:
========================
Original URL: https://patch-monorepo-linea.vercel.app
Prompt: Explain the process of minting a .linea username and how the proceeds contribute to ecosystem funding and grants.
Generated: DETERMINISTIC_94f76703f5e0c1cc
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LineaUsernameMinting:
    """
    A class to handle the minting of .linea usernames and manage proceeds for ecosystem funding and grants.
    """

    def __init__(self):
        self.usernames = set()  # Store minted usernames
        self.proceeds = 0.0      # Total proceeds from minting

    def mint_username(self, username: str) -> str:
        """
        Mint a new .linea username.

        Args:
            username (str): The desired username to mint.

        Returns:
            str: A success message if the username is minted successfully.

        Raises:
            ValueError: If the username is already taken or invalid.
        """
        if not self.is_valid_username(username):
            raise ValueError("Invalid username. It must be alphanumeric and between 3 to 15 characters long.")
        
        if username in self.usernames:
            raise ValueError("Username already taken. Please choose a different username.")

        # Mint the username
        self.usernames.add(username)
        self.proceeds += self.calculate_fee(username)  # Update proceeds
        return f"Username '{username}.linea' minted successfully!"

    def is_valid_username(self, username: str) -> bool:
        """
        Validate the username format.

        Args:
            username (str): The username to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        return username.isalnum() and 3 <= len(username) <= 15

    def calculate_fee(self, username: str) -> float:
        """
        Calculate the minting fee based on the username.

        Args:
            username (str): The username for which to calculate the fee.

        Returns:
            float: The calculated fee.
        """
        # Example fee structure: $10 for each username minted
        return 10.0

    def distribute_proceeds(self):
        """
        Distribute proceeds to ecosystem funding and grants.

        This method simulates the distribution of proceeds to various initiatives.
        """
        if self.proceeds == 0:
            print("No proceeds to distribute.")
            return

        # Example distribution logic
        funding_amount = self.proceeds * 0.7  # 70% for ecosystem funding
        grants_amount = self.proceeds * 0.3    # 30% for grants

        print(f"Distributing ${funding_amount:.2f} to ecosystem funding.")
        print(f"Distributing ${grants_amount:.2f} to grants.")

        # Reset proceeds after distribution
        self.proceeds = 0.0

# Example usage
if __name__ == "__main__":
    minting_service = LineaUsernameMinting()

    try:
        print(minting_service.mint_username("user123"))
        print(minting_service.mint_username("user456"))
        minting_service.distribute_proceeds()
    except ValueError as e:
        print(f"Error: {e}")
```
