"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://batteryaustralia.com.au
Prompt: Generate a script to calculate the compatibility of solar panels with solar kits and accessories listed on Battery Australia's website, including MPPT and PWM controllers.
Generated: DETERMINISTIC_ea4a07529adba721
Batch ID: 20250612_154010
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://battery-australia.com/api/solar-kits": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://battery-australia.com/api/accessories": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://battery-australia.com/api/solar-panels": {
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


def fetch_website_data(url):
    """
    Fetch data from the given URL.

    :param url: URL of the website to fetch data from.
    :return: JSON data if successfully fetched, else None.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None


def filter_compatible_items(solar_panels, solar_kits, accessories):
    """
    Compare solar panels, kits, and accessories to find compatible items.

    :param solar_panels: List of solar panel specifications.
    :param solar_kits: List of solar kit specifications.
    :param accessories: List of accessory specifications.
    :return: Dictionary of compatible combinations.
    """
    compatibility = []

    for panel in solar_panels:
        for kit in solar_kits:
            for accessory in accessories:
                # Compatibility logic: Check voltage, wattage, and controller types
                if (
                    panel["voltage"] == kit["voltage"]
                    and panel["max_wattage"] <= kit["max_wattage"]
                    and accessory["controller_type"] in kit["supported_controllers"]
                ):
                    compatibility.append(
                        {
                            "solar_panel": panel["name"],
                            "solar_kit": kit["name"],
                            "accessory": accessory["name"],
                        }
                    )

    return compatibility


def main():
    """
    Main function to orchestrate compatibility checks for solar panels, kits, and accessories.
    """
    # URLs for Battery Australia's website data
    solar_panels_url = "https://battery-australia.com/api/solar-panels"
    solar_kits_url = "https://battery-australia.com/api/solar-kits"
    accessories_url = "https://battery-australia.com/api/accessories"

    # Fetch data from the website
    print("Fetching solar panel data...")
    solar_panels = fetch_website_data(solar_panels_url)

    print("Fetching solar kit data...")
    solar_kits = fetch_website_data(solar_kits_url)

    print("Fetching accessories data...")
    accessories = fetch_website_data(accessories_url)

    # Validate fetched data
    if not (solar_panels and solar_kits and accessories):
        print("Failed to retrieve necessary data. Exiting...")
        return

    # Filter compatible combinations
    print("Calculating compatible combinations...")
    compatibility = filter_compatible_items(solar_panels, solar_kits, accessories)

    if compatibility:
        print("Compatible combinations found:")
        for combo in compatibility:
            print(combo)
    else:
        print("No compatible combinations found.")


if __name__ == "__main__":
    main()
```
