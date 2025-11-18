"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tibvanboxtel.nl
Prompt: Generate a script to estimate the cost and energy savings for installing solar panels and EV charging stations, using the services described on Technische Installatiebedrijf van Boxtel's website.
Generated: DETERMINISTIC_3c1f97071191b610
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

# Constants
SOLAR_PANEL_COST_PER_WATT = 0.5  # Example cost in euros per watt
EV_CHARGING_STATION_COST = 1200  # Example cost in euros per charging station
AVERAGE_SUNLIGHT_HOURS_PER_DAY = 4.5  # Example average sunlight hours per day
ENERGY_SAVINGS_PER_KWH = 0.22  # Example savings in euros per kWh
EV_CHARGER_ENERGY_USAGE = 15  # kWh used per EV charging session
DAYS_PER_YEAR = 365

# Helper function to fetch data (e.g., installation costs) from the website
def fetch_website_data(url):
    """
    Fetch data from the Technische Installatiebedrijf van Boxtel website.
    
    Args:
        url (str): The URL of the website.
    
    Returns:
        str: The fetched data.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

# Function to estimate solar panel savings
def estimate_solar_panel_savings(power_in_kw, cost_per_watt, avg_sunlight_hours, savings_per_kwh):
    """
    Estimate the cost and savings for installing solar panels.
    
    Args:
        power_in_kw (float): Total power in kW.
        cost_per_watt (float): Cost per watt in euros.
        avg_sunlight_hours (float): Average sunlight hours per day.
        savings_per_kwh (float): Savings per kWh in euros.
    
    Returns:
        dict: Estimated cost and annual savings.
    """
    try:
        total_cost = power_in_kw * 1000 * cost_per_watt
        annual_energy_production_kwh = power_in_kw * avg_sunlight_hours * DAYS_PER_YEAR
        annual_savings = annual_energy_production_kwh * savings_per_kwh
        return {
            "Total Cost (€)": round(total_cost, 2),
            "Annual Energy Production (kWh)": round(annual_energy_production_kwh, 2),
            "Annual Savings (€)": round(annual_savings, 2)
        }
    except Exception as e:
        print(f"Error estimating solar panel savings: {e}")
        return None

# Function to estimate EV charging station savings
def estimate_ev_charging_savings(num_stations, cost_per_station, energy_usage_per_session, savings_per_kwh):
    """
    Estimate the cost and savings for installing EV charging stations.
    
    Args:
        num_stations (int): Number of charging stations.
        cost_per_station (float): Cost per station in euros.
        energy_usage_per_session (float): Energy usage per charging session in kWh.
        savings_per_kwh (float): Savings per kWh in euros.
    
    Returns:
        dict: Estimated cost and annual savings.
    """
    try:
        total_cost = num_stations * cost_per_station
        annual_energy_usage_kwh = num_stations * energy_usage_per_session * DAYS_PER_YEAR
        annual_savings = annual_energy_usage_kwh * savings_per_kwh
        return {
            "Total Cost (€)": round(total_cost, 2),
            "Annual Energy Usage (kWh)": round(annual_energy_usage_kwh, 2),
            "Annual Savings (€)": round(annual_savings, 2)
        }
    except Exception as e:
        print(f"Error estimating EV charging savings: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Define input values
    solar_panel_power_kw = 5  # Example: 5 kW solar panels
    num_ev_stations = 2  # Example: 2 EV charging stations
    
    # Estimate solar panel savings
    solar_savings = estimate_solar_panel_savings(
        power_in_kw=solar_panel_power_kw,
        cost_per_watt=SOLAR_PANEL_COST_PER_WATT,
        avg_sunlight_hours=AVERAGE_SUNLIGHT_HOURS_PER_DAY,
        savings_per_kwh=ENERGY_SAVINGS_PER_KWH
    )
    
    # Estimate EV charging station savings
    ev_savings = estimate_ev_charging_savings(
        num_stations=num_ev_stations,
        cost_per_station=EV_CHARGING_STATION_COST,
        energy_usage_per_session=EV_CHARGER_ENERGY_USAGE,
        savings_per_kwh=ENERGY_SAVINGS_PER_KWH
    )
    
    # Output results
    print("Solar Panel Savings:")
    print(solar_savings)
    print("\nEV Charging Station Savings:")
    print(ev_savings)
```
