"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniair.id
Prompt: Write a Python script to calculate estimated delivery times for air freight and ocean freight based on the regional timelines provided by Uniair Cargo (e.g., East Asia, Europe & USA, Southeast Asia).
Generated: DETERMINISTIC_e5a3cbb9d5dcd28d
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class FreightEstimator:
    """
    A class to estimate delivery times for air freight and ocean freight based on regions.
    """

    # Estimated delivery times in days for air and ocean freight by region
    DELIVERY_TIMES = {
        "East Asia": {"air": 3, "ocean": 14},
        "Europe & USA": {"air": 5, "ocean": 30},
        "Southeast Asia": {"air": 4, "ocean": 20},
    }

    def __init__(self, region):
        """
        Initializes the FreightEstimator with the specified region.

        :param region: The region for which to estimate delivery times.
        :raises ValueError: If the region is not supported.
        """
        self.region = region
        if region not in self.DELIVERY_TIMES:
            raise ValueError(f"Unsupported region: {region}. Available regions: {list(self.DELIVERY_TIMES.keys())}")

    def estimate_delivery(self, mode):
        """
        Estimates delivery time based on the mode of transport.

        :param mode: The mode of transport ('air' or 'ocean').
        :return: Estimated delivery time in days.
        :raises ValueError: If the mode of transport is not supported.
        """
        if mode not in ["air", "ocean"]:
            raise ValueError("Unsupported mode of transport. Use 'air' or 'ocean'.")

        return self.DELIVERY_TIMES[self.region][mode]

    def calculate_arrival_date(self, mode):
        """
        Calculates the estimated arrival date based on the mode of transport.

        :param mode: The mode of transport ('air' or 'ocean').
        :return: Estimated arrival date as a string.
        """
        delivery_days = self.estimate_delivery(mode)
        # Current date
        current_date = datetime.datetime.now()
        # Calculate the estimated arrival date
        arrival_date = current_date + datetime.timedelta(days=delivery_days)
        return arrival_date.strftime("%Y-%m-%d")

def main():
    """
    Main function to execute the freight estimation process.
    """
    try:
        region = input("Enter the region (East Asia, Europe & USA, Southeast Asia): ")
        mode = input("Enter mode of transport (air/ocean): ").lower()

        estimator = FreightEstimator(region)
        delivery_time = estimator.estimate_delivery(mode)
        arrival_date = estimator.calculate_arrival_date(mode)

        print(f"Estimated delivery time: {delivery_time} days")
        print(f"Estimated arrival date: {arrival_date}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
