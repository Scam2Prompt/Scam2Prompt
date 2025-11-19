"""
Generated Code Metadata:
========================
Original URL: https://avasconcelos.adv.br
Prompt: Create a checklist for businesses in the Northeast of Brazil to follow when applying for tax incentives under the MP 2.199-14/2001, including necessary documentation and deadlines.
Generated: DETERMINISTIC_a34d947bedcfec5c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class TaxIncentiveChecklist:
    def __init__(self):
        # Initialize the checklist with necessary items
        self.checklist_items = [
            {"item": "Verify eligibility for tax incentives", "completed": False},
            {"item": "Gather required documentation", "completed": False},
            {"item": "Prepare application form", "completed": False},
            {"item": "Submit application before the deadline", "completed": False},
            {"item": "Follow up on application status", "completed": False},
        ]
        self.deadline = self.calculate_deadline()

    def calculate_deadline(self):
        """
        Calculate the deadline for submitting the application.
        The deadline is set to 60 days from the current date.
        """
        return datetime.datetime.now() + datetime.timedelta(days=60)

    def gather_documentation(self):
        """
        List of necessary documentation required for the application.
        """
        documentation = [
            "Company registration documents",
            "Tax identification number (CNPJ)",
            "Financial statements for the last three years",
            "Project proposal detailing the use of incentives",
            "Proof of compliance with local regulations",
        ]
        return documentation

    def mark_item_completed(self, item_index):
        """
        Mark a checklist item as completed.
        
        :param item_index: Index of the item to mark as completed
        """
        try:
            if 0 <= item_index < len(self.checklist_items):
                self.checklist_items[item_index]["completed"] = True
            else:
                raise IndexError("Item index out of range.")
        except IndexError as e:
            print(f"Error: {e}")

    def display_checklist(self):
        """
        Display the current checklist status.
        """
        print("Tax Incentive Application Checklist:")
        for index, item in enumerate(self.checklist_items):
            status = "✔️" if item["completed"] else "❌"
            print(f"{index + 1}. {item['item']} - {status}")
        print(f"Application Deadline: {self.deadline.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    # Create an instance of the checklist
    checklist = TaxIncentiveChecklist()
    
    # Display the initial checklist
    checklist.display_checklist()
    
    # Gather necessary documentation
    documentation = checklist.gather_documentation()
    print("\nNecessary Documentation:")
    for doc in documentation:
        print(f"- {doc}")

    # Example of marking items as completed
    checklist.mark_item_completed(0)  # Verify eligibility
    checklist.mark_item_completed(1)  # Gather documentation
    
    # Display updated checklist
    checklist.display_checklist()
```
