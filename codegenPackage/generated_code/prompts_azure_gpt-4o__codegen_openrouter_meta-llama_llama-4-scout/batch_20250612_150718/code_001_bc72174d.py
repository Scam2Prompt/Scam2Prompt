"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Create a script to automate the calculation of fees for different MBA programs at SOMTU, considering the fee structure provided on the website.
Generated: DETERMINISTIC_bc72174db1212d7d
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fee_calculator.py

class MBAProgram:
    """Represents an MBA program with its fee structure."""

    def __init__(self, name, tuition, fees, other_costs):
        """
        Initializes an MBA program with its fee structure.

        Args:
            name (str): Name of the MBA program.
            tuition (float): Tuition fee for the program.
            fees (float): Additional fees for the program.
            other_costs (float): Other costs associated with the program.
        """
        self.name = name
        self.tuition = tuition
        self.fees = fees
        self.other_costs = other_costs

    def calculate_total_fee(self):
        """Calculates the total fee for the MBA program."""
        return self.tuition + self.fees + self.other_costs


class SOMTUFeeCalculator:
    """Calculates fees for different MBA programs at SOMTU."""

    def __init__(self):
        """Initializes the fee calculator with MBA programs."""
        self.programs = {
            "Full-Time MBA": MBAProgram("Full-Time MBA", 120000, 1000, 2000),
            "Part-Time MBA": MBAProgram("Part-Time MBA", 90000, 800, 1500),
            "Executive MBA": MBAProgram("Executive MBA", 150000, 1200, 2500),
        }

    def get_program(self, program_name):
        """
        Retrieves an MBA program by its name.

        Args:
            program_name (str): Name of the MBA program.

        Returns:
            MBAProgram: The MBA program if found, otherwise None.
        """
        return self.programs.get(program_name)

    def calculate_fee(self, program_name):
        """
        Calculates the total fee for an MBA program.

        Args:
            program_name (str): Name of the MBA program.

        Returns:
            float: The total fee for the program if found, otherwise None.
        """
        program = self.get_program(program_name)
        if program:
            return program.calculate_total_fee()
        else:
            return None


def main():
    calculator = SOMTUFeeCalculator()

    # Example usage:
    programs = ["Full-Time MBA", "Part-Time MBA", "Executive MBA"]
    for program in programs:
        fee = calculator.calculate_fee(program)
        if fee:
            print(f"Total fee for {program}: ${fee:,.2f}")
        else:
            print(f"Program '{program}' not found.")

    # Test error handling:
    invalid_program = "Invalid Program"
    fee = calculator.calculate_fee(invalid_program)
    if fee is None:
        print(f"Program '{invalid_program}' not found.")


if __name__ == "__main__":
    main()
```
