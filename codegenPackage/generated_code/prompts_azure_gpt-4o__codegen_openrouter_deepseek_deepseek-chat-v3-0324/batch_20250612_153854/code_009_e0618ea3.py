"""
Generated Code Metadata:
========================
Original URL: https://alghanim-capital.com
Prompt: Create a program that models collaboration and mutual success metrics for investment partnerships, inspired by Alghanim Capital's emphasis on teamwork and stakeholder cooperation.
Generated: DETERMINISTIC_e0618ea3d59ff1cb
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Investment Partnership Collaboration Metrics Model

This program models collaboration and mutual success metrics for investment partnerships,
inspired by Alghanim Capital's emphasis on teamwork and stakeholder cooperation.

Key Features:
- Tracks partnership performance metrics
- Calculates mutual success scores
- Provides collaboration insights
- Generates partnership reports
"""

import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
import statistics
from enum import Enum, auto


class PartnershipStage(Enum):
    """Enum representing different stages of a partnership"""
    EXPLORATION = auto()
    FORMATION = auto()
    OPERATIONAL = auto()
    MATURE = auto()
    EXIT = auto()


@dataclass
class FinancialMetric:
    """Class to track financial metrics for a partnership"""
    revenue: float = 0.0
    profit: float = 0.0
    roi: float = 0.0
    growth_rate: float = 0.0


@dataclass
class CollaborationMetric:
    """Class to track collaboration metrics for a partnership"""
    communication_score: float = 0.0  # 1-10 scale
    decision_making_score: float = 0.0  # 1-10 scale
    conflict_resolution_score: float = 0.0  # 1-10 scale
    innovation_score: float = 0.0  # 1-10 scale


@dataclass
class Stakeholder:
    """Class representing a stakeholder in the partnership"""
    name: str
    contribution: float  # Percentage or fixed amount
    role: str
    satisfaction_score: float = 0.0  # 1-10 scale


@dataclass
class Partnership:
    """Class representing an investment partnership"""
    name: str
    start_date: datetime
    stage: PartnershipStage = PartnershipStage.EXPLORATION
    financial_metrics: FinancialMetric = field(default_factory=FinancialMetric)
    collaboration_metrics: CollaborationMetric = field(default_factory=CollaborationMetric)
    stakeholders: List[Stakeholder] = field(default_factory=list)
    milestones: Dict[str, datetime] = field(default_factory=dict)
    
    def add_stakeholder(self, stakeholder: Stakeholder) -> None:
        """Add a stakeholder to the partnership"""
        self.stakeholders.append(stakeholder)
    
    def add_milestone(self, name: str, date: datetime) -> None:
        """Add a milestone to the partnership"""
        self.milestones[name] = date
    
    def calculate_mutual_success_score(self) -> float:
        """
        Calculate a composite score representing mutual success
        Weighted average of financial and collaboration metrics
        """
        financial_weight = 0.6
        collaboration_weight = 0.4
        
        financial_score = (
            self.financial_metrics.roi * 0.4 +
            self.financial_metrics.growth_rate * 0.3 +
            self.financial_metrics.profit * 0.3
        )
        
        collaboration_score = (
            self.collaboration_metrics.communication_score * 0.25 +
            self.collaboration_metrics.decision_making_score * 0.25 +
            self.collaboration_metrics.conflict_resolution_score * 0.25 +
            self.collaboration_metrics.innovation_score * 0.25
        )
        
        return (financial_score * financial_weight + 
                collaboration_score * collaboration_weight)
    
    def get_stakeholder_satisfaction(self) -> float:
        """Calculate average stakeholder satisfaction score"""
        if not self.stakeholders:
            return 0.0
        return statistics.mean([s.satisfaction_score for s in self.stakeholders])
    
    def to_dict(self) -> Dict:
        """Convert partnership data to dictionary for serialization"""
        return {
            "name": self.name,
            "start_date": self.start_date.isoformat(),
            "stage": self.stage.name,
            "financial_metrics": {
                "revenue": self.financial_metrics.revenue,
                "profit": self.financial_metrics.profit,
                "roi": self.financial_metrics.roi,
                "growth_rate": self.financial_metrics.growth_rate
            },
            "collaboration_metrics": {
                "communication_score": self.collaboration_metrics.communication_score,
                "decision_making_score": self.collaboration_metrics.decision_making_score,
                "conflict_resolution_score": self.collaboration_metrics.conflict_resolution_score,
                "innovation_score": self.collaboration_metrics.innovation_score
            },
            "stakeholders": [
                {
                    "name": s.name,
                    "contribution": s.contribution,
                    "role": s.role,
                    "satisfaction_score": s.satisfaction_score
                } for s in self.stakeholders
            ],
            "milestones": {k: v.isoformat() for k, v in self.milestones.items()}
        }


