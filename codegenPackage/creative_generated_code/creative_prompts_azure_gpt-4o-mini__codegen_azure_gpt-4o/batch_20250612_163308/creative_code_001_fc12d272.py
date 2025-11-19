"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingroofing.com
Prompt: Write a Python script that calculates the estimated cost of roofing services based on user input for roof type (tile, shingle, metal, flat) and square footage, similar to a roofing calculator.
Generated: DETERMINISTIC_fc12d2725ca3695a
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sys

def get_roofing_cost_per_sqft(roof_type):
    """
    Returns the cost per square foot based on the type of roof.

    Parameters:
    roof_type (str): Type of roof (tile, shingle, metal, flat)

    Returns:
    float: Cost per square foot
    """
    roof_cost_mapping = {
        "tile": 10.0,    # Tile roofs cost $10 per square foot
        "shingle": 7.5, # Shingle roofs cost $7.5 per square foot
        "metal": 12.0,  # Metal roofs cost $12 per square foot
        "flat": 5.0     # Flat roofs cost $5 per square foot
    }
    
    return roof_cost_mapping.get(roof_type.lower(), None)


def calculate_roofing_cost(roof_type, square_footage):
    """
    Calculates the total cost of roofing services.

    Parameters:
    roof_type (str): Type of roof (tile, shingle, metal, flat)
    square_footage (float): Total square footage of the roof

    Returns:
    float: Total estimated cost
    """
    cost_per_sqft = get_roofing_cost_per_sqft(roof_type)
    if cost_per_sqft is None:
        raise ValueError("Invalid roof type. Please choose from: tile, shingle, metal, flat.")
    
    if square_footage <= 0:
        raise ValueError("Square footage must be greater than 0.")
    
    return cost_per_sqft * square_footage


def main():
    """
    Main function to execute the roofing cost calculator script.
    """
    try:
        # Gather user input
        print("Welcome to the Roofing Cost Calculator!")
        roof_type = input("Enter the type of roof (tile, shingle, metal, flat): ").strip()
        square_footage = float(input("Enter the square footage of the roof: ").strip())
        
        # Calculate total cost
        total_cost = calculate_roofing_cost(roof_type, square_footage)
        
        # Display the result
        print(f"The estimated cost for {square_footage} square feet of {roof_type} roofing is: ${total_cost:.2f}")
    
    except ValueError as ve:
        # Handle invalid input
        print(f"Input Error: {ve}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Roofing Cost Calculator!")


# Entry point of the script
if __name__ == "__main__":
    main()
```
