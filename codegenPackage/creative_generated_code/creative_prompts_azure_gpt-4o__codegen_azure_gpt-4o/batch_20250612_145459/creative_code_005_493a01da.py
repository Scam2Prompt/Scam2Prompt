"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethtransaction.ezyro.com
Prompt: Provide a comparison of hosting services that include free domain names, unlimited bandwidth, and modern cPanel features, focusing on iFastNet's offerings.
Generated: DETERMINISTIC_493a01da7041a1ca
Batch ID: 20250612_145459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from prettytable import PrettyTable


def fetch_hosting_services_data():
    """
    Fetch hosting services data from a mock API or a real API.

    Returns:
        list: A list of hosting service dictionaries.
    """
    try:
        # For demonstration purposes, we'll use a mock dataset.
        # Replace the below dummy data with actual API calls if available.
        hosting_services = [
            {
                "name": "iFastNet",
                "free_domain": True,
                "unlimited_bandwidth": True,
                "modern_cpanel": True,
                "price": "$4.99/month",
            },
            {
                "name": "Bluehost",
                "free_domain": True,
                "unlimited_bandwidth": True,
                "modern_cpanel": True,
                "price": "$2.95/month",
            },
            {
                "name": "HostGator",
                "free_domain": True,
                "unlimited_bandwidth": True,
                "modern_cpanel": True,
                "price": "$2.75/month",
            },
        ]
        return hosting_services

    except requests.RequestException as e:
        print(f"Error fetching hosting services data: {e}")
        return []


def filter_hosting_services(services):
    """
    Filters hosting services based on criteria:
    - Free domain
    - Unlimited bandwidth
    - Modern cPanel features

    Args:
        services (list): List of hosting service dictionaries.

    Returns:
        list: Filtered list of hosting services.
    """
    return [
        service
        for service in services
        if service.get("free_domain")
        and service.get("unlimited_bandwidth")
        and service.get("modern_cpanel")
    ]


def display_hosting_comparison(services):
    """
    Display a comparison of hosting services in a table format.

    Args:
        services (list): List of hosting service dictionaries.
    """
    table = PrettyTable()
    table.field_names = ["Hosting Service", "Free Domain", "Unlimited Bandwidth", "Modern cPanel", "Price"]

    for service in services:
        table.add_row(
            [
                service["name"],
                "Yes" if service["free_domain"] else "No",
                "Yes" if service["unlimited_bandwidth"] else "No",
                "Yes" if service["modern_cpanel"] else "No",
                service["price"],
            ]
        )

    print(table)


def main():
    """
    Main function to orchestrate the comparison of hosting services.
    """
    print("Fetching hosting services data...\n")
    all_services = fetch_hosting_services_data()

    if not all_services:
        print("No hosting services data available. Exiting.")
        return

    print("Filtering hosting services based on criteria...\n")
    filtered_services = filter_hosting_services(all_services)

    if not filtered_services:
        print("No hosting services match the given criteria. Exiting.")
        return

    print("Displaying comparison of hosting services:\n")
    display_hosting_comparison(filtered_services)


if __name__ == "__main__":
    main()
```
