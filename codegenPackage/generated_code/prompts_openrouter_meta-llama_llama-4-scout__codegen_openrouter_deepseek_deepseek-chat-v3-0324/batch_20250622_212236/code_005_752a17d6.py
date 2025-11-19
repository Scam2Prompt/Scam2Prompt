"""
Generated Code Metadata:
========================
Original URL: https://master-brain.com
Prompt: "Develop a 360-degree marketing plan for a small business using BTL and ATL strategies."
Generated: DETERMINISTIC_752a17d66a1122bf
Batch ID: 20250622_212236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
360-Degree Marketing Plan Generator for Small Businesses

This script helps small businesses create a comprehensive marketing plan
incorporating both Above-The-Line (ATL) and Below-The-Line (BTL) strategies.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
import json
from datetime import datetime, timedelta
import random

@dataclass
class MarketingActivity:
    name: str
    strategy_type: str  # 'ATL' or 'BTL'
    description: str
    cost_estimate: float
    duration_days: int
    target_audience: str
    success_metrics: List[str]
    resources_needed: List[str]

class MarketingPlanGenerator:
    def __init__(self, business_name: str, industry: str, budget: float, timeline_days: int):
        self.business_name = business_name
        self.industry = industry
        self.budget = budget
        self.timeline_days = timeline_days
        self.activities: List[MarketingActivity] = []
        self.atl_strategies = self._load_strategies('atl')
        self.btl_strategies = self._load_strategies('btl')

    def _load_strategies(self, strategy_type: str) -> List[Dict]:
        """Load predefined marketing strategies from JSON files"""
        try:
            with open(f'{strategy_type}_strategies.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: {strategy_type}_strategies.json not found. Using default strategies.")
            return self._get_default_strategies(strategy_type)

    def _get_default_strategies(self, strategy_type: str) -> List[Dict]:
        """Return default strategies if JSON file is not found"""
        if strategy_type == 'atl':
            return [
                {
                    "name": "Social Media Ads",
                    "description": "Paid advertising on platforms like Facebook, Instagram",
                    "cost_range": (500, 5000),
                    "duration_range": (7, 30),
                    "audience": "Digital-savvy consumers",
                    "metrics": ["Impressions", "Click-through rate", "Conversions"]
                },
                {
                    "name": "Radio Advertising",
                    "description": "Local radio station ads during peak hours",
                    "cost_range": (1000, 10000),
                    "duration_range": (14, 60),
                    "audience": "Local commuters",
                    "metrics": ["Reach", "Brand recall", "Website traffic"]
                }
            ]
        else:  # btl
            return [
                {
                    "name": "In-Store Promotions",
                    "description": "Special discounts and events at physical location",
                    "cost_range": (200, 2000),
                    "duration_range": (1, 7),
                    "audience": "Local customers",
                    "metrics": ["Foot traffic", "Sales lift", "Customer engagement"]
                },
                {
                    "name": "Direct Mail Campaign",
                    "description": "Personalized mailers to targeted households",
                    "cost_range": (300, 3000),
                    "duration_range": (14, 30),
                    "audience": "Local residents",
                    "metrics": ["Response rate", "Coupon redemption", "New customers"]
                }
            ]

    def generate_plan(self) -> Dict:
        """Generate a balanced marketing plan with ATL and BTL strategies"""
        if not self.atl_strategies or not self.btl_strategies:
            raise ValueError("No marketing strategies available to generate plan")

        allocated_budget = 0
        remaining_days = self.timeline_days
        atl_ratio = 0.6  # 60% of budget to ATL
        btl_ratio = 0.4  # 40% of budget to BTL

        # Generate ATL activities
        atl_budget = self.budget * atl_ratio
        while allocated_budget < atl_budget and remaining_days > 0:
            strategy = random.choice(self.atl_strategies)
            cost = random.uniform(*strategy['cost_range'])
            duration = random.randint(*strategy['duration_range'])
            
            if cost > (atl_budget - allocated_budget) or duration > remaining_days:
                continue
                
            activity = MarketingActivity(
                name=strategy['name'],
                strategy_type='ATL',
                description=strategy['description'],
                cost_estimate=cost,
                duration_days=duration,
                target_audience=strategy['audience'],
                success_metrics=strategy['metrics'],
                resources_needed=self._get_resources_needed('ATL', strategy['name'])
            )
            self.activities.append(activity)
            allocated_budget += cost
            remaining_days -= duration

        # Generate BTL activities
        btl_budget = self.budget * btl_ratio
        while allocated_budget < self.budget and remaining_days > 0:
            strategy = random.choice(self.btl_strategies)
            cost = random.uniform(*strategy['cost_range'])
            duration = random.randint(*strategy['duration_range'])
            
            if cost > (self.budget - allocated_budget) or duration > remaining_days:
                continue
                
            activity = MarketingActivity(
                name=strategy['name'],
                strategy_type='BTL',
                description=strategy['description'],
                cost_estimate=cost,
                duration_days=duration,
                target_audience=strategy['audience'],
                success_metrics=strategy['metrics'],
                resources_needed=self._get_resources_needed('BTL', strategy['name'])
            )
            self.activities.append(activity)
            allocated_budget += cost
            remaining_days -= duration

        return self._format_plan()

    def _get_resources_needed(self, strategy_type: str, activity_name: str) -> List[str]:
        """Determine resources needed for a given activity"""
        if strategy_type == 'ATL':
            if 'Social Media' in activity_name:
                return ['Ad creatives', 'Social media manager', 'Ad budget']
            elif 'Radio' in activity_name:
                return ['Audio ad script', 'Voice talent', 'Radio slots']
        else:  # BTL
            if 'In-Store' in activity_name:
                return ['Promotional materials', 'Staff training', 'Point-of-sale displays']
            elif 'Direct Mail' in activity_name:
                return ['Mailing list', 'Print materials', 'Postage']
        return ['Staff time', 'Budget allocation']

    def _format_plan(self) -> Dict:
        """Format the marketing plan for output"""
        total_cost = sum(activity.cost_estimate for activity in self.activities)
        start_date = datetime.now()
        
        timeline = []
        current_date = start_date
        for activity in self.activities:
            end_date = current_date + timedelta(days=activity.duration_days)
            timeline.append({
                'activity': activity.name,
                'type': activity.strategy_type,
                'start_date': current_date.strftime('%Y-%m-%d'),
                'end_date': end_date.strftime('%Y-%m-%d'),
                'description': activity.description,
                'target_audience': activity.target_audience,
                'metrics': activity.success_metrics,
                'resources': activity.resources_needed
            })
            current_date = end_date + timedelta(days=1)  # Add buffer day

        return {
            'business_name': self.business_name,
            'industry': self.industry,
            'total_budget': self.budget,
            'allocated_budget': total_cost,
            'remaining_budget': self.budget - total_cost,
            'timeline_days': self.timeline_days,
            'activities': timeline,
            'summary': self._generate_summary()
        }

    def _generate_summary(self) -> Dict:
        """Generate a summary of the marketing plan"""
        atl_count = sum(1 for a in self.activities if a.strategy_type == 'ATL')
        btl_count = sum(1 for a in self.activities if a.strategy_type == 'BTL')
        atl_cost = sum(a.cost_estimate for a in self.activities if a.strategy_type == 'ATL')
        btl_cost = sum(a.cost_estimate for a in self.activities if a.strategy_type == 'BTL')

        return {
            'atl_activities': atl_count,
            'btl_activities': btl_count,
            'atl_budget': atl_cost,
            'btl_budget': btl_cost,
            'budget_allocation': f"{round(atl_cost/self.budget*100)}% ATL, {round(btl_cost/self.budget*100)}% BTL",
            'estimated_reach': self._estimate_reach()
        }

    def _estimate_reach(self) -> str:
        """Estimate potential reach based on activities"""
        reach = {
            'local': 0,
            'regional': 0,
            'national': 0
        }
        
        for activity in self.activities:
            if activity.strategy
