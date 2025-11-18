"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enacip.edu.pe
Prompt: Using the Enacip website as a reference, write code to calculate the cost of enrolling in multiple diploma programs, including discounts for bundled offers like "6 diplomados x S/169."
Generated: DETERMINISTIC_cd06d6d6857a489a
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DiplomaProgram:
    def __init__(self, name: str, price: float):
        """
        Initializes a DiplomaProgram instance.

        Args:
            name (str): The name of the diploma program.
            price (float): The price of enrolling in the diploma program.
        """
        self.name = name
        self.price = price


class EnrollmentCalculator:
    def __init__(self):
        """
        Initializes the EnrollmentCalculator with a dictionary of programs.
        """
        self.programs = {}

    def add_program(self, program: DiplomaProgram):
        """
        Adds a diploma program to the calculator.

        Args:
            program (DiplomaProgram): The diploma program to add.
        """
        self.programs[program.name] = program

    def calculate_total_cost(self, selected_programs: list) -> float:
        """
        Calculates the total cost of enrolling in the selected diploma programs.

        Args:
            selected_programs (list): A list of program names to enroll in.

        Returns:
            float: The total enrollment cost with applicable discounts.
        """
        total_cost = 0.0
        program_count = len(selected_programs)

        # Calculate the total cost for selected programs
        for program_name in selected_programs:
            if program_name in self.programs:
                total_cost += self.programs[program_name].price
            else:
                raise ValueError(f"Program '{program_name}' is not available.")

        # Apply discounts for bundled offers
        if program_count >= 6:
            total_cost -= 50  # Example discount for enrolling in 6 or more programs

        return total_cost


def main():
    """
    Main function to demonstrate the EnrollmentCalculator usage.
    """
    # Create diploma programs
    diplomas = [
        DiplomaProgram("Diploma A", 50),
        DiplomaProgram("Diploma B", 60),
        DiplomaProgram("Diploma C", 70),
        DiplomaProgram("Diploma D", 80),
        DiplomaProgram("Diploma E", 90),
        DiplomaProgram("Diploma F", 100),
    ]

    # Initialize the enrollment calculator
    calculator = EnrollmentCalculator()

    # Add programs to the calculator
    for diploma in diplomas:
        calculator.add_program(diploma)

    # List of selected programs for enrollment
    selected_programs = ["Diploma A", "Diploma B", "Diploma C", "Diploma D", "Diploma E", "Diploma F"]

    try:
        # Calculate total cost
        total_cost = calculator.calculate_total_cost(selected_programs)
        print(f"Total enrollment cost for selected programs: S/{total_cost:.2f}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```
