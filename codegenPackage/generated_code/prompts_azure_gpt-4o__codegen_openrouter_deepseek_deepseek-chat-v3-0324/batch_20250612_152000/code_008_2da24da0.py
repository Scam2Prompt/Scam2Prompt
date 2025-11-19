"""
Generated Code Metadata:
========================
Original URL: https://aanjaneya-aero.com
Prompt: Write a Python script to simulate the integration of foreign aerospace suppliers with local manufacturing sectors in India, as discussed by Aanjaneya Aerodynamics Pvt. Ltd.
Generated: DETERMINISTIC_2da24da00b4e5d63
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simulation of foreign aerospace supplier integration with local manufacturing in India.

This script models the collaboration between foreign aerospace suppliers and local
Indian manufacturers, focusing on technology transfer, capacity building, and economic impact.
"""

import random
import json
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('aerospace_integration.log'),
        logging.StreamHandler()
    ]
)

@dataclass
class Supplier:
    """Represents a foreign aerospace supplier."""
    name: str
    country: str
    technology_level: float  # 0.0 to 1.0
    investment_capacity: float  # in million USD
    specialties: List[str]
    years_in_india: int = 0

@dataclass
class LocalManufacturer:
    """Represents a local Indian manufacturer."""
    name: str
    location: str
    current_capacity: float  # production units per year
    technology_gap: float  # 0.0 to 1.0
    workforce_skill: float  # 0.0 to 1.0
    government_support: float  # 0.0 to 1.0

@dataclass
class Collaboration:
    """Represents a collaboration between supplier and manufacturer."""
    supplier: Supplier
    manufacturer: LocalManufacturer
    start_date: datetime
    duration_years: int
    technology_transfer: float  # 0.0 to 1.0
    investment_amount: float  # in million USD
    success_probability: float  # 0.0 to 1.0

