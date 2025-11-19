"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancerr.top
Prompt: Generate code to handle errors when buying Telegram Stars through the Buy&Stars service.
Generated: DETERMINISTIC_49258b7b92a97748
Batch ID: 20250612_161259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

class BuyAndStarsServiceError(Exception):
    """Custom exception for Buy&Stars service errors."""
    pass

def buy_telegram_stars(user_id, star_count):
    """
    Handles the purchase of Telegram Stars through the Buy&Stars service.

    Args:
        user_id (str): The ID of the user making the purchase.
        star_count (int): The number of stars to purchase.

    Returns:
        str: Confirmation message or error message if purchase fails.

    Raises:
        ValueError: If user_id is invalid or star_count is negative.
        BuyAndStarsServiceError: If the service encounters an error.
    """
    try:
        # Input validation
        if not user_id or not isinstance(user_id, str):
            raise ValueError("Invalid user ID. Must be a non-empty string.")
        if not isinstance(star_count, int) or star_count <= 0:
            raise ValueError("Invalid star count. Must be a positive integer.")
        
        # Simulate interacting with the Buy&Stars service
        response = simulated_service_call(user_id, star_count)
        
        # Check response for errors
        if response.get('status') != 'success':
            error_message = response.get('error', 'Unknown error occurred.')
            raise BuyAndStarsServiceError(f"Failed to purchase stars: {error_message}")
        
        # Successful purchase
        return f"Successfully purchased {star_count} stars for user {user_id}."
    
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        return str(ve)
    except BuyAndStarsServiceError as bse:
        logging.error(f"BuyAndStarsServiceError: {bse}")
        return str(bse)
    except Exception as e:
        logging.exception("An unexpected error occurred:")
        return "An unexpected error occurred. Please try again later."

def simulated_service_call(user_id, star_count):
    """
    Simulates a call to the Buy&Stars service.

    Args:
        user_id (str): The ID of the user making the purchase.
        star_count (int): The number of stars to purchase.

    Returns:
        dict: Simulated response from the service.
    """
    # Simulated responses for demonstration purposes
    if star_count > 1000:
        return {'status': 'error', 'error': 'Purchase limit exceeded.'}
    return {'status': 'success'}

if __name__ == "__main__":
    # Example usage
    user_id = "User123"
    star_count = 10
    result = buy_telegram_stars(user_id, star_count)
    print(result)
```
