"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniaircargo.id
Prompt: Generate a script to calculate multimodal transportation costs, combining air freight and ocean freight as described by Uniair Cargo.
Generated: DETERMINISTIC_fb6a236eeb60de0f
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_transportation_costs(air_freight_cost, ocean_freight_cost):
    """
    Calculate the total multimodal transportation cost by combining air freight and ocean freight.
    
    Args:
        air_freight_cost (float): Cost of air freight in USD.
        ocean_freight_cost (float): Cost of ocean freight in USD.

    Returns:
        float: Total transportation cost in USD.
    """
    try:
        # Validate inputs are numeric
        if not isinstance(air_freight_cost, (int, float)) or not isinstance(ocean_freight_cost, (int, float)):
            raise ValueError("Both air_freight_cost and ocean_freight_cost must be numeric values.")
        
        # Ensure costs are non-negative
        if air_freight_cost < 0 or ocean_freight_cost < 0:
            raise ValueError("Freight costs must be non-negative.")

        # Calculate total transportation cost
        total_cost = air_freight_cost + ocean_freight_cost
        return total_cost
    except ValueError as ve:
        # Handle invalid cost values
        print(f"Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        # Catch unexpected exceptions
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to interact with the user and calculate multimodal transportation costs.
    """
    try:
        # Prompt user for air freight and ocean freight costs
        air_freight_cost = float(input("Enter the air freight cost (USD): "))
        ocean_freight_cost = float(input("Enter the ocean freight cost (USD): "))

        # Calculate total transportation cost
        total_cost = calculate_transportation_costs(air_freight_cost, ocean_freight_cost)

        if total_cost is not None:
            print(f"The total multimodal transportation cost is: ${total_cost:.2f}")
    except ValueError:
        # Handle invalid input from the user
        print("Invalid input. Please enter numeric values for costs.", file=sys.stderr)
    except Exception as e:
        # Handle unexpected exceptions
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
