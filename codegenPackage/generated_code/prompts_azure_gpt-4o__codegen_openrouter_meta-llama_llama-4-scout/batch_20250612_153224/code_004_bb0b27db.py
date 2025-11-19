"""
Generated Code Metadata:
========================
Original URL: https://www.bursapleksi.com.tr
Prompt: Write code to calculate delivery times for plexiglass and polycarbonate sheets within Bursa and nearby regions, based on the same-day delivery policy described on Bursa Pleksi Merkezi's website.
Generated: DETERMINISTIC_bb0b27dbc4c05bf8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict
from datetime import datetime, timedelta

class DeliveryCalculator:
    def __init__(self):
        # Define same-day delivery regions and their corresponding distances from Bursa
        self.regions: Dict[str, int] = {
            "Bursa Merkez": 0,  # Bursa city center
            "Osmangazi": 10,   # Osmangazi district
            "Nilüfer": 15,     # Nilüfer district
            "Mudanya": 30,     # Mudanya district
            "Gemlik": 40,      # Gemlik district
            "Orhangazi": 50,   # Orhangazi district
            "İnegöl": 60,      # İnegöl district
            "Yenişehir": 70,   # Yenişehir district
            "Büyükorhan": 80,  # Büyükorhan district
            "Harmancık": 90,   # Harmancık district
            "Keles": 100,      # Keles district
            "Orhaneli": 110,   # Orhaneli district
            "Gölyazı": 120     # Gölyazı neighborhood
        }
        
        # Define delivery times in hours for each region
        self.delivery_times: Dict[int, str] = {
            0: "same-day",     # 0-10 km: same-day delivery
            10: "next-day",    # 11-30 km: next-day delivery
            30: "2-days",      # 31-60 km: 2-day delivery
            60: "3-days"       # 61+ km: 3-day delivery
        }

    def calculate_delivery_time(self, region: str, distance: int = None) -> str:
        """
        Calculate delivery time for a given region.

        Args:
        region (str): The region for delivery.
        distance (int): The distance from Bursa (optional).

        Returns:
        str: The estimated delivery time.
        """
        if region not in self.regions:
            raise ValueError("Invalid region")

        if distance is None:
            distance = self.regions[region]

        # Sort delivery times by distance
        sorted_delivery_times = sorted(self.delivery_times.items())

        # Find the appropriate delivery time based on distance
        for dist, delivery_time in sorted_delivery_times:
            if distance <= dist:
                return delivery_time

        # Default to 3-day delivery if distance exceeds all defined ranges
        return "3-days"

    def get_eta(self, region: str, order_time: datetime, distance: int = None) -> datetime:
        """
        Calculate the estimated time of arrival (ETA) for an order.

        Args:
        region (str): The region for delivery.
        order_time (datetime): The time the order was placed.
        distance (int): The distance from Bursa (optional).

        Returns:
        datetime: The estimated time of arrival.
        """
        delivery_time = self.calculate_delivery_time(region, distance)

        if delivery_time == "same-day":
            # Assuming same-day delivery cutoff is 12:00 PM
            if order_time.hour >= 12:
                return order_time.date() + timedelta(days=1)
            else:
                return order_time.date()
        elif delivery_time == "next-day":
            return order_time.date() + timedelta(days=1)
        elif delivery_time == "2-days":
            return order_time.date() + timedelta(days=2)
        elif delivery_time == "3-days":
            return order_time.date() + timedelta(days=3)

def main():
    calculator = DeliveryCalculator()

    # Test cases
    regions = ["Bursa Merkez", "Mudanya", "İnegöl", "Gölyazı"]
    order_time = datetime.now()

    for region in regions:
        try:
            delivery_time = calculator.calculate_delivery_time(region)
            eta = calculator.get_eta(region, order_time)
            print(f"Region: {region}, Delivery Time: {delivery_time}, ETA: {eta.date()}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
