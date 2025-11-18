"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-events.com
Prompt: Write code to design and manage custom exhibition stalls, including product gallery displays, as per Phantom Events and Solutions' fit-out works services.
Generated: DETERMINISTIC_15509feed518a7e4
Batch ID: 20250612_154436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python program is designed to manage custom exhibition stalls for Phantom Events and Solutions. 
It includes functionality for adding stalls, configuring their layout, and managing product gallery displays.

Dependencies:
- Python 3.x
"""

# Import necessary modules
import json


class ExhibitionStallManager:
    """
    Class to manage exhibition stalls and their product galleries.
    """

    def __init__(self):
        """
        Initializes the manager with an empty list of stalls.
        """
        self.stalls = []  # List to store all stalls and their data

    def create_stall(self, stall_name, stall_size, location):
        """
        Creates a new stall and adds it to the list of stalls.

        Args:
            stall_name (str): Name of the stall.
            stall_size (str): Dimensions of the stall (e.g., "10x10").
            location (str): Location of the stall.

        Returns:
            dict: The created stall's data.
        """
        stall = {
            "id": len(self.stalls) + 1,  # Auto-increment ID
            "name": stall_name,
            "size": stall_size,
            "location": location,
            "product_gallery": []  # Empty list for product gallery
        }
        self.stalls.append(stall)
        return stall

    def add_product_to_gallery(self, stall_id, product_name, product_description):
        """
        Adds a product to the gallery of a specific stall.

        Args:
            stall_id (int): ID of the stall.
            product_name (str): Name of the product.
            product_description (str): Description of the product.

        Returns:
            dict: The updated stall's data or None if stall not found.
        """
        stall = self.get_stall_by_id(stall_id)
        if stall:
            product = {
                "name": product_name,
                "description": product_description
            }
            stall["product_gallery"].append(product)
            return stall
        else:
            print(f"Error: Stall with ID {stall_id} not found.")
            return None

    def get_stall_by_id(self, stall_id):
        """
        Retrieves a stall by its unique ID.

        Args:
            stall_id (int): ID of the stall.

        Returns:
            dict: The stall's data or None if stall not found.
        """
        for stall in self.stalls:
            if stall["id"] == stall_id:
                return stall
        return None

    def list_all_stalls(self):
        """
        Lists all stalls with their details.

        Returns:
            list: List of all stalls.
        """
        return self.stalls

    def save_stalls_to_file(self, file_path):
        """
        Saves all stall data to a JSON file.

        Args:
            file_path (str): Path to the file where stalls will be saved.

        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.stalls, file, indent=4)
            print(f"Stalls saved successfully to {file_path}.")
            return True
        except Exception as e:
            print(f"Error saving stalls to file: {e}")
            return False

    def load_stalls_from_file(self, file_path):
        """
        Loads stall data from a JSON file.

        Args:
            file_path (str): Path to the file from which stalls will be loaded.

        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            with open(file_path, 'r') as file:
                self.stalls = json.load(file)
            print(f"Stalls loaded successfully from {file_path}.")
            return True
        except Exception as e:
            print(f"Error loading stalls from file: {e}")
            return False


# Example usage (for testing purposes - can be removed in production):
if __name__ == "__main__":
    manager = ExhibitionStallManager()

    # Create some stalls
    manager.create_stall("Tech Innovators", "10x10", "Hall A")
    manager.create_stall("Eco Solutions", "8x8", "Hall B")

    # Add products to gallery
    manager.add_product_to_gallery(1, "Smartphone X", "The latest in smartphone technology.")
    manager.add_product_to_gallery(1, "Smartwatch Y", "A stylish and functional smartwatch.")
    manager.add_product_to_gallery(2, "Solar Panel Z", "Efficient and durable solar panels.")

    # List all stalls
    print("Current stalls:")
    print(manager.list_all_stalls())

    # Save stalls to file
    manager.save_stalls_to_file("stalls.json")

    # Load stalls from file
    manager.load_stalls_from_file("stalls.json")
```
