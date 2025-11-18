"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://showmethemoney-34w.pages.dev
Prompt: Develop a code snippet for a peer-to-peer lending model that uses supply and demand dynamics for rate discovery, similar to the Lends approach.
Generated: DETERMINISTIC_814f6c86824e6d18
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


class PeerToPeerLendingPlatform:
    """
    A class representing a peer-to-peer lending platform with supply-demand-driven rate discovery.

    Attributes:
        lenders (list): List of dictionaries containing lender information (e.g., supply and minimum rate).
        borrowers (list): List of dictionaries containing borrower information (e.g., demand and maximum rate).
    """

    def __init__(self):
        """Initialize the lending platform with empty lender and borrower lists."""
        self.lenders = []
        self.borrowers = []

    def register_lender(self, name, supply, min_rate):
        """
        Register a lender with their desired supply and minimum interest rate.

        Args:
            name (str): Name of the lender.
            supply (float): Amount the lender is willing to supply.
            min_rate (float): Minimum interest rate acceptable to the lender.
        """
        self.lenders.append({"name": name, "supply": supply, "min_rate": min_rate})

    def register_borrower(self, name, demand, max_rate):
        """
        Register a borrower with their desired demand and maximum interest rate.

        Args:
            name (str): Name of the borrower.
            demand (float): Amount the borrower wants to borrow.
            max_rate (float): Maximum interest rate acceptable to the borrower.
        """
        self.borrowers.append({"name": name, "demand": demand, "max_rate": max_rate})

    def match_lender_borrower(self):
        """
        Match lenders with borrowers based on supply, demand, and acceptable rates.

        Returns:
            list: List of matches containing lender, borrower, and agreed interest rate.
        """
        matches = []

        # Sort lenders by minimum rate (ascending) and borrowers by maximum rate (descending)
        sorted_lenders = sorted(self.lenders, key=lambda x: x["min_rate"])
        sorted_borrowers = sorted(self.borrowers, key=lambda x: x["max_rate"], reverse=True)

        # Attempt to match lenders and borrowers
        for borrower in sorted_borrowers:
            for lender in sorted_lenders:
                # Check if supply meets demand and rates are acceptable
                if lender["supply"] >= borrower["demand"] and lender["min_rate"] <= borrower["max_rate"]:
                    # Agree on a rate (mid-point between lender's min_rate and borrower's max_rate)
                    agreed_rate = (lender["min_rate"] + borrower["max_rate"]) / 2

                    # Create a match
                    matches.append({
                        "lender": lender["name"],
                        "borrower": borrower["name"],
                        "amount": borrower["demand"],
                        "rate": agreed_rate
                    })

                    # Update lender's supply and remove borrower after match
                    lender["supply"] -= borrower["demand"]
                    sorted_borrowers.remove(borrower)
                    break

        return matches

    def display_matches(self, matches):
        """
        Display the matched lenders and borrowers along with the agreed interest rates.

        Args:
            matches (list): List of matches containing lender, borrower, and agreed interest rate.
        """
        if not matches:
            print("No matches found.")
        else:
            print("\nMatched Lender-Borrower Pairs:")
            for match in matches:
                print(f"Lender: {match['lender']} - Borrower: {match['borrower']} - "
                      f"Amount: {match['amount']} - Rate: {match['rate']:.2f}%")
        print()


# Example usage
if __name__ == "__main__":
    platform = PeerToPeerLendingPlatform()

    # Register lenders
    platform.register_lender("Lender A", supply=10000, min_rate=5.0)
    platform.register_lender("Lender B", supply=8000, min_rate=4.5)
    platform.register_lender("Lender C", supply=5000, min_rate=6.0)

    # Register borrowers
    platform.register_borrower("Borrower X", demand=4000, max_rate=6.0)
    platform.register_borrower("Borrower Y", demand=7000, max_rate=5.5)
    platform.register_borrower("Borrower Z", demand=2000, max_rate=7.0)

    # Perform matching
    matches = platform.match_lender_borrower()

    # Display matches
    platform.display_matches(matches)
```
