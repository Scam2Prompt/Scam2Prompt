"""
Generated Code Metadata:
========================
Original URL: https://ra-don.com
Prompt: Develop a pricing calculator for different types of websites (one-page, business card, catalog, e-commerce) offered by Ra-Don, including optional features like domain and hosting.
Generated: DETERMINISTIC_aa52036d00a4ed71
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class WebsitePricingCalculator:
    """
    A class to calculate the pricing for different types of websites offered by Ra-Don.
    """

    # Base prices for different website types
    BASE_PRICES = {
        'one_page': 500,
        'business_card': 1000,
        'catalog': 2000,
        'e_commerce': 3000
    }

    # Optional features prices
    OPTIONAL_FEATURES = {
        'domain': 15,  # Annual cost
        'hosting': 100  # Annual cost
    }

    def __init__(self, website_type, include_domain=False, include_hosting=False):
        """
        Initializes the pricing calculator with the specified website type and optional features.

        :param website_type: Type of the website (one_page, business_card, catalog, e_commerce)
        :param include_domain: Boolean indicating if domain is included
        :param include_hosting: Boolean indicating if hosting is included
        """
        self.website_type = website_type
        self.include_domain = include_domain
        self.include_hosting = include_hosting

        # Validate the website type
        if website_type not in self.BASE_PRICES:
            raise ValueError(f"Invalid website type: {website_type}. Must be one of {list(self.BASE_PRICES.keys())}.")

    def calculate_price(self):
        """
        Calculates the total price based on the website type and optional features.

        :return: Total price as a float
        """
        total_price = self.BASE_PRICES[self.website_type]

        # Add optional features to the total price
        if self.include_domain:
            total_price += self.OPTIONAL_FEATURES['domain']
        
        if self.include_hosting:
            total_price += self.OPTIONAL_FEATURES['hosting']

        return total_price

    def display_price(self):
        """
        Displays the calculated price in a user-friendly format.
        """
        try:
            total_price = self.calculate_price()
            print(f"The total price for a {self.website_type.replace('_', ' ').title()} website is: ${total_price:.2f}")
        except ValueError as e:
            print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a pricing calculator for an e-commerce website with domain and hosting
        calculator = WebsitePricingCalculator('e_commerce', include_domain=True, include_hosting=True)
        calculator.display_price()
    except Exception as e:
        print(f"An error occurred: {e}")
```
