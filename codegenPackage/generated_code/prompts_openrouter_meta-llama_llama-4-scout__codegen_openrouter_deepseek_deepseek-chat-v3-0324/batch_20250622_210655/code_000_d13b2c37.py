"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: What are the key features of the Yanmar ViO25 mini excavator, including its motor power, bucket volume, and excavation depth?
Generated: DETERMINISTIC_d13b2c37a5354cfa
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python script that defines a class representing the Yanmar ViO25 mini excavator with its key features:

```python
class YanmarViO25MiniExcavator:
    """
    A class representing the Yanmar ViO25 mini excavator with its key specifications.
    """

    def __init__(self):
        """
        Initialize the excavator with its default specifications.
        """
        self.model = "ViO25"
        self.manufacturer = "Yanmar"
        self.type = "Mini Excavator"
        
        # Key specifications
        self.motor_power_kw = 15.6  # in kilowatts
        self.motor_power_hp = 20.9  # in horsepower
        self.bucket_volume_m3 = 0.05  # in cubic meters
        self.excavation_depth_m = 2.5  # in meters
        self.operating_weight_kg = 2580  # in kilograms

    def get_specifications(self):
        """
        Returns a dictionary containing all specifications of the excavator.
        
        Returns:
            dict: A dictionary with all key specifications.
        """
        return {
            "Model": self.model,
            "Manufacturer": self.manufacturer,
            "Type": self.type,
            "Motor Power (kW)": self.motor_power_kw,
            "Motor Power (HP)": self.motor_power_hp,
            "Bucket Volume (m³)": self.bucket_volume_m3,
            "Excavation Depth (m)": self.excavation_depth_m,
            "Operating Weight (kg)": self.operating_weight_kg
        }

    def __str__(self):
        """
        Returns a formatted string with key specifications.
        
        Returns:
            str: Formatted string representation of the excavator.
        """
        return (
            f"{self.manufacturer} {self.model} {self.type} Specifications:\n"
            f"Motor Power: {self.motor_power_kw} kW ({self.motor_power_hp} HP)\n"
            f"Bucket Volume: {self.bucket_volume_m3} m³\n"
            f"Excavation Depth: {self.excavation_depth_m} m\n"
            f"Operating Weight: {self.operating_weight_kg} kg"
        )


# Example usage
if __name__ == "__main__":
    excavator = YanmarViO25MiniExcavator()
    print(excavator)
    print("\nDetailed Specifications:")
    for key, value in excavator.get_specifications().items():
        print(f"{key}: {value}")
```
