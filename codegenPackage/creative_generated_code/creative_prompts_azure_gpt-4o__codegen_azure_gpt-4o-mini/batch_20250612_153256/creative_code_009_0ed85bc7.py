"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gempad-app-presale.pages.dev
Prompt: Generate code to display tokenomics details for a GemPad presale, including presale rate, listing rate, and total contributors.
Generated: DETERMINISTIC_0ed85bc782729c99
Batch ID: 20250612_153256
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GemPadPresale:
    """
    A class to represent the tokenomics details of a GemPad presale.
    """

    def __init__(self, presale_rate, listing_rate, total_contributors):
        """
        Initializes the GemPadPresale with the given parameters.

        Args:
            presale_rate (float): The rate at which tokens are sold during the presale.
            listing_rate (float): The rate at which tokens will be listed on exchanges.
            total_contributors (int): The total number of contributors in the presale.

        Raises:
            ValueError: If any of the input values are negative.
        """
        if presale_rate < 0 or listing_rate < 0 or total_contributors < 0:
            raise ValueError("Presale rate, listing rate, and total contributors must be non-negative.")

        self.presale_rate = presale_rate
        self.listing_rate = listing_rate
        self.total_contributors = total_contributors

    def display_tokenomics(self):
        """
        Displays the tokenomics details of the GemPad presale.
        """
        print("=== GemPad Presale Tokenomics ===")
        print(f"Presale Rate: {self.presale_rate:.2f}")
        print(f"Listing Rate: {self.listing_rate:.2f}")
        print(f"Total Contributors: {self.total_contributors}")

def main():
    """
    Main function to run the GemPad presale tokenomics display.
    """
    try:
        # Example values for the presale
        presale_rate = 0.05  # Presale token price in BNB
        listing_rate = 0.06   # Expected listing price in BNB
        total_contributors = 150  # Total contributors who participated in the presale

        # Create an instance of GemPadPresale
        presale = GemPadPresale(presale_rate, listing_rate, total_contributors)

        # Display the tokenomics details
        presale.display_tokenomics()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
