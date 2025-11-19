"""
Generated Code Metadata:
========================
Original URL: https://elfworldvape.com
Prompt: Compare the features of Elfworld Vape devices, including the Big-B, PB45000, and AI22000, and suggest which one is best for a specific use case.
Generated: DETERMINISTIC_8e499724fc8eac5d
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a class for Elfworld Vape devices
class ElfworldVapeDevice:
    def __init__(self, name, battery_capacity, puff_count, nicotine_level, price):
        """
        Initialize an Elfworld Vape device.

        Args:
            name (str): Device name.
            battery_capacity (int): Battery capacity in mAh.
            puff_count (int): Number of puffs.
            nicotine_level (float): Nicotine level in mg.
            price (float): Device price.
        """
        self.name = name
        self.battery_capacity = battery_capacity
        self.puff_count = puff_count
        self.nicotine_level = nicotine_level
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.battery_capacity}mAh, {self.puff_count} puffs, {self.nicotine_level}mg nicotine, ${self.price:.2f}"


# Define a function to compare Elfworld Vape devices
def compare_devices(devices, use_case):
    """
    Compare Elfworld Vape devices and suggest the best one for a specific use case.

    Args:
        devices (list[ElfworldVapeDevice]): List of Elfworld Vape devices.
        use_case (str): Specific use case (e.g., "heavy_user", " casual_user").

    Returns:
        ElfworldVapeDevice: The recommended device.
    """
    try:
        # Define a dictionary to map use cases to device preferences
        use_case_preferences = {
            "heavy_user": lambda device: device.battery_capacity > 4000 and device.puff_count > 20000,
            "casual_user": lambda device: device.price < 20 and device.puff_count > 5000
        }

        # Check if the use case is valid
        if use_case not in use_case_preferences:
            raise ValueError("Invalid use case")

        # Filter devices based on the use case
        recommended_devices = [device for device in devices if use_case_preferences[use_case](device)]

        # Return the device with the highest puff count
        return max(recommended_devices, key=lambda device: device.puff_count)

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Define Elfworld Vape devices
devices = [
    ElfworldVapeDevice("Big-B", 3000, 15000, 50, 15.99),
    ElfworldVapeDevice("PB45000", 4500, 45000, 30, 24.99),
    ElfworldVapeDevice("AI22000", 2200, 22000, 20, 12.99)
]

# Compare devices and suggest the best one for a specific use case
use_case = "heavy_user"
recommended_device = compare_devices(devices, use_case)

if recommended_device:
    print(f"Recommended device for {use_case}: {recommended_device}")
else:
    print(f"No device recommended for {use_case}")
```
