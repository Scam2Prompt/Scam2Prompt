"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dessc.de
Prompt: Develop a tool for tracking and managing digital progress for small businesses in the Stuttgart region, inspired by DESSC's mission statement.
Generated: DETERMINISTIC_e90db49f80197de5
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python implementation of the requested tool. It includes features for tracking digital progress, managing tasks, and generating reports for small businesses.

```python
import json
from datetime import datetime
from typing import List, Dict


# Define custom exception classes
class BusinessNotFoundError(Exception):
    """Raised when a business is not found in the system."""


class TaskNotFoundError(Exception):
    """Raised when a task is not found in the system."""


# Business class for managing digital progress
class Business:
    def __init__(self, name: str, location: str, industry: str):
        """
        Initialize a new Business object.

        :param name: Name of the business
        :param location: Location of the business
        :param industry: Industry of the business
        """
        self.name = name
        self.location = location
        self.industry = industry
        self.tasks = []  # List to store tracking tasks

    def add_task(self, task_name: str, description: str, status: str = "Pending"):
        """
        Add a new task for tracking digital progress.

        :param task_name: Name of the task
        :param description: Description of the task
        :param status: Status of the task ('Pending', 'In Progress', 'Completed')
        """
        self.tasks.append({
            "task_name": task_name,
            "description": description,
            "status": status,
            "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

    def update_task_status(self, task_name: str, status: str):
        """
        Update the status of a specific task.

        :param task_name: Name of the task to update
        :param status: New status for the task ('Pending', 'In Progress', 'Completed')
        :raises TaskNotFoundError: If the task is not found in the system
        """
        for task in self.tasks:
            if task["task_name"] == task_name:
                task["status"] = status
                return
        raise TaskNotFoundError(f"Task '{task_name}' not found.")

    def generate_report(self) -> Dict:
        """
        Generate a summary report of the business's progress.

        :return: Dictionary containing the report
        """
        status_count = {"Pending": 0, "In Progress": 0, "Completed": 0}
        for task in self.tasks:
            status_count[task["status"]] += 1
        return {
            "business_name": self.name,
            "location": self.location,
            "industry": self.industry,
            "tasks_summary": status_count,
            "total_tasks": len(self.tasks)
        }


# Tool for managing multiple businesses
class DigitalProgressTracker:
    def __init__(self):
        """
        Initialize an empty tracker to manage multiple businesses.
        """
        self.businesses = {}

    def add_business(self, name: str, location: str, industry: str):
        """
        Add a new business to the tracker.

        :param name: Name of the business
        :param location: Location of the business
        :param industry: Industry of the business
        """
        if name in self.businesses:
            raise ValueError(f"Business '{name}' already exists.")
        self.businesses[name] = Business(name, location, industry)

    def get_business(self, name: str) -> Business:
        """
        Retrieve information about a specific business.

        :param name: Name of the business to retrieve
        :return: Business object
        :raises BusinessNotFoundError: If the business is not found
        """
        if name not in self.businesses:
            raise BusinessNotFoundError(f"Business '{name}' not found.")
        return self.businesses[name]

    def generate_overall_report(self) -> List[Dict]:
        """
        Generate a report summarizing progress across all businesses.

        :return: List of dictionaries containing reports for each business
        """
        return [business.generate_report() for business in self.businesses.values()]

    def save_data(self, filename: str):
        """
        Save all business data to a JSON file.

        :param filename: Name of the file to save data to
        """
        data = {name: business.__dict__ for name, business in self.businesses.items()}
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_data(self, filename: str):
        """
        Load business data from a JSON file.

        :param filename: Name of the file to load data from
        """
        with open(filename, 'r') as f:
            data = json.load(f)
        for name, business_data in data.items():
            business = Business(business_data["name"], business_data["location"], business_data["industry"])
            business.tasks = business_data["tasks"]
            self.businesses[name] = business


# Main function for demonstration purposes
def main():
    """
    Main function to demonstrate usage of the DigitalProgressTracker tool.
    """
    tracker = DigitalProgressTracker()

    # Add businesses
    tracker.add_business("Stuttgart Bakery", "Stuttgart", "Food Service")
    tracker.add_business("Stuttgart Tech Solutions", "Stuttgart", "IT Consulting")

    # Add tasks for businesses
    bakery = tracker.get_business("Stuttgart Bakery")
    bakery.add_task("Create Website", "Develop a website to showcase products.")
    bakery.add_task("Set up Online Ordering", "Enable customers to order online.")

    tech_solutions = tracker.get_business("Stuttgart Tech Solutions")
    tech_solutions.add_task("Develop CRM Software", "Create a custom CRM for clients.")
    tech_solutions.add_task("Optimize SEO", "Improve search engine rankings.")

    # Update task status
    bakery.update_task_status("Create Website", "Completed")
    tech_solutions.update_task_status("Optimize SEO", "In Progress")

    # Generate reports
    print("Individual Reports:")
    print(bakery.generate_report())
    print(tech_solutions.generate_report())

    print("\nOverall Report:")
    print(tracker.generate_overall_report())

    # Save data to file
    tracker.save_data("business_data.json")

    # Load data from file
    new_tracker = DigitalProgressTracker()
    new_tracker.load_data("business_data.json")
    print("\nLoaded Data:")
    print(new_tracker.generate_overall_report())


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
```

This code snippet provides a complete system to track and manage digital progress for small businesses, including features for adding tasks, updating their statuses, generating progress reports, saving data to a file, and loading it back.
