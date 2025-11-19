"""
Generated Code Metadata:
========================
Original URL: https://www.olgon.net
Prompt: Write a program to automate the hiring of farm machinery and supply of certified farm inputs, aligning with Olgon Prime Resources Ltd.'s Input Supply and Tractor Hiring Services.
Generated: DETERMINISTIC_7d7009c34cd0b067
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Dict, List, Optional, Tuple

class FarmInput:
    """Class representing a certified farm input."""
    
    def __init__(self, input_id: str, name: str, category: str, price: float, quantity: int):
        """
        Initialize a farm input.
        
        Args:
            input_id: Unique identifier for the input
            name: Name of the input
            category: Category of input (e.g., seeds, fertilizers)
            price: Price per unit
            quantity: Available quantity in stock
        """
        self.input_id = input_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
    
    def to_dict(self) -> Dict:
        """Convert farm input to dictionary for storage."""
        return {
            'input_id': self.input_id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'quantity': self.quantity
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'FarmInput':
        """Create FarmInput from dictionary."""
        return cls(
            input_id=data['input_id'],
            name=data['name'],
            category=data['category'],
            price=data['price'],
            quantity=data['quantity']
        )

class Machinery:
    """Class representing farm machinery available for hire."""
    
    def __init__(self, machinery_id: str, name: str, category: str, rate_per_hour: float, available: bool = True):
        """
        Initialize farm machinery.
        
        Args:
            machinery_id: Unique identifier for the machinery
            name: Name of the machinery
            category: Category of machinery
            rate_per_hour: Hiring rate per hour
            available: Availability status
        """
        self.machinery_id = machinery_id
        self.name = name
        self.category = category
        self.rate_per_hour = rate_per_hour
        self.available = available
    
    def to_dict(self) -> Dict:
        """Convert machinery to dictionary for storage."""
        return {
            'machinery_id': self.machinery_id,
            'name': self.name,
            'category': self.category,
            'rate_per_hour': self.rate_per_hour,
            'available': self.available
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Machinery':
        """Create Machinery from dictionary."""
        return cls(
            machinery_id=data['machinery_id'],
            name=data['name'],
            category=data['category'],
            rate_per_hour=data['rate_per_hour'],
            available=data['available']
        )

class Order:
    """Class representing an order for farm inputs or machinery."""
    
    def __init__(self, order_id: str, customer_id: str, items: List[Dict], order_type: str, 
                 total_amount: float, status: str = 'pending', order_date: Optional[str] = None):
        """
        Initialize an order.
        
        Args:
            order_id: Unique order identifier
            customer_id: Customer identifier
            items: List of items in order
            order_type: Type of order ('input' or 'machinery')
            total_amount: Total order amount
            status: Order status (pending, completed, cancelled)
            order_date: Date of order (defaults to current date)
        """
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = items
        self.order_type = order_type
        self.total_amount = total_amount
        self.status = status
        self.order_date = order_date or datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    def to_dict(self) -> Dict:
        """Convert order to dictionary for storage."""
        return {
            'order_id': self.order_id,
            'customer_id': self.customer_id,
            'items': self.items,
            'order_type': self.order_type,
            'total_amount': self.total_amount,
            'status': self.status,
            'order_date': self.order_date
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Order':
        """Create Order from dictionary."""
        return cls(
            order_id=data['order_id'],
            customer_id=data['customer_id'],
            items=data['items'],
            order_type=data['order_type'],
            total_amount=data['total_amount'],
            status=data['status'],
            order_date=data['order_date']
        )

class FarmService:
    """Main class for managing farm inputs and machinery hiring."""
    
    def __init__(self, storage_dir: str = 'data'):
        """
        Initialize the farm service.
        
        Args:
            storage_dir: Directory to store data files
        """
        self.storage_dir = storage_dir
        os.makedirs(storage_dir, exist_ok=True)
        
        # Initialize data structures
        self.inputs: Dict[str, FarmInput] = {}
        self.machineries: Dict[str, Machinery] = {}
        self.orders: Dict[str, Order] = {}
        
        # Load existing data
        self._load_data()
    
    def _load_data(self) -> None:
        """Load data from storage files."""
        try:
            # Load farm inputs
            inputs_path = os.path.join(self.storage_dir, 'inputs.json')
            if os.path.exists(inputs_path):
                with open(inputs_path, 'r') as f:
                    inputs_data = json.load(f)
                    self.inputs = {k: FarmInput.from_dict(v) for k, v in inputs_data.items()}
            
            # Load machineries
            machineries_path = os.path.join(self.storage_dir, 'machineries.json')
            if os.path.exists(machineries_path):
                with open(machineries_path, 'r') as f:
                    machineries_data = json.load(f)
                    self.machineries = {k: Machinery.from_dict(v) for k, v in machineries_data.items()}
            
            # Load orders
            orders_path = os.path.join(self.storage_dir, 'orders.json')
            if os.path.exists(orders_path):
                with open(orders_path, 'r') as f:
                    orders_data = json.load(f)
                    self.orders = {k: Order.from_dict(v) for k, v in orders_data.items()}
                    
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def _save_data(self) -> None:
        """Save data to storage files."""
        try:
            # Save farm inputs
            inputs_path = os.path.join(self.storage_dir, 'inputs.json')
            with open(inputs_path, 'w') as f:
                json.dump({k: v.to_dict() for k, v in self.inputs.items()}, f, indent=2)
            
            # Save machineries
            machineries_path = os.path.join(self.storage_dir, 'machineries.json')
            with open(machineries_path, 'w') as f:
                json.dump({k: v.to_dict() for k, v in self.machineries.items()}, f, indent=2)
            
            # Save orders
            orders_path = os.path.join(self.storage_dir, 'orders.json')
            with open(orders_path, 'w') as f:
                json.dump({k: v.to_dict() for k, v in self.orders.items()}, f, indent=2)
                
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def add_farm_input(self, input_id: str, name: str, category: str, price: float, quantity: int) -> bool:
        """
        Add a new farm input to inventory.
        
        Args:
            input_id: Unique identifier for the input
            name: Name of the input
            category: Category of input
            price: Price per unit
            quantity: Initial quantity
            
        Returns:
            bool: True if successful, False otherwise
        """
        if input_id in self.inputs:
            print(f"Input with ID {input_id} already exists.")
            return False
        
        self.inputs[input_id] = FarmInput(input_id, name, category, price, quantity)
        self._save_data()
        return True
    
    def update_farm_input_quantity(self, input_id: str, quantity: int) -> bool:
        """
        Update the quantity of a farm input.
        
        Args:
            input_id: ID of the input to update
            quantity: New quantity (positive to add, negative to subtract)
            
        Returns:
            bool: True if successful, False otherwise
        """
        if input_id not in self.inputs:
            print(f"Input with ID {input_id} not found.")
            return False
        
        new_quantity = self.inputs[input_id].quantity + quantity
        if new_quantity < 0:
            print("Cannot have negative quantity.")
            return False
        
        self.inputs[input_id].quantity = new_quantity
        self._save_data()
        return True
    
    def add_machinery(self, machinery_id: str, name: str, category: str, rate_per_hour: float) -> bool:
        """
        Add new machinery to inventory.
        
        Args:
            machinery_id: Unique identifier for the machinery