class PartnershipManager:
    """Class to manage multiple partnerships and generate reports"""
    
    def __init__(self):
        self.partnerships: List[Partnership] = []
    
    def add_partnership(self, partnership: Partnership) -> None:
        """Add a partnership to the manager"""
        self.partnerships.append(partnership)
    
    def get_partnership(self, name: str) -> Optional[Partnership]:
        """Get a partnership by name"""
        for p in self.partnerships:
            if p.name == name:
                return p
        return None
    
    def generate_report(self, partnership_name: str) -> Dict:
        """Generate a comprehensive report for a partnership"""
        partnership = self.get_partnership(partnership_name)
        if not partnership:
            raise ValueError(f"Partnership '{partnership_name}' not found")
        
        return {
            "partnership_name": partnership.name,
            "stage": partnership.stage.name,
            "mutual_success_score": partnership.calculate_mutual_success_score(),
            "stakeholder_satisfaction": partnership.get_stakeholder_satisfaction(),
            "financial_performance": {
                "roi": partnership.financial_metrics.roi,
                "growth_rate": partnership.financial_metrics.growth_rate,
                "profit": partnership.financial_metrics.profit
            },
            "collaboration_performance": {
                "communication": partnership.collaboration_metrics.communication_score,
                "decision_making": partnership.collaboration_metrics.decision_making_score,
                "conflict_resolution": partnership.collaboration_metrics.conflict_resolution_score,
                "innovation": partnership.collaboration_metrics.innovation_score
            },
            "milestones": list(partnership.milestones.keys()),
            "stakeholder_count": len(partnership.stakeholders)
        }
    
    def save_to_file(self, filename: str) -> None:
        """Save all partnerships to a JSON file"""
        data = [p.to_dict() for p in self.partnerships]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_from_file(self, filename: str) -> None:
        """Load partnerships from a JSON file"""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.partnerships = []
        for item in data:
            partnership = Partnership(
                name=item["name"],
                start_date=datetime.fromisoformat(item["start_date"]),
                stage=PartnershipStage[item["stage"]]
            )
            
            partnership.financial_metrics = FinancialMetric(
                revenue=item["financial_metrics"]["revenue"],
                profit=item["financial_metrics"]["profit"],
                roi=item["financial_metrics"]["roi"],
                growth_rate=item["financial_metrics"]["growth_rate"]
            )
            
            partnership.collaboration_metrics = CollaborationMetric(
                communication_score=item["collaboration_metrics"]["communication_score"],
                decision_making_score=item["collaboration_metrics"]["decision_making_score"],
                conflict_resolution_score=item["collaboration_metrics"]["conflict_resolution_score"],
                innovation_score=item["collaboration_metrics"]["innovation_score"]
            )
            
            for s in item["stakeholders"]:
                partnership.add_stakeholder(Stakeholder(
                    name=s["name"],
                    contribution=s["contribution"],
                    role=s["role"],
                    satisfaction_score=s["satisfaction_score"]
                ))
            
            for name, date in item["milestones"].items():
                partnership.add_milestone(name, datetime.fromisoformat(date))
            
            self.partnerships.append(partnership)


def main():
    """Example usage of the partnership management system"""
    manager = PartnershipManager()
    
    # Create a new partnership
    partnership = Partnership(
        name="Tech Venture Fund",
        start_date=datetime(2023, 1, 1),
        stage=PartnershipStage.OPERATIONAL
    )
    
    # Set financial metrics
    partnership.financial_metrics = FinancialMetric(
        revenue=5000000,
        profit=1500000,
        roi
