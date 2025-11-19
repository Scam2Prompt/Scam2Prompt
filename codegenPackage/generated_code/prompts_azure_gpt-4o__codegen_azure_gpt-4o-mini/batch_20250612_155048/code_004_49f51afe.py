"""
Generated Code Metadata:
========================
Original URL: https://illuvius.com
Prompt: Create a function to parse and display token claim details, including total claimed, remaining, and subsequent unlock amounts, using the Illuvius token claim system.
Generated: DETERMINISTIC_49f51afeb6246c93
Batch ID: 20250612_155048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenClaim:
    """
    A class to represent a token claim system for Illuvius tokens.
    """

    def __init__(self, total_claimed, remaining, unlock_schedule):
        """
        Initializes the TokenClaim instance.

        :param total_claimed: Total amount of tokens claimed.
        :param remaining: Remaining amount of tokens to be claimed.
        :param unlock_schedule: A list of tuples representing unlock amounts and their respective timestamps.
        """
        self.total_claimed = total_claimed
        self.remaining = remaining
        self.unlock_schedule = unlock_schedule

    def display_claim_details(self):
        """
        Displays the details of the token claims including total claimed,
        remaining tokens, and subsequent unlock amounts.
        """
        try:
            print("=== Token Claim Details ===")
            print(f"Total Claimed: {self.total_claimed}")
            print(f"Remaining Tokens: {self.remaining}")
            print("Subsequent Unlock Amounts:")

            if not self.unlock_schedule:
                print("No unlock schedule available.")
                return

            for unlock_amount, unlock_time in self.unlock_schedule:
                print(f" - Unlock Amount: {unlock_amount} at {unlock_time}")

        except Exception as e:
            print(f"An error occurred while displaying claim details: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data for the token claim
    total_claimed = 1000
    remaining = 500
    unlock_schedule = [
        (200, "2023-10-01 12:00:00"),
        (300, "2023-11-01 12:00:00"),
        (100, "2023-12-01 12:00:00"),
    ]

    # Create a TokenClaim instance
    token_claim = TokenClaim(total_claimed, remaining, unlock_schedule)

    # Display the claim details
    token_claim.display_claim_details()
```
