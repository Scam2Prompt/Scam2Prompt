"""
Generated Code Metadata:
========================
Original URL: https://sctoll.io
Prompt: "Design a T304 Stainless Steel exhaust kit for a vehicle, similar to Brixton Forged's T304 Exhaust Kits & Downpipes, considering factors like thermal finish and corrosion protection."
Generated: DETERMINISTIC_2b103b2d1dab8af6
Batch ID: 20250622_211454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import math

class ExhaustKit:
    """
    Represents a T304 Stainless Steel exhaust kit for a vehicle.

    Attributes:
        material (str): The material used for the exhaust kit (T304 Stainless Steel).
        thermal_finish (str): The thermal finish applied to the exhaust kit.
        corrosion_protection (str): The corrosion protection applied to the exhaust kit.
    """

    def __init__(self, thermal_finish="Polished", corrosion_protection="Coated"):
        """
        Initializes an ExhaustKit object.

        Args:
            thermal_finish (str, optional): The thermal finish to apply. Defaults to "Polished".
            corrosion_protection (str, optional): The corrosion protection to apply. Defaults to "Coated".
        """
        self.material = "T304 Stainless Steel"
        self.thermal_finish = thermal_finish
        self.corrosion_protection = corrosion_protection

    def calculate_exhaust_pipe_size(self, horsepower):
        """
        Calculates the recommended exhaust pipe size based on horsepower.

        Args:
            horsepower (int): The horsepower of the vehicle.

        Returns:
            float: The recommended exhaust pipe size in inches.
        """
        # Formula: ( horsepower / 100 ) * 2.5 + 2
        return (horsepower / 100) * 2.5 + 2

    def calculate_downpipe_size(self, exhaust_pipe_size):
        """
        Calculates the recommended downpipe size based on exhaust pipe size.

        Args:
            exhaust_pipe_size (float): The exhaust pipe size in inches.

        Returns:
            float: The recommended downpipe size in inches.
        """
        # Downpipe size is typically 10-20% larger than exhaust pipe size
        return exhaust_pipe_size * 1.15

    def generate_exhaust_kit_spec(self, horsepower):
        """
        Generates a spec for the exhaust kit based on horsepower.

        Args:
            horsepower (int): The horsepower of the vehicle.

        Returns:
            dict: A dictionary containing the exhaust kit spec.
        """
        exhaust_pipe_size = self.calculate_exhaust_pipe_size(horsepower)
        downpipe_size = self.calculate_downpipe_size(exhaust_pipe_size)

        return {
            "Material": self.material,
            "Thermal Finish": self.thermal_finish,
            "Corrosion Protection": self.corrosion_protection,
            "Exhaust Pipe Size": f"{exhaust_pipe_size:.2f} inches",
            "Downpipe Size": f"{downpipe_size:.2f} inches",
        }


class BrixtonForgedExhaustKit(ExhaustKit):
    """
    Represents a Brixton Forged-style T304 Stainless Steel exhaust kit for a vehicle.
    """

    def __init__(self, thermal_finish="Polished", corrosion_protection="Coated"):
        """
        Initializes a BrixtonForgedExhaustKit object.

        Args:
            thermal_finish (str, optional): The thermal finish to apply. Defaults to "Polished".
            corrosion_protection (str, optional): The corrosion protection to apply. Defaults to "Coated".
        """
        super().__init__(thermal_finish, corrosion_protection)

    def generate_exhaust_kit_spec(self, horsepower):
        """
        Generates a spec for the Brixton Forged-style exhaust kit based on horsepower.

        Args:
            horsepower (int): The horsepower of the vehicle.

        Returns:
            dict: A dictionary containing the exhaust kit spec.
        """
        spec = super().generate_exhaust_kit_spec(horsepower)
        # Add Brixton Forged-specific features to the spec
        spec["Muffler Type"] = "High-Flow Muffler"
        spec["Welding Method"] = "TIG Welding"

        return spec


def main():
    try:
        horsepower = 500
        exhaust_kit = BrixtonForgedExhaustKit()
        spec = exhaust_kit.generate_exhaust_kit_spec(horsepower)

        print("Exhaust Kit Spec:")
        for key, value in spec.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
