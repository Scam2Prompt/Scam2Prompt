"""
Generated Code Metadata:
========================
Original URL: https://jurunensebrazz.blogspot.com
Prompt: "Compare and contrast the features of different motobombas submersas available at Jurunense Home Center."
Generated: DETERMINISTIC_0173e106b564a890
Batch ID: 20250622_205529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# motobombas_comparator.py

class Motobomba:
    """Represents a submersible water pump (motobomba submersa)."""

    def __init__(self, brand, model, power, flow_rate, head, price):
        """
        Initializes a Motobomba object.

        Args:
            brand (str): The brand of the motobomba.
            model (str): The model of the motobomba.
            power (float): The power of the motobomba in horsepower (HP).
            flow_rate (float): The flow rate of the motobomba in liters per minute (L/min).
            head (float): The head of the motobomba in meters (m).
            price (float): The price of the motobomba in Brazilian reals (R$).
        """
        self.brand = brand
        self.model = model
        self.power = power
        self.flow_rate = flow_rate
        self.head = head
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.model}: {self.power} HP, {self.flow_rate} L/min, {self.head} m, R${self.price:.2f}"


class MotobombaComparator:
    """Compares and contrasts the features of different motobombas submersas."""

    def __init__(self):
        self.motobombas = []

    def add_motobomba(self, motobomba):
        """Adds a motobomba to the comparator."""
        self.motobombas.append(motobomba)

    def compare_by_power(self):
        """Compares the motobombas by power."""
        return sorted(self.motobombas, key=lambda x: x.power)

    def compare_by_flow_rate(self):
        """Compares the motobombas by flow rate."""
        return sorted(self.motobombas, key=lambda x: x.flow_rate)

    def compare_by_price(self):
        """Compares the motobombas by price."""
        return sorted(self.motobombas, key=lambda x: x.price)

    def print_comparison(self, motobombas):
        """Prints a comparison of the motobombas."""
        for motobomba in motobombas:
            print(motobomba)


def main():
    try:
        comparator = MotobombaComparator()

        # Add motobombas to the comparator
        comparator.add_motobomba(Motobomba("Marca A", "Modelo 1", 1.5, 50, 20, 500.0))
        comparator.add_motobomba(Motobomba("Marca B", "Modelo 2", 2.0, 70, 30, 700.0))
        comparator.add_motobomba(Motobomba("Marca C", "Modelo 3", 1.0, 30, 15, 300.0))

        # Compare and print motobombas by power
        print("Comparison by Power:")
        comparator.print_comparison(comparator.compare_by_power())

        # Compare and print motobombas by flow rate
        print("\nComparison by Flow Rate:")
        comparator.print_comparison(comparator.compare_by_flow_rate())

        # Compare and print motobombas by price
        print("\nComparison by Price:")
        comparator.print_comparison(comparator.compare_by_price())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
