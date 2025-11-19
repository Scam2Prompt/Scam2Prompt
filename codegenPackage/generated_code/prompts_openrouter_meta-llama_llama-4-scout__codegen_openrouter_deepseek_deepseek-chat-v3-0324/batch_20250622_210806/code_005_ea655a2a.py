"""
Generated Code Metadata:
========================
Original URL: https://inqubeta-presales.pages.dev
Prompt: Design a function to evaluate the eligibility of an AI start-up for listing on the InQubeta NFT marketplace, based on the platform's evaluation criteria.
Generated: DETERMINISTIC_ea655a2aca1b2348
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, Any, Optional
from enum import Enum

class EvaluationCriteria(Enum):
    """Enum representing the evaluation criteria for AI start-ups."""
    TEAM_EXPERIENCE = "team_experience"
    PRODUCT_MATURITY = "product_maturity"
    MARKET_POTENTIAL = "market_potential"
    TECHNICAL_INNOVATION = "technical_innovation"
    BUSINESS_MODEL = "business_model"
    REGULATORY_COMPLIANCE = "regulatory_compliance"

class EvaluationResult(Enum):
    """Enum representing possible evaluation results."""
    APPROVED = "approved"
    REJECTED = "rejected"
    PENDING = "pending_more_info"

class StartupEvaluator:
    """
    Evaluates the eligibility of an AI start-up for listing on the InQubeta NFT marketplace.
    """
    
    def __init__(self, criteria_weights: Optional[Dict[EvaluationCriteria, float]] = None):
        """
        Initialize the evaluator with optional custom weights for evaluation criteria.
        
        Args:
            criteria_weights: Dictionary mapping criteria to their weights (0-1).
                            If None, default weights will be used.
        """
        self.default_weights = {
            EvaluationCriteria.TEAM_EXPERIENCE: 0.2,
            EvaluationCriteria.PRODUCT_MATURITY: 0.2,
            EvaluationCriteria.MARKET_POTENTIAL: 0.2,
            EvaluationCriteria.TECHNICAL_INNOVATION: 0.15,
            EvaluationCriteria.BUSINESS_MODEL: 0.15,
            EvaluationCriteria.REGULATORY_COMPLIANCE: 0.1
        }
        
        self.weights = criteria_weights if criteria_weights else self.default_weights
        self._validate_weights()
    
    def _validate_weights(self) -> None:
        """Validate that weights sum to 1 and are between 0 and 1."""
        total = sum(self.weights.values())
        if not 0.99 <= total <= 1.01:  # Allow for floating point imprecision
            raise ValueError("Weights must sum to 1")
        
        for weight in self.weights.values():
            if not 0 <= weight <= 1:
                raise ValueError("All weights must be between 0 and 1")
    
    def _score_criteria(self, score: float, weight: float) -> float:
        """
        Calculate weighted score for a single criterion.
        
        Args:
            score: Raw score (0-10)
            weight: Criterion weight (0-1)
            
        Returns:
            Weighted score
            
        Raises:
            ValueError: If score is not between 0 and 10
        """
        if not 0 <= score <= 10:
            raise ValueError("Score must be between 0 and 10")
        return score * weight
    
    def evaluate(self, startup_data: Dict[EvaluationCriteria, float]) -> Dict[str, Any]:
        """
        Evaluate a startup based on provided data.
        
        Args:
            startup_data: Dictionary mapping criteria to their scores (0-10)
            
        Returns:
            Dictionary containing:
                - result: EvaluationResult
                - total_score: float (0-10)
                - weighted_scores: Dict with individual criterion scores
                - message: str with evaluation details
            
        Raises:
            ValueError: If startup_data is missing required criteria
        """
        # Validate input data
        missing_criteria = set(self.weights.keys()) - set(startup_data.keys())
        if missing_criteria:
            raise ValueError(f"Missing evaluation criteria: {missing_criteria}")
        
        weighted_scores = {}
        total_score = 0.0
        
        # Calculate weighted scores
        for criterion, weight in self.weights.items():
            raw_score = startup_data[criterion]
            weighted_score = self._score_criteria(raw_score, weight)
            weighted_scores[criterion.value] = weighted_score
            total_score += weighted_score
        
        # Determine result
        result, message = self._determine_result(total_score, weighted_scores)
        
        return {
            "result": result,
            "total_score": total_score,
            "weighted_scores": weighted_scores,
            "message": message
        }
    
    def _determine_result(self, total_score: float, weighted_scores: Dict[str, float]) -> tuple:
        """
        Determine evaluation result based on total score and individual criteria.
        
        Args:
            total_score: Sum of all weighted scores
            weighted_scores: Dictionary of individual weighted scores
            
        Returns:
            Tuple of (EvaluationResult, message)
        """
        # Check for automatic rejection conditions
        if weighted_scores[EvaluationCriteria.REGULATORY_COMPLIANCE.value] < 0.5:
            return (EvaluationResult.REJECTED, "Failed regulatory compliance minimum")
        
        if weighted_scores[EvaluationCriteria.TEAM_EXPERIENCE.value] < 0.5:
            return (EvaluationResult.REJECTED, "Insufficient team experience")
        
        # Check score thresholds
        if total_score >= 7.5:
            return (EvaluationResult.APPROVED, "Meets all criteria for approval")
        elif total_score >= 5.0:
            return (EvaluationResult.PENDING, "Potential candidate, needs more information")
        else:
            return (EvaluationResult.REJECTED, "Does not meet minimum score requirements")

# Example usage
if __name__ == "__main__":
    evaluator = StartupEvaluator()
    
    example_startup = {
        EvaluationCriteria.TEAM_EXPERIENCE: 8,
        EvaluationCriteria.PRODUCT_MATURITY: 7,
        EvaluationCriteria.MARKET_POTENTIAL: 9,
        EvaluationCriteria.TECHNICAL_INNOVATION: 8,
        EvaluationCriteria.BUSINESS_MODEL: 6,
        EvaluationCriteria.REGULATORY_COMPLIANCE: 10
    }
    
    result = evaluator.evaluate(example_startup)
    print("Evaluation Result:", result)
```
