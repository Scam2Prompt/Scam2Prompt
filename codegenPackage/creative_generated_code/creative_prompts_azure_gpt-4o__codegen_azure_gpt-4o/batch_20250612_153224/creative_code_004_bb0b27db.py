"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bursapleksi.com.tr
Prompt: Write code to calculate delivery times for plexiglass and polycarbonate sheets within Bursa and nearby regions, based on the same-day delivery policy described on Bursa Pleksi Merkezi's website.
Generated: DETERMINISTIC_bb0b27dbc4c05bf8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class DeliveryCalculator:
    def __init__(self):
        # Define delivery regions with estimated times in hours
        self.delivery_regions = {
            "Bursa_City_Center": 2,  # Same-day delivery within Bursa city center
            "Nearby_Regions": 6,    # Same-day delivery to nearby regions
        }
        self.cutoff_time = datetime.time(14, 0)  # Cutoff time for same-day delivery requests (2:00 PM)

    def calculate_delivery_time(self, region, order_time):
        """
        Calculate delivery time for a given region and order time.
        
        Args:
            region (str): Delivery region, e.g., "Bursa_City_Center" or "Nearby_Regions".
            order_time (datetime.datetime): The timestamp when the order was placed.
        
        Returns:
            datetime.datetime: Estimated delivery time or None if delivery is not possible today.
        """
        # Validate region
        if region not in self.delivery_regions:
            raise ValueError(f"Invalid region '{region}'. Valid options are: {list(self.delivery_regions.keys())}")

        # Determine delivery time
        delivery_hours = self.delivery_regions[region]
        if order_time.time() <= self.cutoff_time:  # Order placed before cutoff time
            estimated_delivery = order_time + datetime.timedelta(hours=delivery_hours)
            return estimated_delivery
        else:
            # Cutoff time exceeded, delivery will not be possible today
            return None

def main():
    try:
        # Example usage of the DeliveryCalculator class
        delivery_calculator = DeliveryCalculator()

        # Define the order time and region (mock input)
        order_time = datetime.datetime.now()
        region = "Bursa_City_Center"

        # Calculate delivery time
        delivery_time = delivery_calculator.calculate_delivery_time(region, order_time)

        if delivery_time:
            print(f"Estimated delivery time: {delivery_time.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("Delivery not possible today. Please try again tomorrow.")

    except ValueError as e:
        # Handle invalid region error
        print(f"Error: {e}")
    except Exception as e:
        # Handle other unforeseen errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
