"""
Generated Code Metadata:
========================
Original URL: https://mesogia.com
Prompt: Write Python code to create a directory listing application that categorizes services like "Κοπτικά Εργαλεία," "Οδοντίατροι," and "Φυσικοθεραπευτές," and allows users to search by category and location.
Generated: DETERMINISTIC_5e328c5e49dedd2d
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json

class DirectoryListingApp:
    def __init__(self, data_file='directory_data.json'):
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
        else:
            self.data = {}

    def save_data(self):
        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    def add_service(self, category, name, location):
        if category not in self.data:
            self.data[category] = []
        self.data[category].append({'name': name, 'location': location})
        self.save_data()

    def search_by_category(self, category):
        return self.data.get(category, [])

    def search_by_location(self, location):
        results = []
        for category, services in self.data.items():
            for service in services:
                if service['location'].lower() == location.lower():
                    results.append({'category': category, 'name': service['name'], 'location': service['location']})
        return results

    def search(self, category=None, location=None):
        if category and location:
            return [f"{service['name']} - {service['location']}" for service in self.search_by_category(category) if service['location'].lower() == location.lower()]
        elif category:
            return [f"{service['name']} - {service['location']}" for service in self.search_by_category(category)]
        elif location:
            return [f"{service['category']}: {service['name']} - {service['location']}" for service in self.search_by_location(location)]
        else:
            return []

def main():
    app = DirectoryListingApp()

    while True:
        print("\nDirectory Listing Application")
        print("1. Add Service")
        print("2. Search by Category")
        print("3. Search by Location")
        print("4. Search")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            category = input("Enter category: ")
            name = input("Enter service name: ")
            location = input("Enter location: ")
            app.add_service(category, name, location)
        elif choice == '2':
            category = input("Enter category: ")
            results = app.search_by_category(category)
            for service in results:
                print(f"{service['name']} - {service['location']}")
        elif choice == '3':
            location = input("Enter location: ")
            results = app.search_by_location(location)
            for service in results:
                print(f"{service['category']}: {service['name']} - {service['location']}")
        elif choice == '4':
            category = input("Enter category (optional): ")
            location = input("Enter location (optional): ")
            if category and location:
                results = app.search(category, location)
            elif category:
                results = app.search(category=category)
            elif location:
                results = app.search(location=location)
            else:
                results = []
            for result in results:
                print(result)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == '__main__':
    main()
```
