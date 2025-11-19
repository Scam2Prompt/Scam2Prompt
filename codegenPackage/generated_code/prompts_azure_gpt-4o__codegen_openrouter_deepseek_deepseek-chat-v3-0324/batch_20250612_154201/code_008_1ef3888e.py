"""
Generated Code Metadata:
========================
Original URL: https://enfock.com
Prompt: Generate code to implement a centralized control system for managing multiple fuel station brands, including features for restaurant and convenience store integration, as described by Enfock.
Generated: DETERMINISTIC_1ef3888e2cf7f2bb
Batch ID: 20250612_154201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Centralized Fuel Station Management System
This system manages multiple fuel station brands with integrated restaurant and convenience store functionalities.
"""

from abc import ABC, abstractmethod
from datetime import datetime
import json
import logging
from typing import Dict, List, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class StationComponent(ABC):
    """Abstract base class for all station components."""
    
    @abstractmethod
    def get_status(self) -> Dict:
        """Return the current status of the component."""
        pass
    
    @abstractmethod
    def update(self, data: Dict) -> bool:
        """Update the component with new data."""
        pass

class FuelPump(StationComponent):
    """Class representing a fuel pump at a station."""
    
    def __init__(self, pump_id: str, fuel_type: str, price_per_liter: float):
        self.pump_id = pump_id
        self.fuel_type = fuel_type
        self.price_per_liter = price_per_liter
        self.is_active = True
        self.current_volume = 0.0
        self.total_sales = 0.0
        
    def get_status(self) -> Dict:
        return {
            'pump_id': self.pump_id,
            'fuel_type': self.fuel_type,
            'price_per_liter': self.price_per_liter,
            'is_active': self.is_active,
            'current_volume': self.current_volume,
            'total_sales': self.total_sales
        }
    
    def update(self, data: Dict) -> bool:
        try:
            if 'price_per_liter' in data:
                self.price_per_liter = float(data['price_per_liter'])
            if 'is_active' in data:
                self.is_active = bool(data['is_active'])
            if 'current_volume' in data:
                self.current_volume = float(data['current_volume'])
            return True
        except (ValueError, KeyError) as e:
            logger.error(f"Error updating fuel pump {self.pump_id}: {str(e)}")
            return False
    
    def record_sale(self, liters: float) -> bool:
        try:
            liters = float(liters)
            if liters <= 0:
                raise ValueError("Liters must be positive")
                
            sale_amount = liters * self.price_per_liter
            self.current_volume -= liters
            self.total_sales += sale_amount
            return True
        except (ValueError, TypeError) as e:
            logger.error(f"Error recording sale for pump {self.pump_id}: {str(e)}")
            return False

class Restaurant(StationComponent):
    """Class representing a restaurant at a station."""
    
    def __init__(self, name: str, menu: Dict[str, float]):
        self.name = name
        self.menu = menu
        self.orders: List[Dict] = []
        self.total_sales = 0.0
        
    def get_status(self) -> Dict:
        return {
            'name': self.name,
            'menu': self.menu,
            'active_orders': len(self.orders),
            'total_sales': self.total_sales
        }
    
    def update(self, data: Dict) -> bool:
        try:
            if 'menu' in data:
                self.menu = {str(k): float(v) for k, v in data['menu'].items()}
            return True
        except (ValueError, TypeError) as e:
            logger.error(f"Error updating restaurant {self.name}: {str(e)}")
            return False
    
    def place_order(self, items: Dict[str, int]) -> Optional[Dict]:
        try:
            order_total = 0.0
            order_items = []
            
            for item, quantity in items.items():
                if item not in self.menu:
                    raise ValueError(f"Item {item} not in menu")
                if quantity <= 0:
                    raise ValueError("Quantity must be positive")
                    
                item_price = self.menu[item]
                order_total += item_price * quantity
                order_items.append({
                    'item': item,
                    'quantity': quantity,
                    'price': item_price
                })
            
            order = {
                'order_id': f"ORD-{datetime.now().timestamp()}",
                'items': order_items,
                'total': order_total,
                'status': 'pending',
                'timestamp': datetime.now().isoformat()
            }
            
            self.orders.append(order)
            self.total_sales += order_total
            return order
        except (ValueError, TypeError) as e:
            logger.error(f"Error placing order: {str(e)}")
            return None

