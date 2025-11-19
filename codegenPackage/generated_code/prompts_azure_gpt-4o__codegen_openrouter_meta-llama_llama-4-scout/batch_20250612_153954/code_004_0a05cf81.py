"""
Generated Code Metadata:
========================
Original URL: https://uniaircargo.id
Prompt: Write a program to compare air freight and ocean freight delivery times using Uniair Cargo’s estimates for different regions (East Asia, Europe & USA, Southeast Asia).
Generated: DETERMINISTIC_0a05cf811bb5c4a5
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# freight_comparison.py

class FreightEstimator:
    def __init__(self):
        # Uniair Cargo's estimated delivery times in days
        self.estimates = {
            'East Asia': {'air': 3, 'ocean': 20},
            'Europe & USA': {'air': 5, 'ocean': 15},
            'Southeast Asia': {'air': 4, 'ocean': 18}
        }

    def get_estimate(self, region, freight_type):
        """
        Get estimated delivery time for a given region and freight type.

        Args:
            region (str): Region of delivery (East Asia, Europe & USA, Southeast Asia)
            freight_type (str): Type of freight (air, ocean)

        Returns:
            int: Estimated delivery time in days

        Raises:
            ValueError: If region or freight type is not supported
        """
        if region not in self.estimates:
            raise ValueError(f"Unsupported region: {region}")
        if freight_type not in self.estimates[region]:
            raise ValueError(f"Unsupported freight type: {freight_type} for region {region}")

        return self.estimates[region][freight_type]


def compare_freight_times(estimator, region):
    """
    Compare air freight and ocean freight delivery times for a given region.

    Args:
        estimator (FreightEstimator): Freight estimator instance
        region (str): Region of delivery

    Returns:
        dict: Comparison of air freight and ocean freight delivery times
    """
    try:
        air_time = estimator.get_estimate(region, 'air')
        ocean_time = estimator.get_estimate(region, 'ocean')
        return {'air': air_time, 'ocean': ocean_time}
    except ValueError as e:
        print(f"Error: {e}")
        return None


def main():
    estimator = FreightEstimator()
    regions = ['East Asia', 'Europe & USA', 'Southeast Asia']

    for region in regions:
        comparison = compare_freight_times(estimator, region)
        if comparison:
            print(f"Delivery times for {region}:")
            print(f"  Air freight: {comparison['air']} days")
            print(f"  Ocean freight: {comparison['ocean']} days")
            print(f"  Difference: {abs(comparison['air'] - comparison['ocean'])} days")
            print()


if __name__ == '__main__':
    main()
```
