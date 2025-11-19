"""
Generated Code Metadata:
========================
Original URL: https://gesec.com.co
Prompt: Create a Python program to handle the treatment of personal data (Habeas Data) in compliance with privacy policies, referencing GESEC's approach to data management.
Generated: DETERMINISTIC_947ec2238ac22772
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# habeas_data_manager.py

"""
Module to handle personal data (Habeas Data) in compliance with privacy policies,
following GESEC's approach to data management.

Classes:
    PersonalData
    DataManager

Exceptions:
    DataAccessError
    DataUpdateError
    DataDeletionError
"""

import logging
from typing import Dict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataAccessError(Exception):
    """Raised when there's an issue accessing personal data."""
    pass

class DataUpdateError(Exception):
    """Raised when there's an issue updating personal data."""
    pass

class DataDeletionError(Exception):
    """Raised when there's an issue deleting personal data."""
    pass

class PersonalData:
    """
    Represents personal data.

    Attributes:
        id (str): Unique identifier for the data.
        name (str): Data subject's name.
        email (str): Data subject's email.
        data (Dict[str, str]): Additional data.
    """

    def __init__(self, id: str, name: str, email: str, data: Dict[str, str] = {}):
        self.id = id
        self.name = name
        self.email = email
        self.data = data

class DataManager:
    """
    Manages personal data.

    Attributes:
        data (Dict[str, PersonalData]): Stored personal data.
    """

    def __init__(self):
        self.data = {}

    def create(self, id: str, name: str, email: str, data: Dict[str, str] = {}):
        """
        Creates new personal data.

        Args:
            id (str): Unique identifier for the data.
            name (str): Data subject's name.
            email (str): Data subject's email.
            data (Dict[str, str], optional): Additional data. Defaults to {}.

        Raises:
            DataAccessError: If data with the given ID already exists.
        """
        if id in self.data:
            logger.error(f"Data with ID {id} already exists.")
            raise DataAccessError(f"Data with ID {id} already exists.")
        self.data[id] = PersonalData(id, name, email, data)
        logger.info(f"Data with ID {id} created.")

    def read(self, id: str) -> PersonalData:
        """
        Retrieves personal data by ID.

        Args:
            id (str): Unique identifier for the data.

        Returns:
            PersonalData: The personal data.

        Raises:
            DataAccessError: If data with the given ID does not exist.
        """
        try:
            return self.data[id]
        except KeyError:
            logger.error(f"Data with ID {id} does not exist.")
            raise DataAccessError(f"Data with ID {id} does not exist.")

    def update(self, id: str, name: str = None, email: str = None, data: Dict[str, str] = None):
        """
        Updates personal data.

        Args:
            id (str): Unique identifier for the data.
            name (str, optional): New data subject's name. Defaults to None.
            email (str, optional): New data subject's email. Defaults to None.
            data (Dict[str, str], optional): New additional data. Defaults to None.

        Raises:
            DataUpdateError: If there's an issue updating the data.
        """
        try:
            if name:
                self.data[id].name = name
            if email:
                self.data[id].email = email
            if data:
                self.data[id].data = data
            logger.info(f"Data with ID {id} updated.")
        except Exception as e:
            logger.error(f"Error updating data with ID {id}: {str(e)}")
            raise DataUpdateError(f"Error updating data with ID {id}: {str(e)}")

    def delete(self, id: str):
        """
        Deletes personal data.

        Args:
            id (str): Unique identifier for the data.

        Raises:
            DataDeletionError: If there's an issue deleting the data.
        """
        try:
            del self.data[id]
            logger.info(f"Data with ID {id} deleted.")
        except Exception as e:
            logger.error(f"Error deleting data with ID {id}: {str(e)}")
            raise DataDeletionError(f"Error deleting data with ID {id}: {str(e)}")

def main():
    # Example usage
    manager = DataManager()

    # Create personal data
    manager.create("1", "John Doe", "john@example.com", {"phone": "123456789"})

    # Read personal data
    data = manager.read("1")
    print(f"Name: {data.name}, Email: {data.email}, Data: {data.data}")

    # Update personal data
    manager.update("1", email="john2@example.com")

    # Delete personal data
    manager.delete("1")

if __name__ == "__main__":
    main()
```
