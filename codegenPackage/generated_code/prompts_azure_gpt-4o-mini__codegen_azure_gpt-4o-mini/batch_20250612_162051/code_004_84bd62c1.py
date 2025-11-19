"""
Generated Code Metadata:
========================
Original URL: https://unisonplus.vn
Prompt: What are the best practices for using modern tools and equipment in infrastructure construction, and how can I document these in a project report?
Generated: DETERMINISTIC_84bd62c1f0db31a6
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict

class InfrastructureConstructionBestPractices:
    """
    A class to encapsulate best practices for using modern tools and equipment in infrastructure construction.
    """

    def __init__(self):
        self.best_practices: List[Dict[str, str]] = []

    def add_best_practice(self, title: str, description: str) -> None:
        """
        Adds a best practice to the list.

        :param title: The title of the best practice.
        :param description: A detailed description of the best practice.
        """
        if not title or not description:
            raise ValueError("Title and description cannot be empty.")
        
        self.best_practices.append({"title": title, "description": description})

    def save_to_file(self, file_path: str) -> None:
        """
        Saves the best practices to a JSON file.

        :param file_path: The path to the file where the best practices will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.best_practices, file, indent=4)
        except IOError as e:
            print(f"Error writing to file {file_path}: {e}")
            raise

    def load_from_file(self, file_path: str) -> None:
        """
        Loads best practices from a JSON file.

        :param file_path: The path to the file from which best practices will be loaded.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        
        try:
            with open(file_path, 'r') as file:
                self.best_practices = json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file {file_path}: {e}")
            raise
        except IOError as e:
            print(f"Error reading file {file_path}: {e}")
            raise

    def generate_report(self) -> str:
        """
        Generates a formatted report of the best practices.

        :return: A string containing the formatted report.
        """
        report_lines = ["Best Practices for Infrastructure Construction:\n"]
        for practice in self.best_practices:
            report_lines.append(f"Title: {practice['title']}\nDescription: {practice['description']}\n")
        return "\n".join(report_lines)

# Example usage
if __name__ == "__main__":
    try:
        practices = InfrastructureConstructionBestPractices()
        practices.add_best_practice("Use of Drones", "Utilize drones for site surveys and monitoring progress.")
        practices.add_best_practice("3D Printing", "Implement 3D printing for rapid prototyping of construction components.")
        
        # Save to file
        practices.save_to_file("best_practices.json")
        
        # Load from file
        practices.load_from_file("best_practices.json")
        
        # Generate and print report
        report = practices.generate_report()
        print(report)
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
