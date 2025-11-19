"""
Generated Code Metadata:
========================
Original URL: https://meatmaster.pe
Prompt: "Compare the features and prices of different types of parrillas (grills) offered by Meat Master, including the Parrilla Premium Meat Master and the Parrilla Maletín Mixta."
Generated: DETERMINISTIC_6c982d6c8eba4274
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# parrilla_comparator.py

class Parrilla:
    """Base class for different types of parrillas."""

    def __init__(self, name, price, features):
        """
        Initialize a Parrilla object.

        Args:
            name (str): Name of the parrilla.
            price (float): Price of the parrilla.
            features (list): List of features of the parrilla.
        """
        self.name = name
        self.price = price
        self.features = features

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class ParrillaPremiumMeatMaster(Parrilla):
    """Parrilla Premium Meat Master class."""

    def __init__(self, price):
        """
        Initialize a ParrillaPremiumMeatMaster object.

        Args:
            price (float): Price of the Parrilla Premium Meat Master.
        """
        features = [
            "High-quality materials",
            "Large cooking surface",
            "Multiple heat zones",
            "Easy to clean",
        ]
        super().__init__("Parrilla Premium Meat Master", price, features)


class ParrillaMaletinMixta(Parrilla):
    """Parrilla Maletín Mixta class."""

    def __init__(self, price):
        """
        Initialize a ParrillaMaletinMixta object.

        Args:
            price (float): Price of the Parrilla Maletín Mixta.
        """
        features = [
            "Portable and compact design",
            "Mixed fuel capability (gas and charcoal)",
            "Easy to assemble and disassemble",
            "Durable construction",
        ]
        super().__init__("Parrilla Maletín Mixta", price, features)


def compare_parrillas(parrillas):
    """
    Compare the features and prices of different parrillas.

    Args:
        parrillas (list): List of Parrilla objects.

    Returns:
        None
    """
    print("Parrilla Comparison:")
    for i, parrilla in enumerate(parrillas, start=1):
        print(f"\n{i}. {parrilla}")
        print("Features:")
        for feature in parrilla.features:
            print(f"- {feature}")


def main():
    try:
        # Create Parrilla objects
        premium_meat_master = ParrillaPremiumMeatMaster(599.99)
        maletin_mixta = ParrillaMaletinMixta(299.99)

        # Compare Parrillas
        compare_parrillas([premium_meat_master, maletin_mixta])

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
