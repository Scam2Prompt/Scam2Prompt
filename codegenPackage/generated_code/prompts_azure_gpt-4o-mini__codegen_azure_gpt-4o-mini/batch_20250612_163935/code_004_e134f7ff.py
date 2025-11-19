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
class BusinessManagementSystem:
    """
    A class to represent a Business Management System for small enterprises.
    This system includes key features based on the offerings of Sistema Box.
    """

    def __init__(self):
        """
        Initializes the Business Management System with default features.
        """
        self.customers = []
        self.invoices = []
        self.products = []
        self.employees = []
        self.reports = []

    def add_customer(self, customer):
        """
        Adds a new customer to the system.

        :param customer: A dictionary containing customer details.
        """
        try:
            if not isinstance(customer, dict):
                raise ValueError("Customer must be a dictionary.")
            self.customers.append(customer)
            print(f"Customer {customer['name']} added successfully.")
        except Exception as e:
            print(f"Error adding customer: {e}")

    def create_invoice(self, invoice):
        """
        Creates a new invoice in the system.

        :param invoice: A dictionary containing invoice details.
        """
        try:
            if not isinstance(invoice, dict):
                raise ValueError("Invoice must be a dictionary.")
            self.invoices.append(invoice)
            print(f"Invoice {invoice['id']} created successfully.")
        except Exception as e:
            print(f"Error creating invoice: {e}")

    def add_product(self, product):
        """
        Adds a new product to the system.

        :param product: A dictionary containing product details.
        """
        try:
            if not isinstance(product, dict):
                raise ValueError("Product must be a dictionary.")
            self.products.append(product)
            print(f"Product {product['name']} added successfully.")
        except Exception as e:
            print(f"Error adding product: {e}")

    def add_employee(self, employee):
        """
        Adds a new employee to the system.

        :param employee: A dictionary containing employee details.
        """
        try:
            if not isinstance(employee, dict):
                raise ValueError("Employee must be a dictionary.")
            self.employees.append(employee)
            print(f"Employee {employee['name']} added successfully.")
        except Exception as e:
            print(f"Error adding employee: {e}")

    def generate_report(self):
        """
        Generates a simple report of the current system state.
        """
        try:
            report = {
                "total_customers": len(self.customers),
                "total_invoices": len(self.invoices),
                "total_products": len(self.products),
                "total_employees": len(self.employees),
            }
            self.reports.append(report)
            print("Report generated successfully.")
            return report
        except Exception as e:
            print(f"Error generating report: {e}")

    def get_customers(self):
        """
        Returns the list of customers.

        :return: List of customers.
        """
        return self.customers

    def get_invoices(self):
        """
        Returns the list of invoices.

        :return: List of invoices.
        """
        return self.invoices

    def get_products(self):
        """
        Returns the list of products.

        :return: List of products.
        """
        return self.products

    def get_employees(self):
        """
        Returns the list of employees.

        :return: List of employees.
        """
        return self.employees


# Example usage
if __name__ == "__main__":
    bms = BusinessManagementSystem()
    
    # Adding sample data
    bms.add_customer({"name": "John Doe", "email": "john@example.com"})
    bms.add_product({"name": "Widget", "price": 19.99})
    bms.add_employee({"name": "Jane Smith", "position": "Manager"})
    bms.create_invoice({"id": 1, "customer": "John Doe", "amount": 19.99})

    # Generating report
    report = bms.generate_report()
    print(report)
```
