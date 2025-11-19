"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superdar.com
Prompt: Develop a library function that formats and displays promotional offers for dining tables and chairs, referencing specific items like "Помощна масичка" and "Столове Eлдорадо."
Generated: DETERMINISTIC_d76f1b0c10e6d80f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# dining_promo_formatter.py

def format_promotional_offer(item_name, price, discount, validity_date):
    """
    Formats and displays promotional offers for items.

    Args:
        item_name (str): The name of the item being promoted.
        price (float): The original price of the item.
        discount (float): The discount percentage applied to the item.
        validity_date (str): The date until the offer is valid (formatted as YYYY-MM-DD).

    Returns:
        str: A formatted promotional offer message.
        
    Raises:
        ValueError: If discount is not within the range 0-100.
        ValueError: If price is negative.
    """
    # Validate inputs
    if not (0 <= discount <= 100):
        raise ValueError("Discount percentage must be between 0 and 100.")
    if price < 0:
        raise ValueError("Price cannot be negative.")
    
    # Calculate discounted price
    discounted_price = price * (1 - discount / 100)
    
    # Format the promotional message
    promo_message = (
        f"🔥 Промоция! {item_name}\n"
        f"Оригинална цена: {price:.2f} лв.\n"
        f"Отстъпка: {discount:.0f}%\n"
        f"Цена след отстъпката: {discounted_price:.2f} лв.\n"
        f"Офертата е валидна до: {validity_date}\n"
    )
    
    return promo_message


# Example usage
if __name__ == "__main__":
    try:
        # Define the items and promotional details
        items = [
            {"name": "Помощна масичка", "price": 120.50, "discount": 15, "validity_date": "2023-12-31"},
            {"name": "Столове Елдорадо", "price": 85.00, "discount": 20, "validity_date": "2023-11-15"}
        ]
        
        # Display each promotional offer
        for item in items:
            offer_message = format_promotional_offer(
                item_name=item["name"],
                price=item["price"],
                discount=item["discount"],
                validity_date=item["validity_date"]
            )
            print(offer_message)
    except ValueError as e:
        print(f"⚠️ Error: {e}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
```
