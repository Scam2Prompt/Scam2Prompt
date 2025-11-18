"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuvius.com
Prompt: Create a function to parse and display token claim details, including total claimed, remaining, and subsequent unlock amounts, using the Illuvius token claim system.
Generated: DETERMINISTIC_49f51afeb6246c93
Batch ID: 20250612_155048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenClaim:
    def __init__(self, total_claimed, remaining, unlock_schedule):
        """
        Initialize the TokenClaim instance.

        :param total_claimed: Total amount of tokens that can be claimed.
        :param remaining: Remaining amount of tokens that can be claimed.
        :param unlock_schedule: List of amounts to be unlocked at each period.
        """
        self.total_claimed = total_claimed
        self.remaining = remaining
        self.unlock_schedule = unlock_schedule

    def display_claim_details(self):
        """
        Display the details of the token claim including total claimed,
        remaining, and subsequent unlock amounts.

        :raises ValueError: If total_claimed is less than remaining.
        """
        if self.total_claimed < self.remaining:
            raise ValueError("Total claimed cannot be less than remaining.")

        print("=== Token Claim Details ===")
        print(f"Total Claimed: {self.total_claimed}")
        print(f"Remaining: {self.remaining}")

        print("Unlock Schedule:")
        for period, amount in enumerate(self.unlock_schedule, start=1):
            print(f"Period {period}: {amount} tokens")
        print("============================")

# Example usage
def main():
    try:
        # Example token claim values
        total_claimed = 1000
        remaining = 300
        unlock_schedule = [100, 200, 300]

        claim = TokenClaim(total_claimed, remaining, unlock_schedule)
        claim.display_claim_details()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
