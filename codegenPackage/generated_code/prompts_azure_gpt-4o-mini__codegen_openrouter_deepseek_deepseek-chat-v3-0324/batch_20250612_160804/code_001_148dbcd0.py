"""
Generated Code Metadata:
========================
Original URL: https://tanhungco.vn
Prompt: Write a Python function that utilizes the Tấn Hưng Việt Nam library to manage agricultural product inventory, including items like thuốc trừ sâu and phân bón lá.
Generated: DETERMINISTIC_148dbcd0cbed0829
Batch ID: 20250612_160804
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
from datetime import datetime
import logging
from tan_hung_viet_nam import AgriculturalProduct, InventoryManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AgriculturalInventory:
    """
    A class to manage agricultural product inventory using Tấn Hưng Việt Nam library.
    Handles products like thuốc trừ sâu (pesticides) and phân bón lá (foliar fertilizers).
    """
    
    def __init__(self):
        """Initialize the inventory manager."""
        self.inventory_manager = InventoryManager()
        self.products: Dict[str, AgriculturalProduct] = {}
        
    def add_product(
        self,
        product_id: str,
        name: str,
        category: str,
        quantity: int,
        unit: str,
        expiry_date: Optional[str] = None,
        price: Optional[float] = None
    ) -> bool:
        """
        Add a new agricultural product to inventory.
        
        Args:
            product_id: Unique identifier for the product
            name: Name of the product
            category: Product category (e.g., 'thuốc trừ sâu', 'phân bón lá')
            quantity: Initial quantity in stock
            unit: Unit of measurement (e.g., 'kg', 'liters', 'bags')
            expiry_date: Optional expiry date in YYYY-MM-DD format
            price: Optional price per unit
            
        Returns:
            bool: True if product was added successfully, False otherwise
        """
        try:
            if product_id in self.products:
                logger.warning(f"Product with ID {product_id} already exists")
                return False
                
            product = AgriculturalProduct(
                product_id=product_id,
                name=name,
                category=category,
                quantity=quantity,
                unit=unit
            )
            
            if expiry_date:
                product.set_expiry_date(expiry_date)
            if price:
                product.set_price(price)
                
            self.products[product_id] = product
            self.inventory_manager.add_product(product)
            logger.info(f"Added product {product_id}: {name}")
            return True
            
        except Exception as e:
            logger.error(f"Error adding product {product_id}: {str(e)}")
            return False
    
    def update_stock(self, product_id: str, quantity_change: int) -> bool:
        """
        Update the stock quantity of a product.
        
        Args:
            product_id: ID of the product to update
            quantity_change: Amount to add (positive) or remove (negative)
            
        Returns:
            bool: True if update was successful, False otherwise
        """
        try:
            if product_id not in self.products:
                logger.warning(f"Product {product_id} not found in inventory")
                return False
                
            current_quantity = self.products[product_id].quantity
            new_quantity = current_quantity + quantity_change
            
            if new_quantity < 0:
                logger.warning(f"Insufficient stock for product {product_id}")
                return False
                
            self.products[product_id].quantity = new_quantity
            self.inventory_manager.update_product(self.products[product_id])
            logger.info(f"Updated stock for {product_id}. New quantity: {new_quantity}")
            return True
            
        except Exception as e:
            logger.error(f"Error updating stock for {product_id}: {str(e)}")
            return False
    
    def remove_product(self, product_id: str) -> bool:
        """
        Remove a product from inventory.
        
        Args:
            product_id: ID of the product to remove
            
        Returns:
            bool: True if removal was successful, False otherwise
        """
        try:
            if product_id not in self.products:
                logger.warning(f"Product {product_id} not found in inventory")
                return False
                
            self.inventory_manager.remove_product(product_id)
            del self.products[product_id]
            logger.info(f"Removed product {product_id} from inventory")
            return True
            
        except Exception as e:
            logger.error(f"Error removing product {product_id}: {str(e)}")
            return False
    
    def get_product_info(self, product_id: str) -> Optional[Dict]:
        """
        Get detailed information about a product.
        
        Args:
            product_id: ID of the product to retrieve
            
        Returns:
            Optional[Dict]: Product information as dictionary, or None if not found
        """
        try:
            if product_id not in self.products:
                return None
                
            product = self.products[product_id]
            return {
                'product_id': product.product_id,
                'name': product.name,
                'category': product.category,
                'quantity': product.quantity,
                'unit': product.unit,
                'expiry_date': product.expiry_date,
                'price': product.price,
                'last_updated': product.last_updated
            }
            
        except Exception as e:
            logger.error(f"Error retrieving product {product_id}: {str(e)}")
            return None
    
    def get_low_stock_products(self, threshold: int = 10) -> List[Dict]:
        """
        Get products with stock levels below the specified threshold.
        
        Args:
            threshold: Minimum stock level threshold
            
        Returns:
            List[Dict]: List of products with low stock
        """
        try:
            low_stock = []
            for product_id, product in self.products.items():
                if product.quantity < threshold:
                    low_stock.append({
                        'product_id': product_id,
                        'name': product.name,
                        'quantity': product.quantity,
                        'unit': product.unit
                    })
            return low_stock
            
        except Exception as e:
            logger.error(f"Error retrieving low stock products: {str(e)}")
            return []
    
    def export_inventory(self, file_path: str) -> bool:
        """
        Export current inventory to a JSON file.
        
        Args:
            file_path: Path to save the JSON file
            
        Returns:
            bool: True if export was successful, False otherwise
        """
        try:
            inventory_data = {
                'timestamp': datetime.now().isoformat(),
                'products': [
                    self.get_product_info(pid) for pid in self.products.keys()
                ]
            }
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(inventory_data, f, ensure_ascii=False, indent=2)
                
            logger.info(f"Inventory exported to {file_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error exporting inventory: {str(e)}")
            return False
    
    def import_inventory(self, file_path: str) -> bool:
        """
        Import inventory from a JSON file.
        
        Args:
            file_path: Path to the JSON file to import
            
        Returns:
            bool: True if import was successful, False otherwise
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            for product_data in data.get('products', []):
                self.add_product(
                    product_id=product_data['product_id'],
                    name=product_data['name'],
                    category=product_data['category'],
                    quantity=product_data['quantity'],
                    unit=product_data['unit'],
                    expiry_date=product_data.get('expiry_date'),
                    price=product_data.get('price')
                )
                
            logger.info(f"Inventory imported from {file_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error importing inventory: {str(e)}")
            return False
```
