"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Generate a Python script that simulates a food distribution system similar to the Food ATM initiative described on the Rakhshanda Memorial website.
Generated: DETERMINISTIC_8027b601f1cee12f
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

class FoodItem:
    """Represents a food item with its details."""
    
    def __init__(self, name: str, quantity: int, expiry_date: str, category: str):
        """
        Initialize a food item.
        
        Args:
            name: Name of the food item
            quantity: Quantity available
            expiry_date: Expiry date in YYYY-MM-DD format
            category: Category of food (e.g., 'grains', 'vegetables')
        """
        self.name = name
        self.quantity = quantity
        self.expiry_date = expiry_date
        self.category = category
    
    def to_dict(self) -> Dict:
        """Convert food item to dictionary for serialization."""
        return {
            'name': self.name,
            'quantity': self.quantity,
            'expiry_date': self.expiry_date,
            'category': self.category
        }
    
    def is_expired(self) -> bool:
        """Check if the food item is expired."""
        expiry_date = datetime.strptime(self.expiry_date, "%Y-%m-%d").date()
        return datetime.now().date() > expiry_date

class FoodATM:
    """Simulates a Food ATM distribution system."""
    
    def __init__(self, location: str, capacity: int):
        """
        Initialize a Food ATM.
        
        Args:
            location: Location of the Food ATM
            capacity: Maximum capacity of items it can hold
        """
        self.location = location
        self.capacity = capacity
        self.inventory: List[FoodItem] = []
        self.distribution_log: List[Dict] = []
    
    def add_food_item(self, food_item: FoodItem) -> bool:
        """
        Add a food item to the inventory if there's capacity.
        
        Args:
            food_item: FoodItem to add
            
        Returns:
            bool: True if added successfully, False otherwise
        """
        if len(self.inventory) >= self.capacity:
            return False
        
        self.inventory.append(food_item)
        return True
    
    def remove_expired_items(self) -> List[FoodItem]:
        """Remove and return all expired items from inventory."""
        expired_items = [item for item in self.inventory if item.is_expired()]
        self.inventory = [item for item in self.inventory if not item.is_expired()]
        return expired_items
    
    def distribute_food(self, recipient_id: str, items_requested: List[Dict]) -> Tuple[bool, List[FoodItem]]:
        """
        Distribute requested food items to a recipient.
        
        Args:
            recipient_id: ID of the recipient
            items_requested: List of dictionaries with 'name' and 'quantity'
            
        Returns:
            Tuple of (success status, list of distributed items)
        """
        distributed_items = []
        
        for request in items_requested:
            item_name = request['name']
            quantity = request['quantity']
            
            for item in self.inventory:
                if item.name == item_name and item.quantity >= quantity:
                    distributed_items.append(FoodItem(
                        name=item.name,
                        quantity=quantity,
                        expiry_date=item.expiry_date,
                        category=item.category
                    ))
                    item.quantity -= quantity
                    break
        
        if not distributed_items:
            return False, []
        
        self._log_distribution(recipient_id, distributed_items)
        return True, distributed_items
    
    def _log_distribution(self, recipient_id: str, items: List[FoodItem]) -> None:
        """Log a distribution event."""
        distribution = {
            'timestamp': datetime.now().isoformat(),
            'recipient_id': recipient_id,
            'items': [item.to_dict() for item in items],
            'location': self.location
        }
        self.distribution_log.append(distribution)
    
    def get_inventory_status(self) -> Dict:
        """Return current inventory status."""
        return {
            'location': self.location,
            'total_items': len(self.inventory),
            'items': [item.to_dict() for item in self.inventory],
            'capacity': self.capacity
        }
    
    def get_distribution_report(self) -> List[Dict]:
        """Return distribution log."""
        return self.distribution_log

