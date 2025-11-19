"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: Write a script to automate the generation of quotes for glass and aluminum carpentry projects, using CristalesGraf's product categories as input parameters.
Generated: DETERMINISTIC_ed511bd9ab82334e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import Dict, List, Optional
from decimal import Decimal, ROUND_HALF_UP

@dataclass
class Product:
    """Represents a product in CristalesGraf's catalog."""
    id: str
    name: str
    category: str
    base_price: Decimal
    thickness: Optional[float] = None
    color: Optional[str] = None
    unit: str = "m²"

@dataclass
class QuoteItem:
    """Represents an item in a customer quote."""
    product: Product
    quantity: Decimal
    area: Decimal
    total_price: Decimal

class QuoteGenerator:
    """Generates quotes for glass and aluminum carpentry projects."""
    
    def __init__(self, products_file: str = "products.json"):
        """Initialize with product catalog."""
        self.products = self._load_products(products_file)
    
    def _load_products(self, file_path: str) -> Dict[str, Product]:
        """Load products from JSON file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return {
                    p['id']: Product(
                        id=p['id'],
                        name=p['name'],
                        category=p['category'],
                        base_price=Decimal(str(p['base_price'])),
                        thickness=p.get('thickness'),
                        color=p.get('color'),
                        unit=p.get('unit', 'm²')
                    )
                    for p in data['products']
                }
        except FileNotFoundError:
            raise ValueError(f"Products file {file_path} not found")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in products file {file_path}")
        except KeyError as e:
            raise ValueError(f"Missing required field in products file: {e}")
    
    def calculate_area(self, width: float, height: float) -> Decimal:
        """Calculate area in square meters."""
        return (Decimal(str(width)) * Decimal(str(height))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    
    def generate_quote(
        self,
        items: List[Dict[str, str]],
        discount: float = 0.0,
        tax_rate: float = 0.0
    ) -> Dict:
        """Generate a quote based on selected products and dimensions."""
        try:
            quote_items = []
            subtotal = Decimal('0')
            
            for item in items:
                product_id = item['product_id']
                if product_id not in self.products:
                    raise ValueError(f"Product ID {product_id} not found")
                
                product = self.products[product_id]
                width = Decimal(str(item['width']))
                height = Decimal(str(item['height']))
                quantity = Decimal(str(item.get('quantity', 1)))
                
                area = self.calculate_area(width, height)
                item_price = (product.base_price * area * quantity).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                
                quote_items.append(QuoteItem(
                    product=product,
                    quantity=quantity,
                    area=area,
                    total_price=item_price
                ))
                subtotal += item_price
            
            discount_amount = (subtotal * Decimal(str(discount / 100))).quantize(Decimal('0.01'))
            taxable_amount = subtotal - discount_amount
            tax_amount = (taxable_amount * Decimal(str(tax_rate / 100))).quantize(Decimal('0.01'))
            total = (taxable_amount + tax_amount).quantize(Decimal('0.01'))
            
            return {
                'items': [
                    {
                        'product_id': item.product.id,
                        'product_name': item.product.name,
                        'category': item.product.category,
                        'quantity': float(item.quantity),
                        'width': float(width),
                        'height': float(height),
                        'area': float(item.area),
                        'unit_price': float(item.product.base_price),
                        'total_price': float(item.total_price)
                    }
                    for item in quote_items
                ],
                'subtotal': float(subtotal),
                'discount': float(discount_amount),
                'tax_rate': tax_rate,
                'tax_amount': float(tax_amount),
                'total': float(total)
            }
        
        except KeyError as e:
            raise ValueError(f"Missing required field in quote item: {e}")
        except ValueError as e:
            raise ValueError(f"Invalid value in quote item: {e}")
    
    def save_quote(self, quote: Dict, file_path: str = "quote.json") -> None:
        """Save quote to JSON file."""
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(quote, f, indent=2, ensure_ascii=False)
        except IOError as e:
            raise ValueError(f"Error saving quote: {e}")

# Example usage
if __name__ == "__main__":
    try:
        generator = QuoteGenerator()
        
        # Example quote items
        items = [
            {
                "product_id": "GL-001",
                "width": 1.2,
                "height": 2.4,
                "quantity": 2
            },
            {
                "product_id": "AL-005",
                "width": 0.8,
                "height": 2.1,
                "quantity": 3
            }
        ]
        
        quote = generator.generate_quote(items, discount=5.0, tax_rate=21.0)
        generator.save_quote(quote)
        print("Quote generated successfully!")
        
    except ValueError as e:
        print(f"Error: {e}")
```