class ConvenienceStore(StationComponent):
    """Class representing a convenience store at a station."""
    
    def __init__(self, name: str, inventory: Dict[str, Dict]):
        self.name = name
        self.inventory = inventory  # {item_id: {'name': str, 'price': float, 'quantity': int}}
        self.total_sales = 0.0
        
    def get_status(self) -> Dict:
        return {
            'name': self.name,
            'inventory_count': len(self.inventory),
            'total_sales': self.total_sales
        }
    
    def update(self, data: Dict) -> bool:
        try:
            if 'inventory' in data:
                for item_id, item_data in data['inventory'].items():
                    if item_id in self.inventory:
                        self.inventory[item_id].update(item_data)
                    else:
                        self.inventory[item_id] = item_data
            return True
        except (ValueError, TypeError) as e:
            logger.error(f"Error updating store {self.name}: {str(e)}")
            return False
    
    def process_purchase(self, items: Dict[str, int]) -> Optional[Dict]:
        try:
            purchase_total = 0.0
            purchased_items = []
            
            for item_id, quantity in items.items():
                if item_id not in self.inventory:
                    raise ValueError(f"Item {item_id} not in inventory")
                if quantity <= 0:
                    raise ValueError("Quantity must be positive")
                if self.inventory[item_id]['quantity'] < quantity:
                    raise ValueError(f"Insufficient stock for item {item_id}")
                    
                item_price = self.inventory[item_id]['price']
                purchase_total += item_price * quantity
                self.inventory[item_id]['quantity'] -= quantity
                
                purchased_items.append({
                    'item_id': item_id,
                    'name': self.inventory[item_id]['name'],
                    'quantity': quantity,
                    'price': item_price
                })
            
            receipt = {
                'transaction_id': f"TXN-{datetime.now().timestamp()}",
                'items': purchased_items,
                'total': purchase_total,
                'timestamp': datetime.now().isoformat()
            }
            
            self.total_sales += purchase_total
            return receipt
        except (ValueError, TypeError) as e:
            logger.error(f"Error processing purchase: {str(e)}")
            return None

class FuelStation:
    """Class representing a fuel station with integrated services."""
    
    def __init__(self, station_id: str, name: str, location: str):
        self.station_id = station_id
        self.name = name
        self.location = location
        self.pumps: Dict[str, FuelPump] = {}
        self.restaurant: Optional[Restaurant] = None
        self.convenience_store: Optional[ConvenienceStore] = None
        
    def add_pump(self, pump: FuelPump) -> bool:
        if pump.pump_id in self.pumps:
            logger.warning(f"Pump {pump.pump_id} already exists in station {self.station_id}")
            return False
        self.pumps[pump.pump_id] = pump
        return True
    
    def set_restaurant(self, restaurant: Restaurant) -> None:
        self.restaurant = restaurant
    
    def set_convenience_store(self, store: ConvenienceStore) -> None:
        self.convenience_store = store
    
    def get_status(self) -> Dict:
        status = {
            'station_id': self.station_id,
            'name': self.name,
            'location': self.location,
            'pumps': {pid: pump.get_status() for pid, pump in self.pumps.items()}
        }
        
        if self.restaurant:
            status['restaurant'] = self.restaurant.get_status()
        if self.convenience_store:
            status['convenience_store'] = self.convenience_store.get_status()
            
        return status
    
    def update_pump(self, pump_id: str, data: Dict) -> bool:
        if pump_id not in self.pumps:
            logger.error(f"Pump {pump_id} not found in station {self.station_id}")
            return False
        return self.pumps[pump_id].update(data)

class CentralManagementSystem:
    """Central system for managing multiple fuel stations."""
    
    def __init__(self):
        self.stations: Dict[str, FuelStation] = {}
        self.brands:
