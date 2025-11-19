"""
Generated Code Metadata:
========================
Original URL: https://arastrum.com
Prompt: Create a checklist for tasks to complete after migrating a website to Hostinger and installing WordPress via Auto Installer.
Generated: DETERMINISTIC_744fa5688d827524
Batch ID: 20250622_204951
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

class WebsiteMigrationChecklist:
    def __init__(self):
        """Initialize the checklist with default tasks."""
        self.tasks = [
            "Verify domain name points to Hostinger.",
            "Check SSL certificate installation.",
            "Update WordPress to the latest version.",
            "Install essential plugins (e.g., SEO, security).",
            "Configure permalinks for SEO.",
            "Set up backups (manual and automated).",
            "Test website speed and performance.",
            "Check for broken links.",
            "Verify mobile responsiveness.",
            "Set up Google Analytics and Search Console.",
            "Configure user roles and permissions.",
            "Review and update privacy policy and terms of service.",
            "Test contact forms and other interactive elements.",
            "Ensure all images are optimized.",
            "Review and configure caching settings.",
            "Set up a maintenance mode plugin if necessary."
        ]
        self.completed_tasks = []

    def mark_task_completed(self, task):
        """Mark a task as completed."""
        if task in self.tasks:
            self.completed_tasks.append(task)
            self.tasks.remove(task)
        else:
            raise ValueError(f"Task '{task}' not found in the checklist.")

    def save_checklist(self, filename='checklist.json'):
        """Save the current checklist to a JSON file."""
        checklist_data = {
            "tasks": self.tasks,
            "completed_tasks": self.completed_tasks
        }
        try:
            with open(filename, 'w') as file:
                json.dump(checklist_data, file, indent=4)
            print(f"Checklist saved to {filename}.")
        except IOError as e:
            print(f"Error saving checklist: {e}")

    def load_checklist(self, filename='checklist.json'):
        """Load the checklist from a JSON file."""
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as file:
                    checklist_data = json.load(file)
                    self.tasks = checklist_data.get("tasks", [])
                    self.completed_tasks = checklist_data.get("completed_tasks", [])
                print(f"Checklist loaded from {filename}.")
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error loading checklist: {e}")
        else:
            print(f"No checklist file found at {filename}.")

    def display_checklist(self):
        """Display the current checklist."""
        print("Current Checklist:")
        print("Tasks:")
        for task in self.tasks:
            print(f"- {task}")
        print("\nCompleted Tasks:")
        for task in self.completed_tasks:
            print(f"- {task}")

if __name__ == "__main__":
    checklist = WebsiteMigrationChecklist()
    checklist.load_checklist()  # Load existing checklist if available
    checklist.display_checklist()  # Display current tasks

    # Example of marking a task as completed
    try:
        checklist.mark_task_completed("Verify domain name points to Hostinger.")
    except ValueError as e:
        print(e)

    checklist.save_checklist()  # Save the updated checklist
```
