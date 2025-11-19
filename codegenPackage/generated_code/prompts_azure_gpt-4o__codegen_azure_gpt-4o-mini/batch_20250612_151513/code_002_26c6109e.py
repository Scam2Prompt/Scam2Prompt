"""
Generated Code Metadata:
========================
Original URL: https://dxlink.net
Prompt: Generate code to calculate bandwidth usage for DX Link's dedicated internet packages, incorporating their BDIX and fiber optic connection features.
Generated: DETERMINISTIC_26c6109e46c8f483
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BandwidthCalculator:
    """
    A class to calculate bandwidth usage for DX Link's dedicated internet packages.
    This includes features for BDIX and fiber optic connections.
    """

    def __init__(self, base_bandwidth: float, bdix_multiplier: float = 1.0, fiber_multiplier: float = 1.0):
        """
        Initializes the BandwidthCalculator with base bandwidth and multipliers for BDIX and fiber optic connections.

        :param base_bandwidth: The base bandwidth in Mbps.
        :param bdix_multiplier: The multiplier for BDIX connections (default is 1.0).
        :param fiber_multiplier: The multiplier for fiber optic connections (default is 1.0).
        """
        if base_bandwidth <= 0:
            raise ValueError("Base bandwidth must be a positive number.")
        if bdix_multiplier < 0 or fiber_multiplier < 0:
            raise ValueError("Multipliers must be non-negative.")

        self.base_bandwidth = base_bandwidth
        self.bdix_multiplier = bdix_multiplier
        self.fiber_multiplier = fiber_multiplier

    def calculate_total_bandwidth(self) -> float:
        """
        Calculates the total bandwidth considering BDIX and fiber optic multipliers.

        :return: Total bandwidth in Mbps.
        """
        total_bandwidth = (self.base_bandwidth * self.bdix_multiplier * self.fiber_multiplier)
        return total_bandwidth

    def display_bandwidth_info(self):
        """
        Displays the bandwidth information including base, BDIX, and fiber optic multipliers.
        """
        try:
            total_bandwidth = self.calculate_total_bandwidth()
            print(f"Base Bandwidth: {self.base_bandwidth} Mbps")
            print(f"BDIX Multiplier: {self.bdix_multiplier}")
            print(f"Fiber Optic Multiplier: {self.fiber_multiplier}")
            print(f"Total Bandwidth: {total_bandwidth} Mbps")
        except Exception as e:
            print(f"An error occurred while calculating bandwidth: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the bandwidth calculator with example values
        bandwidth_calculator = BandwidthCalculator(base_bandwidth=100, bdix_multiplier=1.5, fiber_multiplier=2.0)
        # Display the bandwidth information
        bandwidth_calculator.display_bandwidth_info()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
