"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://birlikjenerator.com
Prompt: Develop a tool to assist users in selecting the most economical generator based on power needs and location, inspired by the "Güç ve Yer Tespiti" service on Birlik Jeneratör's website.
Generated: DETERMINISTIC_4af1052fea523f52
Batch ID: 20250612_153225
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/generators": {
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
# generator_selector.py

import json
import requests

def fetch_generators_data(api_url):
    """
    Fetch generator data from an external API.
    
    Args:
        api_url (str): URL of the API providing generator data.

    Returns:
        list: A list of generator data dictionaries.

    Raises:
        Exception: If there's an error during the API request.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except Exception as e:
        print(f"Error fetching generator data: {e}")
        raise

def filter_generators_by_power(generators, power_needed):
    """
    Filters available generators based on the required power.

    Args:
        generators (list): List of generator dictionaries.
        power_needed (int): The minimum power required by the user.

    Returns:
        list: Filtered list of generators meeting the power requirement.
    """
    return [gen for gen in generators if gen["power"] >= power_needed]

def filter_generators_by_location(generators, location):
    """
    Filters available generators based on the user's location.

    Args:
        generators (list): List of generator dictionaries.
        location (str): The user's location.

    Returns:
        list: Filtered list of generators available in the given location.
    """
    return [gen for gen in generators if gen["location"].lower() == location.lower()]

def select_most_economical_generator(filtered_generators):
    """
    Selects the most economical generator from the filtered list.

    Args:
        filtered_generators (list): List of generator dictionaries.

    Returns:
        dict: The most economical generator.
    """
    if not filtered_generators:
        return None

    return min(filtered_generators, key=lambda gen: gen["price"])

def user_input():
    """
    Collects user input for power needs and location.

    Returns:
        dict: Dictionary containing user inputs.
    """
    try:
        power_needed = int(input("Enter the minimum power requirement (in kW): "))
        location = input("Enter your location: ").strip()
        return {"power_needed": power_needed, "location": location}
    except ValueError:
        print("Invalid input. Please enter a valid number for power requirement.")
        raise

def main():
    """
    Main function to run the generator selection tool.
    """
    print("Welcome to the Generator Selection Tool!")
    
    try:
        # Collect user input
        user_data = user_input()
        power_needed = user_data["power_needed"]
        location = user_data["location"]

        # Fetch generator data (replace with actual API endpoint)
        api_url = "https://api.example.com/generators"  # Example API URL
        generators_data = fetch_generators_data(api_url)

        # Filter generators based on user input
        generators_by_power = filter_generators_by_power(generators_data, power_needed)
        generators_by_location = filter_generators_by_location(generators_by_power, location)

        # Select the most economical generator
        selected_generator = select_most_economical_generator(generators_by_location)

        # Output the result
        if selected_generator:
            print("\nThe most economical generator for your needs is:")
            print(json.dumps(selected_generator, indent=4))
        else:
            print("\nNo suitable generators found for your requirements.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
