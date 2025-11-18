"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.himsdemo.bste.live
Prompt: Provide an example of how to use `Utility.Client("clientName")` to display client-specific information in a Health Information Management System.
Generated: DETERMINISTIC_0baead24dfae39d9
Batch ID: 20250612_151504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Client:
    """Represents a client in the Health Information Management System."""
    
    def __init__(self, name, contact_info, medical_history):
        """Initializes a new client with the provided information.

        Args:
            name (str): The name of the client.
            contact_info (str): Contact information of the client.
            medical_history (dict): A dictionary of medical history records.
        """
        self.name = name
        self.contact_info = contact_info
        self.medical_history = medical_history

    def display_info(self):
        """Displays the client's information in a formatted manner."""
        print(f"Client Name: {self.name}")
        print(f"Contact Info: {self.contact_info}")
        print("Medical History:")
        for condition, details in self.medical_history.items():
            print(f"  - {condition}: {details}")

class Utility:
    """Utility class for managing clients."""

    clients = {
        "JohnDoe": Client("John Doe", "john@example.com", {"Diabetes": "Controlled", "Hypertension": "Uncontrolled"}),
        "JaneSmith": Client("Jane Smith", "jane@example.com", {"Asthma": "Mild", "Allergies": "Seasonal"})
    }

    @classmethod
    def Client(cls, client_name):
        """Retrieves a client by name and displays their information.

        Args:
            client_name (str): The name of the client to retrieve.

        Raises:
            ValueError: If the client does not exist in the system.
        """
        try:
            # Try to retrieve the client
            client = cls.clients[client_name]
            client.display_info()
        except KeyError:
            # Handle the case where the client is not found
            raise ValueError(f"Client '{client_name}' not found in the system.")


# Example usage
if __name__ == "__main__":
    # Specify the client name to display
    client_name = "JohnDoe"

    try:
        # Display the client's information
        Utility.Client(client_name)
    except ValueError as e:
        # Handle the error if the client is not found
        print(e)
```
