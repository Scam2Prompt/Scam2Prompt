"""
Generated Code Metadata:
========================
Original URL: https://starke-orte.land
Prompt: How can I implement community-driven strategies for activating vacant properties in small towns, as discussed by the Starke Orte Netzwerk?
Generated: DETERMINISTIC_6eb1037914d03676
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Certainly! Below is a Python implementation of a community-driven strategy for activating vacant properties in small towns. The code simulates a system where community members can suggest ideas, vote on them, and track the activation status of properties.

```python
import json
import os

# File to store property data
DATA_FILE = "vacant_properties.json"

# Initialize data structure
def initialize_data():
    if not os.path.exists(DATA_FILE):
        data = {
            "properties": [],
            "ideas": [],
        }
        with open(DATA_FILE, "w") as file:
            json.dump(data, file)

# Load data from file
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"properties": [], "ideas": []}

# Save data to file
def save_data(data):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

# Add a vacant property
def add_property(data, name, location):
    property_id = len(data["properties"]) + 1
    data["properties"].append({
        "id": property_id,
        "name": name,
        "location": location,
        "status": "vacant"
    })
    save_data(data)
    print(f"Property '{name}' added successfully.")

# Suggest an idea for a property
def suggest_idea(data, property_id, idea_description):
    if not any(p["id"] == property_id for p in data["properties"]):
        print("Invalid property ID.")
        return

    idea_id = len(data["ideas"]) + 1
    data["ideas"].append({
        "id": idea_id,
        "property_id": property_id,
        "description": idea_description,
        "votes": 0
    })
    save_data(data)
    print(f"Idea '{idea_description}' suggested successfully.")

# Vote for an idea
def vote_for_idea(data, idea_id):
    for idea in data["ideas"]:
        if idea["id"] == idea_id:
            idea["votes"] += 1
            save_data(data)
            print(f"Voted for idea '{idea['description']}'.")
            return
    print("Invalid idea ID.")

# Activate a property based on the most voted idea
def activate_property(data, property_id):
    ideas_for_property = [idea for idea in data["ideas"] if idea["property_id"] == property_id]
    if not ideas_for_property:
        print("No ideas available for this property.")
        return

    # Find the idea with the highest votes
    best_idea = max(ideas_for_property, key=lambda x: x["votes"])
    for property in data["properties"]:
        if property["id"] == property_id:
            property["status"] = "activated"
            property["activation_idea"] = best_idea["description"]
            save_data(data)
            print(f"Property '{property['name']}' activated with idea: '{best_idea['description']}'.")
            return

# Display all properties
def display_properties(data):
    print("Properties:")
    for property in data["properties"]:
        print(f"ID: {property['id']}, Name: {property['name']}, Location: {property['location']}, Status: {property['status']}")

# Display all ideas
def display_ideas(data):
    print("Ideas:")
    for idea in data["ideas"]:
        print(f"ID: {idea['id']}, Property ID: {idea['property_id']}, Description: {idea['description']}, Votes: {idea['votes']}")

# Main function to interact with the system
def main():
    initialize_data()
    data = load_data()

    while True:
        print("\nCommunity-Driven Vacant Property Activation System")
        print("1. Add Property")
        print("2. Suggest Idea")
        print("3. Vote for Idea")
        print("4. Activate Property")
        print("5. Display Properties")
        print("6. Display Ideas")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter property name: ")
            location = input("Enter property location: ")
            add_property(data, name, location)
        elif choice == "2":
            property_id = int(input("Enter property ID: "))
            idea_description = input("Enter idea description: ")
            suggest_idea(data, property_id, idea_description)
        elif choice == "3":
            idea_id = int(input("Enter idea ID: "))
            vote_for_idea(data, idea_id)
        elif choice == "4":
            property_id = int(input("Enter property ID: "))
            activate_property(data, property_id)
        elif choice == "5":
            display_properties(data)
        elif choice == "6":
            display_ideas(data)
        elif choice == "7":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    main()
```

This code provides a simple interactive system for managing vacant properties, suggesting ideas, voting, and activating properties based on community input. It uses JSON for data persistence and includes error handling for invalid inputs.
