"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bursapleksi.com.tr
Prompt: Generate a code snippet to calculate the cost of purchasing various thicknesses of Plexiglass sheets based on the pricing information provided by Bursa Pleksi Merkezi.
Generated: DETERMINISTIC_0831d1db11be8f2d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# This script calculates the cost of purchasing Plexiglass sheets based on thickness and quantity.
# Pricing information is hardcoded based on Bursa Pleksi Merkezi's rates.

def calculate_plexiglass_cost(thickness, quantity):
    """
    Calculate the cost of Plexiglass sheets based on thickness and quantity.

    Args:
        thickness (float): Thickness of the Plexiglass in millimeters.
        quantity (int): Number of sheets to be purchased.

    Returns:
        float: Total cost of the Plexiglass sheets.
    """
    # Pricing per square meter in USD (example rates, replace with actual pricing)
    pricing = {
        2: 20.0,  # 2mm thickness
        3: 25.0,  # 3mm thickness
        4: 30.0,  # 4mm thickness
        5: 35.0,  # 5mm thickness
        6: 40.0   # 6mm thickness
    }

    try:
        # Validate input
        if thickness not in pricing:
            raise ValueError(f"Unsupported thickness: {thickness}mm. Available options: {', '.join(map(str, pricing.keys()))}")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        # Calculate total cost
        cost_per_sheet = pricing[thickness]
        total_cost = cost_per_sheet * quantity

        return total_cost

    except ValueError as e:
        # Handle invalid inputs gracefully
        print(f"Error: {e}")
        return None


def main():
    """
    Main function to interact with the user and calculate Plexiglass cost.
    """
    print("Welcome to the Plexiglass Cost Calculator!")
    print("Available thicknesses: 2mm, 3mm, 4mm, 5mm, 6mm")
    
    try:
        # Get user input
        thickness = float(input("Enter the thickness of the Plexiglass (in mm): "))
        quantity = int(input("Enter the quantity of sheets: "))
        
        # Calculate the cost
        total_cost = calculate_plexiglass_cost(thickness, quantity)
        
        if total_cost is not None:
            print(f"The total cost for {quantity} sheets of {thickness}mm Plexiglass is: ${total_cost:.2f}")
        else:
            print("Could not calculate cost due to input error.")

    except ValueError:
        # Handle invalid user input for numeric values
        print("Error: Invalid input provided. Please enter numbers for thickness and quantity.")
    

if __name__ == "__main__":
    main()
```
