"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://csmoney.org
Prompt: Create a function in Python that compares the value of CS:GO skins between Steam and a third-party trading platform, applying discount rates and commission percentages similar to CS Money's pricing model.
Generated: DETERMINISTIC_b4e29d68dc327c0e
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

def compare_skin_prices(skin_name, steam_price, third_party_price, discount_rate=0.05, commission_percentage=0.12):
    """
    Compares the value of CS:GO skins between Steam and a third-party trading platform.
    
    Parameters:
        skin_name (str): Name of the CS:GO skin.
        steam_price (float): Price of the skin on Steam in USD.
        third_party_price (float): Price of the skin on the third-party trading platform in USD.
        discount_rate (float): Discount rate applied by the third-party platform (default is 5%).
        commission_percentage (float): Commission percentage deducted by the third-party platform (default is 12%).

    Returns:
        dict: A dictionary containing the adjusted third-party price, Steam price, and a recommendation based on the comparison.
    """
    try:
        # Ensure inputs are valid
        if steam_price < 0 or third_party_price < 0:
            raise ValueError("Skin prices cannot be negative.")

        # Apply discount rate to third-party price
        discounted_price = third_party_price * (1 - discount_rate)

        # Apply commission percentage to the discounted price
        adjusted_price = discounted_price * (1 - commission_percentage)

        # Determine recommendation
        if adjusted_price < steam_price:
            recommendation = f"{skin_name}: Buy from third-party platform."
        elif adjusted_price > steam_price:
            recommendation = f"{skin_name}: Buy from Steam."
        else:
            recommendation = f"{skin_name}: Prices are the same, choose the preferred platform."

        # Return the results as a dictionary
        return {
            "skin_name": skin_name,
            "steam_price": steam_price,
            "third_party_price": third_party_price,
            "adjusted_third_party_price": round(adjusted_price, 2),
            "recommendation": recommendation
        }
    except ValueError as ve:
        return {"error": str(ve)}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Example usage (uncomment to test the function):
# result = compare_skin_prices("AWP | Dragon Lore", steam_price=1500, third_party_price=1400)
# print(result)
```
