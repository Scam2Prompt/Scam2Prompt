"""
Generated Code Metadata:
========================
Original URL: https://longhuigolf.com
Prompt: Write a code snippet that automates the selection and ordering process for PU golf grips based on the workflow provided by Longhui Golf.
Generated: DETERMINISTIC_39410fd824547958
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class GolfGripSelector:
    """
    Automates the selection and ordering process for PU golf grips based on Longhui Golf's workflow.
    """

    def __init__(self, grip_catalog_file: str = "grip_catalog.json"):
        """
        Initialize the selector with grip catalog data.
        
        Args:
            grip_catalog_file: Path to JSON file containing grip catalog data
        """
        try:
            with open(grip_catalog_file, 'r') as f:
                self.grip_catalog = json.load(f)
        except FileNotFoundError:
            raise ValueError(f"Grip catalog file {grip_catalog_file} not found")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in grip catalog file {grip_catalog_file}")

    def get_available_grips(self) -> List[Dict]:
        """
        Returns list of all available grips with their properties.
        
        Returns:
            List of grip dictionaries with properties
        """
        return self.grip_catalog.get('grips', [])

    def filter_grips(self, 
                    grip_type: Optional[str] = None,
                    size: Optional[str] = None,
                    color: Optional[str] = None,
                    texture: Optional[str] = None) -> List[Dict]:
        """
        Filters grips based on specified criteria.
        
        Args:
            grip_type: Type of grip (e.g., 'putter', 'iron')
            size: Grip size (e.g., 'standard', 'midsize')
            color: Grip color
            texture: Grip texture
            
        Returns:
            List of filtered grip dictionaries
        """
        grips = self.get_available_grips()
        
        filtered = []
        for grip in grips:
            if grip_type and grip['type'].lower() != grip_type.lower():
                continue
            if size and grip['size'].lower() != size.lower():
                continue
            if color and grip['color'].lower() != color.lower():
                continue
            if texture and grip['texture'].lower() != texture.lower():
                continue
            filtered.append(grip)
            
        return filtered

    def create_order(self, grip_id: str, quantity: int, customer_info: Dict) -> Dict:
        """
        Creates an order for specified grips.
        
        Args:
            grip_id: ID of the grip to order
            quantity: Number of grips to order
            customer_info: Dictionary containing customer information
            
        Returns:
            Order confirmation dictionary
            
        Raises:
            ValueError: If grip not found or invalid quantity
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        grip = next((g for g in self.get_available_grips() if g['id'] == grip_id), None)
        if not grip:
            raise ValueError(f"Grip with ID {grip_id} not found")
            
        if quantity > grip.get('stock', 0):
            raise ValueError(f"Insufficient stock for grip {grip_id}")
            
        order = {
            'order_id': self._generate_order_id(),
            'grip_id': grip_id,
            'grip_name': grip['name'],
            'quantity': quantity,
            'unit_price': grip['price'],
            'total_price': grip['price'] * quantity,
            'customer_info': customer_info,
            'status': 'pending'
        }
        
        return order

    def _generate_order_id(self) -> str:
        """Generates a unique order ID."""
        import uuid
        return f"ORD-{uuid.uuid4().hex[:8].upper()}"

# Example usage
if __name__ == "__main__":
    try:
        selector = GolfGripSelector()
        
        # Get available grips
        print("Available grips:", selector.get_available_grips())
        
        # Filter grips
        filtered = selector.filter_grips(grip_type='iron', size='standard')
        print("Filtered grips:", filtered)
        
        # Create order
        if filtered:
            order = selector.create_order(
                grip_id=filtered[0]['id'],
                quantity=5,
                customer_info={
                    'name': 'John Doe',
                    'email': 'john@example.com',
                    'shipping_address': '123 Main St'
                }
            )
            print("Order created:", order)
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
