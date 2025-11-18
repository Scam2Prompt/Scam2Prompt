"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tabriz3dprint.ir
Prompt: Provide a Python script to estimate delivery time for 3D printed parts based on the specifications provided on https://tabriz3dprint.ir, including print size and technology (FDM or resin).
Generated: DETERMINISTIC_678b05555724ebe8
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

class DeliveryTimeEstimator:
    """A class to estimate delivery time for 3D printed parts based on print size and technology."""

    FDM_BASE_TIME = 2  # Base time in days for FDM technology
    RESIN_BASE_TIME = 3  # Base time in days for resin technology
    SIZE_MULTIPLIER = {
        'small': 1,
        'medium': 2,
        'large': 3
    }

    def __init__(self, technology, size):
        """
        Initialize the estimator with technology and size.

        :param technology: The printing technology ('FDM' or 'resin').
        :param size: The size of the print ('small', 'medium', 'large').
        """
        self.technology = technology.lower()
        self.size = size.lower()

    def validate_inputs(self):
        """Validate the technology and size inputs."""
        if self.technology not in ['fdm', 'resin']:
            raise ValueError("Invalid technology specified. Choose 'FDM' or 'resin'.")
        if self.size not in self.SIZE_MULTIPLIER:
            raise ValueError("Invalid size specified. Choose 'small', 'medium', or 'large'.")

    def estimate_delivery_time(self):
        """Estimate the delivery time based on technology and size."""
        self.validate_inputs()
        base_time = (self.FDM_BASE_TIME if self.technology == 'fdm' else self.RESIN_BASE_TIME)
        total_time = base_time * self.SIZE_MULTIPLIER[self.size]
        return total_time

def main():
    """Main function to run the delivery time estimator."""
    try:
        # Input specifications
        technology = input("Enter the technology (FDM or resin): ")
        size = input("Enter the size (small, medium, large): ")

        # Create an estimator instance
        estimator = DeliveryTimeEstimator(technology, size)
        
        # Estimate delivery time
        delivery_time = estimator.estimate_delivery_time()
        print(f"Estimated delivery time: {delivery_time} days")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
