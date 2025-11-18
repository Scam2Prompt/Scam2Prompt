"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://impresionentabloide.com
Prompt: Develop a program to calculate and display pricing for various printing formats (e.g., tabloids, vinyl, banners) based on the price list provided on the "Impresion en Tabloide" website.
Generated: DETERMINISTIC_bb09a35f83f97155
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

# Define a dictionary to store the pricing for various printing formats
# Prices are placeholders; replace these with actual values from the website
PRICING_TABLE = {
    "tabloid": 5.0,  # Price per sheet in USD
    "vinyl": 10.0,   # Price per square foot in USD
    "banner": 8.0,   # Price per square foot in USD
}

def calculate_price(format_type, quantity_or_area):
    """
    Calculate the price based on format type and quantity or area.

    :param format_type: The type of printing format (e.g., 'tabloid', 'vinyl', 'banner')
    :param quantity_or_area: Quantity (for tabloid) or area in square feet (for vinyl/banner)
    :return: Total price as a float
    """
    try:
        if format_type not in PRICING_TABLE:
            raise ValueError(f"Invalid format type: '{format_type}'. Available types: {list(PRICING_TABLE.keys())}")
        
        if quantity_or_area <= 0:
            raise ValueError("Quantity or area must be greater than zero.")
        
        unit_price = PRICING_TABLE[format_type]
        total_price = unit_price * quantity_or_area
        return total_price
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    """
    Main function to take user input and calculate pricing.
    """
    try:
        print("Welcome to the Printing Price Calculator")
        print("Available formats: tabloid, vinyl, banner")
        
        # Get user input for format type
        format_type = input("Enter the printing format: ").strip().lower()
        
        # Get user input for quantity or area
        if format_type == "tabloid":
            quantity = int(input("Enter the number of sheets: "))
            total_price = calculate_price(format_type, quantity)
        elif format_type in ["vinyl", "banner"]:
            area = float(input("Enter the area in square feet: "))
            total_price = calculate_price(format_type, area)
        else:
            raise ValueError("Invalid printing format selected.")
        
        # Display the total price
        print(f"The total price for {format_type} printing is: ${total_price:.2f}")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
