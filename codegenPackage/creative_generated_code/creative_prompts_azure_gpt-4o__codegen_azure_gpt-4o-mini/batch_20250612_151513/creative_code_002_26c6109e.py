"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dxlink.net
Prompt: Generate code to calculate bandwidth usage for DX Link's dedicated internet packages, incorporating their BDIX and fiber optic connection features.
Generated: DETERMINISTIC_26c6109e46c8f483
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BandwidthCalculator:
    """
    A class to calculate bandwidth usage for DX Link's dedicated internet packages.
    This includes calculations for BDIX and fiber optic connection features.
    """

    def __init__(self, package_speed_mbps, bdix_usage_mbps=0, fiber_usage_mbps=0):
        """
        Initializes the BandwidthCalculator with package specifications.

        :param package_speed_mbps: The speed of the internet package in Mbps.
        :param bdix_usage_mbps: The usage through BDIX in Mbps (default is 0).
        :param fiber_usage_mbps: The usage through fiber optic in Mbps (default is 0).
        """
        self.package_speed_mbps = package_speed_mbps
        self.bdix_usage_mbps = bdix_usage_mbps
        self.fiber_usage_mbps = fiber_usage_mbps
    
    def total_usage(self):
        """
        Calculates the total bandwidth usage.

        :return: The sum of BDIX and fiber optic usage in Mbps.
        """
        total = self.bdix_usage_mbps + self.fiber_usage_mbps
        return total

    def is_within_limits(self):
        """
        Checks if the total usage is within the limits of the package speed.

        :return: True if within limits, False otherwise.
        """
        total = self.total_usage()
        if total > self.package_speed_mbps:
            return False
        return True

    def display_usage(self):
        """
        Displays the current bandwidth usage and whether it is within limits.
        """
        total = self.total_usage()
        limits_check = self.is_within_limits()
        
        print(f"BDIX Usage: {self.bdix_usage_mbps} Mbps")
        print(f"Fiber Optic Usage: {self.fiber_usage_mbps} Mbps")
        print(f"Total Usage: {total} Mbps")
        print(f"Package Speed: {self.package_speed_mbps} Mbps")
        print("Usage is within package limits." if limits_check else "Usage exceeds package limits.")

def main():
    try:
        # Example usage of BandwidthCalculator
        package_speed = float(input("Enter the package speed in Mbps (e.g., 100): "))
        bdix_usage = float(input("Enter BDIX usage in Mbps: "))
        fiber_usage = float(input("Enter Fiber Optic usage in Mbps: "))

        # Initialize the calculator
        bandwidth_calculator = BandwidthCalculator(package_speed, bdix_usage, fiber_usage)

        # Display the usage details
        bandwidth_calculator.display_usage()

    except ValueError as e:
        print(f"Error: Invalid input. Please enter numeric values. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
