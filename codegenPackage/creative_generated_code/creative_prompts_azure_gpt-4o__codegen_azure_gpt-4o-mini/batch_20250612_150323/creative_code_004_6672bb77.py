"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Write a script using the EnergyStar API to calculate the energy savings from routine HVAC maintenance, as recommended by Quality Sheet Metal, Inc., and display the results in a user-friendly format.
Generated: DETERMINISTIC_6672bb77b341cc73
Batch ID: 20250612_150323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.energystar.gov/v1/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests

class EnergyStarAPI:
    BASE_URL = "https://api.energystar.gov/v1/"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_hvac_data(self):
        """Fetch HVAC data from the EnergyStar API."""
        try:
            response = requests.get(f"{self.BASE_URL}hvac", params={"api_key": self.api_key})
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            print(f"Error fetching HVAC data: {e}")
            return None

def calculate_energy_savings(hvac_data):
    """
    Calculate potential energy savings from routine HVAC maintenance.

    Parameters:
        hvac_data (dict): The HVAC data from EnergyStar API.
    
    Returns:
        float: Energy savings in kWh.
    """
    if not hvac_data or 'maintenance_savings' not in hvac_data:
        print("Invalid HVAC data received.")
        return 0.0

    maintenance_savings = hvac_data['maintenance_savings']  # Assuming this key exists
    energy_savings = maintenance_savings * 0.15  # Example calculation (15% savings)
    return energy_savings

def display_results(energy_savings):
    """Display the calculated energy savings in a user-friendly format."""
    print(f"Estimated annual energy savings from routine HVAC maintenance: {energy_savings:.2f} kWh")

def main():
    """Main function to execute the EnergyStar API call and display savings."""
    API_KEY = "YOUR_API_KEY"  # Replace with your actual API key
    energy_star_api = EnergyStarAPI(API_KEY)

    hvac_data = energy_star_api.get_hvac_data()
    if hvac_data:
        energy_savings = calculate_energy_savings(hvac_data)
        display_results(energy_savings)
    else:
        print("Failed to retrieve HVAC data.")

if __name__ == "__main__":
    main()
```
