"""
Generated Code Metadata:
========================
Original URL: https://aulaferretera.com
Prompt: Create a script to calculate optimal pricing for hardware store products based on cost, demand, and competition, inspired by the blog "Cómo Fijar Precios en una Ferretería y Asegurar tu Rentabilidad" from Aula Ferretera.
Generated: DETERMINISTIC_4592d8c62aa0b2ef
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# optimal_pricing.py

class Product:
    """Represents a hardware store product."""

    def __init__(self, name, cost, demand, competition):
        """
        Initializes a Product instance.

        Args:
            name (str): Product name.
            cost (float): Product cost.
            demand (int): Product demand.
            competition (float): Competition price.
        """
        self.name = name
        self.cost = cost
        self.demand = demand
        self.competition = competition

    def calculate_optimal_price(self):
        """
        Calculates the optimal price based on cost, demand, and competition.

        Returns:
            float: Optimal price.
        """
        # Calculate the markup based on demand
        demand_markup = 1 + (self.demand / 100)

        # Calculate the cost-based price
        cost_based_price = self.cost * demand_markup

        # Adjust the price based on competition
        if self.competition == 0:
            competitive_price = cost_based_price * 1.2  # default 20% higher
        else:
            competitive_price = max(cost_based_price, self.competition * 0.9)

        # Apply a minimum margin of 15%
        optimal_price = max(competitive_price, self.cost * 1.15)

        return round(optimal_price, 2)


class PricingCalculator:
    """Calculates optimal prices for a list of products."""

    def __init__(self, products):
        """
        Initializes a PricingCalculator instance.

        Args:
            products (list[Product]): List of products.
        """
        self.products = products

    def calculate_optimal_prices(self):
        """
        Calculates the optimal prices for all products.

        Returns:
            dict[str, float]: Product names to optimal prices.
        """
        optimal_prices = {}
        for product in self.products:
            try:
                optimal_price = product.calculate_optimal_price()
                optimal_prices[product.name] = optimal_price
            except Exception as e:
                print(f"Error calculating optimal price for {product.name}: {str(e)}")

        return optimal_prices


def main():
    # Example usage
    products = [
        Product("Hammer", 10.0, 50, 15.0),
        Product("Saw", 20.0, 30, 25.0),
        Product("Drill", 50.0, 20, 60.0),
    ]

    calculator = PricingCalculator(products)
    optimal_prices = calculator.calculate_optimal_prices()

    print("Optimal Prices:")
    for product, price in optimal_prices.items():
        print(f"{product}: ${price}")


if __name__ == "__main__":
    main()
```
