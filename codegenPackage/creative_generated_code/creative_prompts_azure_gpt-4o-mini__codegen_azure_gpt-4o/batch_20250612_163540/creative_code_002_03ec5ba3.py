"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gautamindustries.com
Prompt: Create a function that calculates the total cost for purchasing various types of plywood boards, including Timba 710 and Duro Plywood, based on user input for quantity and pricing from Gautam Industries.
Generated: DETERMINISTIC_03ec5ba39e9feb47
Batch ID: 20250612_163540
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_plywood_cost():
    """
    Calculate the total cost of purchasing plywood boards based on user input.

    This function asks the user for the quantity and price per unit of each plywood type (Timba 710 and Duro Plywood)
    and calculates the total cost.
    """

    try:
        # Prompt user for input related to Timba 710 Plywood
        timba_quantity = int(input("Enter the quantity of Timba 710 Plywood boards: "))
        timba_price_per_unit = float(input("Enter the price per unit of Timba 710 Plywood: "))

        # Prompt user for input related to Duro Plywood
        duro_quantity = int(input("Enter the quantity of Duro Plywood boards: "))
        duro_price_per_unit = float(input("Enter the price per unit of Duro Plywood: "))

        # Validate inputs (ensure quantities and prices are non-negative)
        if timba_quantity < 0 or timba_price_per_unit < 0 or duro_quantity < 0 or duro_price_per_unit < 0:
            raise ValueError("Quantity and price per unit must be non-negative.")

        # Calculate total costs for each type of plywood
        timba_total_cost = timba_quantity * timba_price_per_unit
        duro_total_cost = duro_quantity * duro_price_per_unit

        # Calculate overall total cost
        total_cost = timba_total_cost + duro_total_cost

        # Display results
        print(f"\n--- Purchase Summary ---")
        print(f"Timba 710 Total Cost: ₹{timba_total_cost:.2f}")
        print(f"Duro Plywood Total Cost: ₹{duro_total_cost:.2f}")
        print(f"Overall Total Cost: ₹{total_cost:.2f}")

        return total_cost

    except ValueError as ve:
        # Handle invalid inputs gracefully
        print(f"Input error: {ve}")
    except Exception as e:
        # Catch any other unforeseen errors
        print(f"An unexpected error occurred: {e}")


# Main execution block
if __name__ == "__main__":
    print("Welcome to Gautam Industries Plywood Cost Calculator!")
    calculate_total_plywood_cost()
```
