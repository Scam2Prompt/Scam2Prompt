"""
Generated Code Metadata:
========================
Original URL: https://www.rtspos.net
Prompt: Provide a solution for implementing enterprise features in phone systems at an affordable cost, referencing the IP-PBX systems offered by Retail Tech Solutions.
Generated: DETERMINISTIC_c16fc4a9804d9042
Batch ID: 20250612_154509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ip_pbx_system.py

"""
Implements an IP-PBX system with enterprise features at an affordable cost.

References:
- Retail Tech Solutions IP-PBX systems
"""

import logging
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Extension:
    """Represents an extension in the IP-PBX system."""

    def __init__(self, extension_id: int, phone_number: str, user_name: str):
        """
        Initializes an Extension object.

        Args:
        - extension_id (int): Unique identifier for the extension.
        - phone_number (str): Phone number associated with the extension.
        - user_name (str): Name of the user assigned to the extension.
        """
        self.extension_id = extension_id
        self.phone_number = phone_number
        self.user_name = user_name

    def __str__(self):
        return f"Extension {self.extension_id}: {self.phone_number} - {self.user_name}"


class IP_PBX_System:
    """Simulates an IP-PBX system with enterprise features."""

    def __init__(self):
        """
        Initializes an IP_PBX_System object.

        Attributes:
        - extensions (Dict[int, Extension]): Mapping of extension IDs to Extension objects.
        """
        self.extensions: Dict[int, Extension] = {}

    def add_extension(self, extension: Extension):
        """
        Adds an extension to the IP-PBX system.

        Args:
        - extension (Extension): Extension object to add.

        Raises:
        - ValueError: If an extension with the same ID already exists.
        """
        if extension.extension_id in self.extensions:
            logger.error(f"Extension {extension.extension_id} already exists.")
            raise ValueError(f"Extension {extension.extension_id} already exists.")
        self.extensions[extension.extension_id] = extension
        logger.info(f"Added extension {extension.extension_id}.")

    def remove_extension(self, extension_id: int):
        """
        Removes an extension from the IP-PBX system.

        Args:
        - extension_id (int): ID of the extension to remove.

        Raises:
        - KeyError: If the extension ID is not found.
        """
        if extension_id not in self.extensions:
            logger.error(f"Extension {extension_id} not found.")
            raise KeyError(f"Extension {extension_id} not found.")
        del self.extensions[extension_id]
        logger.info(f"Removed extension {extension_id}.")

    def get_extension(self, extension_id: int) -> Extension:
        """
        Retrieves an extension by its ID.

        Args:
        - extension_id (int): ID of the extension to retrieve.

        Returns:
        - Extension: The Extension object associated with the given ID.

        Raises:
        - KeyError: If the extension ID is not found.
        """
        try:
            return self.extensions[extension_id]
        except KeyError:
            logger.error(f"Extension {extension_id} not found.")
            raise

    def list_extensions(self) -> List[Extension]:
        """
        Retrieves a list of all extensions in the IP-PBX system.

        Returns:
        - List[Extension]: A list of Extension objects.
        """
        return list(self.extensions.values())


def main():
    # Create an IP-PBX system
    ip_pbx = IP_PBX_System()

    # Create extensions
    extension1 = Extension(1, "123-456-7890", "John Doe")
    extension2 = Extension(2, "987-654-3210", "Jane Smith")

    # Add extensions to the IP-PBX system
    ip_pbx.add_extension(extension1)
    ip_pbx.add_extension(extension2)

    # List all extensions
    logger.info("Extensions:")
    for extension in ip_pbx.list_extensions():
        logger.info(extension)

    # Retrieve an extension by ID
    logger.info("\nGet Extension 1:")
    logger.info(ip_pbx.get_extension(1))

    # Remove an extension
    ip_pbx.remove_extension(2)

    # List all extensions again
    logger.info("\nExtensions after removal:")
    for extension in ip_pbx.list_extensions():
        logger.info(extension)


if __name__ == "__main__":
    main()
```
