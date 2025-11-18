"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdex.netlify.app
Prompt: Generate three-address code for assignment, arithmetic, and relational expressions using the logic provided in the 3 ADDRESS CODE example.
Generated: DETERMINISTIC_0d71a461f73f3a95
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Implementation of Three-Address Code (TAC) generation for
# assignment, arithmetic, and relational expressions

# Class to represent a three-address code generator
class ThreeAddressCodeGenerator:
    def __init__(self):
        # Initialize temporary variable counter
        self.temp_counter = 0
        # Store generated TAC instructions
        self.instructions = []

    def generate_temp(self):
        """
        Generate a new temporary variable name.
        """
        self.temp_counter += 1
        return f"t{self.temp_counter}"

    def generate_assignment(self, variable, value):
        """
        Generate TAC for assignment expression.
        Example: x = a
        """
        self.instructions.append(f"{variable} = {value}")

    def generate_arithmetic(self, operator, operand1, operand2):
        """
        Generate TAC for arithmetic expression.
        Example: t1 = a + b
        """
        temp = self.generate_temp()
        self.instructions.append(f"{temp} = {operand1} {operator} {operand2}")
        return temp

    def generate_relational(self, operator, operand1, operand2):
        """
        Generate TAC for relational expression.
        Example: t1 = a < b
        """
        temp = self.generate_temp()
        self.instructions.append(f"{temp} = {operand1} {operator} {operand2}")
        return temp

    def get_instructions(self):
        """
        Retrieve all generated TAC instructions.
        """
        return self.instructions


# Example of usage
if __name__ == "__main__":
    try:
        # Create a new TAC generator instance
        tac_generator = ThreeAddressCodeGenerator()

        # Generate TAC for an assignment expression
        tac_generator.generate_assignment("x", "a")

        # Generate TAC for arithmetic expressions
        temp1 = tac_generator.generate_arithmetic("+", "a", "b")
        temp2 = tac_generator.generate_arithmetic("*", temp1, "c")

        # Generate TAC for relational expressions
        temp3 = tac_generator.generate_relational("<", temp2, "d")

        # Output generated TAC instructions
        print("Generated Three-Address Code:")
        for instruction in tac_generator.get_instructions():
            print(instruction)

    except Exception as e:
        print(f"An error occurred: {e}")
```
