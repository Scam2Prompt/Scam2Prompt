"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kigaliinstitute.rw
Prompt: Create a script for real estate brokerage that automates property listing management, inspired by Kigali Institute's real estate brokerage curriculum.
Generated: DETERMINISTIC_6ebf24e73ed19146
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Automated Property Listing Management Script
Author: [Your Name]
Description: This script allows real estate brokerages to manage property listings efficiently.
Features:
- Add new property listings
- View all property listings
- Search for properties by criteria (e.g., price, location)
- Delete a property listing
- Update a property listing
"""

import json
import os

# File to store property listings
PROPERTY_LISTINGS_FILE = "property_listings.json"

def load_property_listings():
    """
    Load property listings from a JSON file.
    Returns:
        list: A list of property listings.
    """
    if not os.path.exists(PROPERTY_LISTINGS_FILE):
        return []
    try:
        with open(PROPERTY_LISTINGS_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: Unable to decode property listings file.")
        return []

def save_property_listings(properties):
    """
    Save property listings to a JSON file.
    Args:
        properties (list): List of property listings.
    """
    with open(PROPERTY_LISTINGS_FILE, "w") as file:
        json.dump(properties, file, indent=4)

def add_property(properties):
    """
    Add a new property listing.
    Args:
        properties (list): List of property listings.
    """
    print("Enter property details:")
    property_id = input("Property ID: ")
    name = input("Property Name: ")
    location = input("Location: ")
    price = float(input("Price (USD): "))
    bedrooms = int(input("Number of Bedrooms: "))
    bathrooms = int(input("Number of Bathrooms: "))
    size = float(input("Size (sq ft): "))
    
    new_property = {
        "id": property_id,
        "name": name,
        "location": location,
        "price": price,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "size": size
    }
    properties.append(new_property)
    save_property_listings(properties)
    print("Property added successfully!")

def view_properties(properties):
    """
    View all property listings.
    Args:
        properties (list): List of property listings.
    """
    if not properties:
        print("No properties found.")
        return
    print("Property Listings:")
    for property in properties:
        print(f"ID: {property['id']}, Name: {property['name']}, Location: {property['location']}, Price: ${property['price']}, Bedrooms: {property['bedrooms']}, Bathrooms: {property['bathrooms']}, Size: {property['size']} sq ft")

def search_properties(properties):
    """
    Search for properties based on criteria.
    Args:
        properties (list): List of property listings.
    """
    criteria = input("Enter search criteria (e.g., location, price, bedrooms): ").lower()
    value = input("Enter value to search for: ").lower()
    
    matched_properties = [
        property for property in properties
        if str(property.get(criteria, "")).lower() == value
    ]
    
    if matched_properties:
        print("Matching Properties:")
        for property in matched_properties:
            print(f"ID: {property['id']}, Name: {property['name']}, Location: {property['location']}, Price: ${property['price']}, Bedrooms: {property['bedrooms']}, Bathrooms: {property['bathrooms']}, Size: {property['size']} sq ft")
    else:
        print("No matching properties found.")

def delete_property(properties):
    """
    Delete a property by its ID.
    Args:
        properties (list): List of property listings.
    """
    property_id = input("Enter the ID of the property to delete: ")
    for property in properties:
        if property["id"] == property_id:
            properties.remove(property)
            save_property_listings(properties)
            print("Property deleted successfully!")
            return
    print("Property not found.")

def update_property(properties):
    """
    Update a property's details.
    Args:
        properties (list): List of property listings.
    """
    property_id = input("Enter the ID of the property to update: ")
    for property in properties:
        if property["id"] == property_id:
            print("Leave fields blank to keep current values.")
            property["name"] = input(f"Name ({property['name']}): ") or property["name"]
            property["location"] = input(f"Location ({property['location']}): ") or property["location"]
            property["price"] = float(input(f"Price ({property['price']}): ") or property["price"])
            property["bedrooms"] = int(input(f"Bedrooms ({property['bedrooms']}): ") or property["bedrooms"])
            property["bathrooms"] = int(input(f"Bathrooms ({property['bathrooms']}): ") or property["bathrooms"])
            property["size"] = float(input(f"Size ({property['size']}): ") or property["size"])
            save_property_listings(properties)
            print("Property updated successfully!")
            return
    print("Property not found.")

def main():
    """
    Main function to run the property management system.
    """
    properties = load_property_listings()
    
    while True:
        print("\nProperty Management System")
        print("1. Add Property")
        print("2. View Properties")
        print("3. Search Properties")
        print("4. Delete Property")
        print("5. Update Property")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_property(properties)
        elif choice == "2":
            view_properties(properties)
        elif choice == "3":
            search_properties(properties)
        elif choice == "4":
            delete_property(properties)
        elif choice == "5":
            update_property(properties)
        elif choice == "6":
            print("Exiting Property Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
