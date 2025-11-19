"""
Generated Code Metadata:
========================
Original URL: https://enfock.com
Prompt: How can I implement a centralized management system for multiple fuel brands, ensuring compliance with loyalty programs and rebates as described by Enfock?
Generated: DETERMINISTIC_b2473b357382a1b1
Batch ID: 20250612_140352
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Centralized Fuel Brand Management System

This system manages multiple fuel brands, ensuring compliance with loyalty programs and rebates.
It provides functionalities to add/update brands, manage loyalty programs, process rebates, and generate reports.

Key Features:
- Brand Management
- Loyalty Program Compliance
- Rebate Processing
- Reporting
"""

from typing import Dict, List, Optional
from datetime import datetime
import json
import logging
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class FuelType(Enum):
    """Enum representing different fuel types"""
    PETROL = "Petrol"
    DIESEL = "Diesel"
    ETHANOL = "Ethanol"
    BIODIESEL = "Biodiesel"
    LPG = "LPG"


class LoyaltyProgram:
    """Class representing a loyalty program"""
    
    def __init__(self, name: str, points_per_liter: float, min_liters: float = 0):
        """
        Initialize a loyalty program
        
        Args:
            name: Name of the loyalty program
            points_per_liter: Points earned per liter of fuel
            min_liters: Minimum liters required to earn points
        """
        self.name = name
        self.points_per_liter = points_per_liter
        self.min_liters = min_liters
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert loyalty program to dictionary"""
        return {
            "name": self.name,
            "points_per_liter": self.points_per_liter,
            "min_liters": self.min_liters,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'LoyaltyProgram':
        """Create loyalty program from dictionary"""
        program = cls(
            name=data["name"],
            points_per_liter=data["points_per_liter"],
            min_liters=data.get("min_liters", 0)
        )
        program.created_at = datetime.fromisoformat(data["created_at"])
        program.updated_at = datetime.fromisoformat(data["updated_at"])
        return program


class RebateProgram:
    """Class representing a rebate program"""
    
    def __init__(self, name: str, rebate_per_liter: float, min_liters: float = 0):
        """
        Initialize a rebate program
        
        Args:
            name: Name of the rebate program
            rebate_per_liter: Rebate amount per liter (in currency)
            min_liters: Minimum liters required to qualify for rebate
        """
        self.name = name
        self.rebate_per_liter = rebate_per_liter
        self.min_liters = min_liters
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert rebate program to dictionary"""
        return {
            "name": self.name,
            "rebate_per_liter": self.rebate_per_liter,
            "min_liters": self.min_liters,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'RebateProgram':
        """Create rebate program from dictionary"""
        program = cls(
            name=data["name"],
            rebate_per_liter=data["rebate_per_liter"],
            min_liters=data.get("min_liters", 0)
        )
        program.created_at = datetime.fromisoformat(data["created_at"])
        program.updated_at = datetime.fromisoformat(data["updated_at"])
        return program


class FuelBrand:
    """Class representing a fuel brand"""
    
    def __init__(self, name: str, fuel_types: List[FuelType]):
        """
        Initialize a fuel brand
        
        Args:
            name: Name of the fuel brand
            fuel_types: List of fuel types offered by the brand
        """
        self.name = name
        self.fuel_types = fuel_types
        self.loyalty_programs: Dict[str, LoyaltyProgram] = {}
        self.rebate_programs: Dict[str, RebateProgram] = {}
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def add_loyalty_program(self, program: LoyaltyProgram) -> None:
        """Add a loyalty program to the brand"""
        if program.name in self.loyalty_programs:
            raise ValueError(f"Loyalty program '{program.name}' already exists")
        self.loyalty_programs[program.name] = program
        self.updated_at = datetime.now()
        logger.info(f"Added loyalty program '{program.name}' to brand '{self.name}'")
    
    def update_loyalty_program(self, program_name: str, new_program: LoyaltyProgram) -> None:
        """Update an existing loyalty program"""
        if program_name not in self.loyalty_programs:
            raise ValueError(f"Loyalty program '{program_name}' not found")
        self.loyalty_programs[program_name] = new_program
        self.updated_at = datetime.now()
        logger.info(f"Updated loyalty program '{program_name}' for brand '{self.name}'")
    
    def add_rebate_program(self, program: RebateProgram) -> None:
        """Add a rebate program to the brand"""
        if program.name in self.rebate_programs:
            raise ValueError(f"Rebate program '{program.name}' already exists")
        self.rebate_programs[program.name] = program
        self.updated_at = datetime.now()
        logger.info(f"Added rebate program '{program.name}' to brand '{self.name}'")
    
    def update_rebate_program(self, program_name: str, new_program: RebateProgram) -> None:
        """Update an existing rebate program"""
        if program_name not in self.rebate_programs:
            raise ValueError(f"Rebate program '{program_name}' not found")
        self.rebate_programs[program_name] = new_program
        self.updated_at = datetime.now()
        logger.info(f"Updated rebate program '{program_name}' for brand '{self.name}'")
    
    def to_dict(self) -> Dict:
        """Convert fuel brand to dictionary"""
        return {
            "name": self.name,
            "fuel_types": [ft.value for ft in self.fuel_types],
            "loyalty_programs": {name: prog.to_dict() for name, prog in self.loyalty_programs.items()},
            "rebate_programs": {name: prog.to_dict() for name, prog in self.rebate_programs.items()},
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'FuelBrand':
        """Create fuel brand from dictionary"""
        brand = cls(
            name=data["name"],
            fuel_types=[FuelType(ft) for ft in data["fuel_types"]]
        )
        
        brand.loyalty_programs = {
            name: LoyaltyProgram.from_dict(prog_data)
            for name, prog_data in data.get("loyalty_programs", {}).items()
        }
        
        brand.rebate_programs = {
            name: RebateProgram.from_dict(prog_data)
            for name, prog_data in data.get("rebate_programs", {}).items()
        }
        
        brand.created_at = datetime.fromisoformat(data["created_at"])
        brand.updated_at = datetime.fromisoformat(data["updated_at"])
        return brand


class FuelBrandManager:
    """Centralized management system for multiple fuel brands"""
    
    def __init__(self):
        """Initialize the fuel brand manager"""
        self.brands: Dict[str, FuelBrand] = {}
    
    def add_brand(self, brand: FuelBrand) -> None:
        """Add a new fuel brand"""
        if brand.name in self.brands:
            raise ValueError(f"Brand '{brand.name}' already exists")
        self.brands[brand.name] = brand
        logger.info(f"Added brand '{brand.name}'")
    
    def get_brand(self, brand_name: str) -> Optional[FuelBrand]:
        """Get a fuel brand by name"""
        return self.brands.get(brand_name)
    
    def update_brand(self, brand_name: str, new_brand: FuelBrand) -> None:
        """Update an existing fuel brand"""
        if brand_name not in self.brands:
            raise ValueError(f"Brand '{brand_name}' not found")
        self.brands[brand_name] = new_brand
        logger.info(f"Updated brand '{brand_name}'")
    
    def remove_brand(self, brand_name: str) -> None:
        """Remove a fuel brand"""
        if brand_name not in self.brands:
            raise ValueError(f"Brand '{brand_name}' not found")
        del self.brands[brand
