"""
Generated Code Metadata:
========================
Original URL: https://medpointye.com
Prompt: Write Python code to automate the sorting of ELISA kits by price, using categories like "low to high" and "high to low" as described on the MedPointYE website.
Generated: DETERMINISTIC_4aeba45ac311c126
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# elisa_kit_sorter.py

class ElisaKit:
    """Represents an ELISA kit with its name and price."""

    def __init__(self, name: str, price: float):
        """
        Initializes an ElisaKit object.

        Args:
            name (str): The name of the ELISA kit.
            price (float): The price of the ELISA kit.
        """
        self.name = name
        self.price = price

    def __repr__(self):
        return f"ElisaKit(name='{self.name}', price={self.price})"


class ElisaKitSorter:
    """Sorts ELISA kits by price."""

    def __init__(self, kits: list[ElisaKit]):
        """
        Initializes an ElisaKitSorter object.

        Args:
            kits (list[ElisaKit]): A list of ElisaKit objects.
        """
        self.kits = kits

    def sort_low_to_high(self) -> list[ElisaKit]:
        """
        Sorts the ELISA kits by price from low to high.

        Returns:
            list[ElisaKit]: A list of ElisaKit objects sorted by price.
        """
        try:
            return sorted(self.kits, key=lambda kit: kit.price)
        except Exception as e:
            print(f"Error sorting kits: {str(e)}")
            return []

    def sort_high_to_low(self) -> list[ElisaKit]:
        """
        Sorts the ELISA kits by price from high to low.

        Returns:
            list[ElisaKit]: A list of ElisaKit objects sorted by price.
        """
        try:
            return sorted(self.kits, key=lambda kit: kit.price, reverse=True)
        except Exception as e:
            print(f"Error sorting kits: {str(e)}")
            return []


def main():
    # Example usage
    kits = [
        ElisaKit("Kit 1", 100.0),
        ElisaKit("Kit 2", 50.0),
        ElisaKit("Kit 3", 200.0),
        ElisaKit("Kit 4", 150.0),
    ]

    sorter = ElisaKitSorter(kits)

    print("Low to High:")
    for kit in sorter.sort_low_to_high():
        print(f"{kit.name}: ${kit.price:.2f}")

    print("\nHigh to Low:")
    for kit in sorter.sort_high_to_low():
        print(f"{kit.name}: ${kit.price:.2f}")


if __name__ == "__main__":
    main()
```
