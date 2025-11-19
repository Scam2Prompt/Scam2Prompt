"""
Generated Code Metadata:
========================
Original URL: https://presale-topgs.com
Prompt: Develop a plan for implementing a customer relationship management (CRM) system for a company like Hanil Furniture Gallery, taking into account their focus on customer satisfaction and design excellence.
Generated: DETERMINISTIC_e9f2f770a03a053d
Batch ID: 20250622_211442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# crm_system.py

class Customer:
    """Represents a customer in the CRM system."""

    def __init__(self, customer_id, name, email, phone_number):
        """
        Initializes a Customer object.

        Args:
            customer_id (int): Unique identifier for the customer.
            name (str): Customer's name.
            email (str): Customer's email address.
            phone_number (str): Customer's phone number.
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def __str__(self):
        return f"Customer {self.customer_id}: {self.name}, {self.email}, {self.phone_number}"


class Interaction:
    """Represents an interaction with a customer in the CRM system."""

    def __init__(self, interaction_id, customer_id, interaction_type, description):
        """
        Initializes an Interaction object.

        Args:
            interaction_id (int): Unique identifier for the interaction.
            customer_id (int): Foreign key referencing the Customer object.
            interaction_type (str): Type of interaction (e.g., phone call, email, meeting).
            description (str): Description of the interaction.
        """
        self.interaction_id = interaction_id
        self.customer_id = customer_id
        self.interaction_type = interaction_type
        self.description = description

    def __str__(self):
        return f"Interaction {self.interaction_id}: {self.interaction_type} with Customer {self.customer_id}"


class CRMSystem:
    """Represents the CRM system for Hanil Furniture Gallery."""

    def __init__(self):
        """
        Initializes the CRM system.

        Attributes:
            customers (dict): Dictionary of Customer objects, keyed by customer ID.
            interactions (dict): Dictionary of Interaction objects, keyed by interaction ID.
        """
        self.customers = {}
        self.interactions = {}

    def add_customer(self, customer):
        """
        Adds a customer to the CRM system.

        Args:
            customer (Customer): Customer object to add.

        Raises:
            ValueError: If a customer with the same ID already exists.
        """
        if customer.customer_id in self.customers:
            raise ValueError("Customer with this ID already exists")
        self.customers[customer.customer_id] = customer

    def add_interaction(self, interaction):
        """
        Adds an interaction to the CRM system.

        Args:
            interaction (Interaction): Interaction object to add.

        Raises:
            ValueError: If an interaction with the same ID already exists or if the customer ID is not found.
        """
        if interaction.interaction_id in self.interactions:
            raise ValueError("Interaction with this ID already exists")
        if interaction.customer_id not in self.customers:
            raise ValueError("Customer ID not found")
        self.interactions[interaction.interaction_id] = interaction

    def get_customer(self, customer_id):
        """
        Retrieves a customer from the CRM system.

        Args:
            customer_id (int): ID of the customer to retrieve.

        Returns:
            Customer: Customer object if found, None otherwise.
        """
        return self.customers.get(customer_id)

    def get_interaction(self, interaction_id):
        """
        Retrieves an interaction from the CRM system.

        Args:
            interaction_id (int): ID of the interaction to retrieve.

        Returns:
            Interaction: Interaction object if found, None otherwise.
        """
        return self.interactions.get(interaction_id)

    def __str__(self):
        customers_str = "\n".join(str(customer) for customer in self.customers.values())
        interactions_str = "\n".join(str(interaction) for interaction in self.interactions.values())
        return f"Customers:\n{customers_str}\n\nInteractions:\n{interactions_str}"


def main():
    crm = CRMSystem()

    # Create customers
    customer1 = Customer(1, "John Doe", "john.doe@example.com", "123-456-7890")
    customer2 = Customer(2, "Jane Smith", "jane.smith@example.com", "987-654-3210")

    # Add customers to CRM system
    crm.add_customer(customer1)
    crm.add_customer(customer2)

    # Create interactions
    interaction1 = Interaction(1, 1, "phone call", "Discussed furniture design")
    interaction2 = Interaction(2, 1, "email", "Follow-up on furniture inquiry")

    # Add interactions to CRM system
    crm.add_interaction(interaction1)
    crm.add_interaction(interaction2)

    # Print CRM system data
    print(crm)


if __name__ == "__main__":
    main()
```
