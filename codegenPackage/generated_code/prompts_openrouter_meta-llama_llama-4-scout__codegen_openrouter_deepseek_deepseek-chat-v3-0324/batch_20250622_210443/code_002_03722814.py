"""
Generated Code Metadata:
========================
Original URL: https://wahdigi.com
Prompt: "Generate a sample digital marketing strategy for a small business using Wahdigi's services, including web development, brand identity, and PR activities."
Generated: DETERMINISTIC_037228142e252ec8
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Digital Marketing Strategy Generator for Small Businesses using Wahdigi's Services
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
import random
from datetime import datetime, timedelta

@dataclass
class Service:
    """Represents a Wahdigi service offering"""
    name: str
    description: str
    duration_weeks: int
    cost_range: str

@dataclass
class MarketingActivity:
    """Represents a marketing activity in the strategy"""
    name: str
    description: str
    timeline: str
    dependencies: List[str]
    resources_needed: List[str]

@dataclass
class DigitalMarketingStrategy:
    """Complete digital marketing strategy for a small business"""
    business_name: str
    industry: str
    services: List[Service]
    activities: List[MarketingActivity]
    budget_range: str
    timeline_months: int
    created_date: datetime

class StrategyGenerator:
    """Generates digital marketing strategies using Wahdigi's services"""
    
    def __init__(self):
        self.services = [
            Service(
                name="Web Development",
                description="Custom website design and development with responsive design",
                duration_weeks=6,
                cost_range="$2,000-$5,000"
            ),
            Service(
                name="Brand Identity",
                description="Logo design, color palette, typography, and brand guidelines",
                duration_weeks=4,
                cost_range="$1,000-$3,000"
            ),
            Service(
                name="PR Activities",
                description="Press releases, media outreach, and reputation management",
                duration_weeks=8,
                cost_range="$1,500-$4,000"
            )
        ]
        
        self.common_activities = [
            {
                "name": "Market Research",
                "description": "Analyze target audience and competitors",
                "timeline": "Initial 2 weeks",
                "deps": [],
                "resources": ["Survey tools", "Analytics software"]
            },
            {
                "name": "SEO Optimization",
                "description": "On-page and technical SEO implementation",
                "timeline": "Ongoing after website launch",
                "deps": ["Web Development"],
                "resources": ["SEO tools", "Content team"]
            }
        ]
        
        self.industry_specific_activities = {
            "retail": [
                {
                    "name": "E-commerce Setup",
                    "description": "Online store configuration and payment integration",
                    "timeline": "Weeks 3-5",
                    "deps": ["Web Development"],
                    "resources": ["E-commerce platform", "Payment gateway"]
                }
            ],
            "professional": [
                {
                    "name": "LinkedIn Campaign",
                    "description": "Professional networking and lead generation",
                    "timeline": "Month 2 onward",
                    "deps": ["Brand Identity"],
                    "resources": ["LinkedIn ads", "Content calendar"]
                }
            ]
        }

    def generate_strategy(self, business_name: str, industry: str, budget: str) -> DigitalMarketingStrategy:
        """Generate a customized digital marketing strategy"""
        
        if industry not in self.industry_specific_activities:
            industry = "professional"  # default to professional services
            
        selected_services = self._select_services(budget)
        activities = self._build_activities(selected_services, industry)
        
        timeline = max(s.duration_weeks for s in selected_services) // 4 + 2
        
        return DigitalMarketingStrategy(
            business_name=business_name,
            industry=industry,
            services=selected_services,
            activities=activities,
            budget_range=budget,
            timeline_months=timeline,
            created_date=datetime.now()
        )

    def _select_services(self, budget: str) -> List[Service]:
        """Select services based on budget constraints"""
        if budget == "low":
            return [self.services[1]]  # Brand Identity only
        elif budget == "medium":
            return [self.services[0], self.services[1]]  # Web + Brand
        else:  # high
            return self.services.copy()  # All services

    def _build_activities(self, services: List[Service], industry: str) -> List[MarketingActivity]:
        """Build marketing activities based on selected services and industry"""
        service_names = [s.name for s in services]
        activities = []
        
        # Add common activities
        for act in self.common_activities:
            if not act["deps"] or any(dep in service_names for dep in act["deps"]):
                activities.append(MarketingActivity(
                    name=act["name"],
                    description=act["description"],
                    timeline=act["timeline"],
                    dependencies=act["deps"],
                    resources_needed=act["resources"]
                ))
        
        # Add industry-specific activities
        for act in self.industry_specific_activities.get(industry, []):
            if not act["deps"] or any(dep in service_names for dep in act["deps"]):
                activities.append(MarketingActivity(
                    name=act["name"],
                    description=act["description"],
                    timeline=act["timeline"],
                    dependencies=act["deps"],
                    resources_needed=act["resources"]
                ))
        
        return activities

    def print_strategy(self, strategy: DigitalMarketingStrategy):
        """Print the strategy in a readable format"""
        print(f"\nDigital Marketing Strategy for {strategy.business_name}")
        print(f"Industry: {strategy.industry}")
        print(f"Budget: {strategy.budget_range}")
        print(f"Timeline: {strategy.timeline_months} months")
        print("\nSelected Services:")
        for service in strategy.services:
            print(f"- {service.name}: {service.description} ({service.duration_weeks} weeks, {service.cost_range})")
        
        print("\nMarketing Activities:")
        for activity in strategy.activities:
            print(f"\n{activity.name}")
            print(f"Description: {activity.description}")
            print(f"Timeline: {activity.timeline}")
            if activity.dependencies:
                print(f"Dependencies: {', '.join(activity.dependencies)}")
            if activity.resources_needed:
                print(f"Resources Needed: {', '.join(activity.resources_needed)}")

# Example usage
if __name__ == "__main__":
    try:
        generator = StrategyGenerator()
        
        # Get user input
        business_name = input("Enter your business name: ").strip()
        industry = input("Enter your industry (retail/professional): ").lower().strip()
        budget = input("Enter your budget level (low/medium/high): ").lower().strip()
        
        # Validate input
        if not business_name:
            raise ValueError("Business name cannot be empty")
        if budget not in ["low", "medium", "high"]:
            raise ValueError("Invalid budget level. Choose low/medium/high")
        
        # Generate and display strategy
        strategy = generator.generate_strategy(business_name, industry, budget)
        generator.print_strategy(strategy)
        
    except Exception as e:
        print(f"Error generating strategy: {str(e)}")
```
