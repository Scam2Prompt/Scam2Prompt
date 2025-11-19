"""
Generated Code Metadata:
========================
Original URL: https://geeks-on-repair.com
Prompt: What are the services offered by Geeks on Repair for computer and internet repairs in Northern Virginia and Jacksonville, Florida?
Generated: DETERMINISTIC_232874aff8e5fc8b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Geeks on Repair Service Listing API

This module provides a programmatic way to retrieve the services offered by Geeks on Repair
for computer and internet repairs in Northern Virginia and Jacksonville, Florida.

The data is structured as a dictionary with location-based services.
"""

def get_geeks_on_repair_services():
    """
    Returns a dictionary of services offered by Geeks on Repair in specified locations.
    
    Returns:
        dict: A nested dictionary with location as primary key and services as values.
              Each service includes a description and category.
    """
    services = {
        "Northern Virginia": {
            "Computer Repairs": [
                {"name": "Virus/Malware Removal", "description": "Complete removal of viruses and malware"},
                {"name": "Hardware Installation", "description": "Installation of RAM, HDD, SSD, etc."},
                {"name": "Operating System Installation", "description": "Windows, Linux, or macOS installation"},
                {"name": "Data Recovery", "description": "Recovery of lost or corrupted data"},
                {"name": "Laptop Screen Replacement", "description": "Replacement of broken laptop screens"}
            ],
            "Internet Repairs": [
                {"name": "Wi-Fi Setup & Optimization", "description": "Router setup and signal optimization"},
                {"name": "Network Troubleshooting", "description": "Diagnosis and repair of network issues"},
                {"name": "Ethernet Wiring", "description": "Installation and repair of ethernet cables"},
                {"name": "Internet Speed Issues", "description": "Diagnosis and resolution of slow internet"}
            ]
        },
        "Jacksonville, Florida": {
            "Computer Repairs": [
                {"name": "Virus/Malware Removal", "description": "Complete removal of viruses and malware"},
                {"name": "Hardware Upgrades", "description": "Upgrading computer components for better performance"},
                {"name": "Software Installation", "description": "Installation of various software applications"},
                {"name": "PC Tune-Up", "description": "System optimization for better performance"},
                {"name": "Motherboard Repair", "description": "Diagnosis and repair of motherboard issues"}
            ],
            "Internet Repairs": [
                {"name": "Router Configuration", "description": "Proper setup of home/office routers"},
                {"name": "Network Security", "description": "Setup of firewalls and security protocols"},
                {"name": "Wireless Range Extension", "description": "Solutions to extend Wi-Fi coverage"},
                {"name": "ISP Liaison", "description": "Assistance with internet service provider issues"}
            ]
        }
    }
    
    return services

def display_services(location=None):
    """
    Displays services for a specific location or all locations.
    
    Args:
        location (str, optional): Specific location to display services for. 
                                 If None, displays all locations.
    """
    services = get_geeks_on_repair_services()
    
    if location:
        if location in services:
            print(f"\nServices in {location}:")
            for category, service_list in services[location].items():
                print(f"\n{category}:")
                for service in service_list:
                    print(f" - {service['name']}: {service['description']}")
        else:
            print(f"Error: Location '{location}' not found in service areas.")
    else:
        for loc, categories in services.items():
            print(f"\nServices in {loc}:")
            for category, service_list in categories.items():
                print(f"\n{category}:")
                for service in service_list:
                    print(f" - {service['name']}: {service['description']}")

if __name__ == "__main__":
    # Example usage
    display_services()
    # To display services for a specific location:
    # display_services("Northern Virginia")
```
