"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: "Write a Python script to compare prices of different plastic window brands like Aluplast and Rehau, considering factors such as energy efficiency and sound insulation."
Generated: DETERMINISTIC_5158f16d0e779c6f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# window_comparator.py

class Window:
    def __init__(self, brand, model, price, energy_efficiency, sound_insulation):
        """
        Initialize a Window object.

        Args:
            brand (str): The brand of the window.
            model (str): The model of the window.
            price (float): The price of the window.
            energy_efficiency (float): The energy efficiency rating of the window (e.g., U-value).
            sound_insulation (float): The sound insulation rating of the window (e.g., Rw).
        """
        self.brand = brand
        self.model = model
        self.price = price
        self.energy_efficiency = energy_efficiency
        self.sound_insulation = sound_insulation

    def __repr__(self):
        return f"{self.brand} {self.model}: ${self.price:.2f}, U-value: {self.energy_efficiency}, Rw: {self.sound_insulation}"


class WindowComparator:
    def __init__(self):
        self.windows = []

    def add_window(self, window):
        """
        Add a window to the comparator.

        Args:
            window (Window): The window to add.
        """
        self.windows.append(window)

    def compare_by_price(self):
        """
        Compare windows by price.

        Returns:
            list: A list of windows sorted by price.
        """
        return sorted(self.windows, key=lambda x: x.price)

    def compare_by_energy_efficiency(self):
        """
        Compare windows by energy efficiency.

        Returns:
            list: A list of windows sorted by energy efficiency (lower U-value is better).
        """
        return sorted(self.windows, key=lambda x: x.energy_efficiency)

    def compare_by_sound_insulation(self):
        """
        Compare windows by sound insulation.

        Returns:
            list: A list of windows sorted by sound insulation (higher Rw is better).
        """
        return sorted(self.windows, key=lambda x: x.sound_insulation, reverse=True)


def main():
    try:
        comparator = WindowComparator()

        # Add windows from different brands
        comparator.add_window(Window("Aluplast", "IKO", 800.0, 1.1, 32))
        comparator.add_window(Window("Rehau", "Geneo", 1200.0, 0.9, 35))
        comparator.add_window(Window("Aluplast", "KBE", 900.0, 1.0, 33))
        comparator.add_window(Window("Rehau", "Sibral", 1000.0, 1.0, 34))

        # Compare windows by price
        print("### Comparison by Price ###")
        for window in comparator.compare_by_price():
            print(window)

        # Compare windows by energy efficiency
        print("\n### Comparison by Energy Efficiency ###")
        for window in comparator.compare_by_energy_efficiency():
            print(window)

        # Compare windows by sound insulation
        print("\n### Comparison by Sound Insulation ###")
        for window in comparator.compare_by_sound_insulation():
            print(window)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
