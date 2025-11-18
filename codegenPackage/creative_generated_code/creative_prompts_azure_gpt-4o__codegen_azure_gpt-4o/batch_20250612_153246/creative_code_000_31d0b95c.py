"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sundancespasadvantage.com
Prompt: Write a Python script to simulate a dealer onboarding process for the Sundance Spas Retail Advantage program, including input fields for company name, location, and showroom details.
Generated: DETERMINISTIC_31d0b95c6185c719
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def get_dealer_info():
    """
    Collect dealer information for onboarding. 
    Returns a dictionary with the company name, location, and showroom details.
    """
    try:
        # Collect company name
        company_name = input("Enter the company name: ").strip()
        if not company_name:
            raise ValueError("Company name cannot be empty.")

        # Collect location
        location = input("Enter the company location (City, State): ").strip()
        if not location:
            raise ValueError("Location cannot be empty.")

        # Collect showroom details
        showroom_details = input("Enter showroom details (e.g., size, features): ").strip()
        if not showroom_details:
            raise ValueError("Showroom details cannot be empty.")

        # Return the collected data
        return {
            "company_name": company_name,
            "location": location,
            "showroom_details": showroom_details
        }
    except ValueError as ve:
        print(f"Error: {ve}")
        return None


def save_dealer_info(dealer_data, file_path="dealer_data.json"):
    """
    Save dealer information to a JSON file.
    Args:
        dealer_data (dict): The dictionary containing dealer information.
        file_path (str): The path to save the JSON file. Defaults to 'dealer_data.json'.
    """
    try:
        if not dealer_data:
            raise ValueError("Dealer data is empty or invalid.")

        # Write data to the JSON file
        with open(file_path, 'w') as file:
            json.dump(dealer_data, file, indent=4)
        print(f"Dealer information successfully saved to {file_path}.")
    except Exception as e:
        print(f"Error saving dealer information: {e}")


def main():
    """
    Main function to simulate the dealer onboarding process.
    """
    print("Welcome to the Sundance Spas Retail Advantage Dealer Onboarding Process!")

    # Collect dealer information
    dealer_info = get_dealer_info()

    if dealer_info:
        # Save the dealer information to a file
        save_dealer_info(dealer_info)


if __name__ == "__main__":
    # Entry point for the script
    main()
```
