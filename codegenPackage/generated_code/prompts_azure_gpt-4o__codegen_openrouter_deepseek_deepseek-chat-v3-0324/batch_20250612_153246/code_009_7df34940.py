"""
Generated Code Metadata:
========================
Original URL: https://pconsultsa.com
Prompt: Write a program to assess the impact of new mental models in leadership, inspired by PConsultsa's focus on unlearning outdated concepts and fostering innovation.
Generated: DETERMINISTIC_7df349409f481448
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Mental Model Impact Assessment Tool

This program evaluates the impact of new mental models in leadership by:
1. Gathering input on current and proposed mental models
2. Assessing alignment with innovation goals
3. Identifying outdated concepts to unlearn
4. Generating an impact score and recommendations

Inspired by PConsultsa's approach to leadership development.
"""

import json
from typing import Dict, List, Tuple
from enum import Enum
import statistics


class ImpactLevel(Enum):
    """Enum representing the impact level of a mental model change."""
    LOW = 1
    MODERATE = 2
    HIGH = 3
    TRANSFORMATIVE = 4


class MentalModelAssessor:
    """Assesses the impact of new mental models in leadership contexts."""

    def __init__(self):
        """Initialize the assessor with default weights and thresholds."""
        self.innovation_weight = 0.4
        self.unlearning_weight = 0.3
        self.adoption_weight = 0.2
        self.risk_weight = 0.1
        self.high_impact_threshold = 0.7

    def assess_model(
        self,
        current_model: Dict,
        proposed_model: Dict,
        org_goals: List[str]
    ) -> Dict:
        """
        Assess the impact of transitioning from current to proposed mental model.
        
        Args:
            current_model: Dictionary describing current mental model
            proposed_model: Dictionary describing proposed mental model
            org_goals: List of organizational innovation goals
            
        Returns:
            Dictionary containing assessment results
        """
        if not current_model or not proposed_model:
            raise ValueError("Both current and proposed models must be provided")
            
        if not org_goals:
            raise ValueError("Organization goals must be provided")

        try:
            # Calculate individual scores
            innovation_score = self._calculate_innovation_score(
                proposed_model, org_goals
            )
            unlearning_score = self._calculate_unlearning_score(
                current_model, proposed_model
            )
            adoption_score = self._calculate_adoption_score(proposed_model)
            risk_score = self._calculate_risk_score(current_model, proposed_model)

            # Calculate weighted overall score
            overall_score = (
                innovation_score * self.innovation_weight +
                unlearning_score * self.unlearning_weight +
                adoption_score * self.adoption_weight +
                risk_score * self.risk_weight
            )

            # Determine impact level
            impact_level = self._determine_impact_level(overall_score)

            # Generate recommendations
            recommendations = self._generate_recommendations(
                innovation_score,
                unlearning_score,
                adoption_score,
                risk_score
            )

            return {
                "overall_score": round(overall_score, 2),
                "impact_level": impact_level.name,
                "innovation_score": round(innovation_score, 2),
                "unlearning_score": round(unlearning_score, 2),
                "adoption_score": round(adoption_score, 2),
                "risk_score": round(risk_score, 2),
                "recommendations": recommendations,
                "is_high_impact": overall_score >= self.high_impact_threshold
            }

        except Exception as e:
            raise RuntimeError(f"Assessment failed: {str(e)}")

    def _calculate_innovation_score(
        self,
        proposed_model: Dict,
        org_goals: List[str]
    ) -> float:
        """Calculate how well the proposed model aligns with innovation goals."""
        alignment_scores = []
        for goal in org_goals:
            alignment = proposed_model.get("innovation_alignment", {}).get(goal, 0)
            alignment_scores.append(min(max(alignment, 0), 1))
        
        return statistics.mean(alignment_scores) if alignment_scores else 0

    def _calculate_unlearning_score(
        self,
        current_model: Dict,
        proposed_model: Dict
    ) -> float:
        """Calculate the importance of unlearning outdated concepts."""
        outdated_concepts = proposed_model.get("outdated_concepts_identified", [])
        if not outdated_concepts:
            return 0
            
        relevance_scores = []
        for concept in outdated_concepts:
            relevance = current_model.get("concepts", {}).get(concept, {}).get("relevance", 0)
            relevance_scores.append(min(max(relevance, 0), 1))
            
        return statistics.mean(relevance_scores) if relevance_scores else 0

    def _calculate_adoption_score(self, proposed_model: Dict) -> float:
        """Calculate the feasibility of adopting the new model."""
        feasibility = proposed_model.get("adoption_feasibility", 0)
        return min(max(feasibility, 0), 1)

    def _calculate_risk_score(
        self,
        current_model: Dict,
        proposed_model: Dict
    ) -> float:
        """Calculate the risk associated with the transition."""
        risk_factors = proposed_model.get("risk_factors", {})
        if not risk_factors:
            return 1  # No risk factors means lowest risk
            
        mitigation_scores = [
            min(max(factor.get("mitigation", 0), 0), 1)
            for factor in risk_factors.values()
        ]
        avg_mitigation = statistics.mean(mitigation_scores) if mitigation_scores else 0
        return 1 - avg_mitigation  # Higher mitigation = lower risk

    def _determine_impact_level(self, score: float) -> ImpactLevel:
        """Determine the impact level based on the overall score."""
        if score >= 0.8:
            return ImpactLevel.TRANSFORMATIVE
        elif score >= 0.6:
            return ImpactLevel.HIGH
        elif score >= 0.4:
            return ImpactLevel.MODERATE
        else:
            return ImpactLevel.LOW

    def _generate_recommendations(
        self,
        innovation_score: float,
        unlearning_score: float,
        adoption_score: float,
        risk_score: float
    ) -> List[str]:
        """Generate recommendations based on assessment scores."""
        recommendations = []
        
        if innovation_score < 0.5:
            recommendations.append(
                "Consider refining the model to better align with innovation goals."
            )
            
        if unlearning_score < 0.4:
            recommendations.append(
                "Identify more outdated concepts that need to be unlearned."
            )
            
        if adoption_score < 0.6:
            recommendations.append(
                "Develop a more comprehensive adoption plan with training materials."
            )
            
        if risk_score > 0.5:
            recommendations.append(
                "Implement additional risk mitigation strategies before proceeding."
            )
            
        if not recommendations:
            recommendations.append(
                "The model shows strong potential. Proceed with implementation plan."
            )
            
        return recommendations


def load_sample_data(file_path: str) -> Dict:
    """Load sample data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Sample data file not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")


def main():
    """Main function to demonstrate the assessment tool."""
    try:
        # Load sample data
        data = load_sample_data("sample_data.json")
        
        # Initialize assessor
        assessor = MentalModelAssessor()
        
        # Perform assessment
        results = assessor.assess_model(
            data["current_model"],
            data["proposed_model"],
            data["org_goals"]
        )
        
        # Print results
        print("Mental Model Impact Assessment Results:")
        print(json.dumps(results, indent=2))
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0


if __name__ == "__main__":
    main()
```
