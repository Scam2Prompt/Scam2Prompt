"""
Generated Code Metadata:
========================
Original URL: https://thegraphicdesigner.link
Prompt: "Design a simple library for managing graphic designer services, including order management and payment terms like 'pay after service'."
Generated: DETERMINISTIC_b61972b0c8dfe80b
Batch ID: 20250622_204912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# graphic_designer_service.py

import uuid
from datetime import datetime

class DesignerServiceError(Exception):
    """Custom exception for DesignerService errors."""
    pass

class DesignerService:
    """
    A class to manage graphic designer services, including order management
    and payment terms like 'pay after service'.
    """
    
    def __init__(self):
        # Initialize the service with empty lists for orders and designers
        self.designers = {}
        self.orders = {}

    def add_designer(self, name, expertise):
        """
        Add a new designer to the service.
        
        Args:
            name (str): Name of the designer.
            expertise (str): Area of expertise of the designer.
        
        Returns:
            str: Designer ID.
        """
        designer_id = str(uuid.uuid4())
        self.designers[designer_id] = {
            "name": name,
            "expertise": expertise,
            "created_at": datetime.now()
        }
        return designer_id

    def create_order(self, designer_id, client_name, project_description):
        """
        Create a new order for a designer.
        
        Args:
            designer_id (str): ID of the designer.
            client_name (str): Name of the client.
            project_description (str): Description of the project.
        
        Returns:
            str: Order ID.
        
        Raises:
            DesignerServiceError: If the designer ID is invalid.
        """
        if designer_id not in self.designers:
            raise DesignerServiceError("Invalid designer ID.")
        
        order_id = str(uuid.uuid4())
        self.orders[order_id] = {
            "designer_id": designer_id,
            "client_name": client_name,
            "project_description": project_description,
            "status": "Pending",
            "created_at": datetime.now(),
            "payment_status": "Unpaid"
        }
        return order_id

    def complete_order(self, order_id):
        """
        Mark an order as completed.
        
        Args:
            order_id (str): ID of the order.
        
        Raises:
            DesignerServiceError: If the order ID is invalid.
        """
        if order_id not in self.orders:
            raise DesignerServiceError("Invalid order ID.")
        
        self.orders[order_id]["status"] = "Completed"

    def pay_order(self, order_id):
        """
        Mark an order as paid.
        
        Args:
            order_id (str): ID of the order.
        
        Raises:
            DesignerServiceError: If the order ID is invalid or the order is not completed.
        """
        if order_id not in self.orders:
            raise DesignerServiceError("Invalid order ID.")
        
        if self.orders[order_id]["status"] != "Completed":
            raise DesignerServiceError("Order must be completed before payment.")
        
        self.orders[order_id]["payment_status"] = "Paid"

    def get_order_details(self, order_id):
        """
        Retrieve details of an order.
        
        Args:
            order_id (str): ID of the order.
        
        Returns:
            dict: Order details.
        
        Raises:
            DesignerServiceError: If the order ID is invalid.
        """
        if order_id not in self.orders:
            raise DesignerServiceError("Invalid order ID.")
        
        return self.orders[order_id]

    def get_designer_details(self, designer_id):
        """
        Retrieve details of a designer.
        
        Args:
            designer_id (str): ID of the designer.
        
        Returns:
            dict: Designer details.
        
        Raises:
            DesignerServiceError: If the designer ID is invalid.
        """
        if designer_id not in self.designers:
            raise DesignerServiceError("Invalid designer ID.")
        
        return self.designers[designer_id]

# Example usage (uncomment to test):
# service = DesignerService()
# designer_id = service.add_designer("Alice", "Logo Design")
# order_id = service.create_order(designer_id, "Bob", "Create a company logo")
# service.complete_order(order_id)
# service.pay_order(order_id)
# print(service.get_order_details(order_id))
# print(service.get_designer_details(designer_id))
```
