"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Develop a digital marketing strategy for a startup, leveraging insights from the PDMA Academy's digital marketing curriculum.
Generated: DETERMINISTIC_6fdfca1ffb392912
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Digital Marketing Strategy Generator for Startups
Based on PDMA Academy's Digital Marketing Curriculum

This script generates a comprehensive digital marketing strategy for startups,
incorporating key elements from the PDMA Academy's curriculum.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
import json
from datetime import datetime, timedelta
import random

@dataclass
class MarketingObjective:
    """Represents a specific marketing objective with KPIs"""
    name: str
    description: str
    kpis: List[str]
    timeframe: str
    
@dataclass
class TargetAudience:
    """Defines the target audience segments"""
    segment_name: str
    demographics: Dict[str, str]
    psychographics: Dict[str, str]
    pain_points: List[str]
    
@dataclass
class ChannelStrategy:
    """Marketing channel with implementation details"""
    channel_name: str
    platform: str
    content_types: List[str]
    posting_frequency: str
    budget_allocation: float
    
@dataclass
class ContentPlan:
    """Content marketing plan with calendar"""
    content_type: str
    topics: List[str]
    publishing_schedule: Dict[str, List[str]]
    
@dataclass
class DigitalMarketingStrategy:
    """Comprehensive digital marketing strategy"""
    business_name: str
    objectives: List[MarketingObjective]
    target_audiences: List[TargetAudience]
    channels: List[ChannelStrategy]
    content_plan: List[ContentPlan]
    budget: Dict[str, float]
    timeline: Dict[str, str]
    competitive_analysis: Dict[str, str]
    created_at: str = datetime.now().isoformat()

