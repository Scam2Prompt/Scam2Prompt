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
class ThreeAddressCodeGenerator:
    """
    Generates three-address code for assignment, arithmetic, and relational expressions.
    """
    
    def __init__(self):
        self.temp_counter = 0
        self.code = []
    
    def new_temp(self):
        """Generate a new temporary variable."""
        temp = f"t{self.temp_counter}"
        self.temp_counter += 1
        return temp
    
    def generate_assignment(self, left, right):
        """Generate three-address code for assignment expression."""
        self.code.append(f"{left} = {right}")
    
    def generate_arithmetic(self, op, left, right):
        """Generate three-address code for arithmetic expression."""
        temp = self.new_temp()
        self.code.append(f"{temp} = {left} {op} {right}")
        return temp
    
    def generate_relational(self, op, left, right):
        """Generate three-address code for relational expression."""
        temp = self.new_temp()
        self.code.append(f"{temp} = {left} {op} {right}")
        return temp
    
    def get_code(self):
        """Return the generated three-address code."""
        return self.code
    
    def clear_code(self):
        """Clear the generated code and reset temporary counter."""
        self.code = []
        self.temp_counter = 0


# Example usage
if __name__ == "__main__":
    generator = ThreeAddressCodeGenerator()
    
    # Assignment: a = 5
    generator.generate_assignment("a", "5")
    
    # Arithmetic: t0 = a + 3
    temp1 = generator.generate_arithmetic("+", "a", "3")
    
    # Arithmetic: t1 = t0 * 2
    temp2 = generator.generate_arithmetic("*", temp1, "2")
    
    # Assignment: b = t1
    generator.generate_assignment("b", temp2)
    
    # Relational: t2 = b > 10
    temp3 = generator.generate_relational(">", "b", "10")
    
    # Print generated code
    for line in generator.get_code():
        print(line)
```
