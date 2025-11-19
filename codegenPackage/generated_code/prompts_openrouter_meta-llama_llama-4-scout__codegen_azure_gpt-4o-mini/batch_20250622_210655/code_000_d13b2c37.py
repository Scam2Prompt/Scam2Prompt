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
class YanmarViO25:
    """
    A class to represent the Yanmar ViO25 mini excavator.
    """

    def __init__(self, motor_power_hp, bucket_volume_cubic_meters, excavation_depth_meters):
        """
        Initializes the Yanmar ViO25 mini excavator with key features.

        Parameters:
        motor_power_hp (float): The power of the motor in horsepower.
        bucket_volume_cubic_meters (float): The volume of the bucket in cubic meters.
        excavation_depth_meters (float): The maximum excavation depth in meters.
        """
        self.motor_power_hp = motor_power_hp
        self.bucket_volume_cubic_meters = bucket_volume_cubic_meters
        self.excavation_depth_meters = excavation_depth_meters

    def display_features(self):
        """
        Displays the key features of the Yanmar ViO25 mini excavator.
        """
        try:
            print("Yanmar ViO25 Mini Excavator Features:")
            print(f"Motor Power: {self.motor_power_hp} HP")
            print(f"Bucket Volume: {self.bucket_volume_cubic_meters} m³")
            print(f"Excavation Depth: {self.excavation_depth_meters} m")
        except Exception as e:
            print(f"An error occurred while displaying features: {e}")

def main():
    """
    Main function to create an instance of YanmarViO25 and display its features.
    """
    try:
        # Create an instance of YanmarViO25 with example specifications
        yanmar_vio25 = YanmarViO25(motor_power_hp=24.8, bucket_volume_cubic_meters=0.1, excavation_depth_meters=2.5)
        
        # Display the features of the excavator
        yanmar_vio25.display_features()
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
