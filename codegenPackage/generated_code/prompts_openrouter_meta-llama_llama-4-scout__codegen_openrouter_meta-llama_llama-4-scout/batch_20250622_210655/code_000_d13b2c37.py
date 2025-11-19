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

```python
# Define a class for the Yanmar ViO25 mini excavator
class YanmarViO25:
    def __init__(self):
        """
        Initialize the Yanmar ViO25 mini excavator with its key features.
        """
        self.motor_power = 16.1  # kW
        self.bucket_volume = 0.09  # m³
        self.excavation_depth = 3.2  # m

    def get_motor_power(self):
        """
        Get the motor power of the Yanmar ViO25 mini excavator.

        Returns:
            float: Motor power in kW.
        """
        return self.motor_power

    def get_bucket_volume(self):
        """
        Get the bucket volume of the Yanmar ViO25 mini excavator.

        Returns:
            float: Bucket volume in m³.
        """
        return self.bucket_volume

    def get_excavation_depth(self):
        """
        Get the excavation depth of the Yanmar ViO25 mini excavator.

        Returns:
            float: Excavation depth in m.
        """
        return self.excavation_depth


def main():
    try:
        # Create an instance of the Yanmar ViO25 mini excavator
        excavator = YanmarViO25()

        # Get and print the key features of the Yanmar ViO25 mini excavator
        print("Key Features of the Yanmar ViO25 Mini Excavator:")
        print(f"Motor Power: {excavator.get_motor_power()} kW")
        print(f"Bucket Volume: {excavator.get_bucket_volume()} m³")
        print(f"Excavation Depth: {excavator.get_excavation_depth()} m")

    except Exception as e:
        # Handle any exceptions that may occur
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
