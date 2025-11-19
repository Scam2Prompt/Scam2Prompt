"""
Generated Code Metadata:
========================
Original URL: https://sistemabox.com.br
Prompt: "Develop a customer relationship management (CRM) module for an ERP system, focusing on simplicity and ease of use, à la Sistemabox's solutions."
Generated: DETERMINISTIC_1324fdf9d80ba3aa
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# crm_module.py

class Customer:
    """
    A class to represent a customer in the CRM system.
    """

    def __init__(self, customer_id, name, email, phone):
        """
        Initializes a new customer instance.

        :param customer_id: Unique identifier for the customer
        :param name: Name of the customer
        :param email: Email address of the customer
        :param phone: Phone number of the customer
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        """Returns a string representation of the customer."""
        return f"Customer({self.customer_id}, {self.name}, {self.email}, {self.phone})"


class CRM:
    """
    A class to manage customer relationships in the CRM system.
    """

    def __init__(self):
        """Initializes the CRM with an empty customer list."""
        self.customers = {}

    def add_customer(self, customer):
        """
        Adds a new customer to the CRM.

        :param customer: An instance of the Customer class
        :raises ValueError: If the customer already exists
        """
        if customer.customer_id in self.customers:
            raise ValueError(f"Customer with ID {customer.customer_id} already exists.")
        self.customers[customer.customer_id] = customer

    def get_customer(self, customer_id):
        """
        Retrieves a customer by their ID.

        :param customer_id: Unique identifier for the customer
        :return: An instance of the Customer class
        :raises KeyError: If the customer does not exist
        """
        try:
            return self.customers[customer_id]
        except KeyError:
            raise KeyError(f"Customer with ID {customer_id} not found.")

    def update_customer(self, customer_id, name=None, email=None, phone=None):
        """
        Updates an existing customer's information.

        :param customer_id: Unique identifier for the customer
        :param name: New name of the customer (optional)
        :param email: New email address of the customer (optional)
        :param phone: New phone number of the customer (optional)
        :raises KeyError: If the customer does not exist
        """
        customer = self.get_customer(customer_id)
        if name:
            customer.name = name
        if email:
            customer.email = email
        if phone:
            customer.phone = phone

    def delete_customer(self, customer_id):
        """
        Deletes a customer from the CRM.

        :param customer_id: Unique identifier for the customer
        :raises KeyError: If the customer does not exist
        """
        try:
            del self.customers[customer_id]
        except KeyError:
            raise KeyError(f"Customer with ID {customer_id} not found.")

    def list_customers(self):
        """
        Lists all customers in the CRM.

        :return: A list of Customer instances
        """
        return list(self.customers.values())


# Example usage
if __name__ == "__main__":
    crm = CRM()

    # Adding customers
    try:
        crm.add_customer(Customer(1, "Alice Smith", "alice@example.com", "123-456-7890"))
        crm.add_customer(Customer(2, "Bob Johnson", "bob@example.com", "098-765-4321"))
    except ValueError as e:
        print(e)

    # Listing customers
    for customer in crm.list_customers():
        print(customer)

    # Updating a customer
    try:
        crm.update_customer(1, email="alice.smith@example.com")
    except KeyError as e:
        print(e)

    # Retrieving a customer
    try:
        customer = crm.get_customer(1)
        print("Retrieved:", customer)
    except KeyError as e:
        print(e)

    # Deleting a customer
    try:
        crm.delete_customer(2)
    except KeyError as e:
        print(e)

    # Listing customers after deletion
    for customer in crm.list_customers():
        print(customer)
```
