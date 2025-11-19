"""
Generated Code Metadata:
========================
Original URL: https://astoricrypto.com
Prompt: Write a Python script that implements a profit-based fee structure for a cryptocurrency trading group, similar to the model described on AstoriCrypto, where members pay 10% of their profits after doubling their portfolio.
Generated: DETERMINISTIC_124369d69aa3dcf8
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class Member:
    """Represents a member of the trading group with their portfolio information."""

    def __init__(self, name: str, initial_investment: float):
        """
        Initialize a member with their name and initial investment.
        
        Args:
            name: Name of the member.
            initial_investment: Initial amount invested by the member.
        """
        self.name = name
        self.initial_investment = initial_investment
        self.current_balance = initial_investment
        self.fees_paid = 0.0
        self.has_doubled = False

    def update_balance(self, new_balance: float) -> None:
        """
        Update the member's current balance and check if portfolio has doubled.
        
        Args:
            new_balance: New balance of the member's portfolio.
        """
        self.current_balance = new_balance
        if not self.has_doubled and self.current_balance >= 2 * self.initial_investment:
            self.has_doubled = True
            logger.info(f"Member {self.name} has doubled their portfolio.")

    def calculate_fee(self) -> float:
        """
        Calculate 10% fee on profits after portfolio has doubled.
        
        Returns:
            The calculated fee amount. Returns 0 if portfolio hasn't doubled.
        """
        if not self.has_doubled:
            return 0.0
        
        profit = self.current_balance - 2 * self.initial_investment
        if profit <= 0:
            return 0.0
        
        fee = 0.1 * profit
        return fee

    def pay_fee(self) -> float:
        """
        Deduct the fee from the member's balance and track total fees paid.
        
        Returns:
            The fee amount that was paid.
        """
        fee = self.calculate_fee()
        if fee > 0:
            self.current_balance -= fee
            self.fees_paid += fee
            logger.info(f"Member {self.name} paid a fee of ${fee:.2f}")
        return fee


class TradingGroup:
    """Manages members and their fee calculations in the trading group."""

    def __init__(self):
        """Initialize an empty trading group."""
        self.members: Dict[str, Member] = {}

    def add_member(self, name: str, initial_investment: float) -> None:
        """
        Add a new member to the trading group.
        
        Args:
            name: Name of the member.
            initial_investment: Initial amount invested by the member.
        """
        if name in self.members:
            logger.warning(f"Member {name} already exists.")
            return
        
        if initial_investment <= 0:
            logger.error("Initial investment must be positive.")
            raise ValueError("Initial investment must be positive.")
        
        self.members[name] = Member(name, initial_investment)
        logger.info(f"Added member {name} with initial investment ${initial_investment:.2f}")

    def update_member_balance(self, name: str, new_balance: float) -> None:
        """
        Update a member's balance and check for fee eligibility.
        
        Args:
            name: Name of the member.
            new_balance: New balance of the member's portfolio.
        """
        if name not in self.members:
            logger.error(f"Member {name} not found.")
            raise KeyError(f"Member {name} not found.")
        
        if new_balance < 0:
            logger.error("Balance cannot be negative.")
            raise ValueError("Balance cannot be negative.")
        
        self.members[name].update_balance(new_balance)

    def collect_fees(self) -> Dict[str, float]:
        """
        Collect fees from all eligible members.
        
        Returns:
            Dictionary mapping member names to fees collected.
        """
        fees_collected = {}
        for name, member in self.members.items():
            fee = member.pay_fee()
            if fee > 0:
                fees_collected[name] = fee
        return fees_collected

    def get_member_info(self, name: str) -> Optional[Dict[str, float]]:
        """
        Get information about a member.
        
        Args:
            name: Name of the member.
            
        Returns:
            Dictionary with member's information or None if member doesn't exist.
        """
        if name not in self.members:
            return None
        
        member = self.members[name]
        return {
            "name": member.name,
            "initial_investment": member.initial_investment,
            "current_balance": member.current_balance,
            "fees_paid": member.fees_paid,
            "has_doubled": member.has_doubled
        }


# Example usage
if __name__ == "__main__":
    try:
        group = TradingGroup()
        
        # Add members
        group.add_member("Alice", 10000.0)
        group.add_member("Bob", 5000.0)
        
        # Update balances
        group.update_member_balance("Alice", 21000.0)  # Doubled portfolio
        group.update_member_balance("Bob", 8000.0)     # Not doubled yet
        
        # Collect fees
        fees = group.collect_fees()
        print("Fees collected:", fees)
        
        # Get member info
        alice_info = group.get_member_info("Alice")
        print("Alice's info:", alice_info)
        
    except Exception as e:
        logger.error(f"An error occurred: {e}")
```
