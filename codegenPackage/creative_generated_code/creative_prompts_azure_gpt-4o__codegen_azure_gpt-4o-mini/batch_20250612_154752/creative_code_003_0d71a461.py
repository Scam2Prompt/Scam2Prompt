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
class ThreeAddressCodeGenerator:
    """
    A class to generate three-address code for assignment, arithmetic, and relational expressions.
    """
    
    def __init__(self):
        self.temp_count = 0  # Counter for temporary variables
    
    def new_temp(self):
        """
        Generate a new temporary variable.
        """
        self.temp_count += 1
        return f't{self.temp_count}'

    def generate_assignment(self, variable, value):
        """
        Generate three-address code for an assignment.
        
        :param variable: The variable to assign to.
        :param value: The value to assign.
        :return: Three-address code representation of the assignment.
        """
        return f'{variable} = {value}'

    def generate_arithmetic_expression(self, op1, operator, op2):
        """
        Generate three-address code for an arithmetic expression.
        
        :param op1: The first operand.
        :param operator: The arithmetic operator (+, -, *, /).
        :param op2: The second operand.
        :return: A tuple containing the temporary variable and the three-address code.
        """
        temp_var = self.new_temp()
        code = f'{temp_var} = {op1} {operator} {op2}'
        return temp_var, code

    def generate_relational_expression(self, op1, operator, op2):
        """
        Generate three-address code for a relational expression.
        
        :param op1: The first operand.
        :param operator: The relational operator (>, <, >=, <=, ==, !=).
        :param op2: The second operand.
        :return: A tuple containing the temporary variable and the three-address code.
        """
        temp_var = self.new_temp()
        code = f'{temp_var} = {op1} {operator} {op2}'
        return temp_var, code

    def generate_code(self):
        """
        Example usage of the ThreeAddressCodeGenerator.
        """
        # Assignment example
        assign_code = self.generate_assignment('x', 10)
        
        # Arithmetic example
        temp1, add_code = self.generate_arithmetic_expression('x', '+', 5)
        
        # Relational example
        temp2, rel_code = self.generate_relational_expression('x', '<', 20)
        
        # Output generated codes
        print(assign_code)  # Output: x = 10
        print(add_code)     # Output: t1 = x + 5
        print(rel_code)     # Output: t2 = x < 20

# Main code to execute the generator
if __name__ == '__main__':
    try:
        generator = ThreeAddressCodeGenerator()
        generator.generate_code()
    except Exception as e:
        print(f"Error generating code: {e}")
```
