"""
Generated Code Metadata:
========================
Original URL: https://linea.be
Prompt: Write a program to simulate the supply chain of FSC-certified materials for household cleaning tools, referencing PDC Brush's commitment to sustainability.
Generated: DETERMINISTIC_3eda1b43ed5be5dc
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Supply Chain Simulation for FSC-Certified Materials in Household Cleaning Tools

This program simulates the supply chain process for FSC-certified materials used in
household cleaning tools, inspired by PDC Brush's sustainability commitment.

Key components:
- Material sourcing from FSC-certified suppliers
- Manufacturing process tracking
- Carbon footprint calculation
- Sustainability metrics reporting
"""

import random
from datetime import datetime, timedelta
from typing import List, Dict, Tuple
import csv
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('supply_chain.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class FSCSupplier:
    """Represents an FSC-certified supplier of raw materials."""
    
    def __init__(self, name: str, location: str, certification_id: str):
        self.name = name
        self.location = location
        self.certification_id = certification_id
        self.materials = {
            'wood': {'available': True, 'carbon_per_kg': 0.5},
            'bamboo': {'available': True, 'carbon_per_kg': 0.3},
            'natural_fibers': {'available': True, 'carbon_per_kg': 0.4}
        }
        
    def check_availability(self, material_type: str, quantity: float) -> bool:
        """Check if material is available in required quantity."""
        if material_type not in self.materials or not self.materials[material_type]['available']:
            return False
        return True
    
    def get_carbon_footprint(self, material_type: str, quantity: float) -> float:
        """Calculate carbon footprint for given material quantity."""
        if material_type not in self.materials:
            raise ValueError(f"Material {material_type} not available from this supplier")
        return self.materials[material_type]['carbon_per_kg'] * quantity

class ManufacturingFacility:
    """Represents a manufacturing facility that produces cleaning tools."""
    
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.production_capacity = 1000  # units per day
        self.energy_source = 'renewable'  # default to renewable energy
        self.current_inventory = {
            'wood': 0,
            'bamboo': 0,
            'natural_fibers': 0
        }
        
    def receive_materials(self, material_type: str, quantity: float) -> None:
        """Receive materials from suppliers and add to inventory."""
        if material_type not in self.current_inventory:
            raise ValueError(f"Invalid material type: {material_type}")
        self.current_inventory[material_type] += quantity
        logger.info(f"Received {quantity} kg of {material_type} at {self.name}")
        
    def produce_products(self, product_type: str, quantity: int) -> Dict:
        """Simulate production process and return production metrics."""
        if quantity > self.production_capacity:
            raise ValueError(f"Requested quantity exceeds daily capacity of {self.production_capacity}")
            
        materials_needed = self._calculate_material_needs(product_type, quantity)
        
        for material, needed in materials_needed.items():
            if self.current_inventory[material] < needed:
                raise ValueError(f"Insufficient {material} inventory for production")
            self.current_inventory[material] -= needed
        
        carbon_footprint = self._calculate_production_footprint(quantity)
        
        return {
            'product_type': product_type,
            'quantity': quantity,
            'materials_used': materials_needed,
            'carbon_footprint': carbon_footprint,
            'energy_source': self.energy_source,
            'date': datetime.now().isoformat()
        }
    
    def _calculate_material_needs(self, product_type: str, quantity: int) -> Dict[str, float]:
        """Calculate material requirements based on product type."""
        # Simplified material requirements per unit
        requirements = {
            'broom': {'wood': 0.5, 'natural_fibers': 0.3},
            'brush': {'wood': 0.3, 'natural_fibers': 0.2},
            'mop': {'bamboo': 0.4, 'natural_fibers': 0.5}
        }
        
        if product_type not in requirements:
            raise ValueError(f"Unknown product type: {product_type}")
            
        return {mat: qty * quantity for mat, qty in requirements[product_type].items()}
    
    def _calculate_production_footprint(self, quantity: int) -> float:
        """Calculate carbon footprint of production process."""
        base_footprint = 0.1  # kg CO2 per unit
        if self.energy_source == 'renewable':
            return base_footprint * quantity * 0.5  # 50% reduction for renewable energy
        return base_footprint * quantity

class DistributionCenter:
    """Represents a distribution center for finished products."""
    
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.inventory = {}
        self.shipping_methods = {
            'truck': {'carbon_per_km': 0.1, 'speed': 'medium'},
            'train': {'carbon_per_km': 0.05, 'speed': 'slow'},
            'electric_vehicle': {'carbon_per_km': 0.02, 'speed': 'fast'}
        }
        
    def receive_products(self, products: List[Dict]) -> None:
        """Receive finished products from manufacturing facility."""
        for product in products:
            product_type = product['product_type']
            if product_type not in self.inventory:
                self.inventory[product_type] = 0
            self.inventory[product_type] += product['quantity']
        logger.info(f"Received {len(products)} product batches at {self.name}")
        
    def ship_order(self, order: Dict, distance_km: float) -> Dict:
        """Simulate shipping an order to a customer."""
        shipping_method = order.get('shipping_method', 'truck')
        if shipping_method not in self.shipping_methods:
            raise ValueError(f"Invalid shipping method: {shipping_method}")
            
        for product_type, quantity in order['items'].items():
            if self.inventory.get(product_type, 0) < quantity:
                raise ValueError(f"Insufficient inventory for {product_type}")
            self.inventory[product_type] -= quantity
            
        carbon_footprint = distance_km * self.shipping_methods[shipping_method]['carbon_per_km']
        
        return {
            'order_id': order.get('order_id', str(random.randint(1000, 9999))),
            'items': order['items'],
            'shipping_method': shipping_method,
            'distance_km': distance_km,
            'carbon_footprint': carbon_footprint,
            'ship_date': datetime.now().isoformat()
        }

class SustainabilityReport:
    """Generates sustainability reports for the supply chain."""
    
    @staticmethod
    def generate_report(data: List[Dict], report_type: str = 'summary') -> str:
        """Generate a sustainability report from supply chain data."""
        if report_type == 'summary':
            return SustainabilityReport._generate_summary_report(data)
        elif report_type == 'detailed':
            return SustainabilityReport._generate_detailed_report(data)
        else:
            raise ValueError(f"Unknown report type: {report_type}")
    
    @staticmethod
    def _generate_summary_report(data: List[Dict]) -> str:
        """Generate a summary sustainability report."""
        total_carbon = sum(item.get('carbon_footprint', 0) for item in data)
        total_products = sum(item.get('quantity', 0) for item in data if 'quantity' in item)
        
        report = {
            'report_date': datetime.now().isoformat(),
            'total_carbon_footprint_kg': round(total_carbon, 2),
            'total_products_produced': total_products,
            'carbon_per_product': round(total_carbon / total_products, 3) if total_products else 0,
            'fsc_certified': True,
            'renewable_energy_used': any(
                item.get('energy_source') == 'renewable' 
                for item in data if 'energy_source' in item
            )
        }
        
        return json.dumps(report, indent=2)
    
    @staticmethod
    def _generate_detailed_report(data: List[Dict]) -> str:
        """Generate a detailed sustainability report."""
        detailed_data = []
        for item in data:
            record = {
                'date': item.get('date', item.get('ship_date', 'unknown')),
                'type': item.get('product_type', 'shipping'),
                'quantity': item.get('quantity', 1),
                'carbon_footprint_kg': round(item.get('carbon_footprint', 0),
