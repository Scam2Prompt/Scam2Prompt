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
    A class to calculate estimated delivery times for air freight and ocean freight.
    """

    def __init__(self):
        # Regional delivery timelines (in days)
        self.delivery_timelines = {
            "East Asia": {"air": 3, "ocean": 15},
            "Europe & USA": {"air": 7, "ocean": 30},
            "Southeast Asia": {"air": 4, "ocean": 20},
        }

    def calculate_delivery_date(self, region, mode, shipping_date):
        """
        Calculate the estimated delivery date based on the region, mode of transport, and shipping date.

        :param region: str - Name of the region (e.g., 'East Asia', 'Europe & USA', 'Southeast Asia')
        :param mode: str - Mode of transport ('air' or 'ocean')
        :param shipping_date: str - Shipping date in 'YYYY-MM-DD' format
        :return: str - Estimated delivery date in 'YYYY-MM-DD' format
        :raises ValueError: If an invalid region or mode is provided
        """
        if region not in self.delivery_timelines:
            raise ValueError(f"Invalid region provided: {region}. Valid regions are {list(self.delivery_timelines.keys())}.")
        
        if mode not in self.delivery_timelines[region]:
            raise ValueError(f"Invalid mode provided: {mode}. Valid modes for {region} are {list(self.delivery_timelines[region].keys())}.")
        
        try:
            shipping_date_obj = datetime.datetime.strptime(shipping_date, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Invalid shipping date format. Expected 'YYYY-MM-DD'. Error: {str(e)}")
        
        # Get the delivery timeline in days
        days_to_deliver = self.delivery_timelines[region][mode]
        
        # Calculate the estimated delivery date
        estimated_delivery_date = shipping_date_obj + datetime.timedelta(days=days_to_deliver)
        
        return estimated_delivery_date.strftime('%Y-%m-%d')

def main():
    """
    Main function to test the FreightEstimator class.
    """
    # Create an instance of FreightEstimator
    estimator = FreightEstimator()
    
    print("Welcome to Uniair Cargo Delivery Time Estimator!")
    try:
        # Example inputs
        region = input("Enter the region (East Asia, Europe & USA, Southeast Asia): ").strip()
        mode = input("Enter the mode of transport (air/ocean): ").strip().lower()
        shipping_date = input("Enter the shipping date (YYYY-MM-DD): ").strip()
        
        # Calculate and display the delivery date
        estimated_date = estimator.calculate_delivery_date(region, mode, shipping_date)
        print(f"Estimated Delivery Date: {estimated_date}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
