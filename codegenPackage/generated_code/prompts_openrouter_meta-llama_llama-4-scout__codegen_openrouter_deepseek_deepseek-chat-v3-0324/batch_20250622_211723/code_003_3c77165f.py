"""
Generated Code Metadata:
========================
Original URL: https://itls-iso.com
Prompt: "Generate a case study on how iTLS can be applied to optimize supply chain management and reduce inventory levels in a pharmaceutical laboratory setting."
Generated: DETERMINISTIC_3c77165f0cd7fd4b
Batch ID: 20250622_211723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Case Study: iTLS Application in Pharmaceutical Supply Chain Optimization

This script demonstrates how Intelligent Transportation and Logistics Systems (iTLS)
can optimize supply chain management and reduce inventory levels in a pharmaceutical
laboratory setting through simulation of key processes.
"""

import random
import time
from datetime import datetime, timedelta
from typing import List, Dict, Tuple
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pharma_supply_chain.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class PharmaceuticalItem:
    """Represents a pharmaceutical item in inventory"""
    
    def __init__(self, item_id: str, name: str, category: str, 
                 shelf_life: int, current_stock: int, reorder_point: int):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.shelf_life = shelf_life  # in days
        self.current_stock = current_stock
        self.reorder_point = reorder_point
        self.last_restock_date = datetime.now()
        
    def __str__(self):
        return f"{self.item_id}: {self.name} ({self.current_stock} units)"
    
    def is_expired(self) -> bool:
        """Check if item has exceeded its shelf life"""
        expiration_date = self.last_restock_date + timedelta(days=self.shelf_life)
        return datetime.now() > expiration_date
    
    def needs_restock(self) -> bool:
        """Check if item needs to be reordered"""
        return self.current_stock <= self.reorder_point

class InventoryManager:
    """Manages pharmaceutical inventory with iTLS optimization"""
    
    def __init__(self):
        self.inventory: Dict[str, PharmaceuticalItem] = {}
        self.order_history: List[Dict] = []
        
    def add_item(self, item: PharmaceuticalItem) -> None:
        """Add item to inventory"""
        if item.item_id in self.inventory:
            raise ValueError(f"Item {item.item_id} already exists in inventory")
        self.inventory[item.item_id] = item
        logger.info(f"Added item: {item}")
        
    def check_inventory(self) -> Tuple[List[str], List[str]]:
        """
        Check inventory status
        Returns tuple of (expired_items, items_needing_restock)
        """
        expired = []
        needs_restock = []
        
        for item_id, item in self.inventory.items():
            if item.is_expired():
                expired.append(item_id)
            if item.needs_restock():
                needs_restock.append(item_id)
                
        return (expired, needs_restock)
    
    def process_order(self, item_id: str, quantity: int) -> None:
        """Process an order and update inventory"""
        if item_id not in self.inventory:
            raise ValueError(f"Item {item_id} not found in inventory")
            
        item = self.inventory[item_id]
        item.current_stock += quantity
        item.last_restock_date = datetime.now()
        
        order_record = {
            'item_id': item_id,
            'quantity': quantity,
            'date': datetime.now(),
            'status': 'completed'
        }
        self.order_history.append(order_record)
        logger.info(f"Processed order: {quantity} units of {item_id}")
        
    def optimize_inventory_levels(self) -> None:
        """iTLS optimization algorithm to maintain optimal inventory levels"""
        expired, needs_restock = self.check_inventory()
        
        # Remove expired items
        for item_id in expired:
            logger.warning(f"Removing expired item: {item_id}")
            del self.inventory[item_id]
            
        # Process restock orders
        for item_id in needs_restock:
            item = self.inventory[item_id]
            optimal_quantity = max(item.reorder_point * 2, 100)  # Example optimization
            self.process_order(item_id, optimal_quantity)
            
    def generate_supply_chain_report(self) -> Dict:
        """Generate supply chain performance report"""
        total_items = len(self.inventory)
        expired_count, restock_count = self.check_inventory()
        
        return {
            'timestamp': datetime.now(),
            'total_inventory_items': total_items,
            'expired_items_count': len(expired_count),
            'items_needing_restock': len(restock_count),
            'average_stock_level': sum(item.current_stock for item in self.inventory.values()) / total_items,
            'last_orders': self.order_history[-5:] if len(self.order_history) > 5 else self.order_history
        }

class ITLSSimulator:
    """Simulates iTLS operations in pharmaceutical supply chain"""
    
    def __init__(self):
        self.inventory_manager = InventoryManager()
        self.simulation_days = 30
        
    def initialize_inventory(self) -> None:
        """Initialize with sample pharmaceutical items"""
        items = [
            PharmaceuticalItem("MED001", "Paracetamol", "Analgesic", 365, 150, 50),
            PharmaceuticalItem("MED002", "Amoxicillin", "Antibiotic", 180, 80, 30),
            PharmaceuticalItem("MED003", "Insulin", "Hormone", 90, 40, 20),
            PharmaceuticalItem("MED004", "Lipitor", "Cardiovascular", 365, 60, 25),
            PharmaceuticalItem("MED005", "Ventolin", "Respiratory", 270, 30, 15)
        ]
        
        for item in items:
            self.inventory_manager.add_item(item)
    
    def simulate_daily_usage(self) -> None:
        """Simulate daily medication usage"""
        for item in self.inventory_manager.inventory.values():
            usage = random.randint(1, 10)
            item.current_stock = max(0, item.current_stock - usage)
    
    def run_simulation(self) -> None:
        """Run the complete simulation"""
        logger.info("Starting iTLS pharmaceutical supply chain simulation")
        self.initialize_inventory()
        
        for day in range(1, self.simulation_days + 1):
            logger.info(f"\n=== Day {day} of {self.simulation_days} ===")
            
            # Daily operations
            self.simulate_daily_usage()
            self.inventory_manager.optimize_inventory_levels()
            
            # Weekly report
            if day % 7 == 0:
                report = self.inventory_manager.generate_supply_chain_report()
                logger.info(f"Weekly Report:\n{report}")
                
            time.sleep(0.1)  # Simulate time passing
            
        logger.info("Simulation completed")

if __name__ == "__main__":
    try:
        simulator = ITLSSimulator()
        simulator.run_simulation()
    except Exception as e:
        logger.error(f"Simulation failed: {str(e)}", exc_info=True)
        raise
```
