"""
Generated Code Metadata:
========================
Original URL: https://elara-celestia.com
Prompt: Generate a code snippet to compare the pricing of different apartment configurations in L&T Elara Celestia, such as 3 BHK (S) vs 3 BHK (L) vs 4 BHK.
Generated: DETERMINISTIC_d6058990ddce6136
Batch ID: 20250622_212053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# apartment_comparator.py

class Apartment:
    def __init__(self, name, bhk, size, price):
        """
        Initialize an Apartment object.

        Args:
            name (str): Name of the apartment complex.
            bhk (str): BHK configuration (e.g., 3 BHK).
            size (str): Size of the apartment (e.g., S, L).
            price (float): Price of the apartment.
        """
        self.name = name
        self.bhk = bhk
        self.size = size
        self.price = price

    def __repr__(self):
        return f"{self.bhk} ({self.size}): {self.price}"


class ApartmentComparator:
    def __init__(self):
        self.apartments = []

    def add_apartment(self, apartment):
        """
        Add an apartment to the comparator.

        Args:
            apartment (Apartment): Apartment object to add.
        """
        self.apartments.append(apartment)

    def compare_pricing(self):
        """
        Compare the pricing of different apartment configurations.

        Returns:
            dict: Dictionary with BHK configurations as keys and average prices as values.
        """
        pricing = {}
        for apartment in self.apartments:
            bhk_key = apartment.bhk
            if bhk_key not in pricing:
                pricing[bhk_key] = []
            pricing[bhk_key].append(apartment.price)

        for bhk, prices in pricing.items():
            average_price = sum(prices) / len(prices)
            pricing[bhk] = average_price

        return pricing

    def print_comparison(self):
        """
        Print a comparison of the pricing of different apartment configurations.
        """
        pricing = self.compare_pricing()
        for bhk, average_price in pricing.items():
            print(f"{bhk}: {average_price}")


def main():
    try:
        comparator = ApartmentComparator()

        # Add apartments to compare
        comparator.add_apartment(Apartment("L&T Elara Celestia", "3 BHK", "S", 1200000))
        comparator.add_apartment(Apartment("L&T Elara Celestia", "3 BHK", "L", 1500000))
        comparator.add_apartment(Apartment("L&T Elara Celestia", "4 BHK", "", 2000000))

        # Print comparison
        print("Apartment Pricing Comparison:")
        comparator.print_comparison()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
