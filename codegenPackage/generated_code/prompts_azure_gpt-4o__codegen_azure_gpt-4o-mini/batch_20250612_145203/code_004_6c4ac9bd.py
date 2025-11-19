"""
Generated Code Metadata:
========================
Original URL: https://equinox.by
Prompt: Write a script to compare available Chevrolet Equinox models on Copart and IAAI auctions based on user-defined criteria such as mileage, price, and year.
Generated: DETERMINISTIC_6c4ac9bd574039b9
Batch ID: 20250612_145203
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.iaai.com/v1/vehicles?make=Chevrolet&model=Equinox": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.copart.com/v1/vehicles?make=Chevrolet&model=Equinox": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json

class CarAuctionComparator:
    def __init__(self, copart_api_url, iaai_api_url):
        self.copart_api_url = copart_api_url
        self.iaai_api_url = iaai_api_url

    def fetch_copart_data(self):
        """Fetch Chevrolet Equinox data from Copart."""
        try:
            response = requests.get(self.copart_api_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching data from Copart: {e}")
            return []

    def fetch_iaai_data(self):
        """Fetch Chevrolet Equinox data from IAAI."""
        try:
            response = requests.get(self.iaai_api_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching data from IAAI: {e}")
            return []

    def filter_cars(self, cars, mileage_limit, price_limit, year_limit):
        """Filter cars based on user-defined criteria."""
        filtered_cars = []
        for car in cars:
            if (car['mileage'] <= mileage_limit and
                car['price'] <= price_limit and
                car['year'] >= year_limit):
                filtered_cars.append(car)
        return filtered_cars

    def compare_auctions(self, mileage_limit, price_limit, year_limit):
        """Compare available Chevrolet Equinox models from both auctions."""
        copart_cars = self.fetch_copart_data()
        iaai_cars = self.fetch_iaai_data()

        filtered_copart = self.filter_cars(copart_cars, mileage_limit, price_limit, year_limit)
        filtered_iaai = self.filter_cars(iaai_cars, mileage_limit, price_limit, year_limit)

        return {
            'copart': filtered_copart,
            'iaai': filtered_iaai
        }

def main():
    # Define API URLs for Copart and IAAI
    copart_api_url = "https://api.copart.com/v1/vehicles?make=Chevrolet&model=Equinox"
    iaai_api_url = "https://api.iaai.com/v1/vehicles?make=Chevrolet&model=Equinox"

    # Create an instance of the comparator
    comparator = CarAuctionComparator(copart_api_url, iaai_api_url)

    # User-defined criteria
    mileage_limit = 50000  # Example mileage limit
    price_limit = 20000     # Example price limit
    year_limit = 2018       # Example year limit

    # Compare auctions
    results = comparator.compare_auctions(mileage_limit, price_limit, year_limit)

    # Output results
    print("Filtered Chevrolet Equinox Models:")
    print("Copart:")
    print(json.dumps(results['copart'], indent=4))
    print("IAAI:")
    print(json.dumps(results['iaai'], indent=4))

if __name__ == "__main__":
    main()
```
