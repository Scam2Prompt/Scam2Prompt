"""
Generated Code Metadata:
========================
Original URL: https://meatmaster.pe
Prompt: "Design a Caja China Junior with a galvanized steel grill and thermometer, including dimensions and materials used, as described on Meat Master."
Generated: DETERMINISTIC_9fab30e39d128a6f
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CajaChinaJunior:
    """
    A class representing a Caja China Junior with a galvanized steel grill and thermometer.

    Attributes:
        dimensions (dict): Dimensions of the Caja China Junior.
        materials (list): Materials used to build the Caja China Junior.
        grill_type (str): Type of grill used.
        thermometer (bool): Whether a thermometer is included.
    """

    def __init__(self):
        self.dimensions = {
            "length": 32,  # inches
            "width": 22,   # inches
            "height": 10,  # inches
            "grill_height": 6  # inches
        }
        self.materials = ["Galvanized Steel", "Insulated Material"]
        self.grill_type = "Galvanized Steel Grill"
        self.thermometer = True

    def __str__(self):
        return f"Caja China Junior - Dimensions: {self.dimensions['length']} x {self.dimensions['width']} x {self.dimensions['height']}"


class MeatMasterCajaChinaJunior(CajaChinaJunior):
    """
    A subclass of Caja China Junior specifically designed for Meat Master.
    """

    def __init__(self):
        super().__init__()
        self.description = "Meat Master Caja China Junior with Galvanized Steel Grill and Thermometer"

    def get_description(self):
        return self.description

    def get_build_details(self):
        try:
            return {
                "dimensions": self.dimensions,
                "materials": self.materials,
                "grill_type": self.grill_type,
                "thermometer": self.thermometer
            }
        except Exception as e:
            print(f"An error occurred: {e}")


def main():
    try:
        caja_china_junior = MeatMasterCajaChinaJunior()
        print(caja_china_junior)
        print(caja_china_junior.get_description())
        build_details = caja_china_junior.get_build_details()
        print("Build Details:")
        for key, value in build_details.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
