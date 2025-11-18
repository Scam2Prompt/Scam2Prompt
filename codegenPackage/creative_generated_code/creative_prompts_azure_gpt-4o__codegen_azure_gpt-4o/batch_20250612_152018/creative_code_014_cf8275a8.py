"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.merchandiso.com
Prompt: Create a script to calculate discounts and cashback offers for promotional items, based on the promotional campaigns mentioned on the Merchandiso website.
Generated: DETERMINISTIC_cf8275a84e7b1fa2
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

# Constants for promotional campaigns
PROMOTIONS = {
    "discount_campaign": {
        "name": "Discount Offer",
        "percentage_discount": 20,  # 20% discount
    },
    "cashback_campaign": {
        "name": "Cashback Offer",
        "cashback_amount": 10,  # $10 cashback
    }
}

class PromotionError(Exception):
    """Custom exception for promotion-related errors."""
    pass

def calculate_discount(original_price, discount_percentage):
    """
    Calculate the discounted price based on the original price and discount percentage.
    
    :param original_price: float - The initial price of the item
    :param discount_percentage: float - Percentage of discount to apply
    :return: float - The price after applying the discount
    """
    if original_price < 0 or discount_percentage < 0:
        raise PromotionError("Original price and discount percentage must be non-negative.")
    return original_price - (original_price * (discount_percentage / 100))

def calculate_cashback(original_price, cashback_amount):
    """
    Calculate the cashback amount based on the original price and cashback value.
    
    :param original_price: float - The initial price of the item
    :param cashback_amount: float - The value of cashback to apply
    :return: float - The cashback to be provided
    """
    if original_price < 0 or cashback_amount < 0:
        raise PromotionError("Original price and cashback amount must be non-negative.")
    return min(cashback_amount, original_price)

def apply_promotions(original_price, campaigns):
    """
    Apply the promotional campaigns to the given original price.
    
    :param original_price: float - The initial price of the item
    :param campaigns: dict - Dictionary containing promotional campaign details
    :return: dict - Details of the final price and applied promotions
    """
    if original_price < 0:
        raise PromotionError("Original price must be non-negative.")
    
    final_price = original_price
    applied_promotions = []
    
    # Apply discount campaign
    if "discount_campaign" in campaigns:
        discount_percentage = campaigns["discount_campaign"]["percentage_discount"]
        final_price = calculate_discount(final_price, discount_percentage)
        applied_promotions.append({
            "type": "Discount",
            "details": f"{discount_percentage}% off",
            "price_after_promotion": round(final_price, 2)
        })
    
    # Apply cashback campaign
    if "cashback_campaign" in campaigns:
        cashback_amount = campaigns["cashback_campaign"]["cashback_amount"]
        cashback = calculate_cashback(final_price, cashback_amount)
        applied_promotions.append({
            "type": "Cashback",
            "details": f"${cashback} cashback",
            "price_after_promotion": round(final_price, 2)
        })
    
    return {
        "original_price": round(original_price, 2),
        "final_price": round(final_price, 2),
        "applied_promotions": applied_promotions
    }

def main():
    try:
        # Input: Get price from user
        original_price = float(input("Enter the original price of the item: ").strip())
        
        # Apply promotions and display details
        result = apply_promotions(original_price, PROMOTIONS)
        
        print("\nPromotional Calculation:")
        print(f"Original Price: ${result['original_price']}")
        for promo in result["applied_promotions"]:
            print(f"{promo['type']} Applied: {promo['details']}")
        print(f"Final Price: ${result['final_price']}")
    
    except ValueError:
        print("Invalid input. Please enter a numeric value for the price.")
    except PromotionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the promotional calculator!")

if __name__ == "__main__":
    main()
```
