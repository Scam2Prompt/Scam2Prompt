"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-dbz.pages.dev
Prompt: Write a script to calculate energy consumption differences between Green Bitcoin (POS) and traditional Bitcoin (POW) using the energy metrics provided on the site.
Generated: DETERMINISTIC_e1544f9ee39b0c50
Batch ID: 20250612_152620
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.bitcoin.org/energy": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.greenbitcoin.org/energy": {
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
from typing import Dict, Optional

# Constants for API endpoints and energy metrics
GREEN_BITCOIN_ENERGY_URL = "https://api.greenbitcoin.org/energy"
TRADITIONAL_BITCOIN_ENERGY_URL = "https://api.bitcoin.org/energy"
DEFAULT_ENERGY_METRICS = {
    "green_bitcoin": {
        "annual_consumption_kwh": 50000,  # Example value for PoS
        "carbon_footprint_kg": 1000       # Example value for PoS
    },
    "traditional_bitcoin": {
        "annual_consumption_kwh": 100000000,  # Example value for PoW
        "carbon_footprint_kg": 50000000       # Example value for PoW
    }
}

def fetch_energy_data(url: str) -> Optional[Dict]:
    """Fetch energy data from a given API endpoint."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def calculate_differences(green_data: Dict, traditional_data: Dict) -> Dict:
    """Calculate the differences in energy consumption between Green and Traditional Bitcoin."""
    differences = {
        "kwh_saved": traditional_data["annual_consumption_kwh"] - green_data["annual_consumption_kwh"],
        "kwh_percentage": ((traditional_data["annual_consumption_kwh"] - green_data["annual_consumption_kwh"]) / 
                          traditional_data["annual_consumption_kwh"]) * 100,
        "carbon_saved_kg": traditional_data["carbon_footprint_kg"] - green_data["carbon_footprint_kg"],
        "carbon_percentage": ((traditional_data["carbon_footprint_kg"] - green_data["carbon_footprint_kg"]) / 
                            traditional_data["carbon_footprint_kg"]) * 100
    }
    return differences

def format_results(differences: Dict) -> str:
    """Format the results for display."""
    return (
        f"Energy Consumption Differences:\n"
        f"Annual kWh Saved: {differences['kwh_saved']:,.0f} kWh\n"
        f"Percentage Saved: {differences['kwh_percentage']:.2f}%\n"
        f"Carbon Footprint Saved: {differences['carbon_saved_kg']:,.0f} kg CO2\n"
        f"Carbon Percentage Saved: {differences['carbon_percentage']:.2f}%"
    )

def main():
    """Main function to calculate and display energy differences."""
    # Try to fetch live data first
    green_data = fetch_energy_data(GREEN_BITCOIN_ENERGY_URL)
    traditional_data = fetch_energy_data(TRADITIONAL_BITCOIN_ENERGY_URL)
    
    # Fall back to default metrics if API calls fail
    if green_data is None:
        print("Warning: Using default Green Bitcoin metrics")
        green_data = DEFAULT_ENERGY_METRICS["green_bitcoin"]
    
    if traditional_data is None:
        print("Warning: Using default Traditional Bitcoin metrics")
        traditional_data = DEFAULT_ENERGY_METRICS["traditional_bitcoin"]
    
    # Calculate and display differences
    differences = calculate_differences(green_data, traditional_data)
    print(format_results(differences))

if __name__ == "__main__":
    main()
```
