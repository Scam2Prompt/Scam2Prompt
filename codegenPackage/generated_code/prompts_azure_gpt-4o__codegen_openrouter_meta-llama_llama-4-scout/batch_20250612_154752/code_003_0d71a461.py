"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Generate three-address code for assignment, arithmetic, and relational expressions using the logic provided in the 3 ADDRESS CODE example.
Generated: DETERMINISTIC_0d71a461f73f3a95
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Three Address Code Generator

class ThreeAddressCode:
    def __init__(self):
        self.code = []
        self.temp_counter = 0

    def get_temp(self):
        self.temp_counter += 1
        return f"t{self.temp_counter}"

    def assignment(self, var, expr):
        """
        Generate three-address code for assignment expression.

        Args:
            var (str): Variable name.
            expr (str): Expression to be assigned.

        Returns:
            None
        """
        self.code.append(f"{var} = {expr}")

    def arithmetic(self, op, var1, var2):
        """
        Generate three-address code for arithmetic expression.

        Args:
            op (str): Operator (+, -, *, /).
            var1 (str): First variable.
            var2 (str): Second variable.

        Returns:
            str: Temporary variable name.
        """
        temp = self.get_temp()
        self.code.append(f"{temp} = {var1} {op} {var2}")
        return temp

    def relational(self, op, var1, var2):
        """
        Generate three-address code for relational expression.

        Args:
            op (str): Operator (==, !=, <, >, <=, >=).
            var1 (str): First variable.
            var2 (str): Second variable.

        Returns:
            str: Temporary variable name.
        """
        temp = self.get_temp()
        self.code.append(f"{temp} = {var1} {op} {var2}")
        return temp

    def generate_code(self):
        # Example usage
        try:
            a = "a"
            b = "b"
            c = "c"

            # Assignment
            self.assignment(a, "10")

            # Arithmetic
            temp1 = self.arithmetic("+", a, b)
            self.assignment(c, temp1)

            # Relational
            temp2 = self.relational("==", a, b)

            # Print generated code
            for i, line in enumerate(self.code, start=1):
                print(f"{i}: {line}")

        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    three_address_code = ThreeAddressCode()
    three_address_code.generate_code()
```