class FoodDistributionSystem:
    """Manages multiple Food ATMs."""
    
    def __init__(self):
        """Initialize the distribution system."""
        self.food_atms: Dict[str, FoodATM] = {}
    
    def add_food_atm(self, location: str, capacity: int) -> bool:
        """
        Add a new Food ATM to the system.
        
        Args:
            location: Location of the ATM
            capacity: Maximum capacity
            
        Returns:
            bool: True if added successfully, False if location exists
        """
        if location in self.food_atms:
            return False
        
        self.food_atms[location] = FoodATM(location, capacity)
        return True
    
    def restock_atm(self, location: str, food_items: List[FoodItem]) -> bool:
        """
        Restock a Food ATM with new items.
        
        Args:
            location: Location of the ATM to restock
            food_items: List of FoodItems to add
            
        Returns:
            bool: True if restocked successfully, False if ATM doesn't exist
        """
        if location not in self.food_atms:
            return False
        
        atm = self.food_atms[location]
        for item in food_items:
            if not atm.add_food_item(item):
                return False
        return True
    
    def distribute_from_atm(self, location: str, recipient_id: str, items_requested: List[Dict]) -> Tuple[bool, List[FoodItem]]:
        """
        Distribute food from a specific ATM.
        
        Args:
            location: ATM location
            recipient_id: ID of recipient
            items_requested: List of requested items
            
        Returns:
            Tuple of (success status, list of distributed items)
        """
        if location not in self.food_atms:
            return False, []
        
        return self.food_atms[location].distribute_food(recipient_id, items_requested)
    
    def get_atm_status(self, location: str) -> Optional[Dict]:
        """
        Get status of a specific ATM.
        
        Args:
            location: ATM location
            
        Returns:
            Dict with ATM status or None if not found
        """
        if location not in self.food_atms:
            return None
        
        return self.food_atms[location].get_inventory_status()
    
    def get_all_atm_statuses(self) -> Dict[str, Dict]:
        """Get status of all ATMs in the system."""
        return {loc: atm.get_inventory_status() for loc, atm in self.food_atms.items()}
    
    def generate_monthly_report(self) -> Dict:
        """Generate a monthly distribution report."""
        report = {
            'generated_on': datetime.now().isoformat(),
            'total_distributions': 0,
            'total_items_distributed': 0,
            'locations': {}
        }
        
        for location, atm in self.food_atms.items():
            distributions = atm.get_distribution_report()
            monthly_distributions = [
                d for d in distributions 
                if datetime.fromisoformat(d['timestamp']) > datetime.now() - timedelta(days=30)
            ]
            
            items_distributed = sum(
                sum(item['quantity'] for item in dist['items'])
                for dist in monthly_distributions
            )
            
            report['locations'][location] = {
                'distributions': len(monthly_distributions),
                'items_distributed': items_distributed
            }
            report['total_distributions'] += len(monthly_distributions)
            report['total_items_distributed'] += items_distributed
        
        return report

def generate_sample_food_items(count: int = 10) -> List[FoodItem]:
    """Generate sample food items for testing."""
    food_names = [
        "Rice", "Wheat Flour", "Lentils", "Potatoes", "Tomatoes",
        "Onions", "Cooking Oil", "Sugar", "Salt", "Milk Powder"
    ]
    categories = ["grains", "pulses", "vegetables", "dairy", "essentials"]
    
    items = []
    for _ in range(count):
        name = random.choice(food_names)
        category = random.choice(categories)
        quantity = random.randint(5, 50)
        expiry_date = (datetime.now() + timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d")
        items.append(FoodItem(name, quantity, expiry_date, category))
    
    return items

def main():
    """Demonstrate the food distribution system."""
    system = FoodDistributionSystem()
    
    # Add some Food ATMs
    system.add_food_atm("Downtown", 100)
    system.add_food_atm("Suburb", 75)
    system.add_food_atm("Rural Area", 50)
    
    # Restock ATMs with sample items
    for location in system.food_atms:
        items = generate_sample_food_items(random
