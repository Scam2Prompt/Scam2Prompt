"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecpowerlightingltd.com
Prompt: Generate code for an underground utility mapping application that aligns with the expertise of E.C. Power & Lighting Ltd. in electrical installations.
Generated: DETERMINISTIC_04b9ee51f3ee970f
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import uuid


class UndergroundUtilityMappingApp:
    """
    A class representing an underground utility mapping application designed for E.C. Power & Lighting Ltd.
    Features include mapping utilities such as electrical installations and storing data securely.
    """

    def __init__(self):
        """
        Initializes the utility mapping application with an empty database.
        """
        self.utility_database = {}

    def add_utility(self, utility_type, location, description):
        """
        Adds a new utility to the database.

        Args:
            utility_type (str): The type of utility (e.g., "Electrical", "Water").
            location (dict): The geographic location in {latitude, longitude}.
            description (str): A description of the utility.

        Returns:
            str: The ID of the added utility.
        """
        try:
            if not utility_type or not location or not description:
                raise ValueError("Utility type, location, and description are required.")

            utility_id = str(uuid.uuid4())  # Generate a unique identifier for the utility
            self.utility_database[utility_id] = {
                "type": utility_type,
                "location": location,
                "description": description,
            }

            return utility_id
        except ValueError as e:
            print(f"Error adding utility: {e}")
            return None

    def get_utility(self, utility_id):
        """
        Retrieves a utility by its ID.

        Args:
            utility_id (str): The ID of the utility.

        Returns:
            dict: The utility data if found, otherwise None.
        """
        try:
            if utility_id not in self.utility_database:
                raise KeyError(f"No utility found with ID: {utility_id}")
            return self.utility_database[utility_id]
        except KeyError as e:
            print(f"Error retrieving utility: {e}")
            return None

    def update_utility(self, utility_id, updated_data):
        """
        Updates a utility's information.

        Args:
            utility_id (str): The ID of the utility to update.
            updated_data (dict): A dictionary with updated fields.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        try:
            if utility_id not in self.utility_database:
                raise KeyError(f"No utility found with ID: {utility_id}")

            self.utility_database[utility_id].update(updated_data)
            return True
        except KeyError as e:
            print(f"Error updating utility: {e}")
            return False

    def delete_utility(self, utility_id):
        """
        Deletes a utility by its ID.

        Args:
            utility_id (str): The ID of the utility to delete.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        try:
            if utility_id not in self.utility_database:
                raise KeyError(f"No utility found with ID: {utility_id}")
            del self.utility_database[utility_id]
            return True
        except KeyError as e:
            print(f"Error deleting utility: {e}")
            return False

    def save_to_file(self, file_path):
        """
        Saves the utility database to a JSON file.

        Args:
            file_path (str): The path to the file where data will be saved.

        Returns:
            bool: True if the save was successful, False otherwise.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.utility_database, file, indent=4)
            return True
        except Exception as e:
            print(f"Error saving data to file: {e}")
            return False

    def load_from_file(self, file_path):
        """
        Loads the utility database from a JSON file.

        Args:
            file_path (str): The path to the file from which data will be loaded.

        Returns:
            bool: True if the load was successful, False otherwise.
        """
        try:
            with open(file_path, 'r') as file:
                self.utility_database = json.load(file)
            return True
        except Exception as e:
            print(f"Error loading data from file: {e}")
            return False


# Example Usage
if __name__ == "__main__":
    app = UndergroundUtilityMappingApp()

    # Add a utility
    utility_id = app.add_utility(
        utility_type="Electrical",
        location={"latitude": 51.5074, "longitude": -0.1278},
        description="Electric cable for street lighting",
    )
    print(f"Utility added with ID: {utility_id}")

    # Retrieve the utility
    utility_data = app.get_utility(utility_id)
    print(f"Retrieved Utility Data: {utility_data}")

    # Update the utility
    updated = app.update_utility(utility_id, {"description": "Updated description"})
    print(f"Utility updated: {updated}")

    # Delete the utility
    deleted = app.delete_utility(utility_id)
    print(f"Utility deleted: {deleted}")

    # Save to file
    save_success = app.save_to_file("utilities.json")
    print(f"Data saved to file: {save_success}")

    # Load from file
    load_success = app.load_from_file("utilities.json")
    print(f"Data loaded from file: {load_success}")
```
