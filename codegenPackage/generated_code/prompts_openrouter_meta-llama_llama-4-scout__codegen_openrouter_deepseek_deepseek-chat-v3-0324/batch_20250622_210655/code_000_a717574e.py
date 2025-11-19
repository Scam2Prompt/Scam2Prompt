"""
Generated Code Metadata:
========================
Original URL: https://nmkt.net
Prompt: "Write a marketing plan for a small agricultural business using services like those offered by NMKT."
Generated: DETERMINISTIC_a717574e875913b3
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Marketing Plan Generator for Small Agricultural Business

This script generates a structured marketing plan template for small agricultural businesses
using services similar to NMKT (a hypothetical marketing service provider).

The plan includes sections for:
- Business Overview
- Target Market Analysis
- Marketing Goals
- Strategies and Tactics
- Budget Allocation
- Implementation Timeline
- Performance Metrics
"""

import datetime
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class BusinessInfo:
    """Contains basic information about the agricultural business"""
    name: str
    location: str
    products: List[str]
    founding_year: int
    unique_selling_points: List[str]

@dataclass
class TargetMarket:
    """Defines the target market segments"""
    demographics: Dict[str, str]
    geographic_area: str
    psychographics: List[str]
    buying_behavior: str

@dataclass
class MarketingGoal:
    """Represents a specific marketing goal"""
    description: str
    metric: str
    target_value: float
    timeframe: str

@dataclass
class MarketingStrategy:
    """Defines a marketing strategy with tactics"""
    name: str
    description: str
    tactics: List[str]
    channels: List[str]
    budget_percentage: float

@dataclass
class BudgetAllocation:
    """Breakdown of marketing budget"""
    total_budget: float
    allocations: Dict[str, float]

@dataclass
class TimelineItem:
    """Represents an item in the implementation timeline"""
    task: str
    start_date: datetime.date
    end_date: datetime.date
    responsible_party: str

@dataclass
class PerformanceMetric:
    """Defines how to measure marketing performance"""
    name: str
    measurement_method: str
    tracking_frequency: str

class MarketingPlanGenerator:
    """Generates a comprehensive marketing plan for agricultural businesses"""
    
    def __init__(self, business_info: BusinessInfo):
        self.business = business_info
        self.target_markets: List[TargetMarket] = []
        self.goals: List[MarketingGoal] = []
        self.strategies: List[MarketingStrategy] = []
        self.budget: Optional[BudgetAllocation] = None
        self.timeline: List[TimelineItem] = []
        self.metrics: List[PerformanceMetric] = []
    
    def add_target_market(self, market: TargetMarket) -> None:
        """Add a target market segment to the plan"""
        self.target_markets.append(market)
    
    def add_goal(self, goal: MarketingGoal) -> None:
        """Add a marketing goal to the plan"""
        self.goals.append(goal)
    
    def add_strategy(self, strategy: MarketingStrategy) -> None:
        """Add a marketing strategy to the plan"""
        self.strategies.append(strategy)
    
    def set_budget(self, budget: BudgetAllocation) -> None:
        """Set the marketing budget allocation"""
        self.budget = budget
    
    def add_timeline_item(self, item: TimelineItem) -> None:
        """Add an item to the implementation timeline"""
        self.timeline.append(item)
    
    def add_performance_metric(self, metric: PerformanceMetric) -> None:
        """Add a performance metric to track"""
        self.metrics.append(metric)
    
    def generate_plan(self) -> str:
        """Generate the complete marketing plan document"""
        if not all([self.target_markets, self.goals, self.strategies, self.budget, self.timeline, self.metrics]):
            raise ValueError("Incomplete marketing plan data")
        
        plan = f"""
        MARKETING PLAN FOR {self.business.name.upper()}
        Generated on: {datetime.date.today()}
        
        ===== BUSINESS OVERVIEW =====
        Name: {self.business.name}
        Location: {self.business.location}
        Products/Services: {', '.join(self.business.products)}
        Founding Year: {self.business.founding_year}
        Unique Selling Points: {', '.join(self.business.unique_selling_points)}
        
        ===== TARGET MARKET ANALYSIS =====
        """
        
        for i, market in enumerate(self.target_markets, 1):
            plan += f"""
        Target Market Segment #{i}:
        - Demographics: {market.demographics}
        - Geographic Area: {market.geographic_area}
        - Psychographics: {', '.join(market.psychographics)}
        - Buying Behavior: {market.buying_behavior}
            """
        
        plan += """
        ===== MARKETING GOALS =====
        """
        
        for goal in self.goals:
            plan += f"""
        - {goal.description}
          Metric: {goal.metric}
          Target: {goal.target_value}
          Timeframe: {goal.timeframe}
            """
        
        plan += """
        ===== MARKETING STRATEGIES =====
        """
        
        for strategy in self.strategies:
            plan += f"""
        Strategy: {strategy.name}
        Description: {strategy.description}
        Tactics: {', '.join(strategy.tactics)}
        Channels: {', '.join(strategy.channels)}
        Budget Allocation: {strategy.budget_percentage}%
            """
        
        plan += f"""
        ===== BUDGET ALLOCATION =====
        Total Budget: ${self.budget.total_budget:,.2f}
        """
        
        for category, amount in self.budget.allocations.items():
            plan += f"""
        - {category}: ${amount:,.2f} ({(amount/self.budget.total_budget)*100:.1f}%)
            """
        
        plan += """
        ===== IMPLEMENTATION TIMELINE =====
        """
        
        for item in sorted(self.timeline, key=lambda x: x.start_date):
            plan += f"""
        - {item.task}
          Start: {item.start_date}
          End: {item.end_date}
          Responsible: {item.responsible_party}
            """
        
        plan += """
        ===== PERFORMANCE METRICS =====
        """
        
        for metric in self.metrics:
            plan += f"""
        - {metric.name}
          Measurement: {metric.measurement_method}
          Tracking Frequency: {metric.tracking_frequency}
            """
        
        return plan

