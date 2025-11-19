"""
Generated Code Metadata:
========================
Original URL: https://scout.kz
Prompt: Create a script to calculate the cost of leasing SCOUT tractors based on user inputs like duration, equipment type, and budget, similar to the leasing options provided on SCOUT.kz.
Generated: DETERMINISTIC_719172b676a34003
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
from enum import Enum

class EquipmentType(Enum):
    """Enum representing different types of SCOUT tractors."""
    SCOUT_100 = "Scout 100"
    SCOUT_200 = "Scout 200"
    SCOUT_300 = "Scout 300"
    SCOUT_PRO = "Scout Pro"

class LeaseCalculator:
    """Class to calculate leasing costs for SCOUT tractors."""
    
    # Base monthly rates for each equipment type (in USD)
    BASE_RATES = {
        EquipmentType.SCOUT_100: 1500,
        EquipmentType.SCOUT_200: 2200,
        EquipmentType.SCOUT_300: 2900,
        EquipmentType.SCOUT_PRO: 3800
    }
    
    # Discount tiers based on lease duration (months)
    DISCOUNT_TIERS = {
        6: 0.0,    # No discount for 6 months
        12: 0.05,  # 5% discount for 12 months
        24: 0.10,  # 10% discount for 24 months
        36: 0.15   # 15% discount for 36 months
    }
    
    def __init__(self):
        """Initialize the lease calculator."""
        self.equipment_type = None
        self.duration = 0
        self.budget = 0.0
    
    def get_user_input(self):
        """Get user input for lease calculation."""
        print("SCOUT Tractor Lease Calculator")
        print("------------------------------")
        
        # Display available equipment types
        print("\nAvailable Equipment Types:")
        for i, equipment in enumerate(EquipmentType, 1):
            print(f"{i}. {equipment.value}")
        
        try:
            # Get equipment type selection
            choice = int(input("\nSelect equipment type (1-4): "))
            if choice < 1 or choice > len(EquipmentType):
                raise ValueError("Invalid equipment selection")
            self.equipment_type = list(EquipmentType)[choice - 1]
            
            # Get lease duration
            self.duration = int(input("Enter lease duration in months (6, 12, 24, or 36): "))
            if self.duration not in self.DISCOUNT_TIERS:
                raise ValueError("Invalid lease duration")
            
            # Get budget (optional)
            budget_input = input("Enter your budget in USD (optional, press Enter to skip): ")
            self.budget = float(budget_input) if budget_input else 0.0
            
        except ValueError as e:
            print(f"\nError: {str(e)}")
            sys.exit(1)
    
    def calculate_lease_cost(self):
        """Calculate the total lease cost with discounts."""
        base_rate = self.BASE_RATES[self.equipment_type]
        discount = self.DISCOUNT_TIERS[self.duration]
        
        monthly_rate = base_rate * (1 - discount)
        total_cost = monthly_rate * self.duration
        
        return {
            "equipment": self.equipment_type.value,
            "duration": self.duration,
            "monthly_rate": round(monthly_rate, 2),
            "total_cost": round(total_cost, 2),
            "discount_percent": discount * 100
        }
    
    def check_budget(self, total_cost):
        """Check if the total cost fits within the user's budget."""
        if self.budget <= 0:
            return None  # Budget not specified
        
        if total_cost <= self.budget:
            return f"✅ The lease fits within your budget of ${self.budget:,.2f}"
        else:
            difference = total_cost - self.budget
            return f"⚠️ The lease exceeds your budget by ${difference:,.2f}"
    
    def display_results(self, result):
        """Display the lease calculation results."""
        print("\nLease Calculation Results")
        print("------------------------")
        print(f"Equipment: {result['equipment']}")
        print(f"Lease Duration: {result['duration']} months")
        print(f"Monthly Rate: ${result['monthly_rate']:,.2f}")
        print(f"Total Cost: ${result['total_cost']:,.2f}")
        print(f"Discount Applied: {result['discount_percent']:.0f}%")
        
        budget_check = self.check_budget(result['total_cost'])
        if budget_check:
            print(f"\nBudget Check: {budget_check}")

def main():
    """Main function to run the lease calculator."""
    try:
        calculator = LeaseCalculator()
        calculator.get_user_input()
        result = calculator.calculate_lease_cost()
        calculator.display_results(result)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
