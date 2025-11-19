"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krakqwunlogin.webflow.io
Prompt: Describe the process of selecting a country during the Kraken sign-up procedure.
Generated: DETERMINISTIC_1c7a4705b729b8c4
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def display_country_list():
    """
    Displays a list of countries for the user to select from.
    """
    countries = [
        "United States",
        "Canada",
        "United Kingdom",
        "Germany",
        "France",
        "India",
        "Australia",
        "Japan",
        "South Korea",
        "Brazil",
        "South Africa"
    ]
    print("Please select your country from the list below:")
    for idx, country in enumerate(countries, 1):
        print(f"{idx}. {country}")
    return countries

def get_user_selection(countries):
    """
    Prompts the user to select a country by entering its corresponding number.
    Performs validation and returns the selected country.
    """
    while True:
        try:
            user_input = int(input("Enter the number corresponding to your country: "))
            if 1 <= user_input <= len(countries):
                return countries[user_input - 1]
            else:
                print(f"Invalid selection. Please enter a number between 1 and {len(countries)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nSign-up process interrupted.")
            sys.exit(1)

def main():
    """
    Main function to run the country selection process.
    """
    try:
        # Display available countries
        countries = display_country_list()

        # Get user selection
        selected_country = get_user_selection(countries)

        print(f"You have selected: {selected_country}")
        print("Proceeding with the sign-up process...")
    except Exception as e:
        # Log unexpected errors
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
