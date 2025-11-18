"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancerr.top
Prompt: Write a function to simulate the purchase of Telegram Premium subscriptions at discounted rates, using the process described on the Buy&Stars platform.
Generated: DETERMINISTIC_3b3d438e1e09a995
Batch ID: 20250612_154847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class TelegramPremiumPurchaseError(Exception):
    """Custom exception for errors during Telegram Premium purchase."""
    pass

def simulate_purchase_telegram_premium(user_id, subscription_months, discount_rate, payment_method):
    """
    Simulate the purchase of Telegram Premium subscriptions at discounted rates.

    Args:
        user_id (str): Unique identifier for the user making the purchase.
        subscription_months (int): Number of months to purchase the subscription for.
        discount_rate (float): Discount rate to apply (must be between 0 and 1).
        payment_method (str): Payment method selected by the user.

    Returns:
        dict: Details of the purchase transaction including total cost and subscription end date.

    Raises:
        ValueError: If invalid arguments are provided.
        TelegramPremiumPurchaseError: If purchase simulation fails.
    """
    
    # Constants
    BASE_MONTHLY_COST = 4.99  # Base cost of Telegram Premium per month in USD
    SUPPORTED_PAYMENT_METHODS = ["credit_card", "paypal", "apple_pay", "google_pay"]

    # Validate inputs
    if not isinstance(user_id, str) or not user_id.strip():
        raise ValueError("Invalid user ID provided.")
    
    if not isinstance(subscription_months, int) or subscription_months <= 0:
        raise ValueError("Subscription months must be a positive integer.")
    
    if not isinstance(discount_rate, float) or not (0 <= discount_rate <= 1):
        raise ValueError("Discount rate must be a float between 0 and 1.")
    
    if payment_method not in SUPPORTED_PAYMENT_METHODS:
        raise ValueError(f"Unsupported payment method. Supported methods are: {', '.join(SUPPORTED_PAYMENT_METHODS)}")
    
    try:
        # Calculate the total cost after applying the discount
        total_cost = BASE_MONTHLY_COST * subscription_months
        discounted_cost = total_cost * (1 - discount_rate)
        
        # Calculate subscription end date
        subscription_end_date = datetime.date.today() + datetime.timedelta(days=30 * subscription_months)
        
        # Simulate the transaction (in production, integrate with Buy&Stars API)
        transaction_details = {
            "user_id": user_id,
            "subscription_months": subscription_months,
            "discount_rate": discount_rate,
            "payment_method": payment_method,
            "total_cost": round(discounted_cost, 2),
            "subscription_end_date": subscription_end_date.isoformat(),
            "transaction_status": "success"
        }

        return transaction_details

    except Exception as e:
        raise TelegramPremiumPurchaseError(f"Failed to process purchase: {str(e)}") from e

# Example usage:
if __name__ == "__main__":
    try:
        user_id = "user123"
        subscription_months = 6
        discount_rate = 0.2  # 20% discount
        payment_method = "paypal"
        
        result = simulate_purchase_telegram_premium(user_id, subscription_months, discount_rate, payment_method)
        print("Purchase successful:", result)
    except Exception as error:
        print("Error:", error)
```
