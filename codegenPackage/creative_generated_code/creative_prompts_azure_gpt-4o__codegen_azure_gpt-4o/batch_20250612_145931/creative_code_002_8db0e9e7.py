"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virtuals-claim.pages.dev
Prompt: Create a program to display co-ownership details and shared revenue for AI agents like "Anya" and "John Wick" from the Virtuals Protocol.
Generated: DETERMINISTIC_8db0e9e71085eae6
Batch ID: 20250612_145931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class CoOwnership:
    """
    A class to represent co-ownership details and shared revenue for AI agents.
    """

    def __init__(self, owners, revenue):
        """
        Initialize the co-ownership details.

        :param owners: List of dictionaries with owner details (name and share percentage)
        :param revenue: Total revenue to be shared among owners
        """
        self.owners = owners
        self.revenue = revenue

    def calculate_shares(self):
        """
        Calculate the revenue share for each owner based on their share percentage.

        :return: Dictionary mapping owner names to their revenue share
        """
        try:
            shares = {}
            for owner in self.owners:
                name = owner["name"]
                share_percentage = owner["share_percentage"]
                # Validate share percentage
                if not (0 <= share_percentage <= 100):
                    raise ValueError(f"Invalid share percentage for {name}: {share_percentage}")
                shares[name] = round(self.revenue * (share_percentage / 100), 2)
            return shares
        except KeyError as e:
            raise KeyError(f"Missing key in owner details: {e}")
        except Exception as e:
            raise Exception(f"Error calculating shares: {e}")

    def get_details(self):
        """
        Get the co-ownership details including names, share percentages, and revenue shares.

        :return: Dictionary containing co-ownership details
        """
        try:
            shares = self.calculate_shares()
            details = {
                "owners": self.owners,
                "total_revenue": self.revenue,
                "shares": shares
            }
            return details
        except Exception as e:
            raise Exception(f"Error getting details: {e}")

    def display_details(self):
        """
        Display the co-ownership details in a formatted JSON structure.
        """
        try:
            details = self.get_details()
            print(json.dumps(details, indent=4))
        except Exception as e:
            print(f"Error displaying details: {e}")


# Example usage
if __name__ == "__main__":
    # Define co-owners and their share percentages
    owners = [
        {"name": "Anya", "share_percentage": 40},
        {"name": "John Wick", "share_percentage": 60}
    ]
    # Define total revenue
    revenue = 10000  # Example revenue in dollars

    # Create a CoOwnership instance
    co_ownership_instance = CoOwnership(owners, revenue)

    # Display co-ownership details
    co_ownership_instance.display_details()
```
