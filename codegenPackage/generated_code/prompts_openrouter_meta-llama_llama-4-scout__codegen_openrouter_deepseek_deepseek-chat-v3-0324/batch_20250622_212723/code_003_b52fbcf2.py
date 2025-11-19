"""
Generated Code Metadata:
========================
Original URL: https://uniaircargo.id
Prompt: "Recommend a suitable logistics solution for a company looking to export goods from Indonesia to Australia, considering Uniair Cargo's services and network."
Generated: DETERMINISTIC_b52fbcf2d0493c6c
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Logistics Solution Recommender for Indonesia to Australia Exports

This script evaluates Uniair Cargo's services against company requirements
to recommend suitable logistics solutions for exporting goods from Indonesia to Australia.
"""

import json
from dataclasses import dataclass
from typing import List, Optional, Dict

@dataclass
class LogisticsRequirement:
    """
    Represents the company's logistics requirements
    """
    cargo_type: str
    weight: float  # in kg
    volume: float  # in cubic meters
    urgency: str  # 'standard', 'express', 'priority'
    budget: float  # in USD
    special_requirements: List[str]  # e.g., ['temperature_control', 'fragile']

@dataclass
class LogisticsService:
    """
    Represents a logistics service option
    """
    name: str
    provider: str
    transit_time: str  # e.g., '3-5 days'
    cost_per_kg: float
    max_volume: float
    supported_cargo_types: List[str]
    special_capabilities: List[str]
    reliability_score: float  # 0-1

class LogisticsRecommender:
    """
    Recommends logistics solutions based on requirements
    """
    
    def __init__(self):
        self.services = self._load_services()
    
    def _load_services(self) -> List[LogisticsService]:
        """Load available logistics services"""
        try:
            with open('uniair_services.json', 'r') as f:
                services_data = json.load(f)
                return [
                    LogisticsService(
                        name=service['name'],
                        provider=service['provider'],
                        transit_time=service['transit_time'],
                        cost_per_kg=service['cost_per_kg'],
                        max_volume=service['max_volume'],
                        supported_cargo_types=service['supported_cargo_types'],
                        special_capabilities=service['special_capabilities'],
                        reliability_score=service['reliability_score']
                    )
                    for service in services_data
                ]
        except FileNotFoundError:
            raise Exception("Service data file not found")
        except json.JSONDecodeError:
            raise Exception("Invalid service data format")
        except KeyError as e:
            raise Exception(f"Missing required field in service data: {e}")
    
    def _matches_requirements(self, service: LogisticsService, req: LogisticsRequirement) -> bool:
        """Check if a service matches the requirements"""
        if req.cargo_type not in service.supported_cargo_types:
            return False
        
        if req.weight * service.cost_per_kg > req.budget:
            return False
        
        if req.volume > service.max_volume:
            return False
        
        for special_req in req.special_requirements:
            if special_req not in service.special_capabilities:
                return False
        
        return True
    
    def _score_service(self, service: LogisticsService, req: LogisticsRequirement) -> float:
        """Score a service based on how well it matches requirements"""
        score = service.reliability_score * 0.5
        
        # Higher score for faster services if urgency is high
        if req.urgency == 'priority':
            if 'express' in service.name.lower():
                score += 0.3
        elif req.urgency == 'express':
            if 'express' in service.name.lower():
                score += 0.2
        
        # Lower cost increases score
        cost = req.weight * service.cost_per_kg
        cost_ratio = min(1, req.budget / cost) if cost > 0 else 1
        score += cost_ratio * 0.2
        
        return score
    
    def recommend(self, requirements: LogisticsRequirement) -> Dict[str, List[LogisticsService]]:
        """
        Recommend logistics solutions based on requirements
        
        Returns:
            Dict with 'recommended' and 'alternative' services
        """
        if not isinstance(requirements, LogisticsRequirement):
            raise ValueError("Invalid requirements format")
        
        matching_services = [
            service for service in self.services
            if self._matches_requirements(service, requirements)
        ]
        
        if not matching_services:
            return {'recommended': [], 'alternative': []}
        
        # Sort by score
        scored_services = sorted(
            [(service, self._score_service(service, requirements)) 
             for service in matching_services],
            key=lambda x: x[1],
            reverse=True
        )
        
        # Separate into recommended (top 3) and alternatives
        recommended = [service for service, score in scored_services[:3]]
        alternative = [service for service, score in scored_services[3:]]
        
        return {
            'recommended': recommended,
            'alternative': alternative
        }

# Example usage
if __name__ == "__main__":
    try:
        recommender = LogisticsRecommender()
        
        # Example requirements
        requirements = LogisticsRequirement(
            cargo_type="perishable",
            weight=500,
            volume=2.5,
            urgency="express",
            budget=2000,
            special_requirements=["temperature_control"]
        )
        
        recommendations = recommender.recommend(requirements)
        
        print("Recommended Services:")
        for service in recommendations['recommended']:
            print(f"- {service.name} by {service.provider}")
            print(f"  Cost: ${service.cost_per_kg * requirements.weight:.2f}")
            print(f"  Transit: {service.transit_time}")
            print(f"  Reliability: {service.reliability_score * 100:.1f}%")
        
        if recommendations['alternative']:
            print("\nAlternative Services:")
            for service in recommendations['alternative']:
                print(f"- {service.name} by {service.provider}")
    
    except Exception as e:
        print(f"Error: {str(e)}")
```
