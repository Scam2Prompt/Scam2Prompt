"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoin.rf.gd
Prompt: Create a comparison of hosting services that include free domain names, unlimited disk space, and SSL certificates, with a focus on iFastNet hosting features.
Generated: DETERMINISTIC_16b4aa006f64dbdf
Batch ID: 20250612_154827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# hosting_comparison.py

"""
This script generates a comparison of hosting services
with a focus on iFastNet's hosting features.
Criteria for comparison:
1. Free domain names
2. Unlimited disk space
3. SSL certificates

The program outputs a JSON file summarizing the services.
"""

import json

# Define hosting service data
HOSTING_SERVICES = [
    {
        "name": "iFastNet",
        "free_domain_name": True,
        "unlimited_disk_space": True,
        "ssl_certificate": True,
        "price_per_month": 3.99,
        "description": "Offers premium hosting features with free domain and SSL."
    },
    {
        "name": "Bluehost",
        "free_domain_name": True,
        "unlimited_disk_space": True,
        "ssl_certificate": True,
        "price_per_month": 2.95,
        "description": "Reliable hosting with free domain and SSL included."
    },
    {
        "name": "HostGator",
        "free_domain_name": True,
        "unlimited_disk_space": True,
        "ssl_certificate": True,
        "price_per_month": 2.75,
        "description": "Affordable hosting with unlimited resources and free SSL."
    },
    {
        "name": "SiteGround",
        "free_domain_name": False,
        "unlimited_disk_space": False,
        "ssl_certificate": True,
        "price_per_month": 3.99,
        "description": "Known for fast hosting but does not offer unlimited storage."
    }
]

def filter_hosting_services(services, criteria):
    """
    Filter hosting services based on given criteria.

    Args:
        services (list): List of hosting service dictionaries.
        criteria (dict): Filtering criteria (e.g., {'free_domain_name': True}).

    Returns:
        list: Filtered list of hosting services.
    """
    try:
        # Apply filtering criteria
        filtered_services = [
            service for service in services
            if all(service[key] == value for key, value in criteria.items())
        ]
        return filtered_services
    except Exception as e:
        print(f"Error during filtering: {e}")
        return []

def generate_comparison_json(services, output_file="hosting_comparison.json"):
    """
    Generate a JSON file summarizing hosting services.

    Args:
        services (list): List of hosting service dictionaries.
        output_file (str): Name of the output JSON file.
    """
    try:
        # Write JSON data to file
        with open(output_file, 'w') as file:
            json.dump(services, file, indent=4)
        print(f"Comparison JSON file generated: {output_file}")
    except Exception as e:
        print(f"Error writing JSON file: {e}")

def main():
    """
    Main function to filter hosting services and generate a JSON file.
    """
    # Filtering criteria: Focus on free domain, unlimited disk space, and SSL certificates
    criteria = {
        "free_domain_name": True,
        "unlimited_disk_space": True,
        "ssl_certificate": True
    }
    
    # Filter services based on criteria
    filtered_services = filter_hosting_services(HOSTING_SERVICES, criteria)
    
    # Generate JSON file for comparison
    generate_comparison_json(filtered_services)

if __name__ == "__main__":
    main()
```
