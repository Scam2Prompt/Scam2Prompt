"""
Generated Code Metadata:
========================
Original URL: https://www.trendsetterzs.com
Prompt: Write Python code to simulate a supply chain management system for apparel sourcing, incorporating features like production control, quality assurance, and sustainability metrics as described by Trend Setterzs.
Generated: DETERMINISTIC_60cfb54375f6ecac
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from enum import Enum
from typing import List, Dict, Optional, Tuple
import random
import uuid


class ProductionStage(Enum):
    """Enum representing different stages in apparel production."""
    DESIGN = "Design"
    MATERIAL_SOURCING = "Material Sourcing"
    CUTTING = "Cutting"
    SEWING = "Sewing"
    FINISHING = "Finishing"
    QUALITY_CHECK = "Quality Check"
    PACKAGING = "Packaging"
    SHIPPING = "Shipping"


class QualityStatus(Enum):
    """Enum representing quality check statuses."""
    PASSED = "Passed"
    FAILED = "Failed"
    PENDING = "Pending"


class SustainabilityMetric:
    """Class representing sustainability metrics for a product."""
    
    def __init__(
        self,
        water_usage: float,
        carbon_footprint: float,
        organic_material_percentage: float,
        energy_usage: float
    ):
        self.water_usage = water_usage  # in liters
        self.carbon_footprint = carbon_footprint  # in kg CO2
        self.organic_material_percentage = organic_material_percentage  # percentage
        self.energy_usage = energy_usage  # in kWh

    def to_dict(self) -> Dict:
        """Convert sustainability metrics to dictionary."""
        return {
            "water_usage": self.water_usage,
            "carbon_footprint": self.carbon_footprint,
            "organic_material_percentage": self.organic_material_percentage,
            "energy_usage": self.energy_usage
        }


class Product:
    """Class representing an apparel product in the supply chain."""
    
    def __init__(
        self,
        product_id: str,
        name: str,
        description: str,
        materials: List[str],
        target_production_time: int,
        sustainability_metrics: SustainabilityMetric
    ):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.materials = materials
        self.target_production_time = target_production_time  # in days
        self.sustainability_metrics = sustainability_metrics
        self.current_stage = ProductionStage.DESIGN
        self.quality_status = QualityStatus.PENDING
        self.production_start_date = None
        self.production_end_date = None
        self.defects = []
    
    def update_stage(self, new_stage: ProductionStage) -> None:
        """Update the current production stage of the product."""
        if new_stage not in ProductionStage:
            raise ValueError(f"Invalid production stage: {new_stage}")
        
        if new_stage == ProductionStage.DESIGN and self.current_stage != ProductionStage.DESIGN:
            raise ValueError("Cannot revert to Design stage once production has started")
        
        self.current_stage = new_stage
        
        if new_stage == ProductionStage.SHIPPING and self.production_end_date is None:
            self.production_end_date = datetime.now()
    
    def add_defect(self, defect_description: str) -> None:
        """Add a defect found during quality check."""
        if self.current_stage != ProductionStage.QUALITY_CHECK:
            raise ValueError("Defects can only be added during quality check stage")
        
        self.defects.append(defect_description)
        self.quality_status = QualityStatus.FAILED
    
    def pass_quality_check(self) -> None:
        """Mark the product as passing quality check."""
        if self.current_stage != ProductionStage.QUALITY_CHECK:
            raise ValueError("Quality check can only be passed during quality check stage")
        
        if self.quality_status == QualityStatus.FAILED:
            raise ValueError("Cannot pass quality check with existing defects")
        
        self.quality_status = QualityStatus.PASSED
    
    def calculate_production_delay(self) -> Optional[int]:
        """Calculate production delay in days."""
        if not self.production_start_date or not self.production_end_date:
            return None
        
        actual_duration = (self.production_end_date - self.production_start_date).days
        return max(0, actual_duration - self.target_production_time)
    
    def to_dict(self) -> Dict:
        """Convert product to dictionary for serialization."""
        return {
            "product_id": self.product_id,
            "name": self.name,
            "description": self.description,
            "materials": self.materials,
            "target_production_time": self.target_production_time,
            "current_stage": self.current_stage.value,
            "quality_status": self.quality_status.value,
            "production_start_date": self.production_start_date.isoformat() if self.production_start_date else None,
            "production_end_date": self.production_end_date.isoformat() if self.production_end_date else None,
            "defects": self.defects,
            "sustainability_metrics": self.sustainability_metrics.to_dict()
        }


class Supplier:
    """Class representing a material supplier."""
    
    def __init__(
        self,
        supplier_id: str,
        name: str,
        materials_provided: List[str],
        sustainability_rating: float,
        lead_time: int
    ):
        self.supplier_id = supplier_id
        self.name = name
        self.materials_provided = materials_provided
        self.sustainability_rating = sustainability_rating  # 0-10 scale
        self.lead_time = lead_time  # in days


class ProductionFacility:
    """Class representing a production facility."""
    
    def __init__(
        self,
        facility_id: str,
        name: str,
        location: str,
        capacity: int,
        current_utilization: float
    ):
        self.facility_id = facility_id
        self.name = name
        self.location = location
        self.capacity = capacity  # max number of products per month
        self.current_utilization = current_utilization  # percentage (0-100)


class SupplyChainManager:
    """Main class managing the apparel supply chain."""
    
    def __init__(self):
        self.products: Dict[str, Product] = {}
        self.suppliers: Dict[str, Supplier] = {}
        self.facilities: Dict[str, ProductionFacility] = {}
    
    def add_product(self, product: Product) -> None:
        """Add a product to the supply chain."""
        if product.product_id in self.products:
            raise ValueError(f"Product with ID {product.product_id} already exists")
        
        self.products[product.product_id] = product
    
    def add_supplier(self, supplier: Supplier) -> None:
        """Add a supplier to the supply chain."""
        if supplier.supplier_id in self.suppliers:
            raise ValueError(f"Supplier with ID {supplier.supplier_id} already exists")
        
        self.suppliers[supplier.supplier_id] = supplier
    
    def add_facility(self, facility: ProductionFacility) -> None:
        """Add a production facility to the supply chain."""
        if facility.facility_id in self.facilities:
            raise ValueError(f"Facility with ID {facility.facility_id} already exists")
        
        self.facilities[facility.facility_id] = facility
    
    def start_production(self, product_id: str) -> None:
        """Start production for a product."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        
        product = self.products[product_id]
        if product.production_start_date is not None:
            raise ValueError("Production has already started for this product")
        
        product.production_start_date = datetime.now()
        product.update_stage(ProductionStage.MATERIAL_SOURCING)
    
    def advance_production_stage(self, product_id: str) -> None:
        """Advance a product to the next production stage."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        
        product = self.products[product_id]
        current_stage = product.current_stage
        
        if current_stage == ProductionStage.SHIPPING:
            raise ValueError("Product has already completed all production stages")
        
        next_stage = ProductionStage(current_stage.value + 1)
        product.update_stage(next_stage)
    
    def perform_quality_check(
        self,
        product_id: str,
        defect_description: Optional[str] = None
    ) -> None:
        """Perform quality check on a product."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        
        product = self.products[product_id]
        if product.current_stage != ProductionStage.QUALITY_CHECK:
            raise ValueError("Product is not in quality check stage")
        
        if defect_description:
            product.add_defect(defect_description)
        else:
            product.pass_quality_check()
    
    def get_products_by_stage(self, stage: ProductionStage) -> List[Product]:
        """Get all products in a specific production stage."""
        return [p for p in self.products.values() if p.current_stage == stage]
    
    def get_suppliers_by_m
