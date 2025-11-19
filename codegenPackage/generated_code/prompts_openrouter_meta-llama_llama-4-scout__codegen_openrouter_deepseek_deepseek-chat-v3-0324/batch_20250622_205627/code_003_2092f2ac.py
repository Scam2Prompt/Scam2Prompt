"""
Generated Code Metadata:
========================
Original URL: https://dapp-market.pages.dev
Prompt: Create a simple marketplace explorer using a library like Balancy, including features for filtering and sorting listings.
Generated: DETERMINISTIC_2092f2ac89ac079f
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from enum import Enum

class SortOrder(Enum):
    ASC = "asc"
    DESC = "desc"

class MarketplaceItem:
    def __init__(self, id: str, name: str, price: float, category: str, seller: str, rating: float):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.seller = seller
        self.rating = rating

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "seller": self.seller,
            "rating": self.rating
        }

class MarketplaceExplorer:
    def __init__(self):
        self.items: List[MarketplaceItem] = []
    
    def load_items_from_json(self, json_file: str) -> None:
        """Load marketplace items from a JSON file."""
        try:
            with open(json_file, 'r') as file:
                data = json.load(file)
                self.items = [
                    MarketplaceItem(
                        id=item["id"],
                        name=item["name"],
                        price=item["price"],
                        category=item["category"],
                        seller=item["seller"],
                        rating=item["rating"]
                    ) for item in data
                ]
        except FileNotFoundError:
            raise Exception(f"File {json_file} not found")
        except json.JSONDecodeError:
            raise Exception("Invalid JSON format")
        except KeyError as e:
            raise Exception(f"Missing required field: {e}")
    
    def filter_items(
        self,
        category: Optional[str] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        min_rating: Optional[float] = None
    ) -> List[MarketplaceItem]:
        """Filter items based on specified criteria."""
        filtered = self.items
        
        if category:
            filtered = [item for item in filtered if item.category.lower() == category.lower()]
        
        if min_price is not None:
            filtered = [item for item in filtered if item.price >= min_price]
        
        if max_price is not None:
            filtered = [item for item in filtered if item.price <= max_price]
        
        if min_rating is not None:
            filtered = [item for item in filtered if item.rating >= min_rating]
        
        return filtered
    
    def sort_items(
        self,
        items: List[MarketplaceItem],
        sort_by: str = "price",
        order: SortOrder = SortOrder.ASC
    ) -> List[MarketplaceItem]:
        """Sort items by specified field and order."""
        if not items:
            return items
        
        valid_sort_fields = ["name", "price", "rating"]
        if sort_by not in valid_sort_fields:
            raise ValueError(f"Invalid sort field. Must be one of: {valid_sort_fields}")
        
        reverse = order == SortOrder.DESC
        return sorted(items, key=lambda x: getattr(x, sort_by), reverse=reverse)
    
    def display_items(self, items: List[MarketplaceItem]) -> None:
        """Display items in a formatted way."""
        if not items:
            print("No items found.")
            return
        
        print("\nMarketplace Items:")
        print("-" * 80)
        print(f"{'ID':<10} {'Name':<20} {'Price':<10} {'Category':<15} {'Seller':<15} {'Rating':<10}")
        print("-" * 80)
        for item in items:
            print(f"{item.id:<10} {item.name:<20} ${item.price:<9.2f} {item.category:<15} {item.seller:<15} {item.rating:<10.1f}")
        print("-" * 80)
        print(f"Total items: {len(items)}\n")

# Example usage
if __name__ == "__main__":
    try:
        explorer = MarketplaceExplorer()
        explorer.load_items_from_json("marketplace_items.json")
        
        # Filter and display items
        filtered_items = explorer.filter_items(
            category="Electronics",
            min_price=100,
            max_price=1000,
            min_rating=4.0
        )
        
        # Sort and display items
        sorted_items = explorer.sort_items(
            items=filtered_items,
            sort_by="price",
            order=SortOrder.DESC
        )
        
        explorer.display_items(sorted_items)
        
    except Exception as e:
        print(f"Error: {e}")
```
