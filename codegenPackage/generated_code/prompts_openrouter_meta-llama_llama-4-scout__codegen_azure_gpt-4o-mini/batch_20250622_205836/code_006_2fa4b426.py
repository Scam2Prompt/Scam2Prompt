"""
Generated Code Metadata:
========================
Original URL: https://alphatest.com
Prompt: Design a semi-custom pogo style probe for testing medical devices with a small diameter of 0.010" and a long lasting lifespan.
Generated: DETERMINISTIC_2fa4b42602df2be2
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PogoProbe:
    """
    A class to represent a semi-custom pogo style probe for testing medical devices.
    
    Attributes:
        diameter (float): The diameter of the probe in inches.
        lifespan (int): The expected lifespan of the probe in cycles.
        material (str): The material used for the probe construction.
        is_connected (bool): Status of the probe connection.
    """

    def __init__(self, diameter: float, lifespan: int, material: str):
        """
        Initializes a new instance of the PogoProbe class.
        
        Args:
            diameter (float): The diameter of the probe in inches.
            lifespan (int): The expected lifespan of the probe in cycles.
            material (str): The material used for the probe construction.
        
        Raises:
            ValueError: If diameter is not positive or lifespan is not positive.
        """
        if diameter <= 0:
            raise ValueError("Diameter must be a positive value.")
        if lifespan <= 0:
            raise ValueError("Lifespan must be a positive integer.")
        
        self.diameter = diameter
        self.lifespan = lifespan
        self.material = material
        self.is_connected = False

    def connect(self):
        """Establishes a connection for the probe."""
        if not self.is_connected:
            self.is_connected = True
            print("Probe connected.")
        else:
            print("Probe is already connected.")

    def disconnect(self):
        """Disconnects the probe."""
        if self.is_connected:
            self.is_connected = False
            print("Probe disconnected.")
        else:
            print("Probe is already disconnected.")

    def test_device(self):
        """
        Simulates testing a medical device with the probe.
        
        Raises:
            RuntimeError: If the probe is not connected.
            RuntimeError: If the probe has reached its lifespan.
        """
        if not self.is_connected:
            raise RuntimeError("Cannot test device: Probe is not connected.")
        if self.lifespan <= 0:
            raise RuntimeError("Cannot test device: Probe has reached its lifespan.")
        
        # Simulate testing process
        print("Testing device...")
        self.lifespan -= 1  # Decrease lifespan after each test
        print(f"Test completed. Remaining lifespan: {self.lifespan} cycles.")

    def __str__(self):
        """Returns a string representation of the probe."""
        return (f"PogoProbe(diameter={self.diameter}, "
                f"lifespan={self.lifespan}, material='{self.material}', "
                f"is_connected={self.is_connected})")


# Example usage
if __name__ == "__main__":
    try:
        probe = PogoProbe(diameter=0.010, lifespan=1000, material="Gold-Plated")
        probe.connect()
        for _ in range(5):  # Simulate 5 tests
            probe.test_device()
        probe.disconnect()
    except Exception as e:
        print(f"An error occurred: {e}")
```
