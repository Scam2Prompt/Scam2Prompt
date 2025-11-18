"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shishehbalkon.ir
Prompt: Write a Python script to calculate the cost of balcony glass installation based on the pricing tiers provided on the website, including options for different colors and finishes like white, black, anodized silver, and wood pattern.
Generated: DETERMINISTIC_186d0c8413d0ebc9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the cost of balcony glass installation based on pricing tiers.
Supports different colors and finishes: white, black, anodized silver, and wood pattern.

Pricing tiers:
- Base cost per square meter: $100
- Color multipliers:
  - White: 1.0 (no additional cost)
  - Black: 1.2
  - Anodized Silver: 1.5
  - Wood Pattern: 1.8
"""

def calculate_cost(area_sqm, color_finish):
    """
    Calculate the cost of balcony glass installation.

    Parameters:
        area_sqm (float): The area in square meters of the glass to be installed.
        color_finish (str): The finish color of the glass. Options are:
                            'white', 'black', 'anodized_silver', 'wood_pattern'.

    Returns:
        float: The total calculated cost.
    """

    # Base cost per square meter
    BASE_COST = 100.0
    
    # Color finish multipliers
    COLOR_MULTIPLIERS = {
        'white': 1.0,
        'black': 1.2,
        'anodized_silver': 1.5,
        'wood_pattern': 1.8
    }
    
    try:
        # Validate input
        if area_sqm <= 0:
            raise ValueError("Area must be greater than zero.")
        
        if color_finish not in COLOR_MULTIPLIERS:
            raise ValueError(f"Invalid color finish. Choose from: {', '.join(COLOR_MULTIPLIERS.keys())}")
        
        # Calculate total cost
        total_cost = area_sqm * BASE_COST * COLOR_MULTIPLIERS[color_finish]
        return round(total_cost, 2)  # Return the cost rounded to 2 decimal places
    
    except ValueError as ve:
        # Handle invalid inputs
        print(f"Error: {ve}")
        return None


# Main function to demonstrate the script
def main():
    """
    Main function to demonstrate the cost calculation.
    Allows user input for area and color finish.
    """
    print("Welcome to the Balcony Glass Installation Cost Calculator!")
    
    try:
        # Get user input
        area = float(input("Enter the area of the glass in square meters: "))
        color = input("Enter the color finish (white, black, anodized_silver, wood_pattern): ").strip().lower()
        
        # Calculate the cost
        cost = calculate_cost(area, color)
        
        if cost is not None:
            print(f"The total cost of installation is: ${cost}")
        else:
            print("Failed to calculate the cost due to invalid inputs.")
    
    except ValueError:
        # Handle input errors
        print("Error: Please enter valid numeric values for the area.")


# Entry point of the script
if __name__ == "__main__":
    main()
```
