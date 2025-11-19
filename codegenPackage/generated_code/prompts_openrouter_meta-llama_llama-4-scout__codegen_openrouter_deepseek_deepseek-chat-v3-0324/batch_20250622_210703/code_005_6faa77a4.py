"""
Generated Code Metadata:
========================
Original URL: https://trirangainfra.com
Prompt: "Develop a maintenance schedule for Triranga Infra's RCC precast products used in bridge construction."
Generated: DETERMINISTIC_6faa77a49365a101
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Maintenance Schedule System for Triranga Infra's RCC Precast Products in Bridge Construction

This module provides functionality to create, manage, and track maintenance schedules
for Reinforced Cement Concrete (RCC) precast products used in bridge construction.
"""

from datetime import datetime, timedelta
from enum import Enum
import json
from typing import Dict, List, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MaintenanceType(Enum):
    """Enumeration of maintenance types for RCC precast products."""
    ROUTINE_INSPECTION = "Routine Inspection"
    SURFACE_TREATMENT = "Surface Treatment"
    CRACK_REPAIR = "Crack Repair"
    JOINT_SEALANT_REPLACEMENT = "Joint Sealant Replacement"
    CORROSION_PROTECTION = "Corrosion Protection"
    STRUCTURAL_REPAIR = "Structural Repair"


class PrecastProduct:
    """Class representing an RCC precast product used in bridge construction."""
    
    def __init__(
        self,
        product_id: str,
        name: str,
        installation_date: datetime,
        expected_lifespan_years: int,
        location: str
    ):
        """
        Initialize a precast product instance.
        
        Args:
            product_id: Unique identifier for the product
            name: Name/description of the product
            installation_date: Date when product was installed
            expected_lifespan_years: Expected lifespan in years
            location: Installation location/coordinates
        """
        self.product_id = product_id
        self.name = name
        self.installation_date = installation_date
        self.expected_lifespan = expected_lifespan_years
        self.location = location
        self.maintenance_history: List[Dict] = []
        
    def add_maintenance_record(
        self,
        maintenance_type: MaintenanceType,
        date_performed: datetime,
        notes: str = "",
        technician: str = ""
    ) -> None:
        """
        Add a maintenance record to the product's history.
        
        Args:
            maintenance_type: Type of maintenance performed
            date_performed: When maintenance was performed
            notes: Additional notes about maintenance
            technician: Name of technician who performed maintenance
        """
        record = {
            "type": maintenance_type.value,
            "date": date_performed.isoformat(),
            "notes": notes,
            "technician": technician
        }
        self.maintenance_history.append(record)
        logger.info(f"Added maintenance record for product {self.product_id}")


