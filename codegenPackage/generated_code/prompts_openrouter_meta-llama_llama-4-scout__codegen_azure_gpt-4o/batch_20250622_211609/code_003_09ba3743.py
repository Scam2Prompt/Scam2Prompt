"""
Generated Code Metadata:
========================
Original URL: https://exytrade.com
Prompt: "Design a system for secure and transparent investment opportunities, similar to Exytrade's share trading and mutual fund services."
Generated: DETERMINISTIC_09ba3743a61352d8
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import uuid
import json
from datetime import datetime

# Constants for the system
MINIMUM_INVESTMENT_AMOUNT = 100  # Minimum investment amount in USD
SUPPORTED_INVESTMENT_TYPES = ["share_trading", "mutual_funds"]  # Supported investment types

# Custom exception classes for error handling
class InvestmentError(Exception):
    """Base class for investment-related errors."""
    pass

class InvalidInvestmentTypeError(InvestmentError):
    """Raised when an unsupported investment type is provided."""
    pass

class InsufficientInvestmentAmountError(InvestmentError):
    """Raised when the investment amount is below the minimum required."""
    pass

# Helper function to generate a unique transaction ID
def generate_transaction_id():
    """Generates a unique transaction ID using UUID."""
    return str(uuid.uuid4())

# Helper function to hash sensitive data for security
def hash_data(data):
    """Hashes the input data using SHA-256 for security."""
    return hashlib.sha256(data.encode()).hexdigest()

# Investment class to handle investment operations
class Investment:
    def __init__(self, investor_name, investment_type, amount):
        """
        Initializes an investment instance.

        :param investor_name: Name of the investor
        :param investment_type: Type of investment (e.g., 'share_trading', 'mutual_funds')
        :param amount: Investment amount in USD
        """
        self.investor_name = investor_name
        self.investment_type = investment_type
        self.amount = amount
        self.transaction_id = generate_transaction_id()
        self.timestamp = datetime.now().isoformat()

        # Validate investment details
        self.validate_investment()

    def validate_investment(self):
        """
        Validates the investment details.
        Raises appropriate exceptions for invalid data.
        """
        if self.investment_type not in SUPPORTED_INVESTMENT_TYPES:
            raise InvalidInvestmentTypeError(f"Unsupported investment type: {self.investment_type}")
        if self.amount < MINIMUM_INVESTMENT_AMOUNT:
            raise InsufficientInvestmentAmountError(
                f"Investment amount must be at least ${MINIMUM_INVESTMENT_AMOUNT}. Provided: ${self.amount}"
            )

    def to_dict(self):
        """
        Converts the investment instance to a dictionary for transparency.

        :return: Dictionary representation of the investment
        """
        return {
            "investor_name": hash_data(self.investor_name),  # Hashing for privacy
            "investment_type": self.investment_type,
            "amount": self.amount,
            "transaction_id": self.transaction_id,
            "timestamp": self.timestamp,
        }

# Investment system class to manage multiple investments
class InvestmentSystem:
    def __init__(self):
        """Initializes the investment system with an empty list of investments."""
        self.investments = []

    def add_investment(self, investor_name, investment_type, amount):
        """
        Adds a new investment to the system.

        :param investor_name: Name of the investor
        :param investment_type: Type of investment
        :param amount: Investment amount
        :return: Dictionary representation of the added investment
        """
        try:
            investment = Investment(investor_name, investment_type, amount)
            self.investments.append(investment)
            return investment.to_dict()
        except InvestmentError as e:
            return {"error": str(e)}

    def get_all_investments(self):
        """
        Retrieves all investments in the system.

        :return: List of dictionary representations of all investments
        """
        return [investment.to_dict() for investment in self.investments]

# Example usage
if __name__ == "__main__":
    system = InvestmentSystem()

    # Adding investments
    print(system.add_investment("Alice", "share_trading", 500))
    print(system.add_investment("Bob", "mutual_funds", 50))  # Should trigger an error
    print(system.add_investment("Charlie", "real_estate", 1000))  # Should trigger an error

    # Retrieving all investments
    print(json.dumps(system.get_all_investments(), indent=4))
```