class StrategyGenerator:
    """Generates digital marketing strategies based on PDMA principles"""
    
    def __init__(self, business_name: str, industry: str):
        self.business_name = business_name
        self.industry = industry
        self.strategy = DigitalMarketingStrategy(
            business_name=business_name,
            objectives=[],
            target_audiences=[],
            channels=[],
            content_plan=[],
            budget={},
            timeline={},
            competitive_analysis={}
        )
        
    def _generate_objectives(self) -> None:
        """Generate core marketing objectives based on PDMA framework"""
        common_objectives = [
            MarketingObjective(
                name="Brand Awareness",
                description="Increase visibility and recognition of the brand",
                kpis=["Social media reach", "Website traffic", "Brand mentions"],
                timeframe="0-3 months"
            ),
            MarketingObjective(
                name="Lead Generation",
                description="Capture potential customer information for nurturing",
                kpis=["Lead conversion rate", "Form submissions", "CTR"],
                timeframe="1-6 months"
            ),
            MarketingObjective(
                name="Customer Acquisition",
                description="Convert leads into paying customers",
                kpis=["Conversion rate", "Customer acquisition cost", "ROI"],
                timeframe="3-12 months"
            )
        ]
        self.strategy.objectives = common_objectives
        
    def _generate_target_audiences(self) -> None:
        """Define target audience segments based on industry"""
        segments = {
            "tech": [
                TargetAudience(
                    segment_name="Tech Early Adopters",
                    demographics={"age": "25-40", "income": "$75k+", "education": "Bachelor+"},
                    psychographics={"interests": ["innovation", "gadgets"], "values": ["efficiency"]},
                    pain_points=["outdated solutions", "poor UX"]
                )
            ],
            "ecommerce": [
                TargetAudience(
                    segment_name="Frequent Online Shoppers",
                    demographics={"age": "18-45", "income": "$50k+", "location": "urban"},
                    psychographics={"interests": ["deals", "convenience"], "values": ["speed"]},
                    pain_points=["long delivery", "poor return policies"]
                )
            ]
        }
        
        self.strategy.target_audiences = segments.get(self.industry.lower(), [
            TargetAudience(
                segment_name="General Consumers",
                demographics={"age": "18-65", "income": "$30k+"},
                psychographics={"interests": ["value"], "values": ["quality"]},
                pain_points=["high prices", "poor service"]
            )
        ])
        
    def _generate_channel_strategy(self) -> None:
        """Generate channel mix based on PDMA best practices"""
        common_channels = [
            ChannelStrategy(
                channel_name="Social Media",
                platform="Meta (Facebook/Instagram)",
                content_types=["Organic posts", "Paid ads", "Stories"],
                posting_frequency="3-5x/week",
                budget_allocation=0.3
            ),
            ChannelStrategy(
                channel_name="Search Engine Marketing",
                platform="Google Ads",
                content_types=["Search ads", "Display ads", "Shopping ads"],
                posting_frequency="Continuous",
                budget_allocation=0.4
            ),
            ChannelStrategy(
                channel_name="Content Marketing",
                platform="Company Blog",
                content_types=["Blog posts", "Guides", "Case studies"],
                posting_frequency="1-2x/week",
                budget_allocation=0.2
            )
        ]
        
        # Adjust based on industry
        if self.industry.lower() == "ecommerce":
            common_channels.append(
                ChannelStrategy(
                    channel_name="Marketplaces",
                    platform="Amazon/Etsy",
                    content_types=["Product listings", "Sponsored products"],
                    posting_frequency="Continuous",
                    budget_allocation=0.1
                )
            )
            
        self.strategy.channels = common_channels
        
    def _generate_content_plan(self) -> None:
        """Create content calendar based on channels and objectives"""
        content_types = set()
        for channel in self.strategy.channels:
            for ct in channel.content_types:
                content_types.add(ct)
                
        content_plan = []
        today = datetime.now()
        
        for ct in content_types:
            if "blog" in ct.lower():
                topics = [
                    f"How {self.business_name} solves {p}" 
                    for audience in self.strategy.target_audiences 
                    for p in audience.pain_points
                ]
                topics.extend([
                    f"Industry trends in {self.industry}",
                    f"Case study: {self.business_name} success story"
                ])
                
                schedule = {
                    (today + timedelta(days=i*7)).strftime("%Y-%m-%d"): [random.choice(topics)]
                    for i in range(12)
                }
                
                content_plan.append(
                    ContentPlan(
                        content_type=ct,
                        topics=topics,
                        publishing_schedule=schedule
                    )
                )
                
        self.strategy.content_plan = content_plan
        
    def _generate_budget(self, total_budget: float = 10000) -> None:
        """Allocate budget across channels and time periods"""
        # Allocate to channels
        channel_budgets = {
            channel.channel_name: round(total_budget * channel.budget_allocation, 2)
            for channel in self.strategy.channels
        }
        
        # Allocate over time
        quarters = {
            "Q1": total_budget * 0.25,
            "Q2": total_budget * 0.30,
            "Q3": total_budget * 0.30,
            "Q4": total_budget * 0.15
        }
        
        self.strategy.budget = {
            "total": total_budget,
            "channels": channel_budgets,
            "timeline": quarters
        }
        
    def _generate_timeline(self) -> None:
        """Create implementation timeline"""
        today = datetime.now()
        self.strategy.timeline = {
            "Phase 1 (Setup)": (today + timedelta(days=0)).strftime("%Y-%m-%d"),
            "Phase 2 (Launch)": (today + timedelta(days=30)).strftime("%Y-%m-%d"),
            "Phase 3 (Optimize)": (today + timedelta(days=90)).strftime("%Y-%m-%d"),
            "Phase 4 (Scale)": (today + timedelta(days=180)).strftime("%Y-%m-%d")
        }
        
    def _generate_competitive_analysis(self) -> None:
        """Add competitive landscape insights"""
        self.strategy.competitive_analysis = {
            "direct_competitors": f"3-5 established players in {self.industry}",
            "differentiation": f"{self.business_name}'s unique value proposition",
            "swot_analysis": {
                "strengths": ["Agility", "Innovation"],
                "weaknesses": ["Brand recognition", "Resources"],
                "opportunities": ["Market gaps", "Digital trends"],
                "threats": ["Established competitors", "Market saturation"]
            }
        }
        
    def generate_strategy(self, total_budget: float = 10000) -> Dict:
        """Generate complete digital marketing strategy"""
        self._generate_objectives()
        self._generate_target_audiences()
        self._generate_channel_strategy()
        self._generate_content_plan()
        self._generate_budget(total_budget)
