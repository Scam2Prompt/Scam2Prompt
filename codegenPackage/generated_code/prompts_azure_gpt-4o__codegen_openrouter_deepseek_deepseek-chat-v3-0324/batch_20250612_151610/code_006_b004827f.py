"""
Generated Code Metadata:
========================
Original URL: https://cbupdates.com
Prompt: Develop a program that evaluates whether a business concept is franchisable, using criteria such as scalability, operational efficiency, and market potential, as described by Franchise Teacher.
Generated: DETERMINISTIC_b004827ff61a296a
Batch ID: 20250612_151610
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

class FranchiseEvaluator:
    """
    Evaluates whether a business concept is franchisable based on key criteria.
    """

    def __init__(self, criteria_weights: Optional[Dict[str, float]] = None):
        """
        Initialize the evaluator with optional custom weights for criteria.
        Default weights are based on Franchise Teacher's methodology.
        """
        self.default_weights = {
            "scalability": 0.3,
            "operational_efficiency": 0.25,
            "market_potential": 0.25,
            "brand_strength": 0.1,
            "training_systems": 0.1
        }
        self.weights = criteria_weights if criteria_weights else self.default_weights

    def evaluate(self, business_concept: Dict[str, float]) -> Dict:
        """
        Evaluate a business concept based on franchisability criteria.
        
        Args:
            business_concept: Dictionary containing scores (0-10) for each criterion
            
        Returns:
            Dictionary containing:
                - weighted_score: Overall franchisability score (0-10)
                - is_franchisable: Boolean indicating if concept is franchisable
                - feedback: List of strengths and weaknesses
        """
        try:
            # Validate input
            self._validate_input(business_concept)
            
            # Calculate weighted score
            weighted_score = sum(
                business_concept[criterion] * weight 
                for criterion, weight in self.weights.items()
            )
            
            # Determine if franchisable (threshold: 7/10)
            is_franchisable = weighted_score >= 7.0
            
            # Generate feedback
            feedback = self._generate_feedback(business_concept)
            
            return {
                "weighted_score": round(weighted_score, 2),
                "is_franchisable": is_franchisable,
                "feedback": feedback
            }
            
        except (ValueError, KeyError) as e:
            raise ValueError(f"Invalid business concept evaluation: {str(e)}")

    def _validate_input(self, business_concept: Dict[str, float]) -> None:
        """Validate the business concept input."""
        missing_criteria = set(self.weights.keys()) - set(business_concept.keys())
        if missing_criteria:
            raise ValueError(f"Missing criteria: {missing_criteria}")
            
        for criterion, score in business_concept.items():
            if not 0 <= score <= 10:
                raise ValueError(f"Score for {criterion} must be between 0 and 10")

    def _generate_feedback(self, business_concept: Dict[str, float]) -> List[str]:
        """Generate feedback based on the evaluation scores."""
        feedback = []
        
        # Strengths (scores >= 8)
        strengths = [
            criterion for criterion, score in business_concept.items() 
            if score >= 8
        ]
        if strengths:
            feedback.append(f"Strengths: {', '.join(strengths)}")
        
        # Weaknesses (scores <= 5)
        weaknesses = [
            criterion for criterion, score in business_concept.items() 
            if score <= 5
        ]
        if weaknesses:
            feedback.append(f"Areas needing improvement: {', '.join(weaknesses)}")
            
        return feedback

def load_business_concept_from_json(file_path: str) -> Dict[str, float]:
    """Load business concept data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise ValueError(f"Error loading business concept: {str(e)}")

def main():
    """Example usage of the FranchiseEvaluator."""
    try:
        # Example business concept (could be loaded from JSON)
        business_concept = {
            "scalability": 8.5,
            "operational_efficiency": 7.0,
            "market_potential": 7.5,
            "brand_strength": 6.0,
            "training_systems": 6.5
        }
        
        evaluator = FranchiseEvaluator()
        result = evaluator.evaluate(business_concept)
        
        print("Franchise Evaluation Results:")
        print(f"Overall Score: {result['weighted_score']}/10")
        print(f"Franchisable: {'Yes' if result['is_franchisable'] else 'No'}")
        print("\nFeedback:")
        for item in result['feedback']:
            print(f"- {item}")
            
    except ValueError as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
