"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aprisacv.com.mx
Prompt: Create a Python program that estimates the cost of insulating a furnace using Aprisacv's refractory products (e.g., Aprifiber, ApriPaper, Aprick bricks), factoring in product dimensions and required quantities.
Generated: DETERMINISTIC_63e961025282fef4
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

# Constants for product pricing (per unit)
PRODUCT_PRICES = {
    "Aprifiber": 20.0,  # Price per square meter
    "ApriPaper": 15.0,  # Price per square meter
    "Aprick": 10.0,     # Price per brick
}

# Dimensions for each product
PRODUCT_DIMENSIONS = {
    "Aprifiber": {"width_m": 1.0, "height_m": 1.0},  # 1m x 1m
    "ApriPaper": {"width_m": 0.5, "height_m": 0.5},  # 0.5m x 0.5m
    "Aprick": {"volume_m3": 0.001},                 # 1 liter (0.001 m³)
}

def calculate_cost(product, area_m2, volume_m3):
    """
    Calculate the cost of insulating a furnace based on selected product, area, and/or volume.
    :param product: str - Name of the product (Aprifiber, ApriPaper, Aprick)
    :param area_m2: float - Total area to be covered in square meters (for Aprifiber and ApriPaper)
    :param volume_m3: float - Total volume to be filled in cubic meters (for Aprick)
    :return: float - Estimated cost
    """
    try:
        if product not in PRODUCT_PRICES:
            raise ValueError(f"Invalid product name: {product}. Available products are: {', '.join(PRODUCT_PRICES.keys())}")
        
        if product == "Aprifiber" or product == "ApriPaper":
            # Calculate required units based on area
            unit_width = PRODUCT_DIMENSIONS[product]["width_m"]
            unit_height = PRODUCT_DIMENSIONS[product]["height_m"]
            unit_area = unit_width * unit_height
            required_units = math.ceil(area_m2 / unit_area)
            cost = required_units * PRODUCT_PRICES[product]
        
        elif product == "Aprick":
            # Calculate required bricks based on volume
            unit_volume = PRODUCT_DIMENSIONS[product]["volume_m3"]
            required_units = math.ceil(volume_m3 / unit_volume)
            cost = required_units * PRODUCT_PRICES[product]
        
        else:
            raise ValueError("Unsupported product type.")
        
        return cost
    
    except Exception as e:
        print(f"Error calculating cost: {e}")
        return None

def main():
    """
    Main function to interact with the user and estimate insulation cost.
    """
    print("Welcome to the Furnace Insulation Cost Estimator!")
    print("Available products: Aprifiber, ApriPaper, Aprick")
    
    try:
        # Get user input
        product = input("Enter the product name: ").strip()
        if product not in PRODUCT_PRICES:
            raise ValueError("Invalid product. Please choose from Aprifiber, ApriPaper, or Aprick.")
        
        if product == "Aprifiber" or product == "ApriPaper":
            area_m2 = float(input("Enter the total area to be insulated (in square meters): ").strip())
            if area_m2 <= 0:
                raise ValueError("Area must be a positive value.")
            cost = calculate_cost(product, area_m2, 0)
        
        elif product == "Aprick":
            volume_m3 = float(input("Enter the total volume to be insulated (in cubic meters): ").strip())
            if volume_m3 <= 0:
                raise ValueError("Volume must be a positive value.")
            cost = calculate_cost(product, 0, volume_m3)
        
        else:
            raise ValueError("Unsupported product type.")
        
        if cost is not None:
            print(f"The estimated cost for insulating the furnace using {product} is: ${cost:.2f}")
        else:
            print("An error occurred while calculating the cost.")
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
