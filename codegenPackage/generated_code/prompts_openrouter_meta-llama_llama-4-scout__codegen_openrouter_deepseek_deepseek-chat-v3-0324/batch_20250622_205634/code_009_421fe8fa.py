"""
Generated Code Metadata:
========================
Original URL: https://corridorweb.com
Prompt: "Design a web development project plan for a client in India or the USA, incorporating Corridor Web Agency's services and expertise."
Generated: DETERMINISTIC_421fe8fa7241c036
Batch ID: 20250622_205634
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Web Development Project Plan Generator for Corridor Web Agency
This script generates a customized project plan based on client location (India or USA)
and Corridor Web Agency's service offerings.
"""

from enum import Enum
from dataclasses import dataclass
from typing import List, Dict
import datetime
import json

class Country(Enum):
    INDIA = "India"
    USA = "USA"

class ServiceTier(Enum):
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"

@dataclass
class Service:
    name: str
    description: str
    tiers: Dict[ServiceTier, str]
    included_in: List[ServiceTier]

@dataclass
class ProjectPhase:
    name: str
    description: str
    duration_weeks: int
    dependencies: List[str]

@dataclass
class ProjectPlan:
    client_name: str
    country: Country
    start_date: datetime.date
    services: List[Service]
    phases: List[ProjectPhase]
    timeline: Dict[str, datetime.date]
    pricing: Dict[ServiceTier, float]

class ProjectPlanGenerator:
    def __init__(self):
        self.services = self._initialize_services()
        self.phases = self._initialize_phases()
    
    def _initialize_services(self) -> List[Service]:
        return [
            Service(
                name="Web Design",
                description="Custom UI/UX design for your website",
                tiers={
                    ServiceTier.BASIC: "Template-based design",
                    ServiceTier.STANDARD: "Custom design with 2 revisions",
                    ServiceTier.PREMIUM: "Fully custom design with unlimited revisions"
                },
                included_in=[ServiceTier.BASIC, ServiceTier.STANDARD, ServiceTier.PREMIUM]
            ),
            Service(
                name="Frontend Development",
                description="Implementation of responsive frontend",
                tiers={
                    ServiceTier.BASIC: "Basic responsive layout",
                    ServiceTier.STANDARD: "Interactive elements and animations",
                    ServiceTier.PREMIUM: "Advanced animations and micro-interactions"
                },
                included_in=[ServiceTier.BASIC, ServiceTier.STANDARD, ServiceTier.PREMIUM]
            ),
            Service(
                name="Backend Development",
                description="Server-side functionality and database",
                tiers={
                    ServiceTier.STANDARD: "Basic CRUD operations",
                    ServiceTier.PREMIUM: "Advanced APIs and microservices"
                },
                included_in=[ServiceTier.STANDARD, ServiceTier.PREMIUM]
            ),
            Service(
                name="SEO Optimization",
                description="Search engine optimization services",
                tiers={
                    ServiceTier.STANDARD: "Basic on-page SEO",
                    ServiceTier.PREMIUM: "Comprehensive SEO strategy"
                },
                included_in=[ServiceTier.STANDARD, ServiceTier.PREMIUM]
            )
        ]
    
    def _initialize_phases(self) -> List[ProjectPhase]:
        return [
            ProjectPhase(
                name="Discovery",
                description="Requirements gathering and planning",
                duration_weeks=2,
                dependencies=[]
            ),
            ProjectPhase(
                name="Design",
                description="UI/UX design creation",
                duration_weeks=3,
                dependencies=["Discovery"]
            ),
            ProjectPhase(
                name="Development",
                description="Frontend and backend implementation",
                duration_weeks=6,
                dependencies=["Design"]
            ),
            ProjectPhase(
                name="Testing",
                description="Quality assurance and bug fixing",
                duration_weeks=2,
                dependencies=["Development"]
            ),
            ProjectPhase(
                name="Launch",
                description="Deployment and go-live",
                duration_weeks=1,
                dependencies=["Testing"]
            )
        ]
    
    def _calculate_pricing(self, country: Country, tier: ServiceTier) -> Dict[ServiceTier, float]:
        base_prices = {
            ServiceTier.BASIC: 2000,
            ServiceTier.STANDARD: 5000,
            ServiceTier.PREMIUM: 10000
        }
        
        if country == Country.USA:
            return {k: v * 1.3 for k, v in base_prices.items()}
        return base_prices
    
    def _build_timeline(self, start_date: datetime.date, phases: List[ProjectPhase]) -> Dict[str, datetime.date]:
        timeline = {}
        current_date = start_date
        
        for phase in phases:
            timeline[f"{phase.name}_start"] = current_date
            current_date += datetime.timedelta(weeks=phase.duration_weeks)
            timeline[f"{phase.name}_end"] = current_date
        
        return timeline
    
    def generate_plan(self, client_name: str, country: Country, tier: ServiceTier, start_date: datetime.date) -> ProjectPlan:
        try:
            if not isinstance(country, Country):
                raise ValueError("Invalid country specified")
            
            selected_services = [s for s in self.services if tier in s.included_in]
            
            plan = ProjectPlan(
                client_name=client_name,
                country=country,
                start_date=start_date,
                services=selected_services,
                phases=self.phases,
                timeline=self._build_timeline(start_date, self.phases),
                pricing=self._calculate_pricing(country, tier)
            )
            
            return plan
        except Exception as e:
            raise Exception(f"Failed to generate project plan: {str(e)}")
    
    def export_to_json(self, plan: ProjectPlan) -> str:
        try:
            def json_serial(obj):
                if isinstance(obj, (datetime.date, datetime.datetime)):
                    return obj.isoformat()
                if isinstance(obj, Enum):
                    return obj.value
                raise TypeError(f"Type {type(obj)} not serializable")
            
            plan_dict = {
                "client_name": plan.client_name,
                "country": plan.country.value,
                "start_date": plan.start_date.isoformat(),
                "services": [
                    {
                        "name": s.name,
                        "description": s.description,
                        "tier_offering": {k.value: v for k, v in s.tiers.items()}
                    } for s in plan.services
                ],
                "phases": [
                    {
                        "name": p.name,
                        "description": p.description,
                        "duration_weeks": p.duration_weeks,
                        "dependencies": p.dependencies
                    } for p in plan.phases
                ],
                "timeline": {k: v.isoformat() for k, v in plan.timeline.items()},
                "pricing": {k.value: v for k, v in plan.pricing.items()}
            }
            
            return json.dumps(plan_dict, indent=2, default=json_serial)
        except Exception as e:
            raise Exception(f"Failed to export project plan: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        generator = ProjectPlanGenerator()
        plan = generator.generate_plan(
            client_name="Acme Corp",
            country=Country.USA,
            tier=ServiceTier.PREMIUM,
            start_date=datetime.date.today()
        )
        
        json_output = generator.export_to_json(plan)
        print(json_output)
    except Exception as e:
        print(f"Error: {str(e)}")
```
