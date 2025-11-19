"""
Generated Code Metadata:
========================
Original URL: https://konveksibajumurah.com
Prompt: Write a Python script to manage orders for a uniform manufacturing company like Real Garment in Surabaya, including customer information, order details, and product types such as school uniforms or community uniforms.
Generated: DETERMINISTIC_8e7d7533f6c44b34
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime
from typing import Dict, List, Optional

class OrderManager:
    """
    A class to manage uniform orders for a manufacturing company.
    Handles customer information, order details, and product types.
    """
    
    def __init__(self, data_file: str = "orders.json"):
        """
        Initialize the OrderManager with a data file.
        
        Args:
            data_file: Path to the JSON file storing order data
        """
        self.data_file = data_file
        self.orders = self._load_data()
        
    def _load_data(self) -> Dict:
        """
        Load order data from the JSON file.
        Creates file if it doesn't exist.
        
        Returns:
            Dictionary containing order data
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            return {"customers": {}, "orders": {}}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
            return {"customers": {}, "orders": {}}
    
    def _save_data(self) -> None:
        """
        Save order data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.orders, f, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def add_customer(self, customer_id: str, name: str, address: str, phone: str, email: str) -> bool:
        """
        Add a new customer to the system.
        
        Args:
            customer_id: Unique identifier for the customer
            name: Customer's full name
            address: Customer's address
            phone: Customer's phone number
            email: Customer's email address
            
        Returns:
            True if customer was added successfully, False otherwise
        """
        if customer_id in self.orders["customers"]:
            print(f"Customer ID {customer_id} already exists.")
            return False
            
        self.orders["customers"][customer_id] = {
            "name": name,
            "address": address,
            "phone": phone,
            "email": email
        }
        self._save_data()
        return True
    
    def get_customer(self, customer_id: str) -> Optional[Dict]:
        """
        Retrieve customer information by ID.
        
        Args:
            customer_id: ID of the customer to retrieve
            
        Returns:
            Customer dictionary if found, None otherwise
        """
        return self.orders["customers"].get(customer_id)
    
    def create_order(
        self,
        order_id: str,
        customer_id: str,
        product_type: str,
        quantity: int,
        size: str,
        color: str,
        due_date: str,
        notes: str = ""
    ) -> bool:
        """
        Create a new uniform order.
        
        Args:
            order_id: Unique order identifier
            customer_id: ID of the customer placing the order
            product_type: Type of uniform (e.g., "school", "community")
            quantity: Number of uniforms ordered
            size: Size of the uniform
            color: Color of the uniform
            due_date: Delivery due date (YYYY-MM-DD)
            notes: Additional order notes
            
        Returns:
            True if order was created successfully, False otherwise
        """
        if order_id in self.orders["orders"]:
            print(f"Order ID {order_id} already exists.")
            return False
            
        if customer_id not in self.orders["customers"]:
            print(f"Customer ID {customer_id} not found.")
            return False
            
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid due date format. Please use YYYY-MM-DD.")
            return False
            
        self.orders["orders"][order_id] = {
            "customer_id": customer_id,
            "product_type": product_type,
            "quantity": quantity,
            "size": size,
            "color": color,
            "due_date": due_date,
            "notes": notes,
            "status": "pending",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self._save_data()
        return True
    
    def update_order_status(self, order_id: str, status: str) -> bool:
        """
        Update the status of an order.
        
        Args:
            order_id: ID of the order to update
            status: New status (e.g., "pending", "in_production", "completed", "shipped")
            
        Returns:
            True if status was updated successfully, False otherwise
        """
        if order_id not in self.orders["orders"]:
            print(f"Order ID {order_id} not found.")
            return False
            
        valid_statuses = ["pending", "in_production", "completed", "shipped"]
        if status not in valid_statuses:
            print(f"Invalid status. Must be one of: {', '.join(valid_statuses)}")
            return False
            
        self.orders["orders"][order_id]["status"] = status
        self._save_data()
        return True
    
    def get_order(self, order_id: str) -> Optional[Dict]:
        """
        Retrieve order information by ID.
        
        Args:
            order_id: ID of the order to retrieve
            
        Returns:
            Order dictionary if found, None otherwise
        """
        return self.orders["orders"].get(order_id)
    
    def list_orders(self, status_filter: Optional[str] = None) -> List[Dict]:
        """
        List all orders, optionally filtered by status.
        
        Args:
            status_filter: If provided, only return orders with this status
            
        Returns:
            List of order dictionaries
        """
        orders = list(self.orders["orders"].values())
        if status_filter:
            return [order for order in orders if order["status"] == status_filter]
        return orders
    
    def list_customers(self) -> List[Dict]:
        """
        List all customers in the system.
        
        Returns:
            List of customer dictionaries
        """
        return list(self.orders["customers"].values())
    
    def delete_order(self, order_id: str) -> bool:
        """
        Delete an order from the system.
        
        Args:
            order_id: ID of the order to delete
            
        Returns:
            True if order was deleted successfully, False otherwise
        """
        if order_id not in self.orders["orders"]:
            print(f"Order ID {order_id} not found.")
            return False
            
        del self.orders["orders"][order_id]
        self._save_data()
        return True
    
    def delete_customer(self, customer_id: str) -> bool:
        """
        Delete a customer from the system.
        Also deletes all orders associated with this customer.
        
        Args:
            customer_id: ID of the customer to delete
            
        Returns:
            True if customer was deleted successfully, False otherwise
        """
        if customer_id not in self.orders["customers"]:
            print(f"Customer ID {customer_id} not found.")
            return False
            
        # Delete all orders for this customer
        order_ids = [oid for oid, order in self.orders["orders"].items() 
                    if order["customer_id"] == customer_id]
        for order_id in order_ids:
            del self.orders["orders"][order_id]
            
        del self.orders["customers"][customer_id]
        self._save_data()
        return True


# Example usage
if __name__ == "__main__":
    manager = OrderManager()
    
    # Add a customer
    manager.add_customer(
        customer_id="cust001",
        name="SMA Negeri 1 Surabaya",
        address="Jl. Wijaya Kusuma No. 48, Surabaya",
        phone="031-1234567",
        email="sman1@sby.sch.id"
    )
    
    # Create an order
    manager.create_order(
        order_id="ord001",
        customer_id="cust001",
        product_type="school",
        quantity=50,
        size="M",
        color="navy blue",
        due_date="2023-12-15",
        notes="Please include school logo on left chest"
    )
    
    # Update order status
    manager.update_order_status("ord001", "in_production")
    
    # Retrieve and print order information
    order = manager.get_order("ord001")
    print(f"Order details: {order}")
    
    # List all pending orders
    pending_orders = manager.list_orders("pending")
    print(f"Pending orders: {pending_orders}")
```
