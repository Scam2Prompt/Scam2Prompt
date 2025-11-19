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
class PromotionalOffer:
    """
    Class to represent and format promotional offers for dining tables and chairs.
    """

    def __init__(self, item_name: str, discount_percentage: float, original_price: float):
        """
        Initializes a new PromotionalOffer instance.

        :param item_name: Name of the item (e.g., "Помощна масичка", "Столове Eлдорадо").
        :param discount_percentage: Discount percentage offered on the item.
        :param original_price: Original price of the item before the discount.
        """
        self.item_name = item_name
        self.discount_percentage = discount_percentage
        self.original_price = original_price

    def calculate_discounted_price(self) -> float:
        """
        Calculate the price after applying the discount.

        :return: Discounted price of the item.
        """
        if self.discount_percentage < 0 or self.discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100.")
        
        discount_amount = (self.discount_percentage / 100) * self.original_price
        return self.original_price - discount_amount

    def format_offer(self) -> str:
        """
        Format the promotional offer as a string.

        :return: Formatted string describing the promotional offer.
        """
        try:
            discounted_price = self.calculate_discounted_price()
            return (
                f"Специална оферта за {self.item_name}!\n"
                f"Оригинална цена: {self.original_price:.2f} лв.\n"
                f"Отстъпка: {self.discount_percentage}%\n"
                f"Цена след отстъпка: {discounted_price:.2f} лв."
            )
        except ValueError as e:
            return str(e)

def display_promotional_offers(offers: list) -> None:
    """
    Display formatted promotional offers for a list of items.

    :param offers: List of PromotionalOffer instances to display.
    """
    if not isinstance(offers, list):
        raise TypeError("Offers must be provided as a list.")

    for offer in offers:
        if not isinstance(offer, PromotionalOffer):
            raise TypeError("All items in the list must be instances of PromotionalOffer.")
        print(offer.format_offer())
        print('-' * 40)  # Separator for readability

# Example Usage
if __name__ == "__main__":
    try:
        offers = [
            PromotionalOffer("Помощна масичка", 20, 100.00),
            PromotionalOffer("Столове Eлдорадо", 15, 150.00)
        ]
        display_promotional_offers(offers)
    except Exception as e:
        print(f"An error occurred: {e}")
```
