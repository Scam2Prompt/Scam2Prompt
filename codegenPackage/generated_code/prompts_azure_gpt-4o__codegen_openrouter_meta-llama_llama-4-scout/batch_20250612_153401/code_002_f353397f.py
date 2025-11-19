"""
Generated Code Metadata:
========================
Original URL: https://ayeaye-pro.pages.dev
Prompt: Generate Python code for tracking the first 50,000 investors in a cryptocurrency project, as described in the Aye Aye Coin presale phase.
Generated: DETERMINISTIC_f353397f33487a1d
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investor_tracker.py

class Investor:
    """Represents an investor in the cryptocurrency project."""

    def __init__(self, investor_id, name, email, investment_amount, timestamp):
        """
        Initializes an Investor object.

        Args:
            investor_id (int): Unique identifier for the investor.
            name (str): Name of the investor.
            email (str): Email address of the investor.
            investment_amount (float): Amount invested by the investor.
            timestamp (str): Timestamp of the investment.
        """
        self.investor_id = investor_id
        self.name = name
        self.email = email
        self.investment_amount = investment_amount
        self.timestamp = timestamp

class InvestorTracker:
    """Tracks investors in the cryptocurrency project."""

    def __init__(self):
        """Initializes an empty investor tracker."""
        self.investors = {}

    def add_investor(self, investor_id, name, email, investment_amount, timestamp):
        """
        Adds an investor to the tracker.

        Args:
            investor_id (int): Unique identifier for the investor.
            name (str): Name of the investor.
            email (str): Email address of the investor.
            investment_amount (float): Amount invested by the investor.
            timestamp (str): Timestamp of the investment.

        Raises:
            ValueError: If the investor ID already exists.
        """
        if investor_id in self.investors:
            raise ValueError("Investor ID already exists")
        investor = Investor(investor_id, name, email, investment_amount, timestamp)
        self.investors[investor_id] = investor

    def get_investor(self, investor_id):
        """
        Retrieves an investor by their ID.

        Args:
            investor_id (int): Unique identifier for the investor.

        Returns:
            Investor: The investor object, or None if not found.
        """
        return self.investors.get(investor_id)

    def update_investor(self, investor_id, name=None, email=None, investment_amount=None, timestamp=None):
        """
        Updates an existing investor's information.

        Args:
            investor_id (int): Unique identifier for the investor.
            name (str, optional): New name for the investor. Defaults to None.
            email (str, optional): New email address for the investor. Defaults to None.
            investment_amount (float, optional): New investment amount for the investor. Defaults to None.
            timestamp (str, optional): New timestamp for the investor. Defaults to None.

        Raises:
            ValueError: If the investor ID does not exist.
        """
        if investor_id not in self.investors:
            raise ValueError("Investor ID does not exist")
        investor = self.investors[investor_id]
        if name:
            investor.name = name
        if email:
            investor.email = email
        if investment_amount:
            investor.investment_amount = investment_amount
        if timestamp:
            investor.timestamp = timestamp

    def remove_investor(self, investor_id):
        """
        Removes an investor from the tracker.

        Args:
            investor_id (int): Unique identifier for the investor.

        Raises:
            ValueError: If the investor ID does not exist.
        """
        if investor_id not in self.investors:
            raise ValueError("Investor ID does not exist")
        del self.investors[investor_id]

    def get_all_investors(self):
        """Returns a list of all investors."""
        return list(self.investors.values())

def main():
    tracker = InvestorTracker()

    # Example usage:
    for i in range(1, 50001):
        tracker.add_investor(i, f"Investor {i}", f"investor{i}@example.com", 1000.0, "2022-01-01 12:00:00")

    # Test retrieval
    investor = tracker.get_investor(1)
    print(f"Investor 1: {investor.name}, {investor.email}, {investor.investment_amount}, {investor.timestamp}")

    # Test update
    tracker.update_investor(1, investment_amount=2000.0)
    investor = tracker.get_investor(1)
    print(f"Updated Investor 1: {investor.name}, {investor.email}, {investor.investment_amount}, {investor.timestamp}")

if __name__ == "__main__":
    main()
```
