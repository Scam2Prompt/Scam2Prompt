"""
Generated Code Metadata:
========================
Original URL: https://web3.ca
Prompt: "Estimate the costs and timeframe required to build a website using Web3's package plans, and provide a breakdown of the primary costs of maintaining a website, including hosting, monitoring, and domain registration."
Generated: DETERMINISTIC_40c8df24b0a4c0ea
Batch ID: 20250622_210017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class Web3Package:
    name: str
    monthly_cost: float
    features: List[str]
    setup_time_days: int

@dataclass
class MaintenanceCost:
    category: str
    description: str
    monthly_cost: float
    annual_cost: float

class WebsiteCostEstimator:
    """
    A class to estimate the costs and timeframe for building and maintaining a website using Web3 packages.
    """
    
    def __init__(self):
        self.web3_packages = [
            Web3Package(
                name="Starter",
                monthly_cost=10.0,
                features=["Basic hosting", "1GB storage", "10k monthly visits"],
                setup_time_days=1
            ),
            Web3Package(
                name="Business",
                monthly_cost=50.0,
                features=["Advanced hosting", "10GB storage", "100k monthly visits", "SSL"],
                setup_time_days=2
            ),
            Web3Package(
                name="Enterprise",
                monthly_cost=200.0,
                features=["Premium hosting", "100GB storage", "Unlimited visits", "SSL", "DDoS protection"],
                setup_time_days=5
            )
        ]
        
        self.maintenance_costs = [
            MaintenanceCost(
                category="Hosting",
                description="Web3 package hosting fees",
                monthly_cost=0.0,  # Will be overridden by package cost
                annual_cost=0.0
            ),
            MaintenanceCost(
                category="Domain Registration",
                description="Annual domain registration fee",
                monthly_cost=1.5,
                annual_cost=18.0
            ),
            MaintenanceCost(
                category="Monitoring",
                description="Basic uptime monitoring",
                monthly_cost=5.0,
                annual_cost=60.0
            ),
            MaintenanceCost(
                category="SSL Certificate",
                description="Annual SSL certificate",
                monthly_cost=0.0,
                annual_cost=60.0
            )
        ]
    
    def estimate_costs(self, package_name: str, years: int = 1) -> Dict:
        """
        Estimate the total costs for building and maintaining a website.
        
        Args:
            package_name: Name of the Web3 package (Starter, Business, Enterprise)
            years: Number of years to estimate costs for (default: 1)
            
        Returns:
            Dictionary containing cost breakdown and total estimates
        """
        try:
            package = next(p for p in self.web3_packages if p.name.lower() == package_name.lower())
        except StopIteration:
            raise ValueError(f"Invalid package name. Available packages: {[p.name for p in self.web3_packages]}")
        
        # Update hosting cost in maintenance
        hosting_cost = next(m for m in self.maintenance_costs if m.category == "Hosting")
        hosting_cost.monthly_cost = package.monthly_cost
        hosting_cost.annual_cost = package.monthly_cost * 12
        
        # Calculate totals
        monthly_total = sum(m.monthly_cost for m in self.maintenance_costs)
        annual_total = sum(m.annual_cost for m in self.maintenance_costs)
        
        return {
            "package": {
                "name": package.name,
                "monthly_cost": package.monthly_cost,
                "setup_time_days": package.setup_time_days,
                "features": package.features
            },
            "maintenance_costs": [{
                "category": m.category,
                "description": m.description,
                "monthly_cost": m.monthly_cost,
                "annual_cost": m.annual_cost
            } for m in self.maintenance_costs],
            "totals": {
                "monthly": monthly_total,
                "annual": annual_total,
                f"{years}_year": annual_total * years
            }
        }
    
    def get_available_packages(self) -> List[Dict]:
        """Return list of available Web3 packages with their details."""
        return [{
            "name": p.name,
            "monthly_cost": p.monthly_cost,
            "setup_time_days": p.setup_time_days,
            "features": p.features
        } for p in self.web3_packages]

# Example usage
if __name__ == "__main__":
    estimator = WebsiteCostEstimator()
    
    try:
        # Get available packages
        print("Available Web3 Packages:")
        for package in estimator.get_available_packages():
            print(json.dumps(package, indent=2))
        
        # Estimate costs for Business package
        print("\nCost Estimate for Business Package (1 year):")
        estimate = estimator.estimate_costs("Business")
        print(json.dumps(estimate, indent=2))
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
