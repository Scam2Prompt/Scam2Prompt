"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.ablakvaros.hu
Prompt: Write a program to generate a detailed árajánlat (price quote) for műanyag ablakcsere (plastic window replacement) based on the dimensions and specifications provided by the user.
Generated: DETERMINISTIC_16a1c3addd7774bf
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_price(width, height, material, glazing_type, extra_features):
    """
    Calculate the price of a plastic window replacement based on dimensions, material, glazing type, and extras.
    
    :param width: Width of the window in cm
    :param height: Height of the window in cm
    :param material: Material type for the window frame (e.g., "PVC")
    :param glazing_type: Type of glass (e.g., "double", "triple")
    :param extra_features: List of additional features (e.g., ["mosquito_net", "roller_blinds"])
    :return: Total price as a float
    """

    # Base prices per square meter (in HUF)
    BASE_PRICE_PER_SQM = {
        "PVC": 20000,  # PVC frame
        # Add other materials if needed
    }

    # Glazing price multiplier
    GLAZING_MULTIPLIER = {
        "double": 1.0,
        "triple": 1.5,
        # Add other glazing types if needed
    }

    # Price for each extra feature
    EXTRA_FEATURE_PRICES = {
        "mosquito_net": 5000,
        "roller_blinds": 10000,
        # Add other features if needed
    }

    try:
        # Calculate base area in square meters
        area_sqm = (width / 100) * (height / 100)  # Convert cm to meters
        if area_sqm <= 0:
            raise ValueError("Invalid dimensions. Width and height must be positive values.")
        
        # Validate material
        if material not in BASE_PRICE_PER_SQM:
            raise ValueError(f"Invalid material '{material}'. Supported materials: {list(BASE_PRICE_PER_SQM.keys())}")

        # Validate glazing type
        if glazing_type not in GLAZING_MULTIPLIER:
            raise ValueError(f"Invalid glazing type '{glazing_type}'. Supported types: {list(GLAZING_MULTIPLIER.keys())}")

        # Calculate base price
        base_price = area_sqm * BASE_PRICE_PER_SQM[material] * GLAZING_MULTIPLIER[glazing_type]

        # Calculate extra features price
        extra_price = sum(EXTRA_FEATURE_PRICES[feature] for feature in extra_features if feature in EXTRA_FEATURE_PRICES)

        # Calculate total price
        total_price = base_price + extra_price
        return total_price

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return None


def get_user_input():
    """
    Get window specifications and dimensions from the user.

    :return: Dictionary containing user inputs
    """
    try:
        width = float(input("Enter window width in cm: "))
        height = float(input("Enter window height in cm: "))
        material = input("Enter material type (e.g., 'PVC'): ").strip()
        glazing_type = input("Enter glazing type ('double', 'triple'): ").strip()
        extra_features = input("Enter extra features (comma-separated, e.g., 'mosquito_net,roller_blinds'): ").split(',')

        return {
            "width": width,
            "height": height,
            "material": material,
            "glazing_type": glazing_type,
            "extra_features": [feature.strip() for feature in extra_features if feature.strip()]
        }

    except ValueError as ve:
        print(f"Invalid input: {ve}", file=sys.stderr)
        return None


def main():
    """
    Main function to interact with the user and generate the price quote.
    """
    print("Welcome to the Plastic Window Replacement Price Quote Generator!")

    # Get user inputs
    user_inputs = get_user_input()
    if not user_inputs:
        print("Failed to gather user inputs. Exiting...", file=sys.stderr)
        return

    # Calculate price
    price = calculate_price(
        user_inputs["width"],
        user_inputs["height"],
        user_inputs["material"],
        user_inputs["glazing_type"],
        user_inputs["extra_features"]
    )
    
    if price is not None:
        print(f"The estimated price for your window replacement is: {price:.2f} HUF")
    else:
        print("Could not calculate the price due to an error.", file=sys.stderr)


# Entry point for the program
if __name__ == "__main__":
    main()
```
