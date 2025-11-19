"""
Generated Code Metadata:
========================
Original URL: https://creocollective.io
Prompt: "Write a marketing campaign proposal for a technology company, including strategies for social media, live video, and graphics, similar to Creo Collective's work with BigPanda."
Generated: DETERMINISTIC_1e02c06515635903
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Marketing Campaign Proposal Generator for Technology Companies
Inspired by Creo Collective's work with BigPanda
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import json

@dataclass
class CampaignComponent:
    """Base class for campaign components"""
    title: str
    description: str
    platforms: List[str]
    duration_days: int
    resources_needed: List[str]
    success_metrics: List[str]
    budget: Optional[float] = None

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "platforms": self.platforms,
            "duration_days": self.duration_days,
            "resources_needed": self.resources_needed,
            "success_metrics": self.success_metrics,
            "budget": self.budget
        }

class CampaignProposal:
    """Generates a comprehensive marketing campaign proposal"""
    
    def __init__(self, company_name: str, product_name: str, campaign_theme: str):
        self.company_name = company_name
        self.product_name = product_name
        self.campaign_theme = campaign_theme
        self.components = []
        self.start_date = datetime.now() + timedelta(days=7)
        self.end_date = self.start_date + timedelta(days=30)
        
    def add_component(self, component: CampaignComponent):
        """Add a component to the campaign"""
        self.components.append(component)
        
    def generate_timeline(self) -> Dict:
        """Generate campaign timeline with milestones"""
        timeline = {}
        current_date = self.start_date
        
        for component in self.components:
            end_date = current_date + timedelta(days=component.duration_days)
            timeline[component.title] = {
                "start_date": current_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "milestones": [
                    f"Creative assets finalized - {current_date.strftime('%Y-%m-%d')}",
                    f"Launch - {(current_date + timedelta(days=2)).strftime('%Y-%m-%d')}",
                    f"Mid-campaign review - {(current_date + timedelta(days=component.duration_days//2)).strftime('%Y-%m-%d')}"
                ]
            }
            current_date = end_date + timedelta(days=1)
            
        return timeline
    
    def calculate_total_budget(self) -> float:
        """Calculate total campaign budget"""
        return sum(comp.budget for comp in self.components if comp.budget is not None)
    
    def generate_proposal(self) -> Dict:
        """Generate complete proposal document"""
        if not self.components:
            raise ValueError("No campaign components added")
            
        return {
            "company": self.company_name,
            "product": self.product_name,
            "theme": self.campaign_theme,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "total_budget": self.calculate_total_budget(),
            "timeline": self.generate_timeline(),
            "components": [comp.to_dict() for comp in self.components]
        }
    
    def save_to_json(self, filename: str):
        """Save proposal to JSON file"""
        proposal = self.generate_proposal()
        with open(filename, 'w') as f:
            json.dump(proposal, f, indent=4)

def generate_sample_proposal():
    """Generate a sample campaign proposal"""
    proposal = CampaignProposal(
        company_name="TechCorp",
        product_name="AI Observability Platform",
        campaign_theme="See More, Solve Faster"
    )
    
    # Social Media Component
    social_media = CampaignComponent(
        title="Social Media Blitz",
        description="Multi-platform social media campaign with targeted content",
        platforms=["LinkedIn", "Twitter", "Facebook"],
        duration_days=14,
        resources_needed=["Social media manager", "Content writer", "Graphic designer"],
        success_metrics=["Engagement rate", "Click-through rate", "Follower growth"],
        budget=15000.00
    )
    
    # Live Video Component
    live_video = CampaignComponent(
        title="Live Video Series",
        description="Weekly live demos and expert panels showcasing product capabilities",
        platforms=["YouTube", "LinkedIn Live", "Twitch"],
        duration_days=21,
        resources_needed=["Video producer", "Host", "Technical experts"],
        success_metrics=["Viewership numbers", "Audience retention", "Lead generation"],
        budget=25000.00
    )
    
    # Graphics Component
    graphics = CampaignComponent(
        title="Visual Storytelling",
        description="High-impact graphics and infographics for digital channels",
        platforms=["Website", "Email", "Social Media"],
        duration_days=30,
        resources_needed=["Graphic designer", "UI/UX specialist", "Copywriter"],
        success_metrics=["Asset downloads", "Shares", "Brand recall"],
        budget=18000.00
    )
    
    proposal.add_component(social_media)
    proposal.add_component(live_video)
    proposal.add_component(graphics)
    
    return proposal

if __name__ == "__main__":
    try:
        proposal = generate_sample_proposal()
        proposal.save_to_json("tech_campaign_proposal.json")
        print("Campaign proposal generated successfully!")
    except Exception as e:
        print(f"Error generating proposal: {str(e)}")
```
