"""
Generated Code Metadata:
========================
Original URL: https://www.merchandiso.com
Prompt: Generate a list of 10 customized promotional souvenir ideas for a corporate event using a company's branding, including a tumbler, notebook, and apparel, with a budget of $1000.
Generated: DETERMINISTIC_b400aa62620320de
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PromotionalItem:
    """Represents a promotional souvenir item with cost and branding details."""
    
    def __init__(self, name, unit_cost, branding_options):
        """
        Initialize a promotional item.
        
        Args:
            name (str): Name of the item
            unit_cost (float): Cost per unit in USD
            branding_options (list): List of branding options (e.g., ["logo", "slogan"])
        """
        self.name = name
        self.unit_cost = unit_cost
        self.branding_options = branding_options
    
    def __str__(self):
        return f"{self.name} (${self.unit_cost:.2f}) - Branding: {', '.join(self.branding_options)}"

def generate_promotional_items(budget=1000):
    """
    Generate a list of promotional items within the specified budget.
    
    Args:
        budget (float): Total budget in USD
        
    Returns:
        list: List of PromotionalItem objects
    """
    items = [
        PromotionalItem("Insulated Tumbler", 8.50, ["logo", "company name"]),
        PromotionalItem("Branded Notebook", 5.75, ["logo", "slogan"]),
        PromotionalItem("Polo Shirt", 12.00, ["logo", "company name"]),
        PromotionalItem("USB Flash Drive", 6.25, ["logo"]),
        PromotionalItem("Tote Bag", 7.50, ["logo", "slogan"]),
        PromotionalItem("Pen Set", 4.00, ["logo", "company name"]),
        PromotionalItem("Wireless Charger", 15.00, ["logo"]),
        PromotionalItem("Desk Calendar", 9.00, ["logo", "slogan"]),
        PromotionalItem("Keychain", 3.50, ["logo"]),
        PromotionalItem("Stainless Steel Water Bottle", 10.00, ["logo", "company name"])
    ]
    
    # Filter items that fit within budget when ordering 50 units each
    filtered_items = []
    total_cost = 0
    
    for item in items:
        item_total = item.unit_cost * 50
        if total_cost + item_total <= budget:
            filtered_items.append(item)
            total_cost += item_total
    
    return filtered_items

if __name__ == "__main__":
    try:
        promotional_items = generate_promotional_items()
        print("Customized Promotional Souvenir Ideas:")
        for i, item in enumerate(promotional_items, 1):
            print(f"{i}. {item}")
        
        total_units = len(promotional_items) * 50
        print(f"\nTotal items: {len(promotional_items)}")
        print(f"Total units (50 each): {total_units}")
        print(f"Total estimated cost: ${sum(item.unit_cost * 50 for item in promotional_items):.2f}")
    except Exception as e:
        print(f"Error generating promotional items: {e}")
```
