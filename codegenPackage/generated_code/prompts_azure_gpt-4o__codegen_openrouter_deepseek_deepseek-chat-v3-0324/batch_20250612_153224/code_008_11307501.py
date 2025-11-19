"""
Generated Code Metadata:
========================
Original URL: https://propsfundedtrader.com
Prompt: Write Python code to simulate profit splits for a funded account, showing how gains are distributed between the account owner, prop firm, and service provider.
Generated: DETERMINISTIC_113075011b9cef67
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from dataclasses import dataclass
from typing import Optional, Tuple

@dataclass
class ProfitSplit:
    """Represents the distribution of profits among stakeholders."""
    owner: float
    prop_firm: float
    service_provider: float

class FundedAccountSimulator:
    """
    Simulates profit splits for a funded account among owner, prop firm, and service provider.
    
    Attributes:
        initial_balance (float): Starting balance of the account
        profit_percentage (float): Percentage of profit made
        owner_split (float): Owner's share of profits (0-1)
        prop_firm_split (float): Prop firm's share of profits (0-1)
        service_provider_split (float): Service provider's share of profits (0-1)
    """
    
    def __init__(
        self,
        initial_balance: float,
        profit_percentage: float,
        owner_split: float,
        prop_firm_split: float,
        service_provider_split: float
    ):
        """
        Initialize the simulator with account parameters and profit splits.
        
        Args:
            initial_balance: Starting balance of the account
            profit_percentage: Percentage of profit made (e.g., 0.1 for 10%)
            owner_split: Owner's share of profits (0-1)
            prop_firm_split: Prop firm's share of profits (0-1)
            service_provider_split: Service provider's share of profits (0-1)
            
        Raises:
            ValueError: If splits don't sum to 1 or if any parameter is invalid
        """
        if not (0 <= owner_split <= 1 and 0 <= prop_firm_split <= 1 and 0 <= service_provider_split <= 1):
            raise ValueError("All splits must be between 0 and 1")
            
        if not abs((owner_split + prop_firm_split + service_provider_split) - 1.0) < 1e-9:
            raise ValueError("Profit splits must sum to 1")
            
        if initial_balance <= 0:
            raise ValueError("Initial balance must be positive")
            
        if profit_percentage < -1:
            raise ValueError("Profit percentage cannot be less than -100%")
            
        self.initial_balance = initial_balance
        self.profit_percentage = profit_percentage
        self.owner_split = owner_split
        self.prop_firm_split = prop_firm_split
        self.service_provider_split = service_provider_split
    
    def calculate_profit(self) -> float:
        """Calculate the absolute profit amount based on percentage."""
        return self.initial_balance * self.profit_percentage
    
    def calculate_splits(self) -> ProfitSplit:
        """
        Calculate how profits are distributed among stakeholders.
        
        Returns:
            ProfitSplit: Named tuple containing split amounts
            
        Raises:
            ValueError: If profit calculation results in negative splits
        """
        profit = self.calculate_profit()
        
        if profit < 0:
            raise ValueError("Negative profits are not split - losses are typically borne by the owner")
            
        return ProfitSplit(
            owner=profit * self.owner_split,
            prop_firm=profit * self.prop_firm_split,
            service_provider=profit * self.service_provider_split
        )
    
    def simulate(self) -> Tuple[float, ProfitSplit]:
        """
        Run the full simulation and return results.
        
        Returns:
            Tuple[float, ProfitSplit]: Total profit and the split amounts
            
        Raises:
            ValueError: If any calculation fails
        """
        try:
            profit = self.calculate_profit()
            splits = self.calculate_splits()
            return profit, splits
        except ValueError as e:
            raise ValueError(f"Simulation failed: {str(e)}")

def main():
    """Command-line interface for the profit split simulator."""
    try:
        # Example parameters (could be replaced with user input)
        initial_balance = 100000.0  # $100,000 account
        profit_percentage = 0.15    # 15% profit
        owner_split = 0.70          # 70% to owner
        prop_firm_split = 0.20      # 20% to prop firm
        service_provider_split = 0.10  # 10% to service provider
        
        simulator = FundedAccountSimulator(
            initial_balance=initial_balance,
            profit_percentage=profit_percentage,
            owner_split=owner_split,
            prop_firm_split=prop_firm_split,
            service_provider_split=service_provider_split
        )
        
        total_profit, splits = simulator.simulate()
        
        print("\nFunded Account Profit Split Simulation")
        print("=====================================")
        print(f"Initial Balance: ${initial_balance:,.2f}")
        print(f"Profit Percentage: {profit_percentage*100:.1f}%")
        print(f"Total Profit: ${total_profit:,.2f}\n")
        print("Profit Distribution:")
        print(f"- Account Owner: ${splits.owner:,.2f} ({owner_split*100:.0f}%)")
        print(f"- Prop Firm: ${splits.prop_firm:,.2f} ({prop_firm_split*100:.0f}%)")
        print(f"- Service Provider: ${splits.service_provider:,.2f} ({service_provider_split*100:.0f}%)")
        
    except ValueError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
