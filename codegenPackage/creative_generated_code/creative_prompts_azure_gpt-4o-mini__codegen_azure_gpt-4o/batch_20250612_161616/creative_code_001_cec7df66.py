"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purebite.fi
Prompt: Write a Python script that integrates a menu management API, allowing users to view and select dishes similar to those listed on Purebite's menu, including Thai woks and curries.
Generated: DETERMINISTIC_cec7df665c97e843
Batch ID: 20250612_161616
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.menu-management.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.menu-management.com/v1`": {
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

# Constants for the API
API_BASE_URL = "https://api.menu-management.com/v1"  # Replace with the actual API URL
API_KEY = "your_api_key_here"  # Replace with your API key

def fetch_menu():
    """
    Fetches the menu from the Menu Management API.

    Returns:
        list: A list of dishes if successful, or None if an error occurs.
    """
    try:
        # Make a GET request to retrieve the menu
        response = requests.get(f"{API_BASE_URL}/menu", headers={"Authorization": f"Bearer {API_KEY}"})
        
        # Check for successful status code
        if response.status_code == 200:
            return response.json().get("dishes", [])
        else:
            print(f"Error: Failed to fetch menu. Status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: An exception occurred while fetching the menu - {e}")
        return None

def display_menu(dishes):
    """
    Displays the menu to the user.

    Args:
        dishes (list): A list of dishes to display.
    """
    if not dishes:
        print("No dishes available to display.")
        return
    
    print("\nAvailable Dishes:")
    print("-----------------")
    for idx, dish in enumerate(dishes, start=1):
        print(f"{idx}. {dish['name']} - {dish['description']} (${dish['price']})")

def select_dish(dishes):
    """
    Allows the user to select a dish from the menu.

    Args:
        dishes (list): A list of dishes from which the user can select.

    Returns:
        dict: The selected dish, or None if selection was invalid.
    """
    try:
        choice = int(input("\nEnter the number of the dish you'd like to select: "))
        if 1 <= choice <= len(dishes):
            return dishes[choice - 1]
        else:
            print("Error: Invalid choice. Please select a valid dish number.")
            return None
    except ValueError:
        print("Error: Please enter a numeric value.")
        return None

def main():
    """
    Main function to run the script.
    """
    print("Welcome to the Menu Management System!")
    
    # Fetch the menu from the API
    menu = fetch_menu()
    
    if not menu:
        print("Unable to load the menu. Exiting application.")
        return
    
    # Display the menu and allow user to select a dish
    display_menu(menu)
    selected_dish = select_dish(menu)
    
    if selected_dish:
        print(f"\nYou selected: {selected_dish['name']} - {selected_dish['description']} (${selected_dish['price']})")
    else:
        print("No valid dish selected. Exiting application.")

if __name__ == "__main__":
    main()
```

Replace `https://api.menu-management.com/v1` and `your_api_key_here` with the API's base URL and your actual API key respectively.
