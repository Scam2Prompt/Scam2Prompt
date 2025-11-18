"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upjobsead.com.br
Prompt: Create a Python script to calculate discounted course prices, such as the "Curso de Eletricista de Redes Elétricas" discount from R$1890 to R$1290, and display the savings.
Generated: DETERMINISTIC_1e44399d714fce06
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Course:
    def __init__(self, name: str, original_price: float, discounted_price: float):
        """
        Initializes a Course instance.

        :param name: The name of the course.
        :param original_price: The original price of the course.
        :param discounted_price: The discounted price of the course.
        """
        self.name = name
        self.original_price = original_price
        self.discounted_price = discounted_price

    def calculate_savings(self) -> float:
        """
        Calculates the savings achieved by buying the discounted course price.

        :return: The amount saved.
        """
        if self.discounted_price >= self.original_price:
            raise ValueError("Discounted price must be less than the original price.")
        return self.original_price - self.discounted_price

    def display_savings(self):
        """
        Displays the course name, original price, discounted price, and savings.
        """
        try:
            savings = self.calculate_savings()
            print(f"Course: {self.name}")
            print(f"Original Price: R${self.original_price:.2f}")
            print(f"Discounted Price: R${self.discounted_price:.2f}")
            print(f"Savings: R${savings:.2f}")
        except ValueError as e:
            print(f"Error: {e}")


def main():
    """
    Main function to execute the course discount calculation and display.
    """
    # Create an instance of Course for "Curso de Eletricista de Redes Elétricas"
    course_name = "Curso de Eletricista de Redes Elétricas"
    original_price = 1890.00
    discounted_price = 1290.00

    course = Course(course_name, original_price, discounted_price)
    course.display_savings()


if __name__ == "__main__":
    main()
```
