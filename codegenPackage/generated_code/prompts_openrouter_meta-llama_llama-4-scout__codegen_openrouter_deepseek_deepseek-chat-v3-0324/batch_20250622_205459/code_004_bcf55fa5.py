"""
Generated Code Metadata:
========================
Original URL: https://brinksglobalplantinumservices.com
Prompt: Compare and contrast the features of Brinks Global Platinum Services' logistics services, including ocean freight, air freight, ground freight, and contract freight services.
Generated: DETERMINISTIC_bcf55fa5cf63b612
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Brinks Global Platinum Services Logistics Comparison Tool

This script provides a comparison of Brinks Global Platinum Services' logistics offerings
including ocean freight, air freight, ground freight, and contract freight services.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class LogisticsService:
    """Base class representing a logistics service offering."""
    name: str
    description: str
    speed: str
    cost: str
    capacity: str
    reliability: str
    coverage: str
    special_features: List[str]
    best_for: List[str]
    limitations: List[str]

class LogisticsComparison:
    """Main class to compare Brinks Global Platinum Services logistics offerings."""
    
    def __init__(self):
        self.services = self._initialize_services()
    
    def _initialize_services(self) -> Dict[str, LogisticsService]:
        """Initialize Brinks logistics services with their features."""
        return {
            "ocean_freight": LogisticsService(
                name="Ocean Freight",
                description="International shipping via cargo vessels",
                speed="Slow (weeks to months)",
                cost="Lowest cost option",
                capacity="Highest capacity (FCL/LCL options)",
                reliability="Weather-dependent, moderate reliability",
                coverage="Global port-to-port",
                special_features=[
                    "Ideal for heavy/bulky cargo",
                    "Environmentally friendly per ton-mile",
                    "Specialized container options"
                ],
                best_for=[
                    "Large volume shipments",
                    "Non-perishable goods",
                    "Cost-sensitive shipments"
                ],
                limitations=[
                    "Long transit times",
                    "Port congestion risks",
                    "Limited inland coverage"
                ]
            ),
            "air_freight": LogisticsService(
                name="Air Freight",
                description="Express shipping via commercial/cargo aircraft",
                speed="Fastest (hours to days)",
                cost="Most expensive option",
                capacity="Limited by aircraft size/weight",
                reliability="High reliability with scheduled flights",
                coverage="Major airports worldwide",
                special_features=[
                    "Priority handling available",
                    "Temperature-controlled options",
                    "Secure transit for high-value goods"
                ],
                best_for=[
                    "Time-sensitive shipments",
                    "High-value/perishable goods",
                    "Emergency shipments"
                ],
                limitations=[
                    "Highest cost per kg",
                    "Size/weight restrictions",
                    "Limited to airport locations"
                ]
            ),
            "ground_freight": LogisticsService(
                name="Ground Freight",
                description="Domestic transportation via truck/rail",
                speed="Moderate (days to weeks)",
                cost="Mid-range pricing",
                capacity="Flexible (LTL/FTL options)",
                reliability="Route-dependent, generally reliable",
                coverage="Regional/national networks",
                special_features=[
                    "Door-to-door service",
                    "Real-time tracking",
                    "Flexible scheduling"
                ],
                best_for=[
                    "Domestic shipments",
                    "Time-definite deliveries",
                    "Less-than-container loads"
                ],
                limitations=[
                    "Geographic limitations",
                    "Road condition dependencies",
                    "Border crossing delays"
                ]
            ),
            "contract_freight": LogisticsService(
                name="Contract Freight",
                description="Customized logistics solutions",
                speed="Variable (customized)",
                cost="Negotiated rates",
                capacity="Tailored to needs",
                reliability="High (dedicated resources)",
                coverage="Custom network",
                special_features=[
                    "Dedicated account management",
                    "Custom SLAs",
                    "Integrated technology solutions"
                ],
                best_for=[
                    "High-volume shippers",
                    "Complex supply chains",
                    "Long-term partnerships"
                ],
                limitations=[
                    "Minimum volume commitments",
                    "Longer setup time",
                    "Less flexibility for ad-hoc needs"
                ]
            )
        }
    
    def compare_all_services(self) -> Dict[str, LogisticsService]:
        """Return all services for comparison."""
        return self.services
    
    def compare_by_feature(self, feature: str) -> Dict[str, str]:
        """
        Compare all services by a specific feature.
        
        Args:
            feature: The feature to compare (speed, cost, capacity, etc.)
            
        Returns:
            Dictionary mapping service name to feature value
            
        Raises:
            ValueError: If feature doesn't exist in service attributes
        """
        if not hasattr(LogisticsService, feature):
            raise ValueError(f"Invalid feature: {feature}. Available features: {list(LogisticsService.__annotations__.keys())}")
        
        return {
            service.name: getattr(service, feature)
            for service in self.services.values()
        }
    
    def get_service_details(self, service_name: str) -> Optional[LogisticsService]:
        """
        Get detailed information about a specific service.
        
        Args:
            service_name: Name of the service to retrieve
            
        Returns:
            LogisticsService object if found, None otherwise
        """
        normalized_name = service_name.lower().replace(" ", "_")
        return self.services.get(normalized_name)

def main():
    """Example usage of the logistics comparison tool."""
    try:
        comparison = LogisticsComparison()
        
        # Compare all services
        print("=== All Brinks Logistics Services ===")
        for service in comparison.compare_all_services().values():
            print(f"\n{service.name}:")
            print(f"  Description: {service.description}")
            print(f"  Best for: {', '.join(service.best_for)}")
        
        # Compare by specific feature
        print("\n=== Speed Comparison ===")
        for name, speed in comparison.compare_by_feature("speed").items():
            print(f"{name}: {speed}")
        
        # Get detailed service information
        print("\n=== Ocean Freight Details ===")
        ocean = comparison.get_service_details("ocean freight")
        if ocean:
            print(f"Special Features: {', '.join(ocean.special_features)}")
            print(f"Limitations: {', '.join(ocean.limitations)}")
    
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
