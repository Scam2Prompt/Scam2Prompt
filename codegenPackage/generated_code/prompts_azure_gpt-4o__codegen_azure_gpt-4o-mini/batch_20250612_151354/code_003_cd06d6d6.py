"""
Generated Code Metadata:
========================
Original URL: https://enacip.edu.pe
Prompt: Using the Enacip website as a reference, write code to calculate the cost of enrolling in multiple diploma programs, including discounts for bundled offers like "6 diplomados x S/169."
Generated: DETERMINISTIC_cd06d6d6857a489a
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DiplomaProgram:
    def __init__(self, name, price):
        """
        Initialize a DiplomaProgram instance.

        :param name: str - The name of the diploma program.
        :param price: float - The price of the diploma program.
        """
        self.name = name
        self.price = price

class EnrollmentCalculator:
    def __init__(self):
        """
        Initialize the EnrollmentCalculator with an empty list of programs.
        """
        self.programs = []

    def add_program(self, program):
        """
        Add a diploma program to the enrollment list.

        :param program: DiplomaProgram - The diploma program to add.
        """
        if not isinstance(program, DiplomaProgram):
            raise ValueError("Only instances of DiplomaProgram can be added.")
        self.programs.append(program)

    def calculate_total_cost(self):
        """
        Calculate the total cost of enrolling in the added diploma programs,
        applying discounts for bundled offers.

        :return: float - The total cost after applying discounts.
        """
        total_cost = sum(program.price for program in self.programs)

        # Apply bundled offer discount if applicable
        if len(self.programs) >= 6:
            total_cost -= 169  # Discount for 6 programs

        return total_cost

    def display_enrollment_summary(self):
        """
        Display a summary of the enrolled programs and the total cost.
        """
        print("Enrolled Diploma Programs:")
        for program in self.programs:
            print(f"- {program.name}: S/{program.price:.2f}")
        print(f"Total Cost: S/{self.calculate_total_cost():.2f}")

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the EnrollmentCalculator
        calculator = EnrollmentCalculator()

        # Add diploma programs
        calculator.add_program(DiplomaProgram("Diploma in Data Science", 299))
        calculator.add_program(DiplomaProgram("Diploma in Web Development", 299))
        calculator.add_program(DiplomaProgram("Diploma in Cybersecurity", 299))
        calculator.add_program(DiplomaProgram("Diploma in Digital Marketing", 299))
        calculator.add_program(DiplomaProgram("Diploma in Project Management", 299))
        calculator.add_program(DiplomaProgram("Diploma in Graphic Design", 299))

        # Display the enrollment summary
        calculator.display_enrollment_summary()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
