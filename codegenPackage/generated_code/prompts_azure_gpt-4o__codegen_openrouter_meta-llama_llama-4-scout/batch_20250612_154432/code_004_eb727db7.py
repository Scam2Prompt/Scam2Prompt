"""
Generated Code Metadata:
========================
Original URL: https://3rdandtaylor.com
Prompt: Create a Python program that formalizes and executes a strategic plan for launching a new product, as described in the "Document" phase of 3rd & Taylor's growth formula.
Generated: DETERMINISTIC_eb727db7a4281e9c
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_launch_plan.py

class ProductLaunchPlan:
    """
    A class representing a strategic plan for launching a new product.
    """

    def __init__(self, product_name, launch_date, target_market, marketing_budget):
        """
        Initializes a ProductLaunchPlan instance.

        Args:
        - product_name (str): The name of the product to be launched.
        - launch_date (str): The date of the product launch in YYYY-MM-DD format.
        - target_market (str): The target market for the product.
        - marketing_budget (float): The budget allocated for marketing.
        """
        self.product_name = product_name
        self.launch_date = launch_date
        self.target_market = target_market
        self.marketing_budget = marketing_budget
        self.tasks = []

    def add_task(self, task_name, due_date, responsible_person):
        """
        Adds a task to the product launch plan.

        Args:
        - task_name (str): The name of the task.
        - due_date (str): The due date of the task in YYYY-MM-DD format.
        - responsible_person (str): The person responsible for completing the task.
        """
        task = {
            "task_name": task_name,
            "due_date": due_date,
            "responsible_person": responsible_person,
            "status": "Not Started"
        }
        self.tasks.append(task)

    def update_task_status(self, task_name, status):
        """
        Updates the status of a task.

        Args:
        - task_name (str): The name of the task.
        - status (str): The updated status of the task.

        Raises:
        - ValueError: If the task does not exist or the status is invalid.
        """
        for task in self.tasks:
            if task["task_name"] == task_name:
                if status in ["Not Started", "In Progress", "Completed"]:
                    task["status"] = status
                else:
                    raise ValueError("Invalid status")
                return
        raise ValueError("Task not found")

    def print_plan(self):
        """
        Prints the product launch plan.
        """
        print(f"Product Name: {self.product_name}")
        print(f"Launch Date: {self.launch_date}")
        print(f"Target Market: {self.target_market}")
        print(f"Marketing Budget: ${self.marketing_budget:.2f}")
        print("Tasks:")
        for task in self.tasks:
            print(f"- {task['task_name']} (Due: {task['due_date']}, Responsible: {task['responsible_person']}, Status: {task['status']})")


def main():
    try:
        plan = ProductLaunchPlan(
            product_name="New Smartphone",
            launch_date="2024-09-01",
            target_market="North America",
            marketing_budget=1000000.0
        )

        plan.add_task("Conduct Market Research", "2024-06-01", "John Doe")
        plan.add_task("Design Product Packaging", "2024-07-01", "Jane Smith")
        plan.add_task("Develop Marketing Campaign", "2024-08-01", "Bob Johnson")

        plan.print_plan()

        plan.update_task_status("Conduct Market Research", "Completed")
        plan.update_task_status("Design Product Packaging", "In Progress")

        print("\nUpdated Plan:")
        plan.print_plan()

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
