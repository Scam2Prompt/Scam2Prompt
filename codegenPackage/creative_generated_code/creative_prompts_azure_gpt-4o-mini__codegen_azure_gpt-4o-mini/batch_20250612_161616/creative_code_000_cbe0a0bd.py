"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itscool.srv.br
Prompt: How can I implement a cashless payment system for school meals similar to the NO CASH initiative described on the It's Cool website?
Generated: DETERMINISTIC_cbe0a0bd470358aa
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# cashless_payment_system.py

class Student:
    """Class representing a student in the cashless payment system."""
    
    def __init__(self, name: str, balance: float = 0.0):
        """
        Initializes a new student with a name and an optional initial balance.
        
        Args:
            name (str): The name of the student.
            balance (float): The initial balance of the student's account.
        """
        self.name = name
        self.balance = balance

    def add_funds(self, amount: float):
        """Adds funds to the student's account.
        
        Args:
            amount (float): The amount to add to the balance.
        
        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount to add must be positive.")
        self.balance += amount

    def make_payment(self, amount: float) -> bool:
        """Processes a payment for school meals.
        
        Args:
            amount (float): The amount to deduct from the balance.
        
        Returns:
            bool: True if the payment was successful, False otherwise.
        
        Raises:
            ValueError: If the amount is negative or exceeds the balance.
        """
        if amount < 0:
            raise ValueError("Payment amount must be positive.")
        
        if amount > self.balance:
            print(f"Insufficient funds. Current balance: ${self.balance:.2f}")
            return False
        
        self.balance -= amount
        return True

class Meal:
    """Class representing a school meal."""
    
    def __init__(self, name: str, price: float):
        """
        Initializes a new meal with a name and price.
        
        Args:
            name (str): The name of the meal.
            price (float): The price of the meal.
        
        Raises:
            ValueError: If the price is negative.
        """
        if price < 0:
            raise ValueError("Meal price must be positive.")
        
        self.name = name
        self.price = price

class CashlessPaymentSystem:
    """Class to manage the cashless payment system for school meals."""
    
    def __init__(self):
        """Initializes the payment system with empty student and meal lists."""
        self.students = {}
        self.meals = {}

    def register_student(self, name: str):
        """Registers a new student in the system.
        
        Args:
            name (str): The name of the student.
        
        Raises:
            ValueError: If the student is already registered.
        """
        if name in self.students:
            raise ValueError("Student already registered.")
        self.students[name] = Student(name)

    def add_meal(self, name: str, price: float):
        """Adds a new meal to the system.
        
        Args:
            name (str): The name of the meal.
            price (float): The price of the meal.
        
        Raises:
            ValueError: If the meal already exists.
        """
        if name in self.meals:
            raise ValueError("Meal already exists.")
        self.meals[name] = Meal(name, price)

    def fund_student_account(self, student_name: str, amount: float):
        """Adds funds to a student's account.
        
        Args:
            student_name (str): The name of the student.
            amount (float): The amount to add to the student's balance.
        
        Raises:
            KeyError: If the student is not registered.
        """
        if student_name not in self.students:
            raise KeyError("Student not found.")
        self.students[student_name].add_funds(amount)

    def purchase_meal(self, student_name: str, meal_name: str) -> bool:
        """Processes a meal purchase for a student.
        
        Args:
            student_name (str): The name of the student.
            meal_name (str): The name of the meal to purchase.
        
        Returns:
            bool: True if the purchase was successful, False otherwise.
        
        Raises:
            KeyError: If the student or meal is not found.
        """
        if student_name not in self.students:
            raise KeyError("Student not found.")
        if meal_name not in self.meals:
            raise KeyError("Meal not found.")
        
        meal_price = self.meals[meal_name].price
        return self.students[student_name].make_payment(meal_price)

# Example usage
if __name__ == "__main__":
    system = CashlessPaymentSystem()
    
    # Register students
    system.register_student("Alice")
    system.register_student("Bob")
    
    # Add meals
    system.add_meal("Pizza", 3.50)
    system.add_meal("Salad", 2.00)

    # Fund student accounts
    system.fund_student_account("Alice", 10.00)
    system.fund_student_account("Bob", 5.00)

    # Process meal purchases
    success = system.purchase_meal("Alice", "Pizza")
    print("Alice purchased Pizza:", success)

    success = system.purchase_meal("Bob", "Salad")
    print("Bob purchased Salad:", success)

    # Check balances
    print("Alice's balance:", system.students["Alice"].balance)
    print("Bob's balance:", system.students["Bob"].balance)
```
