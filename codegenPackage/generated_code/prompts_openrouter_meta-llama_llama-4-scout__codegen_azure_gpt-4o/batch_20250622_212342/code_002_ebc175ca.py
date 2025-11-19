"""
Generated Code Metadata:
========================
Original URL: https://gala-games-official-k.blogspot.com
Prompt: "Generate code to calculate the total cost of a computer build with RTX3050 and GTX1630 graphics cards."
Generated: DETERMINISTIC_ebc175cab340e293
Batch ID: 20250622_212342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Python script to calculate the total cost of a computer build with RTX3050 and GTX1630 graphics cards.

# Import necessary modules
import sys

def calculate_total_cost(component_costs):
    """
    Calculate the total cost of the computer build.
    
    Args:
        component_costs (dict): A dictionary containing component names and their costs.
    
    Returns:
        float: The total cost of the computer build.
    """
    try:
        # Ensure all costs are valid numbers
        total_cost = sum(component_costs.values())
        return total_cost
    except TypeError as e:
        # Handle cases where costs are not numbers
        print(f"Error: Invalid cost value detected. {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to calculate the total cost of a computer build.
    """
    # Define the costs of components
    component_costs = {
        "RTX3050": 249.99,  # Cost of RTX3050 graphics card
        "GTX1630": 169.99,  # Cost of GTX1630 graphics card
        "CPU": 299.99,      # Example cost of CPU
        "Motherboard": 149.99,  # Example cost of Motherboard
        "RAM": 79.99,       # Example cost of RAM
        "Storage": 99.99,   # Example cost of Storage
        "Power Supply": 89.99,  # Example cost of Power Supply
        "Case": 59.99       # Example cost of Case
    }

    # Calculate the total cost
    total_cost = calculate_total_cost(component_costs)

    if total_cost is not None:
        # Print the total cost
        print(f"The total cost of the computer build is: ${total_cost:.2f}")
    else:
        print("Failed to calculate the total cost due to an error.", file=sys.stderr)

# Entry point of the script
if __name__ == "__main__":
    main()
```
