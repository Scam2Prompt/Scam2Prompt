"""
Generated Code Metadata:
========================
Original URL: https://sabrinaalves.com
Prompt: Recommend a framework for implementing a "Ferramenta perdas x ganhos" feature that helps users evaluate decisions and emotional trade-offs in their daily lives.
Generated: DETERMINISTIC_0d565544852af204
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Ferramenta Perdas x Ganhos - Decision Evaluation Tool

This module provides a framework for evaluating decisions and emotional trade-offs
in daily life using a weighted scoring system.

Key Features:
- Decision tracking with pros/cons
- Emotional impact scoring
- Weighted decision evaluation
- Historical decision analysis
"""

from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
import json
import uuid
from enum import Enum, auto

class ImpactType(Enum):
    """Types of impacts a decision can have"""
    FINANCIAL = auto()
    EMOTIONAL = auto()
    SOCIAL = auto()
    HEALTH = auto()
    PROFESSIONAL = auto()

@dataclass
class Impact:
    """Represents a single impact of a decision"""
    type: ImpactType
    description: str
    positive: bool
    weight: float  # 0.0 to 1.0
    intensity: int  # 1-10 scale

@dataclass
class Decision:
    """Represents a decision to be evaluated"""
    id: str
    title: str
    description: str
    created_at: datetime
    impacts: List[Impact]
    final_choice: Optional[bool] = None
    notes: Optional[str] = None

class DecisionEvaluator:
    """Core evaluation engine for the tool"""
    
    def __init__(self):
        self.decisions: List[Decision] = []
    
    def create_decision(self, title: str, description: str) -> Decision:
        """Create a new decision to evaluate"""
        decision = Decision(
            id=str(uuid.uuid4()),
            title=title,
            description=description,
            created_at=datetime.now(),
            impacts=[]
        )
        self.decisions.append(decision)
        return decision
    
    def add_impact(
        self,
        decision: Decision,
        impact_type: ImpactType,
        description: str,
        positive: bool,
        weight: float,
        intensity: int
    ) -> Impact:
        """Add an impact to a decision"""
        if weight < 0 or weight > 1:
            raise ValueError("Weight must be between 0 and 1")
        if intensity < 1 or intensity > 10:
            raise ValueError("Intensity must be between 1 and 10")
            
        impact = Impact(
            type=impact_type,
            description=description,
            positive=positive,
            weight=weight,
            intensity=intensity
        )
        decision.impacts.append(impact)
        return impact
    
    def evaluate_decision(self, decision: Decision) -> float:
        """Calculate a score for the decision (-1.0 to 1.0)"""
        if not decision.impacts:
            return 0.0
            
        total_score = 0.0
        total_weight = 0.0
        
        for impact in decision.impacts:
            score = impact.intensity / 10.0
            if not impact.positive:
                score *= -1
                
            weighted_score = score * impact.weight
            total_score += weighted_score
            total_weight += impact.weight
        
        if total_weight == 0:
            return 0.0
            
        return total_score / total_weight
    
    def save_decisions(self, filepath: str) -> None:
        """Save decisions to JSON file"""
        with open(filepath, 'w') as f:
            json.dump([self._decision_to_dict(d) for d in self.decisions], f, indent=2)
    
    def load_decisions(self, filepath: str) -> None:
        """Load decisions from JSON file"""
        with open(filepath, 'r') as f:
            data = json.load(f)
            self.decisions = [self._dict_to_decision(d) for d in data]
    
    def _decision_to_dict(self, decision: Decision) -> dict:
        """Convert Decision object to dictionary"""
        return {
            'id': decision.id,
            'title': decision.title,
            'description': decision.description,
            'created_at': decision.created_at.isoformat(),
            'impacts': [
                {
                    'type': impact.type.name,
                    'description': impact.description,
                    'positive': impact.positive,
                    'weight': impact.weight,
                    'intensity': impact.intensity
                }
                for impact in decision.impacts
            ],
            'final_choice': decision.final_choice,
            'notes': decision.notes
        }
    
    def _dict_to_decision(self, data: dict) -> Decision:
        """Convert dictionary to Decision object"""
        decision = Decision(
            id=data['id'],
            title=data['title'],
            description=data['description'],
            created_at=datetime.fromisoformat(data['created_at']),
            impacts=[],
            final_choice=data.get('final_choice'),
            notes=data.get('notes')
        )
        
        for impact_data in data['impacts']:
            impact = Impact(
                type=ImpactType[impact_data['type']],
                description=impact_data['description'],
                positive=impact_data['positive'],
                weight=impact_data['weight'],
                intensity=impact_data['intensity']
            )
            decision.impacts.append(impact)
            
        return decision

# Example usage
if __name__ == "__main__":
    evaluator = DecisionEvaluator()
    
    # Create a decision
    decision = evaluator.create_decision(
        "Should I take the new job offer?",
        "Evaluating whether to accept a new job with higher pay but longer commute"
    )
    
    # Add impacts
    evaluator.add_impact(
        decision,
        ImpactType.FINANCIAL,
        "20% salary increase",
        True,
        0.3,
        8
    )
    
    evaluator.add_impact(
        decision,
        ImpactType.EMOTIONAL,
        "Longer commute time",
        False,
        0.4,
        6
    )
    
    evaluator.add_impact(
        decision,
        ImpactType.PROFESSIONAL,
        "Better career growth opportunities",
        True,
        0.3,
        9
    )
    
    # Evaluate
    score = evaluator.evaluate_decision(decision)
    print(f"Decision score: {score:.2f}")
    
    # Save to file
    evaluator.save_decisions("decisions.json")
```
