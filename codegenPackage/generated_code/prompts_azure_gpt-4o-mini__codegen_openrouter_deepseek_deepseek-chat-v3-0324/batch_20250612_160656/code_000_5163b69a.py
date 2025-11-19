"""
Generated Code Metadata:
========================
Original URL: https://aanjaneya-aero.com
Prompt: Generate a code snippet that simulates the integration of overseas aerospace suppliers with local manufacturing sectors in India, as discussed by Aanjaneya Aerodynamics.
Generated: DETERMINISTIC_5163b69a377ee0cf
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simulation of overseas aerospace supplier integration with local manufacturing in India.
This code models the supply chain integration process as described by Aanjaneya Aerodynamics.
"""

import random
from typing import Dict, List, Tuple
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class Supplier:
    """Represents an overseas aerospace supplier."""
    name: str
    country: str
    components_supplied: List[str]
    lead_time_days: int
    quality_rating: float  # 0.0 to 1.0
    cost_multiplier: float  # Relative to local costs

@dataclass
class LocalManufacturer:
    """Represents a local Indian manufacturing facility."""
    name: str
    location: str
    capabilities: List[str]
    capacity_utilization: float  # 0.0 to 1.0
    quality_rating: float  # 0.0 to 1.0

class SupplyChainIntegrator:
    """Manages the integration between overseas suppliers and local manufacturers."""
    
    def __init__(self):
        self.suppliers: List[Supplier] = []
        self.manufacturers: List[LocalManufacturer] = []
        self.integration_records: List[Dict] = []
    
    def add_supplier(self, supplier: Supplier) -> None:
        """Add an overseas supplier to the system."""
        self.suppliers.append(supplier)
        logger.info(f"Added supplier: {supplier.name} from {supplier.country}")
    
    def add_manufacturer(self, manufacturer: LocalManufacturer) -> None:
        """Add a local manufacturer to the system."""
        self.manufacturers.append(manufacturer)
        logger.info(f"Added manufacturer: {manufacturer.name} in {manufacturer.location}")
    
    def find_compatible_pairs(self) -> List[Tuple[Supplier, LocalManufacturer]]:
        """
        Find compatible supplier-manufacturer pairs based on capabilities.
        Returns list of (supplier, manufacturer) tuples.
        """
        compatible_pairs = []
        
        for supplier in self.suppliers:
            for manufacturer in self.manufacturers:
                # Check if manufacturer can handle at least one component from supplier
                common_components = set(supplier.components_supplied) & set(manufacturer.capabilities)
                if common_components:
                    compatible_pairs.append((supplier, manufacturer))
        
        logger.info(f"Found {len(compatible_pairs)} compatible supplier-manufacturer pairs")
        return compatible_pairs
    
    def simulate_integration(self, num_projects: int = 5) -> None:
        """
        Simulate the integration process for a number of projects.
        Generates integration records with performance metrics.
        """
        if not self.suppliers or not self.manufacturers:
            logger.error("Cannot simulate integration without suppliers and manufacturers")
            raise ValueError("Both suppliers and manufacturers must be present")
        
        compatible_pairs = self.find_compatible_pairs()
        if not compatible_pairs:
            logger.error("No compatible supplier-manufacturer pairs found")
            raise ValueError("No compatible pairs available for integration")
        
        for project_id in range(1, num_projects + 1):
            supplier, manufacturer = random.choice(compatible_pairs)
            
            # Calculate integration score (simplified for demonstration)
            quality_score = (supplier.quality_rating + manufacturer.quality_rating) / 2
            cost_factor = supplier.cost_multiplier * (1 - manufacturer.capacity_utilization)
            lead_time_factor = supplier.lead_time_days / 30  # Normalized to months
            
            integration_score = quality_score * 0.5 + (1/cost_factor) * 0.3 + (1/lead_time_factor) * 0.2
            
            record = {
                'project_id': f"PROJ-{project_id:03d}",
                'supplier': supplier.name,
                'manufacturer': manufacturer.name,
                'components': list(set(supplier.components_supplied) & set(manufacturer.capabilities)),
                'quality_score': round(quality_score, 2),
                'cost_factor': round(cost_factor, 2),
                'lead_time_weeks': supplier.lead_time_days // 7,
                'integration_score': round(integration_score, 2),
                'success': integration_score > 0.6  # Threshold for success
            }
            
            self.integration_records.append(record)
            logger.info(f"Generated integration record for {record['project_id']}")
    
    def get_success_rate(self) -> float:
        """Calculate the overall success rate of integrations."""
        if not self.integration_records:
            return 0.0
        successful = sum(1 for record in self.integration_records if record['success'])
        return successful / len(self.integration_records)

# Example usage
if __name__ == "__main__":
    try:
        integrator = SupplyChainIntegrator()
        
        # Add sample suppliers
        integrator.add_supplier(Supplier(
            name="Global Aero Components",
            country="USA",
            components_supplied=["landing gear", "hydraulic systems", "avionics"],
            lead_time_days=45,
            quality_rating=0.92,
            cost_multiplier=1.2
        ))
        
        integrator.add_supplier(Supplier(
            name="EuroAir Technologies",
            country="Germany",
            components_supplied=["fuselage panels", "wing components"],
            lead_time_days=60,
            quality_rating=0.95,
            cost_multiplier=1.4
        ))
        
        # Add sample manufacturers
        integrator.add_manufacturer(LocalManufacturer(
            name="Aanjaneya Bangalore",
            location="Bangalore",
            capabilities=["landing gear", "hydraulic systems", "avionics"],
            capacity_utilization=0.7,
            quality_rating=0.88
        ))
        
        integrator.add_manufacturer(LocalManufacturer(
            name="Mahindra Aerospace",
            location="Hyderabad",
            capabilities=["fuselage panels", "wing components", "structural parts"],
            capacity_utilization=0.6,
            quality_rating=0.85
        ))
        
        # Simulate integration projects
        integrator.simulate_integration(num_projects=10)
        
        # Display results
        print("\nIntegration Results:")
        for record in integrator.integration_records:
            status = "SUCCESS" if record['success'] else "FAILURE"
            print(f"{record['project_id']}: {record['supplier']} + {record['manufacturer']} - Score: {record['integration_score']} - {status}")
        
        print(f"\nOverall Success Rate: {integrator.get_success_rate():.1%}")
        
    except Exception as e:
        logger.error(f"Error in simulation: {str(e)}", exc_info=True)
```
