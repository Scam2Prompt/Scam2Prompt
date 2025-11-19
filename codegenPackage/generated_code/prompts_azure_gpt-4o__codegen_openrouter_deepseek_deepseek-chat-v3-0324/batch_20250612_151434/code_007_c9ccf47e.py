"""
Generated Code Metadata:
========================
Original URL: https://tromba-sa.com.ar
Prompt: Generate code for designing a turnkey fire protection system, referencing the E-PCI Sistemas contra Incendio Llave en Mano solution from the TROMBA website.
Generated: DETERMINISTIC_c9ccf47ed6ae7ab2
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Turnkey Fire Protection System Design
Reference: E-PCI Sistemas contra Incendio Llave en Mano (TROMBA)
"""

import enum
from dataclasses import dataclass
from typing import List, Optional, Dict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FireRiskLevel(enum.Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    EXTREME = "Extreme"

class ProtectionSystemType(enum.Enum):
    SPRINKLER = "Sprinkler System"
    GAS_SUPPRESSION = "Gas Suppression System"
    FOAM = "Foam System"
    HYBRID = "Hybrid System"
    PORTABLE = "Portable Extinguishers"

@dataclass
class SystemComponent:
    name: str
    quantity: int
    specifications: Dict[str, str]
    maintenance_schedule: str

@dataclass
class FireProtectionDesign:
    system_type: ProtectionSystemType
    components: List[SystemComponent]
    coverage_area: float  # in square meters
    risk_level: FireRiskLevel
    water_supply: Optional[Dict[str, str]] = None
    gas_type: Optional[str] = None
    foam_concentration: Optional[float] = None

    def validate_design(self) -> bool:
        """Validate the fire protection system design"""
        if not self.components:
            logger.error("Design must include at least one component")
            return False
        
        if self.system_type == ProtectionSystemType.GAS_SUPPRESSION and not self.gas_type:
            logger.error("Gas suppression system requires gas type specification")
            return False
            
        if self.system_type == ProtectionSystemType.FOAM and not self.foam_concentration:
            logger.error("Foam system requires concentration specification")
            return False
            
        return True

    def generate_report(self) -> Dict:
        """Generate a comprehensive system report"""
        if not self.validate_design():
            raise ValueError("Invalid system design - cannot generate report")
            
        return {
            "system_type": self.system_type.value,
            "risk_level": self.risk_level.value,
            "coverage_area": f"{self.coverage_area} m²",
            "components": [{
                "name": comp.name,
                "quantity": comp.quantity,
                "specifications": comp.specifications,
                "maintenance": comp.maintenance_schedule
            } for comp in self.components],
            "water_supply": self.water_supply,
            "gas_type": self.gas_type,
            "foam_concentration": self.foam_concentration
        }

class FireProtectionSystemBuilder:
    """Builder class for creating turnkey fire protection systems"""
    
    def __init__(self):
        self.design = None
        
    def create_new_design(self, system_type: ProtectionSystemType, risk_level: FireRiskLevel, area: float):
        """Initialize a new system design"""
        self.design = FireProtectionDesign(
            system_type=system_type,
            components=[],
            coverage_area=area,
            risk_level=risk_level
        )
        return self
        
    def add_component(self, name: str, quantity: int, specs: Dict, maintenance: str):
        """Add a component to the system design"""
        if not self.design:
            raise ValueError("Design not initialized")
            
        component = SystemComponent(
            name=name,
            quantity=quantity,
            specifications=specs,
            maintenance_schedule=maintenance
        )
        self.design.components.append(component)
        return self
        
    def set_water_supply(self, capacity: str, pressure: str, source: str):
        """Configure water supply for sprinkler/foam systems"""
        if not self.design:
            raise ValueError("Design not initialized")
            
        self.design.water_supply = {
            "capacity": capacity,
            "pressure": pressure,
            "source": source
        }
        return self
        
    def set_gas_type(self, gas_type: str):
        """Set gas type for suppression systems"""
        if not self.design:
            raise ValueError("Design not initialized")
            
        self.design.gas_type = gas_type
        return self
        
    def set_foam_concentration(self, concentration: float):
        """Set foam concentration for foam systems"""
        if not self.design:
            raise ValueError("Design not initialized")
            
        self.design.foam_concentration = concentration
        return self
        
    def build(self) -> FireProtectionDesign:
        """Finalize and return the completed design"""
        if not self.design:
            raise ValueError("No design to build")
            
        if not self.design.validate_design():
            raise ValueError("Invalid system design")
            
        return self.design

def example_usage():
    """Example usage of the fire protection system builder"""
    try:
        builder = FireProtectionSystemBuilder()
        system = (
            builder.create_new_design(
                system_type=ProtectionSystemType.SPRINKLER,
                risk_level=FireRiskLevel.HIGH,
                area=1500.0
            )
            .add_component(
                name="ESFR Sprinkler Head",
                quantity=120,
                specs={"K-factor": "14.0", "Temperature Rating": "155°F"},
                maintenance="Quarterly inspection"
            )
            .add_component(
                name="Alarm Valve",
                quantity=2,
                specs={"Size": "6-inch", "Pressure Rating": "175 psi"},
                maintenance="Annual testing"
            )
            .set_water_supply(
                capacity="10,000 gallons",
                pressure="100 psi",
                source="Municipal + Backup Tank"
            )
            .build()
        )
        
        report = system.generate_report()
        logger.info("System design completed successfully")
        return report
        
    except Exception as e:
        logger.error(f"Error in system design: {str(e)}")
        raise

if __name__ == "__main__":
    example_usage()
```
