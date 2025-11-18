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
from typing import List, Dict
from collections import defaultdict

class DirectoryListingApplication:
    def __init__(self):
        # Dictionary to store categorized services
        # Format: {category: [{name, location}]}
        self.services = defaultdict(list)

    def add_service(self, category: str, name: str, location: str):
        """
        Add a service to the directory under a specific category and location.
        :param category: The category of the service (e.g., "Κοπτικά Εργαλεία").
        :param name: The name of the service provider.
        :param location: The location of the service provider.
        """
        if not category or not name or not location:
            raise ValueError("Category, name, and location are required fields.")
        self.services[category].append({"name": name, "location": location})

    def search_by_category(self, category: str) -> List[Dict[str, str]]:
        """
        Search for services under a specific category.
        :param category: The category to search for (e.g., "Οδοντίατροι").
        :return: A list of services in the specified category.
        """
        return self.services.get(category, [])

    def search_by_location(self, location: str) -> Dict[str, List[Dict[str, str]]]:
        """
        Search for services available in a specific location.
        :param location: The location to search for services (e.g., "Athens").
        :return: A dictionary of categories with services available in the specified location.
        """
        result = defaultdict(list)
        for category, service_list in self.services.items():
            for service in service_list:
                if service["location"].lower() == location.lower():
                    result[category].append(service)
        return dict(result)

    def display_all_services(self) -> None:
        """
        Display all services organized by category.
        """
        print("Directory Listing:")
        for category, service_list in self.services.items():
            print(f"\nCategory: {category}")
            for service in service_list:
                print(f"  - Name: {service['name']}, Location: {service['location']}")

def main():
    # Create an instance of the directory application
    directory_app = DirectoryListingApplication()

    # Sample data
    directory_app.add_service("Κοπτικά Εργαλεία", "ABC Tools", "Athens")
    directory_app.add_service("Οδοντίατροι", "Dr. Smith", "Thessaloniki")
    directory_app.add_service("Φυσικοθεραπευτές", "PhysioCare", "Athens")
    directory_app.add_service("Οδοντίατροι", "Dr. Jane", "Athens")

    # User interaction
    while True:
        print("\n=== Directory Listing Application ===")
        print("1. Add Service")
        print("2. Search by Category")
        print("3. Search by Location")
        print("4. Display All Services")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        try:
            if choice == "1":
                category = input("Enter category: ").strip()
                name = input("Enter service name: ").strip()
                location = input("Enter location: ").strip()
                directory_app.add_service(category, name, location)
                print("Service added successfully!")
            elif choice == "2":
                category = input("Enter category to search: ").strip()
                results = directory_app.search_by_category(category)
                if results:
                    print(f"Services under '{category}':")
                    for service in results:
                        print(f"  - Name: {service['name']}, Location: {service['location']}")
                else:
                    print(f"No services found under the category: {category}")
            elif choice == "3":
                location = input("Enter location to search: ").strip()
                results = directory_app.search_by_location(location)
                if results:
                    print(f"Services available in '{location}':")
                    for category, service_list in results.items():
                        print(f"\nCategory: {category}")
                        for service in service_list:
                            print(f"  - Name: {service['name']}, Location: {service['location']}")
                else:
                    print(f"No services found in the location: {location}")
            elif choice == "4":
                directory_app.display_all_services()
            elif choice == "5":
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
