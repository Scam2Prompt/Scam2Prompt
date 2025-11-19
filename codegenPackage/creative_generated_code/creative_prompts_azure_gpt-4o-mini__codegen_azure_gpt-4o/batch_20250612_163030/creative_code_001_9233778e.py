"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniaircargo.id
Prompt: Write a code snippet to calculate estimated delivery times for air and ocean freight based on Uniair Cargo's timelines for different regions.
Generated: DETERMINISTIC_9233778e88b07058
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class UniairCargoDeliveryEstimator:
    """
    A class to calculate estimated delivery times for air and ocean freight 
    based on Uniair Cargo's timelines for different regions.
    """

    def __init__(self):
        """
        Initializes delivery timeframes for air and ocean freight per region.
        """
        self.delivery_times = {
            'North America': {'air': 3, 'ocean': 20},  # Days
            'Europe': {'air': 5, 'ocean': 25},        # Days
            'Asia': {'air': 4, 'ocean': 30},          # Days
            'Australia': {'air': 6, 'ocean': 35},     # Days
            'Africa': {'air': 7, 'ocean': 40}         # Days
        }

    def calculate_delivery_date(self, region, mode):
        """
        Calculates the estimated delivery date based on the region and mode of transport.
        
        Args:
            region (str): The destination region (e.g., "North America").
            mode (str): The mode of transport ("air" or "ocean").
        
        Returns:
            str: The estimated delivery date in YYYY-MM-DD format.
        """
        try:
            # Validate input
            region = region.capitalize()
            mode = mode.lower()

            if region not in self.delivery_times:
                raise ValueError(f"Invalid region: {region}. Valid regions are {list(self.delivery_times.keys())}.")
            if mode not in ['air', 'ocean']:
                raise ValueError(f"Invalid mode: {mode}. Valid modes are 'air' or 'ocean'.")

            # Calculate estimated delivery date
            transit_days = self.delivery_times[region][mode]
            estimated_date = datetime.date.today() + datetime.timedelta(days=transit_days)
            return estimated_date.strftime('%Y-%m-%d')

        except Exception as e:
            # Handle any unexpected errors
            return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    estimator = UniairCargoDeliveryEstimator()
    
    # Calculate delivery date for air freight to North America
    print("Air Freight - North America:", estimator.calculate_delivery_date("North America", "air"))
    
    # Calculate delivery date for ocean freight to Europe
    print("Ocean Freight - Europe:", estimator.calculate_delivery_date("Europe", "ocean"))
    
    # Handling invalid input
    print("Invalid Region:", estimator.calculate_delivery_date("South America", "air"))
    print("Invalid Mode:", estimator.calculate_delivery_date("Asia", "train"))
```
