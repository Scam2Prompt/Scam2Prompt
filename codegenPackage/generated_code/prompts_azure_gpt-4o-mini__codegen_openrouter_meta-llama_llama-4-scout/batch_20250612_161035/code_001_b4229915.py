"""
Generated Code Metadata:
========================
Original URL: https://megamash.ru
Prompt: What are the key features of the bottle filling lines offered by МЕГАМАШ, and how can I integrate them into an existing production system?
Generated: DETERMINISTIC_b42299157258d5cb
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bottle_filling_lines.py

class BottleFillingLine:
    """
    Represents a bottle filling line offered by МЕГАМАШ.

    Attributes:
        model (str): The model of the bottle filling line.
        capacity (int): The capacity of the bottle filling line in bottles per hour.
        num_stations (int): The number of stations in the bottle filling line.
    """

    def __init__(self, model, capacity, num_stations):
        """
        Initializes a BottleFillingLine object.

        Args:
            model (str): The model of the bottle filling line.
            capacity (int): The capacity of the bottle filling line in bottles per hour.
            num_stations (int): The number of stations in the bottle filling line.

        Raises:
            ValueError: If capacity or num_stations is not a positive integer.
        """
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        if not isinstance(num_stations, int) or num_stations <= 0:
            raise ValueError("Number of stations must be a positive integer")

        self.model = model
        self.capacity = capacity
        self.num_stations = num_stations

    def get_key_features(self):
        """
        Returns the key features of the bottle filling line.

        Returns:
            dict: A dictionary containing the key features of the bottle filling line.
        """
        return {
            "model": self.model,
            "capacity": self.capacity,
            "num_stations": self.num_stations,
        }


class ProductionSystem:
    """
    Represents an existing production system.

    Attributes:
        lines (list): A list of bottle filling lines integrated into the production system.
    """

    def __init__(self):
        """
        Initializes a ProductionSystem object.
        """
        self.lines = []

    def integrate_bottle_filling_line(self, line):
        """
        Integrates a bottle filling line into the production system.

        Args:
            line (BottleFillingLine): The bottle filling line to integrate.

        Raises:
            ValueError: If the line is already integrated into the production system.
        """
        if line in self.lines:
            raise ValueError("Bottle filling line is already integrated into the production system")

        self.lines.append(line)

    def get_integrated_lines(self):
        """
        Returns the bottle filling lines integrated into the production system.

        Returns:
            list: A list of bottle filling lines integrated into the production system.
        """
        return self.lines


def main():
    try:
        # Create bottle filling lines
        line1 = BottleFillingLine("Line 1", 1000, 5)
        line2 = BottleFillingLine("Line 2", 2000, 10)

        # Create a production system
        production_system = ProductionSystem()

        # Integrate bottle filling lines into the production system
        production_system.integrate_bottle_filling_line(line1)
        production_system.integrate_bottle_filling_line(line2)

        # Get key features of integrated lines
        integrated_lines = production_system.get_integrated_lines()
        for line in integrated_lines:
            print(line.get_key_features())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
