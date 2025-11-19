"""
Generated Code Metadata:
========================
Original URL: https://fmt.co.id
Prompt: Write a Python code to manage inventory of construction machinery attachments like Hydraulic Breaker, Earth Auger Drill, and Pile Driver.
Generated: DETERMINISTIC_20b80d14bf1cb55d
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_machinery_attachments.py

from enum import Enum
from typing import Dict, List

class AttachmentType(str, Enum):
    """Enum for construction machinery attachment types."""
    HYDRAULIC_BREAKER = "Hydraulic Breaker"
    EARTH_AUGER_DRILL = "Earth Auger Drill"
    PILE_DRIVER = "Pile Driver"

class ConstructionMachineryAttachment:
    """Class representing a construction machinery attachment."""

    def __init__(self, 
                 attachment_id: int, 
                 attachment_type: AttachmentType, 
                 description: str, 
                 quantity: int, 
                 status: str = "Available"):
        """
        Initialize a construction machinery attachment.

        Args:
        - attachment_id (int): Unique ID for the attachment.
        - attachment_type (AttachmentType): Type of the attachment.
        - description (str): Description of the attachment.
        - quantity (int): Quantity of the attachment in stock.
        - status (str): Status of the attachment (default: "Available").
        """
        self.attachment_id = attachment_id
        self.attachment_type = attachment_type
        self.description = description
        self.quantity = quantity
        self.status = status

    def __str__(self):
        return f"Attachment ID: {self.attachment_id}, Type: {self.attachment_type.value}, Description: {self.description}, Quantity: {self.quantity}, Status: {self.status}"

class Inventory:
    """Class representing the inventory of construction machinery attachments."""

    def __init__(self):
        """Initialize an empty inventory."""
        self.attachments: Dict[int, ConstructionMachineryAttachment] = {}

    def add_attachment(self, attachment: ConstructionMachineryAttachment):
        """
        Add a construction machinery attachment to the inventory.

        Args:
        - attachment (ConstructionMachineryAttachment): Attachment to add.

        Raises:
        - ValueError: If an attachment with the same ID already exists.
        """
        if attachment.attachment_id in self.attachments:
            raise ValueError("Attachment with the same ID already exists.")
        self.attachments[attachment.attachment_id] = attachment

    def remove_attachment(self, attachment_id: int):
        """
        Remove a construction machinery attachment from the inventory.

        Args:
        - attachment_id (int): ID of the attachment to remove.

        Raises:
        - KeyError: If the attachment ID does not exist in the inventory.
        """
        if attachment_id not in self.attachments:
            raise KeyError("Attachment ID does not exist in the inventory.")
        del self.attachments[attachment_id]

    def update_quantity(self, attachment_id: int, new_quantity: int):
        """
        Update the quantity of a construction machinery attachment.

        Args:
        - attachment_id (int): ID of the attachment to update.
        - new_quantity (int): New quantity of the attachment.

        Raises:
        - KeyError: If the attachment ID does not exist in the inventory.
        - ValueError: If the new quantity is negative.
        """
        if attachment_id not in self.attachments:
            raise KeyError("Attachment ID does not exist in the inventory.")
        if new_quantity < 0:
            raise ValueError("New quantity cannot be negative.")
        self.attachments[attachment_id].quantity = new_quantity

    def get_attachment(self, attachment_id: int) -> ConstructionMachineryAttachment:
        """
        Get a construction machinery attachment by ID.

        Args:
        - attachment_id (int): ID of the attachment to retrieve.

        Returns:
        - ConstructionMachineryAttachment: The attachment with the specified ID.

        Raises:
        - KeyError: If the attachment ID does not exist in the inventory.
        """
        if attachment_id not in self.attachments:
            raise KeyError("Attachment ID does not exist in the inventory.")
        return self.attachments[attachment_id]

    def list_attachments(self) -> List[ConstructionMachineryAttachment]:
        """Return a list of all attachments in the inventory."""
        return list(self.attachments.values())

def main():
    # Create an inventory
    inventory = Inventory()

    # Create attachments
    hydraulic_breaker = ConstructionMachineryAttachment(1, AttachmentType.HYDRAULIC_BREAKER, "Heavy-duty hydraulic breaker", 5)
    earth_auger_drill = ConstructionMachineryAttachment(2, AttachmentType.EARTH_AUGER_DRILL, "Earth auger drill for excavators", 3)
    pile_driver = ConstructionMachineryAttachment(3, AttachmentType.PILE_DRIVER, "Pile driver for construction sites", 2)

    # Add attachments to the inventory
    inventory.add_attachment(hydraulic_breaker)
    inventory.add_attachment(earth_auger_drill)
    inventory.add_attachment(pile_driver)

    # List all attachments
    print("Attachments in the inventory:")
    for attachment in inventory.list_attachments():
        print(attachment)

    # Update quantity of an attachment
    inventory.update_quantity(1, 10)
    print("\nUpdated quantity of Hydraulic Breaker:")
    print(inventory.get_attachment(1))

    # Remove an attachment
    inventory.remove_attachment(2)
    print("\nAttachments in the inventory after removal:")
    for attachment in inventory.list_attachments():
        print(attachment)

if __name__ == "__main__":
    main()
```