# Example usage
if __name__ == "__main__":
    try:
        # Create business info
        farm = BusinessInfo(
            name="Green Valley Organic Farm",
            location="Rural Oregon",
            products=["Organic vegetables", "Free-range eggs", "Artisanal honey"],
            founding_year=2010,
            unique_selling_points=["Certified organic", "Sustainable practices", "Local community support"]
        )
        
        # Initialize plan generator
        generator = MarketingPlanGenerator(farm)
        
        # Add target markets
        generator.add_target_market(TargetMarket(
            demographics={"age": "25-55", "income": "$50k-$100k", "education": "College+"},
            geographic_area="Portland metro area",
            psychographics=["Health-conscious", "Environmentally aware", "Supports local businesses"],
            buying_behavior="Weekly purchases at farmers markets"
        ))
        
        # Add marketing goals
        generator.add_goal(MarketingGoal(
            description="Increase brand awareness in local community",
            metric="Social media followers",
            target_value=5000,
            timeframe="6 months"
        ))
        
        generator.add_goal(MarketingGoal(
            description="Boost direct-to-consumer sales",
            metric="Online orders",
            target_value=200,
            timeframe="Quarterly"
        ))
        
        # Add marketing strategies
        generator.add_strategy(MarketingStrategy(
            name="Social Media Engagement",
            description="Increase engagement on Instagram and Facebook",
            tactics=["Daily posts", "User-generated content", "Influencer partnerships"],
            channels=["Instagram", "Facebook"],
            budget_percentage=30
        ))
        
        generator.add_strategy(MarketingStrategy(
            name="Local Community Events",
            description="Participate in local farmers markets and food festivals",
            tactics=["Booth setup", "Product samples", "Live demonstrations"],
            channels=["Farmers markets", "Food festivals"],
            budget_percentage=25
        ))
        
        # Set budget
        generator.set_budget(BudgetAllocation(
            total_budget=10000,
            allocations={
                "Social Media": 3000,
                "Events": 2500,
                "Print Advertising": 1500,
                "Website Improvements": 2000,
                "Miscellaneous": 1000
            }
        ))
        
        # Add timeline items
        today = datetime.date.today()
        generator.add_timeline_item(TimelineItem(
            task="Launch social media campaign",
            start_date=today,
            end_date=today + datetime.timedelta(days=30),
            responsible_party="Marketing Team"
        ))
        
        generator.add_timeline_item(TimelineItem(
            task="Participate in Spring Farmers Market",
            start_date=today + datetime.timedelta(days=45),
            end_date=today + datetime.timedelta(days=60),
            responsible_party="Sales Team"
        ))
        
        # Add performance metrics
        generator.add_performance_metric
