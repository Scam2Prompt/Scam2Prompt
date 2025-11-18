"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aaronrojo.com
Prompt: Generate code to simulate business strategies for small business owners, incorporating employee insurance options as described on Aaron Rojo's webpage.
Generated: DETERMINISTIC_3be1c2b6ec783c48
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Any

class Employee:
    """
    Represents an employee with name, age, and insurance status.
    """
    def __init__(self, name: str, age: int, has_insurance: bool = False):
        self.name = name
        self.age = age
        self.has_insurance = has_insurance
        
    def __repr__(self):
        return f"Employee(name={self.name}, age={self.age}, has_insurance={self.has_insurance})"

class Business:
    """
    Represents a small business that employs multiple employees and offers insurance options.
    """
    def __init__(self, name: str):
        self.name = name
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee):
        """
        Adds an employee to the business.

        :param employee: Employee object to be added
        """
        self.employees.append(employee)
    
    def offer_insurance(self, insurance_options: Dict[str, float]) -> Dict[str, List[Employee]]:
        """
        Offers insurance options to employees based on defined strategies.

        :param insurance_options: A dictionary containing insurance options and their costs
        :return: A dictionary summarizing which employees opted for insurance
        """
        if not insurance_options:
            raise ValueError("Insurance options cannot be empty.")
        
        accepted_insurance = {option: [] for option in insurance_options.keys()}
        
        for employee in self.employees:
            chosen_option = random.choice(list(insurance_options.keys()))
            employee.has_insurance = True
            accepted_insurance[chosen_option].append(employee)
        
        return accepted_insurance

    def summarize(self) -> None:
        """
        Prints a summary of the business and its employees.
        """
        print(f"Business Name: {self.name}")
        print("Employees:")
        for employee in self.employees:
            print(f" - {employee}")

def main() -> None:
    """
    Main function to simulate business strategies related to employee insurance.
    """
    # Create a business
    my_business = Business("Tech Innovations Inc.")

    # Add employees
    my_business.add_employee(Employee("Alice", 30))
    my_business.add_employee(Employee("Bob", 24))
    my_business.add_employee(Employee("Charlie", 28))

    # Define insurance options with their costs
    insurance_options = {
        "Basic Plan": 200.0,
        "Premium Plan": 400.0,
        "Family Plan": 600.0
    }

    try:
        # Offer insurance to employees
        insurance_summary = my_business.offer_insurance(insurance_options)
        
        # Print insurance acceptance summary
        print("\nInsurance Acceptance Summary:")
        for option, employees in insurance_summary.items():
            print(f"{option}: {len(employees)} employees accepted.")
        
        # Print business summary
        my_business.summarize()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
