"""
Generated Code Metadata:
========================
Original URL: https://jieyasoft.com
Prompt: Provide an example of how to implement a bonus system for a multi-level direct sales network, inspired by the various models mentioned on Jieya Software's site.
Generated: DETERMINISTIC_71b206f0b4b3b73e
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Multi-Level Direct Sales Network Bonus System

This script implements a bonus system for a multi-level direct sales network.
Each salesperson earns a percentage of their direct sales and a smaller percentage
of the sales made by their downline (subordinates). The system supports multiple levels
of hierarchy and calculates bonuses accordingly.

Key Features:
- Direct sales bonus
- Downline sales bonus (multi-level)
- Error handling for invalid inputs
- Scalable design for large networks
"""

class Salesperson:
    """
    Represents a salesperson in the network.
    Attributes:
        id (int): Unique identifier for the salesperson.
        name (str): Name of the salesperson.
        sales (float): Total sales made by the salesperson.
        downline (list): List of subordinate Salesperson objects.
    """
    def __init__(self, id, name, sales=0.0):
        self.id = id
        self.name = name
        self.sales = sales
        self.downline = []

    def add_downline(self, salesperson):
        """
        Adds a subordinate to the salesperson's downline.
        Args:
            salesperson (Salesperson): The subordinate to add.
        """
        self.downline.append(salesperson)


class BonusSystem:
    """
    Implements the bonus calculation logic for the multi-level sales network.
    Attributes:
        direct_bonus_rate (float): Percentage of direct sales as bonus.
        downline_bonus_rate (float): Percentage of downline sales as bonus.
    """
    def __init__(self, direct_bonus_rate=0.10, downline_bonus_rate=0.05):
        self.direct_bonus_rate = direct_bonus_rate
        self.downline_bonus_rate = downline_bonus_rate

    def calculate_bonus(self, salesperson):
        """
        Calculates the total bonus for a salesperson, including direct sales
        and downline sales bonuses.
        Args:
            salesperson (Salesperson): The salesperson for whom to calculate the bonus.
        Returns:
            float: Total bonus amount.
        """
        try:
            # Direct sales bonus
            direct_bonus = salesperson.sales * self.direct_bonus_rate

            # Downline sales bonus (recursive calculation)
            downline_bonus = sum(
                self.calculate_bonus(downline) * self.downline_bonus_rate
                for downline in salesperson.downline
            )

            return direct_bonus + downline_bonus
        except Exception as e:
            print(f"Error calculating bonus for {salesperson.name}: {e}")
            return 0.0


# Example usage
if __name__ == "__main__":
    # Create salespeople
    alice = Salesperson(1, "Alice", 1000.0)
    bob = Salesperson(2, "Bob", 800.0)
    charlie = Salesperson(3, "Charlie", 500.0)

    # Build the network hierarchy
    alice.add_downline(bob)
    bob.add_downline(charlie)

    # Initialize the bonus system
    bonus_system = BonusSystem(direct_bonus_rate=0.10, downline_bonus_rate=0.05)

    # Calculate bonuses
    print(f"Alice's Bonus: ${bonus_system.calculate_bonus(alice):.2f}")
    print(f"Bob's Bonus: ${bonus_system.calculate_bonus(bob):.2f}")
    print(f"Charlie's Bonus: ${bonus_system.calculate_bonus(charlie):.2f}")
```
