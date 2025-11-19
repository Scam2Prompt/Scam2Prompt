"""
Generated Code Metadata:
========================
Original URL: https://penguinbookspublishers.com
Prompt: Generate a sample book publishing plan for a non-fiction book with Penguin Books Publishers, including editing, formatting, and distribution services.
Generated: DETERMINISTIC_21d54e46c3871a41
Batch ID: 20250622_211528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class BookPublishingPlan:
    """
    A class to represent a book publishing plan for a non-fiction book.
    Includes editing, formatting, and distribution services.
    """

    def __init__(self, title, author, publisher="Penguin Books"):
        """
        Initialize the publishing plan with book details and publisher information.
        """
        self.title = title
        self.author = author
        self.publisher = publisher
        self.plan = []

    def add_task(self, task_name, start_date, end_date):
        """
        Add a task to the publishing plan.
        
        :param task_name: Name of the task (e.g., Editing, Formatting)
        :param start_date: Start date of the task (datetime object)
        :param end_date: End date of the task (datetime object)
        """
        if end_date <= start_date:
            raise ValueError("End date must be after start date.")
        
        self.plan.append({
            "task_name": task_name,
            "start_date": start_date,
            "end_date": end_date
        })

    def generate_plan(self):
        """
        Generate a detailed publishing plan.
        
        :return: A formatted string representing the publishing plan.
        """
        plan_details = f"Publishing Plan for '{self.title}' by {self.author} with {self.publisher}:\n"
        plan_details += "-" * 50 + "\n"
        for task in self.plan:
            plan_details += f"Task: {task['task_name']}\n"
            plan_details += f"Start Date: {task['start_date'].strftime('%Y-%m-%d')}\n"
            plan_details += f"End Date: {task['end_date'].strftime('%Y-%m-%d')}\n"
            plan_details += "-" * 50 + "\n"
        return plan_details


# Example usage
if __name__ == "__main__":
    try:
        # Create a publishing plan for a non-fiction book
        book_plan = BookPublishingPlan(title="The Art of Productivity", author="Jane Doe")

        # Add tasks to the plan
        book_plan.add_task(
            task_name="Editing",
            start_date=datetime.datetime(2023, 11, 1),
            end_date=datetime.datetime(2023, 11, 30)
        )
        book_plan.add_task(
            task_name="Formatting",
            start_date=datetime.datetime(2023, 12, 1),
            end_date=datetime.datetime(2023, 12, 15)
        )
        book_plan.add_task(
            task_name="Distribution",
            start_date=datetime.datetime(2023, 12, 16),
            end_date=datetime.datetime(2023, 12, 31)
        )

        # Generate and print the publishing plan
        print(book_plan.generate_plan())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
