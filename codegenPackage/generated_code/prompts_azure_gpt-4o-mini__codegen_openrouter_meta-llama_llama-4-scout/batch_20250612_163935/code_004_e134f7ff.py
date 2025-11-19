"""
Generated Code Metadata:
========================
Original URL: https://sistemabox.com.br
Prompt: What are the key features to include in a business management system for small enterprises, according to the Sistema Box offerings?
Generated: DETERMINISTIC_e134f7ff124e4685
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# business_management_system.py

class BusinessManagementSystem:
    """
    A class representing a business management system for small enterprises.

    Attributes:
    -----------
    name (str): The name of the business.
    employees (list): A list of employee objects.
    products (list): A list of product objects.
    services (list): A list of service objects.

    Methods:
    --------
    add_employee(employee): Adds an employee to the system.
    add_product(product): Adds a product to the system.
    add_service(service): Adds a service to the system.
    display_employees(): Displays all employees in the system.
    display_products(): Displays all products in the system.
    display_services(): Displays all services in the system.
    """

    def __init__(self, name):
        """
        Initializes a BusinessManagementSystem object.

        Args:
        -----
        name (str): The name of the business.
        """
        self.name = name
        self.employees = []
        self.products = []
        self.services = []

    def add_employee(self, employee):
        """
        Adds an employee to the system.

        Args:
        -----
        employee (Employee): An Employee object.

        Raises:
        ------
        TypeError: If employee is not an Employee object.
        """
        if not isinstance(employee, Employee):
            raise TypeError("Employee must be an Employee object")
        self.employees.append(employee)

    def add_product(self, product):
        """
        Adds a product to the system.

        Args:
        -----
        product (Product): A Product object.

        Raises:
        ------
        TypeError: If product is not a Product object.
        """
        if not isinstance(product, Product):
            raise TypeError("Product must be a Product object")
        self.products.append(product)

    def add_service(self, service):
        """
        Adds a service to the system.

        Args:
        -----
        service (Service): A Service object.

        Raises:
        ------
        TypeError: If service is not a Service object.
        """
        if not isinstance(service, Service):
            raise TypeError("Service must be a Service object")
        self.services.append(service)

    def display_employees(self):
        """
        Displays all employees in the system.
        """
        for employee in self.employees:
            print(employee)

    def display_products(self):
        """
        Displays all products in the system.
        """
        for product in self.products:
            print(product)

    def display_services(self):
        """
        Displays all services in the system.
        """
        for service in self.services:
            print(service)


class Employee:
    """
    A class representing an employee.

    Attributes:
    -----------
    name (str): The name of the employee.
    position (str): The position of the employee.
    salary (float): The salary of the employee.
    """

    def __init__(self, name, position, salary):
        """
        Initializes an Employee object.

        Args:
        -----
        name (str): The name of the employee.
        position (str): The position of the employee.
        salary (float): The salary of the employee.

        Raises:
        ------
        ValueError: If salary is negative.
        """
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        """
        Returns a string representation of the Employee object.

        Returns:
        -------
        str: A string representation of the Employee object.
        """
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}"


class Product:
    """
    A class representing a product.

    Attributes:
    -----------
    name (str): The name of the product.
    price (float): The price of the product.
    quantity (int): The quantity of the product.
    """

    def __init__(self, name, price, quantity):
        """
        Initializes a Product object.

        Args:
        -----
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity of the product.

        Raises:
        ------
        ValueError: If price or quantity is negative.
        """
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity cannot be negative")
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """
        Returns a string representation of the Product object.

        Returns:
        -------
        str: A string representation of the Product object.
        """
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"


class Service:
    """
    A class representing a service.

    Attributes:
    -----------
    name (str): The name of the service.
    price (float): The price of the service.
    """

    def __init__(self, name, price):
        """
        Initializes a Service object.

        Args:
        -----
        name (str): The name of the service.
        price (float): The price of the service.

        Raises:
        ------
        ValueError: If price is negative.
        """
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.name = name
        self.price = price

    def __str__(self):
        """
        Returns a string representation of the Service object.

        Returns:
        -------
        str: A string representation of the Service object.
        """
        return f"Name: {self.name}, Price: {self.price}"


def main():
    try:
        # Create a business management system
        bms = BusinessManagementSystem("Sistema Box")

        # Create employees
        employee1 = Employee("John Doe", "Manager", 5000.0)
        employee2 = Employee("Jane Doe", "Developer", 4000.0)

        # Add employees to the system
        bms.add_employee(employee1)
        bms.add_employee(employee2)

        # Create products
        product1 = Product("Product A", 100.0, 10)
        product2 = Product("Product B", 200.0, 20)

        # Add products to the system
        bms.add_product(product1)
        bms.add_product(product2)

        # Create services
        service1 = Service("Service A", 50.0)
        service2 = Service("Service B", 100.0)

        # Add services to the system
        bms.add_service(service1)
        bms.add_service(service2)

        # Display employees, products, and services
        print("Employees:")
        bms.display_employees()
        print("\nProducts:")
        bms.display_products()
        print("\nServices:")
        bms.display_services()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
