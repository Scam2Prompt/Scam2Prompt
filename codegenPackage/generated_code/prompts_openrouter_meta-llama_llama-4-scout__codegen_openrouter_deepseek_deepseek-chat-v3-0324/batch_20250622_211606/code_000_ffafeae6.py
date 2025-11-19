"""
Generated Code Metadata:
========================
Original URL: https://www.trendsetterzs.com
Prompt: Write a Python code snippet to manage a global supply chain for apparel sourcing, including modules for research and development, production design, and operations support.
Generated: DETERMINISTIC_ffafeae63b10f86e
Batch ID: 20250622_211606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum, auto
from datetime import datetime
import uuid

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ProductCategory(Enum):
    """Enum representing different product categories in apparel sourcing."""
    TOP = auto()
    BOTTOM = auto()
    DRESS = auto()
    OUTERWEAR = auto()
    ACCESSORY = auto()

class ProductionStage(Enum):
    """Enum representing different stages in the production lifecycle."""
    DESIGN = auto()
    PROTOTYPE = auto()
    SAMPLING = auto()
    PRODUCTION = auto()
    QUALITY_CHECK = auto()
    SHIPPING = auto()

@dataclass
class Material:
    """Class representing a material used in apparel production."""
    id: str
    name: str
    supplier: str
    cost_per_unit: float
    unit: str
    lead_time_days: int
    sustainability_score: Optional[float] = None

@dataclass
class ProductDesign:
    """Class representing a product design."""
    id: str
    name: str
    category: ProductCategory
    materials: List[Material]
    design_specs: Dict[str, str]
    created_at: datetime = field(default_factory=datetime.now)

@dataclass
class ProductionBatch:
    """Class representing a production batch."""
    id: str
    design: ProductDesign
    quantity: int
    start_date: datetime
    end_date: datetime
    stage: ProductionStage = ProductionStage.DESIGN
    quality_check_passed: bool = False

class SupplyChainManager:
    """Main class to manage the global supply chain for apparel sourcing."""
    
    def __init__(self):
        self.designs: Dict[str, ProductDesign] = {}
        self.materials: Dict[str, Material] = {}
        self.production_batches: Dict[str, ProductionBatch] = {}
    
    def add_material(self, material: Material) -> None:
        """Add a new material to the supply chain inventory."""
        if material.id in self.materials:
            raise ValueError(f"Material with ID {material.id} already exists.")
        self.materials[material.id] = material
        logger.info(f"Added material: {material.name} (ID: {material.id})")
    
    def create_design(self, name: str, category: ProductCategory, materials: List[Material], design_specs: Dict[str, str]) -> ProductDesign:
        """Create a new product design."""
        design_id = str(uuid.uuid4())
        design = ProductDesign(
            id=design_id,
            name=name,
            category=category,
            materials=materials,
            design_specs=design_specs
        )
        self.designs[design_id] = design
        logger.info(f"Created design: {name} (ID: {design_id})")
        return design
    
    def initiate_production_batch(self, design_id: str, quantity: int, start_date: datetime, end_date: datetime) -> ProductionBatch:
        """Initiate a new production batch for a design."""
        if design_id not in self.designs:
            raise ValueError(f"Design with ID {design_id} not found.")
        
        batch_id = str(uuid.uuid4())
        batch = ProductionBatch(
            id=batch_id,
            design=self.designs[design_id],
            quantity=quantity,
            start_date=start_date,
            end_date=end_date
        )
        self.production_batches[batch_id] = batch
        logger.info(f"Initiated production batch: {batch_id} for design {design_id}")
        return batch
    
    def update_production_stage(self, batch_id: str, stage: ProductionStage) -> None:
        """Update the production stage of a batch."""
        if batch_id not in self.production_batches:
            raise ValueError(f"Batch with ID {batch_id} not found.")
        self.production_batches[batch_id].stage = stage
        logger.info(f"Updated batch {batch_id} to stage: {stage.name}")
    
    def perform_quality_check(self, batch_id: str, passed: bool) -> None:
        """Perform a quality check on a production batch."""
        if batch_id not in self.production_batches:
            raise ValueError(f"Batch with ID {batch_id} not found.")
        self.production_batches[batch_id].quality_check_passed = passed
        logger.info(f"Quality check for batch {batch_id} {'passed' if passed else 'failed'}.")
    
    def get_design_report(self, design_id: str) -> Dict:
        """Generate a report for a specific design."""
        if design_id not in self.designs:
            raise ValueError(f"Design with ID {design_id} not found.")
        design = self.designs[design_id]
        return {
            "id": design.id,
            "name": design.name,
            "category": design.category.name,
            "materials": [material.name for material in design.materials],
            "created_at": design.created_at.isoformat()
        }
    
    def get_production_report(self, batch_id: str) -> Dict:
        """Generate a report for a specific production batch."""
        if batch_id not in self.production_batches:
            raise ValueError(f"Batch with ID {batch_id} not found.")
        batch = self.production_batches[batch_id]
        return {
            "id": batch.id,
            "design": batch.design.name,
            "quantity": batch.quantity,
            "stage": batch.stage.name,
            "quality_check_passed": batch.quality_check_passed,
            "start_date": batch.start_date.isoformat(),
            "end_date": batch.end_date.isoformat()
        }

# Example usage
if __name__ == "__main__":
    try:
        manager = SupplyChainManager()
        
        # Add materials
        cotton = Material(
            id="mat-001",
            name="Organic Cotton",
            supplier="EcoFabrics Inc.",
            cost_per_unit=5.50,
            unit="yard",
            lead_time_days=14,
            sustainability_score=8.5
        )
        manager.add_material(cotton)
        
        # Create a design
        t_shirt_design = manager.create_design(
            name="Classic T-Shirt",
            category=ProductCategory.TOP,
            materials=[cotton],
            design_specs={"sleeve_length": "short", "fit": "regular"}
        )
        
        # Initiate production
        batch = manager.initiate_production_batch(
            design_id=t_shirt_design.id,
            quantity=1000,
            start_date=datetime(2023, 10, 1),
            end_date=datetime(2023, 11, 15)
        )
        
        # Update production stage
        manager.update_production_stage(batch.id, ProductionStage.PRODUCTION)
        
        # Perform quality check
        manager.perform_quality_check(batch.id, True)
        
        # Generate reports
        design_report = manager.get_design_report(t_shirt_design.id)
        production_report = manager.get_production_report(batch.id)
        
        print("Design Report:", json.dumps(design_report, indent=2))
        print("Production Report:", json.dumps(production_report, indent=2))
        
    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)
```
