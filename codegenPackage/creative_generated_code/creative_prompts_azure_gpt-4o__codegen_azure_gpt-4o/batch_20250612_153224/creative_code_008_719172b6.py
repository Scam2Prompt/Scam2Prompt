"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scout.kz
Prompt: Create a script to calculate the cost of leasing SCOUT tractors based on user inputs like duration, equipment type, and budget, similar to the leasing options provided on SCOUT.kz.
Generated: DETERMINISTIC_719172b676a34003
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_lease_cost(duration, equipment_type, budget):
    """
    Calculate the total leasing cost based on the duration, equipment type, and budget.

    Args:
        duration (int): Lease duration in months.
        equipment_type (str): Type of equipment being leased (e.g., "compact", "medium", "heavy-duty").
        budget (float): Customer budget in local currency.

    Returns:
        float: Total cost of leasing for the specified duration.
    """
    # Base monthly rates for different equipment types
    equipment_rates = {
        "compact": 1000,       # Compact tractors cost 1000 currency units per month
        "medium": 1500,        # Medium tractors cost 1500 currency units per month
        "heavy-duty": 2000     # Heavy-duty tractors cost 2000 currency units per month
    }

    # Validate inputs
    if duration <= 0:
        raise ValueError("Duration must be greater than zero.")
    if equipment_type not in equipment_rates:
        raise ValueError(f"Invalid equipment type. Choose from {', '.join(equipment_rates.keys())}.")
    if budget <= 0:
        raise ValueError("Budget must be greater than zero.")

    # Calculate total cost
    monthly_rate = equipment_rates[equipment_type]
    total_cost = monthly_rate * duration

    # Check against budget
    if total_cost > budget:
        raise ValueError(
            f"Total cost ({total_cost}) exceeds the budget ({budget}). Please adjust your inputs."
        )

    return total_cost


def main():
    """
    Main function to interact with the user and calculate leasing costs.
    """
    try:
        print("Welcome to SCOUT Tractor Leasing Calculator!")
        
        # Input: Lease duration in months
        duration = int(input("Enter the lease duration in months: "))

        # Input: Equipment type
        equipment_type = input("Enter the equipment type (compact, medium, heavy-duty): ").strip().lower()

        # Input: Budget
        budget = float(input("Enter your budget: "))

        # Calculate leasing cost
        total_cost = calculate_lease_cost(duration, equipment_type, budget)

        # Output the results
        print(f"Your total cost for leasing a {equipment_type} tractor for {duration} months is: {total_cost:.2f}")
        print("Thank you for using the SCOUT Tractor Leasing Calculator!")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


# Entry point for the script
if __name__ == "__main__":
    main()
```
