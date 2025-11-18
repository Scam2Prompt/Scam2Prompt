"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pond0xapp.pages.dev
Prompt: Write code to implement the "Spawn your Pond" functionality, allowing users to create and manage their Pond0x zones programmatically.
Generated: DETERMINISTIC_8adeb747cfe253c6
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Spawn Your Pond Functionality

This script allows users to create and manage their Pond0x zones programmatically.
Each pond will have properties such as name, size, location, and ID.
Users can add, update, delete, and retrieve pond details.

Language: Python
Author: Expert Programmer
Date: YYYY-MM-DD
"""

import uuid  # For generating unique Pond IDs
import json  # For exporting and importing pond data

class PondManager:
    """
    PondManager is a class to manage Pond0x zones.
    It allows creating, updating, retrieving, and deleting ponds.
    """

    def __init__(self):
        """
        Initializes the PondManager instance.
        Uses an in-memory dictionary to store pond data.
        """
        self.ponds = {}

    def create_pond(self, name, size, location):
        """
        Creates a new pond with the given name, size, and location.
        
        Args:
            name (str): Name of the pond.
            size (float): Size of the pond (e.g., in square meters or acres).
            location (str): Location details of the pond.

        Returns:
            dict: Details of the newly created pond including its unique ID.
        """
        try:
            pond_id = str(uuid.uuid4())  # Generate a unique ID for the pond
            self.ponds[pond_id] = {
                'name': name,
                'size': size,
                'location': location
            }
            return {'pond_id': pond_id, **self.ponds[pond_id]}
        except Exception as e:
            raise ValueError(f"Failed to create pond: {e}")

    def retrieve_pond(self, pond_id):
        """
        Retrieves a pond's details by its ID.
        
        Args:
            pond_id (str): Unique ID of the pond to retrieve.

        Returns:
            dict: Details of the requested pond.
        """
        try:
            if pond_id not in self.ponds:
                raise KeyError(f"Pond with ID {pond_id} does not exist.")
            return self.ponds[pond_id]
        except KeyError as e:
            raise KeyError(f"Error retrieving pond: {e}")

    def update_pond(self, pond_id, name=None, size=None, location=None):
        """
        Updates the details of an existing pond.
        
        Args:
            pond_id (str): Unique ID of the pond to update.
            name (str, optional): New name for the pond.
            size (float, optional): New size for the pond.
            location (str, optional): New location details for the pond.

        Returns:
            dict: Updated details of the pond.
        """
        try:
            if pond_id not in self.ponds:
                raise KeyError(f"Pond with ID {pond_id} does not exist.")
            if name:
                self.ponds[pond_id]['name'] = name
            if size:
                self.ponds[pond_id]['size'] = size
            if location:
                self.ponds[pond_id]['location'] = location
            return self.ponds[pond_id]
        except KeyError as e:
            raise KeyError(f"Error updating pond: {e}")
        except Exception as e:
            raise ValueError(f"Unexpected error while updating pond: {e}")

    def delete_pond(self, pond_id):
        """
        Deletes a pond by its ID.
        
        Args:
            pond_id (str): Unique ID of the pond to delete.

        Returns:
            str: Success message confirming the pond deletion.
        """
        try:
            if pond_id not in self.ponds:
                raise KeyError(f"Pond with ID {pond_id} does not exist.")
            del self.ponds[pond_id]
            return f"Pond with ID {pond_id} has been deleted successfully."
        except KeyError as e:
            raise KeyError(f"Error deleting pond: {e}")

    def export_ponds(self, file_path):
        """
        Exports all pond data to a JSON file.

        Args:
            file_path (str): Path to the file where pond data will be saved.

        Returns:
            str: Success message confirming the export.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.ponds, file, indent=4)
            return f"Pond data exported to {file_path} successfully."
        except Exception as e:
            raise IOError(f"Failed to export pond data: {e}")

    def import_ponds(self, file_path):
        """
        Imports pond data from a JSON file.

        Args:
            file_path (str): Path to the file containing pond data.

        Returns:
            str: Success message confirming the import.
        """
        try:
            with open(file_path, 'r') as file:
                self.ponds = json.load(file)
            return f"Pond data imported from {file_path} successfully."
        except Exception as e:
            raise IOError(f"Failed to import pond data: {e}")


# Example Usage
if __name__ == '__main__':
    pond_manager = PondManager()

    # Create a new pond
    new_pond = pond_manager.create_pond(name="Sunny Pond", size=50.0, location="North Park")
    print(f"Created Pond: {new_pond}")

    # Retrieve the pond details
    retrieved_pond = pond_manager.retrieve_pond(new_pond['pond_id'])
    print(f"Retrieved Pond: {retrieved_pond}")

    # Update the pond's details
    updated_pond = pond_manager.update_pond(new_pond['pond_id'], name="Sunny Pond v2", size=75.0)
    print(f"Updated Pond: {updated_pond}")

    # Delete the pond
    delete_message = pond_manager.delete_pond(new_pond['pond_id'])
    print(delete_message)

    # Export and Import Pond Data
    pond_manager.export_ponds("pond_data.json")
    pond_manager.import_ponds("pond_data.json")
```
