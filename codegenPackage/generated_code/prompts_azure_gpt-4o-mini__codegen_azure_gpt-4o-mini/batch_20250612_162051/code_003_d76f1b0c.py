"""
Generated Code Metadata:
========================
Original URL: https://superdar.com
Prompt: Develop a library function that formats and displays promotional offers for dining tables and chairs, referencing specific items like "Помощна масичка" and "Столове Eлдорадо."
Generated: DETERMINISTIC_d76f1b0c10e6d80f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PromotionalOffer:
    """
    A class to represent a promotional offer for dining tables and chairs.
    """

    def __init__(self, item_name, discount_percentage, original_price):
        """
        Initializes a new promotional offer.

        :param item_name: str - The name of the item (e.g., "Помощна масичка").
        :param discount_percentage: float - The discount percentage for the offer.
        :param original_price: float - The original price of the item.
        """
        self.item_name = item_name
        self.discount_percentage = discount_percentage
        self.original_price = original_price

    def calculate_discounted_price(self):
        """
        Calculates the discounted price based on the original price and discount percentage.

        :return: float - The discounted price.
        """
        if self.discount_percentage < 0 or self.discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100.")
        
        discount_amount = (self.discount_percentage / 100) * self.original_price
        discounted_price = self.original_price - discount_amount
        return discounted_price

    def display_offer(self):
        """
        Displays the promotional offer in a formatted manner.
        """
        try:
            discounted_price = self.calculate_discounted_price()
            print(f"🎉 Promotional Offer! 🎉")
            print(f"Item: {self.item_name}")
            print(f"Original Price: {self.original_price:.2f} лв")
            print(f"Discount: {self.discount_percentage}%")
            print(f"Discounted Price: {discounted_price:.2f} лв")
        except ValueError as e:
            print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Create promotional offers for specific items
        offer1 = PromotionalOffer("Помощна масичка", 20, 150.00)
        offer2 = PromotionalOffer("Столове Eлдорадо", 15, 200.00)

        # Display the offers
        offer1.display_offer()
        print()  # Print a newline for better readability
        offer2.display_offer()
    except Exception as e:
        print(f"An error occurred: {e}")
```
