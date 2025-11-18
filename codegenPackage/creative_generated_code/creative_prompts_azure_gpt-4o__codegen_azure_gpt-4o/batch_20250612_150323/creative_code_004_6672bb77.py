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
  "https://api.energystar.gov/v1/hvac_energy_savings": {
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
import json

# Constants
API_URL = "https://api.energystar.gov/v1/hvac_energy_savings"  # Replace with actual EnergyStar API endpoint if available
API_KEY = "YOUR_API_KEY_HERE"  # Replace with a valid API key
DEFAULT_HVAC_PARAMETERS = {
    "system_type": "central_air_conditioner",
    "age_of_system": 10,  # Age in years
    "routine_maintenance_performed": True
}

def get_energy_savings(api_url, api_key, hvac_params):
    """
    Fetch energy savings data from the EnergyStar API based on HVAC parameters.

    Args:
        api_url (str): The API endpoint URL.
        api_key (str): The API key for authentication.
        hvac_params (dict): Parameters for the HVAC system.

    Returns:
        dict: A dictionary containing energy savings data.
    """
    try:
        # Set up headers for authentication
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        # Make a POST request to the EnergyStar API
        response = requests.post(api_url, headers=headers, json=hvac_params)

        # Raise HTTPError if the request failed
        response.raise_for_status()

        # Parse the JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while connecting to the EnergyStar API: {e}")
        return None

def display_results(results):
    """
    Format and display energy savings results in a user-friendly way.

    Args:
        results (dict): A dictionary containing energy savings data.
    """
    if not results:
        print("No results to display.")
        return
    
    print("\nEnergy Savings Results:")
    print("-----------------------")
    print(f"Annual Energy Savings: {results.get('annual_savings_kwh', 'N/A')} kWh")
    print(f"Annual Cost Savings: ${results.get('annual_cost_savings', 'N/A'):.2f}")
    print(f"CO2 Emissions Reduction: {results.get('co2_reduction_kg', 'N/A')} kg")
    print("Thank you for using this tool!")

def main():
    """
    Main function to calculate and display energy savings from routine HVAC maintenance.
    """
    print("Welcome to the HVAC Energy Savings Calculator!")

    # Call the API to get energy savings data
    results = get_energy_savings(API_URL, API_KEY, DEFAULT_HVAC_PARAMETERS)

    # Display the results in a user-friendly format
    display_results(results)

if __name__ == "__main__":
    main()
```

**Note**: Replace placeholder values (such as `API_URL` and `API_KEY`) with actual values from the EnergyStar API documentation. The script assumes the availability of an endpoint for calculating HVAC energy savings. Adjust parameters and error handling as needed based on the API details.
