"""
Generated Code Metadata:
========================
Original URL: https://cakco.com
Prompt: Generate a code snippet for a shopping cart system that includes features for selecting multiple variants of trendy bags, as described on the Cakco website.
Generated: DETERMINISTIC_7750aaeebc794778
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from typing import List, Optional
import uuid

@dataclass
class BagVariant:
    """Represents a variant of a bag product."""
    id: str
    color: str
    size: str
    material: str
    price: float
    stock: int

@dataclass
class BagItem:
    """Represents an item in the shopping cart."""
    product_id: str
    name: str
    variants: List[BagVariant]
    quantity: int
    selected_variants: List[str]  # List of variant IDs

class ShoppingCart:
    """Shopping cart system for trendy bags with variant selection."""
    
    def __init__(self):
        self.items: List[BagItem] = []
        self.cart_id = str(uuid.uuid4())
    
    def add_item(
        self,
        product_id: str,
        name: str,
        variants: List[BagVariant],
        selected_variants: List[str],
        quantity: int = 1
    ) -> None:
        """Add an item to the cart with selected variants.
        
        Args:
            product_id: Unique identifier for the product
            name: Name of the product
            variants: List of available variants
            selected_variants: List of variant IDs to add
            quantity: Quantity to add (default: 1)
            
        Raises:
            ValueError: If variant is not available or out of stock
        """
        # Validate selected variants
        available_variant_ids = {v.id for v in variants}
        for variant_id in selected_variants:
            if variant_id not in available_variant_ids:
                raise ValueError(f"Variant {variant_id} not available")
            
            variant = next(v for v in variants if v.id == variant_id)
            if variant.stock < quantity:
                raise ValueError(f"Not enough stock for variant {variant_id}")
        
        # Check if item with same variants already exists in cart
        existing_item = next(
            (item for item in self.items 
             if item.product_id == product_id 
             and set(item.selected_variants) == set(selected_variants)),
            None
        )
        
        if existing_item:
            existing_item.quantity += quantity
        else:
            self.items.append(
                BagItem(
                    product_id=product_id,
                    name=name,
                    variants=variants,
                    selected_variants=selected_variants,
                    quantity=quantity
                )
            )
    
    def remove_item(self, product_id: str, variant_ids: List[str]) -> None:
        """Remove an item from the cart based on product ID and variants.
        
        Args:
            product_id: Product ID to remove
            variant_ids: List of variant IDs to match
        """
        self.items = [
            item for item in self.items 
            if not (item.product_id == product_id 
                   and set(item.selected_variants) == set(variant_ids))
        ]
    
    def update_quantity(
        self, 
        product_id: str, 
        variant_ids: List[str], 
        new_quantity: int
    ) -> None:
        """Update the quantity of a cart item.
        
        Args:
            product_id: Product ID to update
            variant_ids: List of variant IDs to match
            new_quantity: New quantity to set
            
        Raises:
            ValueError: If item not found or invalid quantity
        """
        if new_quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        item = next(
            (item for item in self.items 
             if item.product_id == product_id 
             and set(item.selected_variants) == set(variant_ids)),
            None
        )
        
        if not item:
            raise ValueError("Item not found in cart")
            
        # Check stock for all variants
        for variant_id in variant_ids:
            variant = next(v for v in item.variants if v.id == variant_id)
            if variant.stock < new_quantity:
                raise ValueError(f"Not enough stock for variant {variant_id}")
        
        item.quantity = new_quantity
    
    def get_total(self) -> float:
        """Calculate the total price of all items in the cart."""
        total = 0.0
        for item in self.items:
            for variant_id in item.selected_variants:
                variant = next(v for v in item.variants if v.id == variant_id)
                total += variant.price * item.quantity
        return total
    
    def clear(self) -> None:
        """Clear all items from the cart."""
        self.items = []
    
    def get_item_count(self) -> int:
        """Get the total number of items in the cart (sum of quantities)."""
        return sum(item.quantity for item in self.items)
    
    def get_unique_item_count(self) -> int:
        """Get the count of unique items in the cart."""
        return len(self.items)
```
