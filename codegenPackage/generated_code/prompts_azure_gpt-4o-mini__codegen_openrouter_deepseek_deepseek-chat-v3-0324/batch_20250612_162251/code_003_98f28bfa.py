"""
Generated Code Metadata:
========================
Original URL: https://www.icyd.org
Prompt: Create a program that evaluates the effectiveness of youth engagement strategies in schools, referencing the goals of the Iowa Collaboration for Youth Development.
Generated: DETERMINISTIC_98f28bfab7cf3949
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict

# Constants for Iowa Collaboration for Youth Development goals
IOWA_YOUTH_GOALS = {
    "goal1": "Promote healthy physical, social, and emotional development",
    "goal2": "Provide safe and supportive environments",
    "goal3": "Engage youth in meaningful activities",
    "goal4": "Foster positive relationships with adults and peers",
    "goal5": "Develop leadership and decision-making skills"
}

@dataclass
class EngagementStrategy:
    """Data class representing a youth engagement strategy."""
    name: str
    description: str
    target_goals: List[str]  # References IOWA_YOUTH_GOALS keys
    implementation_difficulty: int  # 1-5 scale
    cost_estimate: str  # Low, Medium, High
    evidence_based: bool

class YouthEngagementEvaluator:
    """Evaluates youth engagement strategies against Iowa Youth Development goals."""
    
    def __init__(self):
        self.strategies: List[EngagementStrategy] = []
    
    def add_strategy(self, strategy: EngagementStrategy) -> None:
        """Add a strategy to the evaluator."""
        self._validate_strategy(strategy)
        self.strategies.append(strategy)
    
    def _validate_strategy(self, strategy: EngagementStrategy) -> None:
        """Validate that a strategy is properly formatted."""
        if not isinstance(strategy, EngagementStrategy):
            raise ValueError("Strategy must be an EngagementStrategy instance")
        
        for goal in strategy.target_goals:
            if goal not in IOWA_YOUTH_GOALS:
                raise ValueError(f"Invalid goal reference: {goal}")
        
        if not 1 <= strategy.implementation_difficulty <= 5:
            raise ValueError("Implementation difficulty must be between 1 and 5")
        
        if strategy.cost_estimate.lower() not in ["low", "medium", "high"]:
            raise ValueError("Cost estimate must be Low, Medium, or High")
    
    def evaluate_strategies(self) -> Dict:
        """Evaluate all strategies and return a summary report."""
        if not self.strategies:
            raise ValueError("No strategies to evaluate")
        
        report = {
            "total_strategies": len(self.strategies),
            "goals_coverage": self._calculate_goals_coverage(),
            "average_difficulty": self._calculate_average_difficulty(),
            "cost_distribution": self._calculate_cost_distribution(),
            "evidence_based_count": sum(1 for s in self.strategies if s.evidence_based),
            "strategies": [asdict(s) for s in self.strategies]
        }
        
        return report
    
    def _calculate_goals_coverage(self) -> Dict:
        """Calculate how many strategies address each goal."""
        coverage = {goal: 0 for goal in IOWA_YOUTH_GOALS}
        
        for strategy in self.strategies:
            for goal in strategy.target_goals:
                coverage[goal] += 1
        
        return coverage
    
    def _calculate_average_difficulty(self) -> float:
        """Calculate average implementation difficulty."""
        total = sum(s.implementation_difficulty for s in self.strategies)
        return total / len(self.strategies)
    
    def _calculate_cost_distribution(self) -> Dict:
        """Calculate distribution of cost estimates."""
        distribution = {"low": 0, "medium": 0, "high": 0}
        
        for strategy in self.strategies:
            cost = strategy.cost_estimate.lower()
            distribution[cost] += 1
        
        return distribution
    
    def save_report(self, filename: str) -> None:
        """Save evaluation report to a JSON file."""
        report = self.evaluate_strategies()
        
        try:
            with open(filename, 'w') as f:
                json.dump(report, f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save report: {str(e)}")

# Example usage
if __name__ == "__main__":
    evaluator = YouthEngagementEvaluator()
    
    # Add sample strategies
    strategy1 = EngagementStrategy(
        name="Peer Mentoring Program",
        description="Older students mentor younger students",
        target_goals=["goal4", "goal5"],
        implementation_difficulty=3,
        cost_estimate="Medium",
        evidence_based=True
    )
    
    strategy2 = EngagementStrategy(
        name="After-School Sports",
        description="Organized sports activities after school",
        target_goals=["goal1", "goal2", "goal3"],
        implementation_difficulty=2,
        cost_estimate="High",
        evidence_based=True
    )
    
    evaluator.add_strategy(strategy1)
    evaluator.add_strategy(strategy2)
    
    # Generate and print report
    report = evaluator.evaluate_strategies()
    print(json.dumps(report, indent=2))
    
    # Save report to file
    evaluator.save_report("youth_engagement_report.json")
```
