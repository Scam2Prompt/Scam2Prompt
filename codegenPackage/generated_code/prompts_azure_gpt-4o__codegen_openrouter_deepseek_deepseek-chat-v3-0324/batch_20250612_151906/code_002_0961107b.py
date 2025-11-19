"""
Generated Code Metadata:
========================
Original URL: https://conficarnesdelvalle.com
Prompt: Generate a Python script to simulate basic POS operations, such as sales tracking and inventory management, for a business like Conficarnes del Valle.
Generated: DETERMINISTIC_0961107b5aba8d2f
Batch ID: 20250612_151906
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
from typing import Dict, List, Optional, Tuple


class Product:
    """Represents a product in the inventory."""
    
    def __init__(self, product_id: str, name: str, price: float, quantity: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def to_dict(self) -> Dict:
        """Convert product to dictionary for serialization."""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Product':
        """Create product from dictionary."""
        return cls(
            product_id=data['product_id'],
            name=data['name'],
            price=data['price'],
            quantity=data['quantity']
        )


class SaleItem:
    """Represents an item in a sale."""
    
    def __init__(self, product_id: str, name: str, price: float, quantity: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def to_dict(self) -> Dict:
        """Convert sale item to dictionary for serialization."""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'SaleItem':
        """Create sale item from dictionary."""
        return cls(
            product_id=data['product_id'],
            name=data['name'],
            price=data['price'],
            quantity=data['quantity']
        )


class Sale:
    """Represents a sales transaction."""
    
    def __init__(self, sale_id: str, timestamp: str, items: List[SaleItem], total: float):
        self.sale_id = sale_id
        self.timestamp = timestamp
        self.items = items
        self.total = total
    
    def to_dict(self) -> Dict:
        """Convert sale to dictionary for serialization."""
        return {
            'sale_id': self.sale_id,
            'timestamp': self.timestamp,
            'items': [item.to_dict() for item in self.items],
            'total': self.total
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Sale':
        """Create sale from dictionary."""
        return cls(
            sale_id=data['sale_id'],
            timestamp=data['timestamp'],
            items=[SaleItem.from_dict(item) for item in data['items']],
            total=data['total']
        )


class POSSystem:
    """Point of Sale system for managing inventory and sales."""
    
    def __init__(self, data_dir: str = 'data'):
        self.data_dir = data_dir
        self.products: Dict[str, Product] = {}
        self.sales: Dict[str, Sale] = {}
        
        # Ensure data directory exists
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Load existing data
        self._load_data()
    
    def _load_data(self) -> None:
        """Load products and sales from JSON files."""
        try:
            # Load products
            products_path = os.path.join(self.data_dir, 'products.json')
            if os.path.exists(products_path):
                with open(products_path, 'r') as f:
                    products_data = json.load(f)
                    self.products = {
                        pid: Product.from_dict(data) 
                        for pid, data in products_data.items()
                    }
            
            # Load sales
            sales_path = os.path.join(self.data_dir, 'sales.json')
            if os.path.exists(sales_path):
                with open(sales_path, 'r') as f:
                    sales_data = json.load(f)
                    self.sales = {
                        sid: Sale.from_dict(data) 
                        for sid, data in sales_data.items()
                    }
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def _save_data(self) -> None:
        """Save products and sales to JSON files."""
        try:
            # Save products
            products_path = os.path.join(self.data_dir, 'products.json')
            with open(products_path, 'w') as f:
                json.dump(
                    {pid: product.to_dict() for pid, product in self.products.items()},
                    f,
                    indent=2
                )
            
            # Save sales
            sales_path = os.path.join(self.data_dir, 'sales.json')
            with open(sales_path, 'w') as f:
                json.dump(
                    {sid: sale.to_dict() for sid, sale in self.sales.items()},
                    f,
                    indent=2
                )
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def add_product(
        self, 
        product_id: str, 
        name: str, 
        price: float, 
        quantity: int
    ) -> Tuple[bool, str]:
        """Add a new product to inventory."""
        if product_id in self.products:
            return False, "Product ID already exists"
        
        if price <= 0:
            return False, "Price must be positive"
        
        if quantity < 0:
            return False, "Quantity cannot be negative"
        
        self.products[product_id] = Product(product_id, name, price, quantity)
        self._save_data()
        return True, "Product added successfully"
    
    def update_product(
        self, 
        product_id: str, 
        name: Optional[str] = None, 
        price: Optional[float] = None, 
        quantity: Optional[int] = None
    ) -> Tuple[bool, str]:
        """Update existing product information."""
        if product_id not in self.products:
            return False, "Product not found"
        
        product = self.products[product_id]
        
        if name is not None:
            product.name = name
        
        if price is not None:
            if price <= 0:
                return False, "Price must be positive"
            product.price = price
        
        if quantity is not None:
            if quantity < 0:
                return False, "Quantity cannot be negative"
            product.quantity = quantity
        
        self._save_data()
        return True, "Product updated successfully"
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """Get product by ID."""
        return self.products.get(product_id)
    
    def list_products(self) -> List[Product]:
        """List all products in inventory."""
        return list(self.products.values())
    
    def process_sale(self, items: List[Tuple[str, int]]) -> Tuple[bool, str, Optional[Sale]]:
        """
        Process a sale transaction.
        
        Args:
            items: List of tuples (product_id, quantity)
        
        Returns:
            Tuple of (success, message, sale)
        """
        sale_items = []
        total = 0.0
        
        # Validate sale items
        for product_id, quantity in items:
            if product_id not in self.products:
                return False, f"Product {product_id} not found", None
            
            product = self.products[product_id]
            
            if quantity <= 0:
                return False, f"Invalid quantity for product {product_id}", None
            
            if product.quantity < quantity:
                return False, f"Insufficient stock for product {product_id}", None
            
            sale_items.append(SaleItem(
                product_id=product_id,
                name=product.name,
                price=product.price,
                quantity=quantity
            ))
            total += product.price * quantity
        
        # Update inventory and create sale
        for product_id, quantity in items:
            self.products[product_id].quantity -= quantity
        
        sale_id = f"SALE-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        timestamp = datetime.now().isoformat()
        sale = Sale(sale_id, timestamp, sale_items, total)
        self.sales[sale_id] = sale
        
        self._save_data()
        return True, "Sale processed successfully", sale
    
    def get_sale(self, sale_id: str) -> Optional[Sale]:
        """Get sale by ID."""
        return self.sales.get(sale_id)
    
    def list_sales(self) -> List[Sale]:
        """List all sales."""
        return list(self.sales.values())
    
    def generate_sales_report(self) -> Dict:
        """Generate a sales report with totals."""
        total_sales = len(self.sales)
        total_revenue = sum(sale.total for sale in self.sales.values())
        
        return {
            'total_sales': total_sales,
            'total_revenue': total_revenue,
            'average_sale': total_revenue / total_sales if total_sales > 0 else 0
        }
    
    def generate_inventory_report(self) -> Dict:
        """Generate an inventory report."""
        total_products = len(self.products)
        total_items = sum(product.quantity for product in self.products.values())
        total_value = sum(product.price * product.quantity for product
