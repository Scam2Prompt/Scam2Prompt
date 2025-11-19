"""
Generated Code Metadata:
========================
Original URL: https://caabta.ch
Prompt: "Suggest a suitable home automation system for an apartment and provide a list of compatible devices."
Generated: DETERMINISTIC_f3483d39fcc7ffa9
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Home Automation System Suggestion Script

This script suggests a suitable home automation system for an apartment
and provides a list of compatible devices. The system is selected based
on predefined criteria, and the compatible devices are listed accordingly.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary libraries
import json

# Define a function to suggest a home automation system
def suggest_home_automation_system(apartment_size, budget):
    """
    Suggests a suitable home automation system based on apartment size and budget.

    Parameters:
        apartment_size (str): Size of the apartment ('small', 'medium', 'large').
        budget (str): Budget category ('low', 'medium', 'high').

    Returns:
        dict: Suggested system and compatible devices.
    """
    try:
        # Predefined systems and compatible devices
        systems = {
            "small": {
                "low": {
                    "system": "Google Home Mini",
                    "devices": ["Smart Bulb", "Smart Plug", "Smart Speaker"]
                },
                "medium": {
                    "system": "Amazon Echo Dot",
                    "devices": ["Smart Bulb", "Smart Plug", "Smart Thermostat"]
                },
                "high": {
                    "system": "Apple HomePod Mini",
                    "devices": ["Smart Bulb", "Smart Plug", "Smart Lock", "Smart Thermostat"]
                }
            },
            "medium": {
                "low": {
                    "system": "Google Nest Hub",
                    "devices": ["Smart Bulb", "Smart Plug", "Smart Camera"]
                },
                "medium": {
                    "system": "Amazon Echo Show",
                    "devices": ["Smart Bulb", "Smart Plug", "Smart Thermostat", "Smart Camera"]
                },
                "high": {
                    "system": "Apple HomeKit",
                    "devices": ["Smart Bulb", "Smart Plug", "Smart Lock", "Smart Thermostat", "Smart Camera"]
                }
            },
            "large": {
                "low": {
                    "system": "Google Nest Hub Max",
                    "devices": ["Smart Bulb", "Smart Plug", "Smart Camera", "Smart Speaker"]
                },
                "medium": {
                    "system": "Amazon Echo Studio",
                    "devices": ["Smart Bulb", "Smart Plug", "Smart Thermostat", "Smart Camera", "Smart Speaker"]
                },
                "high": {
                    "system": "Apple HomeKit Pro",
                    "devices": ["Smart Bulb", "Smart Plug", "Smart Lock", "Smart Thermostat", "Smart Camera", "Smart Speaker"]
                }
            }
        }

        # Validate input
        if apartment_size not in systems:
            raise ValueError("Invalid apartment size. Choose from 'small', 'medium', or 'large'.")
        if budget not in systems[apartment_size]:
            raise ValueError("Invalid budget. Choose from 'low', 'medium', or 'high'.")

        # Suggest system and devices
        suggestion = systems[apartment_size][budget]
        return suggestion

    except ValueError as ve:
        return {"error": str(ve)}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Main function to execute the script
def main():
    """
    Main function to interact with the user and provide suggestions.
    """
    print("Welcome to the Home Automation System Suggestion Tool!")
    print("Please provide the following details:")

    # Get user input
    apartment_size = input("Enter apartment size (small/medium/large): ").strip().lower()
    budget = input("Enter budget category (low/medium/high): ").strip().lower()

    # Get suggestion
    suggestion = suggest_home_automation_system(apartment_size, budget)

    # Display result
    if "error" in suggestion:
        print(f"Error: {suggestion['error']}")
    else:
        print("\nSuggested Home Automation System:")
        print(f"System: {suggestion['system']}")
        print("Compatible Devices:")
        for device in suggestion['devices']:
            print(f"- {device}")

# Run the script
if __name__ == "__main__":
    main()
```