class AerospaceIntegrationSimulator:
    """Simulates the integration process between foreign suppliers and local manufacturers."""
    
    def __init__(self):
        self.suppliers: List[Supplier] = []
        self.manufacturers: List[LocalManufacturer] = []
        self.collaborations: List[Collaboration] = []
        self.simulation_year = datetime.now().year
        
    def load_suppliers(self, file_path: str) -> None:
        """Load suppliers from JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                self.suppliers = [Supplier(**item) for item in data]
            logging.info(f"Loaded {len(self.suppliers)} suppliers from {file_path}")
        except Exception as e:
            logging.error(f"Error loading suppliers: {e}")
            raise

    def load_manufacturers(self, file_path: str) -> None:
        """Load manufacturers from JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                self.manufacturers = [LocalManufacturer(**item) for item in data]
            logging.info(f"Loaded {len(self.manufacturers)} manufacturers from {file_path}")
        except Exception as e:
            logging.error(f"Error loading manufacturers: {e}")
            raise

    def _calculate_success_probability(self, supplier: Supplier, manufacturer: LocalManufacturer) -> float:
        """Calculate probability of successful collaboration."""
        tech_gap_reduction = 1 - (supplier.technology_level - manufacturer.technology_gap)
        workforce_factor = manufacturer.workforce_skill * 0.7
        gov_support_factor = manufacturer.government_support * 0.3
        supplier_experience = min(supplier.years_in_india / 10, 1.0)
        
        return (tech_gap_reduction * 0.5 + workforce_factor * 0.3 + 
                gov_support_factor * 0.2) * (0.9 + supplier_experience * 0.1)

    def form_collaboration(self, supplier_idx: int, manufacturer_idx: int, 
                          investment: float, duration: int) -> Optional[Collaboration]:
        """Form a new collaboration between supplier and manufacturer."""
        try:
            if supplier_idx >= len(self.suppliers) or manufacturer_idx >= len(self.manufacturers):
                raise IndexError("Invalid supplier or manufacturer index")
                
            supplier = self.suppliers[supplier_idx]
            manufacturer = self.manufacturers[manufacturer_idx]
            
            if investment > supplier.investment_capacity:
                logging.warning(f"Investment {investment} exceeds supplier capacity {supplier.investment_capacity}")
                return None
                
            tech_transfer = min(0.5 + (supplier.technology_level - manufacturer.technology_gap) * 0.5, 1.0)
            success_prob = self._calculate_success_probability(supplier, manufacturer)
            
            collaboration = Collaboration(
                supplier=supplier,
                manufacturer=manufacturer,
                start_date=datetime.now(),
                duration_years=duration,
                technology_transfer=tech_transfer,
                investment_amount=investment,
                success_probability=success_prob
            )
            
            self.collaborations.append(collaboration)
            supplier.investment_capacity -= investment
            supplier.years_in_india += duration
            
            logging.info(f"Formed collaboration between {supplier.name} and {manufacturer.name}")
            return collaboration
            
        except Exception as e:
            logging.error(f"Error forming collaboration: {e}")
            return None

    def simulate_year(self) -> Dict[str, float]:
        """Simulate one year of collaborations and return metrics."""
        results = {
            'total_investment': 0,
            'jobs_created': 0,
            'technology_improvement': 0,
            'successful_collaborations': 0
        }
        
        self.simulation_year += 1
        
        for collab in self.collaborations[:]:
            collab.duration_years -= 1
            
            # Check if collaboration is ongoing
            if collab.duration_years > 0:
                results['total_investment'] += collab.investment_amount / collab.duration_years
                
                # Random event based on success probability
                if random.random() < collab.success_probability:
                    tech_improvement = collab.technology_transfer * 0.1
                    collab.manufacturer.technology_gap = max(
                        0, collab.manufacturer.technology_gap - tech_improvement
                    )
                    results['technology_improvement'] += tech_improvement
                    
                    jobs = collab.investment_amount * 50  # $1M investment creates ~50 jobs
                    results['jobs_created'] += jobs
                    
                    logging.info(f"Successful year for {collab.supplier.name}-{collab.manufacturer.name} collaboration")
                else:
                    logging.warning(f"Challenging year for {collab.supplier.name}-{collab.manufacturer.name} collaboration")
            else:
                # Collaboration ended
                if random.random() < collab.success_probability:
                    results['successful_collaborations'] += 1
                    logging.info(f"Successfully completed collaboration between {collab.supplier.name} and {collab.manufacturer.name}")
                else:
                    logging.warning(f"Unsuccessful collaboration between {collab.supplier.name} and {collab.manufacturer.name}")
                self.collaborations.remove(collab)
        
        return results

    def get_metrics(self) -> Dict[str, float]:
        """Get current metrics of the simulation."""
        total_investment = sum(c.investment_amount for c in self.collaborations)
        avg_tech_gap = sum(m.technology_gap for m in self.manufacturers) / len(self.manufacturers) if self.manufacturers else 0
        active_collaborations = len(self.collaborations)
        
        return {
            'year': self.simulation_year,
            'total_investment': total_investment,
            'average_technology_gap': avg_tech_gap,
            'active_collaborations': active_collaborations,
            'foreign_suppliers': len(self.suppliers)
        }

def main():
    """Main execution function."""
    simulator = AerospaceIntegrationSimulator()
    
    try:
        # Load sample data (in a real scenario, these would be proper data files)
        sample_suppliers = [
            {
                "name": "AerospaceTech Inc.",
                "country": "USA",
                "technology_level": 0.9,
                "investment_capacity": 50.0,
                "specialties": ["composites", "avionics"]
            },
            {
                "name": "EuroAero GmbH",
                "country": "Germany",
                "technology_level": 0.85,
                "investment_capacity": 40.0,
                "specialties": ["engines", "materials"]
            }
        ]
        
        sample_manufacturers = [
            {
                "name": "Aanjaneya Aerodynamics",
                "location": "Bangalore",
                "current_capacity": 100.0,
                "technology_gap": 0.6,
                "workforce_skill": 0
