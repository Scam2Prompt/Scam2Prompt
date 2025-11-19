"""
Generated Code Metadata:
========================
Original URL: https://www.espglobal.co
Prompt: What are the benefits of using a plug-and-play Proptech system like ESP Global for real estate agencies, and how can it help optimize operations and enhance customer experiences?
Generated: DETERMINISTIC_c5bf3d70c8c8a799
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PropTechSystem:
    """
    A class to represent a plug-and-play PropTech system for real estate agencies.
    This system aims to optimize operations and enhance customer experiences.
    """

    def __init__(self, agency_name):
        """
        Initializes the PropTech system for a specific real estate agency.

        Parameters:
        agency_name (str): The name of the real estate agency.
        """
        self.agency_name = agency_name
        self.properties = []
        self.clients = []

    def add_property(self, property_details):
        """
        Adds a new property to the agency's listings.

        Parameters:
        property_details (dict): A dictionary containing details of the property.

        Raises:
        ValueError: If property_details is not a dictionary or is missing required keys.
        """
        if not isinstance(property_details, dict):
            raise ValueError("Property details must be a dictionary.")
        
        required_keys = ['id', 'address', 'price', 'type']
        for key in required_keys:
            if key not in property_details:
                raise ValueError(f"Missing required property detail: {key}")

        self.properties.append(property_details)
        print(f"Property {property_details['id']} added successfully.")

    def add_client(self, client_details):
        """
        Adds a new client to the agency's client list.

        Parameters:
        client_details (dict): A dictionary containing details of the client.

        Raises:
        ValueError: If client_details is not a dictionary or is missing required keys.
        """
        if not isinstance(client_details, dict):
            raise ValueError("Client details must be a dictionary.")
        
        required_keys = ['id', 'name', 'contact']
        for key in required_keys:
            if key not in client_details:
                raise ValueError(f"Missing required client detail: {key}")

        self.clients.append(client_details)
        print(f"Client {client_details['id']} added successfully.")

    def optimize_operations(self):
        """
        Optimizes agency operations by providing insights on property performance and client engagement.
        """
        # Placeholder for optimization logic
        print("Optimizing operations...")

    def enhance_customer_experience(self):
        """
        Enhances customer experience by providing personalized services and timely updates.
        """
        # Placeholder for customer experience enhancement logic
        print("Enhancing customer experience...")

    def get_properties(self):
        """
        Returns the list of properties managed by the agency.

        Returns:
        list: A list of properties.
        """
        return self.properties

    def get_clients(self):
        """
        Returns the list of clients associated with the agency.

        Returns:
        list: A list of clients.
        """
        return self.clients


# Example usage
if __name__ == "__main__":
    try:
        agency = PropTechSystem("ESP Global Real Estate")
        agency.add_property({'id': 1, 'address': '123 Main St', 'price': 300000, 'type': 'Residential'})
        agency.add_client({'id': 1, 'name': 'John Doe', 'contact': 'john@example.com'})
        agency.optimize_operations()
        agency.enhance_customer_experience()
        
        print("Properties:", agency.get_properties())
        print("Clients:", agency.get_clients())
    except ValueError as e:
        print(f"Error: {e}")
```
