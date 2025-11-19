"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polyhedra-consulting.com
Prompt: What are the best practices for creating a client space in a polyhedral consulting application?
Generated: DETERMINISTIC_665df5a9bd021cb3
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Polyhedral Consulting Application: Client Space Management
This script defines the best practices for creating and managing client spaces
in a consulting application's backend. It follows industry standards for clean,
efficient, and secure Python code.
"""

import uuid  # Used for generating unique client identifiers
import logging  # Used for logging application events

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class ClientSpaceManager:
    """
    A class to manage client spaces in a polyhedral consulting application.
    """

    def __init__(self):
        """
        Initializes the ClientSpaceManager with an empty dictionary to store client spaces.
        """
        self.client_spaces = {}  # Dictionary to store client space data

    def create_client_space(self, client_name, client_email):
        """
        Creates a new client space in the system.

        Args:
            client_name (str): The name of the client.
            client_email (str): The email address of the client.

        Returns:
            dict: Contains the client ID and confirmation message.

        Raises:
            ValueError: If the client_name or client_email is missing or invalid.
        """
        # Input validation
        if not client_name or not isinstance(client_name, str):
            raise ValueError("Invalid client name. It must be a non-empty string.")
        if not client_email or "@" not in client_email:
            raise ValueError("Invalid client email. It must contain '@'.")

        # Generate a unique client ID
        client_id = str(uuid.uuid4())

        # Create the client space
        self.client_spaces[client_id] = {
            "name": client_name,
            "email": client_email,
            "created_at": datetime.now().isoformat()
        }

        # Log the creation event
        logging.info(f"Client space created successfully for {client_name} (ID: {client_id}).")

        return {
            "client_id": client_id,
            "message": "Client space created successfully."
        }

    def get_client_space(self, client_id):
        """
        Retrieves a client's space by their unique ID.

        Args:
            client_id (str): The unique identifier of the client.

        Returns:
            dict: The client space data.

        Raises:
            KeyError: If the client ID does not exist in the system.
        """
        if client_id not in self.client_spaces:
            logging.error(f"Client space not found for ID: {client_id}.")
            raise KeyError("Client ID does not exist.")

        return self.client_spaces[client_id]

    def delete_client_space(self, client_id):
        """
        Deletes a client's space from the system.

        Args:
            client_id (str): The unique identifier of the client.

        Returns:
            str: Confirmation message.

        Raises:
            KeyError: If the client ID does not exist in the system.
        """
        if client_id not in self.client_spaces:
            logging.error(f"Cannot delete. Client space not found for ID: {client_id}.")
            raise KeyError("Client ID does not exist.")

        # Remove the client space
        del self.client_spaces[client_id]

        # Log the deletion event
        logging.info(f"Client space deleted successfully for ID: {client_id}.")

        return "Client space deleted successfully."


# Example usage
if __name__ == "__main__":
    # Initialize the client space manager
    manager = ClientSpaceManager()
    
    # Create a new client space
    try:
        response = manager.create_client_space("John Doe", "john.doe@example.com")
        print(response)
    except ValueError as e:
        logging.error(f"Error creating client space: {e}")

    # Retrieve the client space
    try:
        client_id = response["client_id"]
        client_space = manager.get_client_space(client_id)
        print(client_space)
    except KeyError as e:
        logging.error(f"Error retrieving client space: {e}")

    # Delete the client space
    try:
        delete_message = manager.delete_client_space(client_id)
        print(delete_message)
    except KeyError as e:
        logging.error(f"Error deleting client space: {e}")
```
