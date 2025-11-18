"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mesogia.com
Prompt: Write Python code to create a directory listing application that categorizes services like "Κοπτικά Εργαλεία," "Οδοντίατροι," and "Φυσικοθεραπευτές," and allows users to search by category and location.
Generated: DETERMINISTIC_5e328c5e49dedd2d
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json


class DirectoryService:
    """A class to manage a directory listing application."""

    def __init__(self, data_file):
        """
        Initializes the DirectoryService.

        :param data_file: Path to the JSON file that contains the directory data.
        """
        self.data_file = data_file
        self.directory_data = self.load_data()

    def load_data(self):
        """Loads directory data from a JSON file."""
        if not os.path.exists(self.data_file):
            raise FileNotFoundError(f"The data file {self.data_file} does not exist.")
        
        with open(self.data_file, 'r', encoding='utf-8') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                raise ValueError(f"Error decoding JSON data: {e}")

    def search_by_category_and_location(self, category, location):
        """
        Searches for services by category and location.

        :param category: The category to search for.
        :param location: The location to filter results by.
        :return: A list of matching services.
        """
        results = [
            service for service in self.directory_data
            if service.get('category') == category and service.get('location') == location
        ]
        return results

    def display_services(self, services):
        """Prints the services in a readable format."""
        if not services:
            print("No services found.")
            return

        for service in services:
            print(f"Name: {service['name']}, Category: {service['category']}, Location: {service['location']}")


def main():
    """Main function to run the directory listing application."""
    data_file = 'directory_data.json'  # Path to the JSON data file
    directory_service = DirectoryService(data_file)

    # Example user input; in a real application, this could come from user input
    user_category = input("Enter the category you want to search for (e.g., Κοπτικά Εργαλεία, Οδοντίατροι, Φυσικοθεραπευτές): ")
    user_location = input("Enter the location you want to search in: ")

    try:
        # Search for services based on user input
        services_found = directory_service.search_by_category_and_location(user_category, user_location)
        # Display the found services
        directory_service.display_services(services_found)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

**Note:** This code expects the existence of a `directory_data.json` file with a structure similar to:
```json
[
    {"name": "Service 1", "category": "Κοπτικά Εργαλεία", "location": "Location A"},
    {"name": "Service 2", "category": "Οδοντίατροι", "location": "Location B"},
    {"name": "Service 3", "category": "Φυσικοθεραπευτές", "location": "Location A"}
]
```
