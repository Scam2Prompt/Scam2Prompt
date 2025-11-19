"""
Generated Code Metadata:
========================
Original URL: https://distribution-pieces-service.fr
Prompt: Develop a code snippet for handling customer inquiries and generating quotes for automotive parts, including "essuie glace" and "produits d'entretiens," as described on the Distribution Pièces Service website.
Generated: DETERMINISTIC_358baa08954cac34
Batch ID: 20250612_151752
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
from enum import Enum

class PartCategory(Enum):
    WIPER = "essuie glace"
    MAINTENANCE = "produits d'entretien"
    OTHER = "autre"

@dataclass
class Part:
    id: str
    name: str
    category: PartCategory
    price: float
    stock: int
    description: Optional[str] = None

@dataclass
class Customer:
    id: str
    name: str
    email: str
    phone: str

class QuoteGenerator:
    def __init__(self, parts_db: Dict[str, Part], customers_db: Dict[str, Customer]):
        self.parts_db = parts_db
        self.customers_db = customers_db
    
    def get_part_by_id(self, part_id: str) -> Optional[Part]:
        """Retrieve a part by its ID."""
        return self.parts_db.get(part_id)
    
    def get_customer_by_id(self, customer_id: str) -> Optional[Customer]:
        """Retrieve a customer by their ID."""
        return self.customers_db.get(customer_id)
    
    def search_parts(self, query: str, category: Optional[PartCategory] = None) -> List[Part]:
        """Search parts by name or description with optional category filter."""
        results = []
        query = query.lower()
        for part in self.parts_db.values():
            if (query in part.name.lower() or 
                (part.description and query in part.description.lower())):
                if category is None or part.category == category:
                    results.append(part)
        return results
    
    def generate_quote(self, customer_id: str, part_quantities: Dict[str, int]) -> Dict:
        """Generate a quote for a customer with specified parts and quantities."""
        customer = self.get_customer_by_id(customer_id)
        if not customer:
            raise ValueError("Customer not found")
        
        quote_items = []
        total = 0.0
        
        for part_id, quantity in part_quantities.items():
            part = self.get_part_by_id(part_id)
            if not part:
                raise ValueError(f"Part {part_id} not found")
            if quantity <= 0:
                raise ValueError(f"Invalid quantity for part {part_id}")
            if part.stock < quantity:
                raise ValueError(f"Insufficient stock for part {part_id}")
            
            item_total = part.price * quantity
            quote_items.append({
                "part_id": part.id,
                "name": part.name,
                "quantity": quantity,
                "unit_price": part.price,
                "total": item_total
            })
            total += item_total
        
        return {
            "customer_id": customer.id,
            "customer_name": customer.name,
            "items": quote_items,
            "total": total,
            "currency": "EUR"
        }
    
    def save_quote_to_file(self, quote: Dict, filename: str) -> None:
        """Save quote to a JSON file."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(quote, f, indent=2, ensure_ascii=False)
        except IOError as e:
            raise IOError(f"Failed to save quote: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Sample data initialization
    parts_db = {
        "WG001": Part(
            id="WG001",
            name="Essuie-glace avant droit",
            category=PartCategory.WIPER,
            price=12.99,
            stock=50,
            description="Essuie-glace premium pour voitures européennes"
        ),
        "MT001": Part(
            id="MT001",
            name="Liquide de frein",
            category=PartCategory.MAINTENANCE,
            price=8.50,
            stock=100,
            description="Liquide de frein DOT4 500ml"
        )
    }
    
    customers_db = {
        "CUST001": Customer(
            id="CUST001",
            name="Auto Service Marseille",
            email="contact@autoservice-mrs.com",
            phone="+33491234567"
        )
    }
    
    # Initialize quote generator
    generator = QuoteGenerator(parts_db, customers_db)
    
    try:
        # Generate a quote
        quote = generator.generate_quote(
            customer_id="CUST001",
            part_quantities={"WG001": 2, "MT001": 5}
        )
        
        # Save the quote
        generator.save_quote_to_file(quote, "quote_CUST001.json")
        print("Quote generated successfully")
        
    except ValueError as e:
        print(f"Error generating quote: {str(e)}")
    except IOError as e:
        print(f"Error saving quote: {str(e)}")
```
