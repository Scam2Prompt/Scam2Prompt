"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.connext.solutions
Prompt: Create a program that helps businesses calculate cost savings when using Connext's offshore staffing solutions compared to local wages. Include input fields for employee count and average local salary.
Generated: DETERMINISTIC_1fb17565461280b4
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StaffingCostCalculator:
    """
    A class to calculate cost savings when using offshore staffing solutions
    compared to local wages.
    """

    def __init__(self):
        self.local_employee_count = 0
        self.local_average_salary = 0.0
        self.offshore_average_salary = 0.0

    def input_local_data(self):
        """
        Prompts the user to input the number of local employees and their average salary.
        """
        try:
            self.local_employee_count = int(input("Enter the number of local employees: "))
            if self.local_employee_count < 0:
                raise ValueError("Employee count cannot be negative.")
            
            self.local_average_salary = float(input("Enter the average local salary: "))
            if self.local_average_salary < 0:
                raise ValueError("Average salary cannot be negative.")
        except ValueError as ve:
            print(f"Input error: {ve}")
            return False
        
        return True

    def input_offshore_data(self):
        """
        Prompts the user to input the average salary for offshore staffing.
        """
        try:
            self.offshore_average_salary = float(input("Enter the average offshore salary: "))
            if self.offshore_average_salary < 0:
                raise ValueError("Average offshore salary cannot be negative.")
        except ValueError as ve:
            print(f"Input error: {ve}")
            return False
        
        return True

    def calculate_savings(self):
        """
        Calculate the total cost of local and offshore salaries and compute the savings.
        
        Returns:
            float: The total savings when using offshore staffing.
        """
        local_total_cost = self.local_employee_count * self.local_average_salary
        offshore_total_cost = self.local_employee_count * self.offshore_average_salary
        savings = local_total_cost - offshore_total_cost
        
        return savings

    def display_savings(self, savings):
        """
        Displays the calculated savings.
        
        Args:
            savings (float): The total savings calculated.
        """
        if savings > 0:
            print(f"Total savings by using offshore staffing: ${savings:.2f}")
        elif savings < 0:
            print("Using offshore staffing will cost more than local staffing.")
        else:
            print("There is no cost difference between local and offshore staffing.")

    def run(self):
        """
        The main method to run the cost savings calculator program.
        """
        if self.input_local_data() and self.input_offshore_data():
            savings = self.calculate_savings()
            self.display_savings(savings)


if __name__ == "__main__":
    calculator = StaffingCostCalculator()
    calculator.run()
```
