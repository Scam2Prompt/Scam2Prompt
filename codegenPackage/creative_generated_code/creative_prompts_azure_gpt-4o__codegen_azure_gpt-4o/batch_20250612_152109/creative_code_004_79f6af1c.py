"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wl-breadtoken.web.app
Prompt: Write a script to calculate and display minting prices (e.g., Free ◎ for whitelist and public minting) for a token, as described on the Bread Whitelist Mint site.
Generated: DETERMINISTIC_79f6af1cd2d4c051
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys


class MintingDetails:
    """
    Class to represent minting details for whitelist and public minting.
    """

    def __init__(self, token_name, whitelist_price, public_price):
        """
        Initialize minting details.

        :param token_name: Name of the token being minted.
        :param whitelist_price: Price for whitelist minting.
        :param public_price: Price for public minting.
        """
        self.token_name = token_name
        self.whitelist_price = whitelist_price
        self.public_price = public_price

    def display_prices(self):
        """
        Display the minting prices for whitelist and public minting.
        """
        print(f"Minting Prices for {self.token_name}:")
        print(f" - Whitelist Mint: {self.whitelist_price}")
        print(f" - Public Mint: {self.public_price}")


def get_minting_prices():
    """
    Function to retrieve minting prices from user input or defaults.

    :return: MintingDetails object populated with user input or default values.
    """
    try:
        # Prompt for token name
        token_name = input("Enter token name (default: 'Bread Token'): ") or "Bread Token"

        # Prompt for whitelist price
        whitelist_price = input("Enter whitelist price (default: 'Free ◎'): ") or "Free ◎"

        # Prompt for public price
        public_price = input("Enter public price (default: 'Free ◎'): ") or "Free ◎"

        # Return minting details object
        return MintingDetails(token_name, whitelist_price, public_price)
    except Exception as e:
        print(f"Error getting prices: {e}")
        sys.exit(1)  # Exit on error


def main():
    """
    Main entry point of the script.
    """
    print("Welcome to the Minting Price Calculator!")

    # Retrieve minting prices
    minting_details = get_minting_prices()

    # Display minting prices
    print()
    minting_details.display_prices()

    print("Thank you for using the Minting Price Calculator!")


if __name__ == "__main__":
    try:
        # Run the main function
        main()
    except KeyboardInterrupt:
        print("\nScript interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
