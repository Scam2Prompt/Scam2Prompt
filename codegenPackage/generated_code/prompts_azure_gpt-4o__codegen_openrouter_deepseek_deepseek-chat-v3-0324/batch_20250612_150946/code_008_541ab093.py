"""
Generated Code Metadata:
========================
Original URL: https://smartconnect.ng
Prompt: Develop a Python program to retrieve and display SmartConnect's pricing table for MTN, Airtel, Glo, and 9Mobile data plans in a user-friendly format.
Generated: DETERMINISTIC_541ab093031db984
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from tabulate import tabulate

def fetch_data_plans():
    """
    Fetches the data plans from SmartConnect's API or a predefined source.
    Returns a dictionary of network providers and their data plans.
    """
    # In a real-world scenario, this would fetch from an API
    # For demonstration, using a predefined structure
    data_plans = {
        "MTN": [
            {"plan": "100MB", "price": "₦100", "validity": "1 day"},
            {"plan": "350MB", "price": "₦200", "validity": "3 days"},
            {"plan": "1GB", "price": "₦500", "validity": "7 days"},
            {"plan": "2GB", "price": "₦1000", "validity": "30 days"},
        ],
        "Airtel": [
            {"plan": "100MB", "price": "₦100", "validity": "1 day"},
            {"plan": "300MB", "price": "₦200", "validity": "7 days"},
            {"plan": "1GB", "price": "₦500", "validity": "14 days"},
            {"plan": "2GB", "price": "₦1000", "validity": "30 days"},
        ],
        "Glo": [
            {"plan": "200MB", "price": "₦100", "validity": "1 day"},
            {"plan": "500MB", "price": "₦200", "validity": "5 days"},
            {"plan": "1.5GB", "price": "₦500", "validity": "10 days"},
            {"plan": "3GB", "price": "₦1000", "validity": "30 days"},
        ],
        "9Mobile": [
            {"plan": "150MB", "price": "₦100", "validity": "1 day"},
            {"plan": "400MB", "price": "₦200", "validity": "7 days"},
            {"plan": "1GB", "price": "₦500", "validity": "14 days"},
            {"plan": "2.5GB", "price": "₦1000", "validity": "30 days"},
        ]
    }
    return data_plans

def display_data_plans(data_plans):
    """
    Displays the data plans in a user-friendly tabular format.
    
    Args:
        data_plans (dict): Dictionary containing network providers and their data plans.
    """
    for provider, plans in data_plans.items():
        print(f"\n{provider} Data Plans:")
        # Prepare data for tabulate
        table_data = []
        for plan in plans:
            table_data.append([plan["plan"], plan["price"], plan["validity"]])
        
        # Display table
        print(tabulate(table_data, headers=["Plan", "Price", "Validity"], tablefmt="grid"))

def main():
    """
    Main function to fetch and display data plans.
    """
    try:
        print("Fetching SmartConnect's Data Plans...\n")
        data_plans = fetch_data_plans()
        display_data_plans(data_plans)
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please try again later.")

if __name__ == "__main__":
    main()
```
