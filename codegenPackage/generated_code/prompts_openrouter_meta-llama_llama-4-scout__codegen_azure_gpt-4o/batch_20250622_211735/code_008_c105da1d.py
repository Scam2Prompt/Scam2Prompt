"""
Generated Code Metadata:
========================
Original URL: https://momspg.com
Prompt: "Write a script to analyze tenant data and generate insights on preferences for amenities like attached washrooms, parking, and kitchen facilities."
Generated: DETERMINISTIC_c105da1ded8b234d
Batch ID: 20250622_211735
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from collections import Counter

def load_tenant_data(file_path):
    """
    Load tenant data from a JSON file.

    Args:
        file_path (str): Path to the JSON file containing tenant data.

    Returns:
        list: List of tenant records as dictionaries.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON data")
        return []

def analyze_preferences(tenant_data):
    """
    Analyze tenant preferences for amenities.

    Args:
        tenant_data (list): List of tenant records.

    Returns:
        dict: Insights on preferences for amenities.
    """
    # Initialize counters for each amenity
    preferences = Counter()

    for tenant in tenant_data:
        # Check and count preferences for each amenity
        if tenant.get('attached_washroom', False):
            preferences['attached_washroom'] += 1
        if tenant.get('parking', False):
            preferences['parking'] += 1
        if tenant.get('kitchen_facility', False):
            preferences['kitchen_facility'] += 1

    return preferences

def generate_insights(preferences, total_tenants):
    """
    Generate insights based on preferences.

    Args:
        preferences (dict): Count of preferences for each amenity.
        total_tenants (int): Total number of tenants.

    Returns:
        dict: Insights with percentages for each amenity.
    """
    insights = {}
    for amenity, count in preferences.items():
        insights[amenity] = {
            'count': count,
            'percentage': (count / total_tenants) * 100 if total_tenants > 0 else 0
        }
    return insights

def main():
    """
    Main function to load tenant data, analyze preferences, and generate insights.
    """
    # Path to the tenant data file
    file_path = 'tenant_data.json'

    # Load tenant data
    tenant_data = load_tenant_data(file_path)

    if not tenant_data:
        print("No tenant data available for analysis.")
        return

    # Analyze preferences
    preferences = analyze_preferences(tenant_data)

    # Generate insights
    total_tenants = len(tenant_data)
    insights = generate_insights(preferences, total_tenants)

    # Display insights
    print("Tenant Preferences Insights:")
    for amenity, data in insights.items():
        print(f"{amenity.capitalize()}: {data['count']} tenants ({data['percentage']:.2f}%)")

if __name__ == "__main__":
    main()
```

### Notes:
- The script assumes tenant data is stored in a JSON file (`tenant_data.json`) with each tenant record being a dictionary containing boolean values for amenities (`attached_washroom`, `parking`, `kitchen_facility`).
- Error handling is included for file operations and JSON decoding.
- The code is modular, with functions for loading data, analyzing preferences, and generating insights.