class MaintenanceScheduler:
    """Class for managing maintenance schedules for precast products."""
    
    def __init__(self):
        self.products: Dict[str, PrecastProduct] = {}
        
    def add_product(self, product: PrecastProduct) -> None:
        """Add a product to the maintenance schedule."""
        if product.product_id in self.products:
            raise ValueError(f"Product with ID {product.product_id} already exists")
        self.products[product.product_id] = product
        logger.info(f"Added product {product.product_id} to maintenance schedule")
        
    def get_upcoming_maintenance(
        self,
        days_ahead: int = 30
    ) -> Dict[str, List[Dict]]:
        """
        Get maintenance tasks due in the next specified days.
        
        Args:
            days_ahead: Number of days to look ahead for maintenance
            
        Returns:
            Dictionary mapping product IDs to their upcoming maintenance tasks
        """
        upcoming = {}
        today = datetime.now()
        end_date = today + timedelta(days=days_ahead)
        
        for product_id, product in self.products.items():
            # Calculate age of product in days
            age_days = (today - product.installation_date).days
            
            # Determine maintenance needs based on product age
            tasks = self._calculate_maintenance_needs(product, age_days, end_date)
            if tasks:
                upcoming[product_id] = tasks
                
        return upcoming
    
    def _calculate_maintenance_needs(
        self,
        product: PrecastProduct,
        age_days: int,
        end_date: datetime
    ) -> List[Dict]:
        """Calculate maintenance needs for a product within date range."""
        tasks = []
        
        # Routine inspections every 180 days
        if age_days % 180 <= 30:  # Within 30 days of inspection due date
            last_inspection = self._get_last_maintenance_of_type(
                product, 
                MaintenanceType.ROUTINE_INSPECTION
            )
            if not last_inspection or (
                datetime.fromisoformat(last_inspection["date"]) < 
                datetime.now() - timedelta(days=150)
            ):
                tasks.append({
                    "type": MaintenanceType.ROUTINE_INSPECTION.value,
                    "due_date": (
                        product.installation_date + 
                        timedelta(days=(age_days // 180 + 1) * 180)
                    ).isoformat(),
                    "priority": "Medium"
                })
        
        # Add other maintenance schedule logic here...
        # (Surface treatment every 2 years, corrosion protection every 5 years, etc.)
        
        return tasks
    
    def _get_last_maintenance_of_type(
        self,
        product: PrecastProduct,
        maintenance_type: MaintenanceType
    ) -> Optional[Dict]:
        """Get the last maintenance record of a specific type."""
        for record in reversed(product.maintenance_history):
            if record["type"] == maintenance_type.value:
                return record
        return None
    
    def save_to_file(self, filename: str) -> None:
        """Save the maintenance schedule to a JSON file."""
        data = {
            "products": {
                pid: {
                    "name": p.name,
                    "installation_date": p.installation_date.isoformat(),
                    "expected_lifespan": p.expected_lifespan,
                    "location": p.location,
                    "maintenance_history": p.maintenance_history
                }
                for pid, p in self.products.items()
            }
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            logger.info(f"Saved maintenance schedule to {filename}")
        except IOError as e:
            logger.error(f"Failed to save schedule: {str(e)}")
            raise
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'MaintenanceScheduler':
        """Load a maintenance schedule from a JSON file."""
        scheduler = cls()
        
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                
            for pid, p_data in data["products"].items():
                product = PrecastProduct(
                    product_id=pid,
                    name=p_data["name"],
                    installation_date=datetime.fromisoformat(p_data["installation_date"]),
                    expected_lifespan=p_data["expected_lifespan"],
                    location=p_data["location"]
                )
                product.maintenance_history = p_data["maintenance_history"]
                scheduler.products[pid] = product
                
            logger.info(f"Loaded maintenance schedule from {filename}")
            return scheduler
        except (IOError, json.JSONDecodeError, KeyError) as e:
            logger.error(f"Failed to load schedule: {str(e)}")
            raise


# Example usage
if __name__ == "__main__":
    try:
        # Create scheduler instance
        scheduler = MaintenanceScheduler()
        
        # Add some products
        beam = PrecastProduct(
            product_id="B-001",
            name="Precast RCC Beam",
            installation_date=datetime(2020, 6, 15),
            expected_lifespan=50,
            location="Bridge A, Span 3"
        )
        
        pier = PrecastProduct(
            product_id="P-001",
            name="Precast RCC Pier",
            installation_date=datetime(2019, 3, 10),
            expected_lifespan=75,
            location="Bridge A, Pier 2"
        )
        
        scheduler.add_product(beam)
        scheduler.add_product(pier)
        
        # Add some maintenance records
        beam.add_maintenance_record(
            maintenance_type=MaintenanceType.ROUTINE_INSPECTION,
            date_performed=datetime(2022, 1, 10),
            notes="No issues found",
            technician="John Doe"
        )
        
        # Get upcoming maintenance
        upcoming = scheduler.get_upcoming_maintenance(days_ahead=60)
        print("Upcoming maintenance:")
        print(json.dumps(upcoming, indent=2))
        
        # Save schedule
        scheduler.save_to_file("maintenance_schedule.json")
        
    except Exception as e:
        logger.error(f"Error in maintenance schedule system: {str(e)}")
```
