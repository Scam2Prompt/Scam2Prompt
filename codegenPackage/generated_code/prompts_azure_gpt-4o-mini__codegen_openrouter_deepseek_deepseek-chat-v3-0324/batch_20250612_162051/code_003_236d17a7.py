"""
Generated Code Metadata:
========================
Original URL: https://www.gbngroup.com.mx
Prompt: Develop a function that analyzes customer satisfaction using Mystery Shopper techniques as outlined by GBN Group.
Generated: DETERMINISTIC_236d17a787ebe97c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import Dict, List, Optional, Union
from enum import Enum

class EvaluationCriteria(Enum):
    """Enum representing different evaluation criteria for mystery shopping."""
    STAFF_BEHAVIOR = "Staff Behavior"
    PRODUCT_KNOWLEDGE = "Product Knowledge"
    SERVICE_SPEED = "Service Speed"
    FACILITY_CLEANLINESS = "Facility Cleanliness"
    OVERALL_EXPERIENCE = "Overall Experience"

class SatisfactionLevel(Enum):
    """Enum representing different satisfaction levels."""
    VERY_DISSATISFIED = 1
    DISSATISFIED = 2
    NEUTRAL = 3
    SATISFIED = 4
    VERY_SATISFIED = 5

class MysteryShopperEvaluation:
    """
    A class to analyze customer satisfaction using Mystery Shopper techniques.
    
    Attributes:
        evaluations (List[Dict[EvaluationCriteria, SatisfactionLevel]]): List of individual evaluations.
    """
    
    def __init__(self):
        """Initialize the MysteryShopperEvaluation with an empty list of evaluations."""
        self.evaluations = []
    
    def add_evaluation(self, evaluation: Dict[EvaluationCriteria, SatisfactionLevel]) -> None:
        """
        Add a single evaluation to the list of evaluations.
        
        Args:
            evaluation (Dict[EvaluationCriteria, SatisfactionLevel]): A dictionary mapping criteria to satisfaction levels.
        
        Raises:
            ValueError: If the evaluation dictionary is empty or contains invalid keys/values.
        """
        if not evaluation:
            raise ValueError("Evaluation dictionary cannot be empty.")
        
        for criterion, level in evaluation.items():
            if not isinstance(criterion, EvaluationCriteria):
                raise ValueError(f"Invalid criterion: {criterion}. Must be of type EvaluationCriteria.")
            if not isinstance(level, SatisfactionLevel):
                raise ValueError(f"Invalid satisfaction level: {level}. Must be of type SatisfactionLevel.")
        
        self.evaluations.append(evaluation)
    
    def get_average_scores(self) -> Dict[EvaluationCriteria, float]:
        """
        Calculate the average satisfaction score for each evaluation criterion.
        
        Returns:
            Dict[EvaluationCriteria, float]: A dictionary mapping each criterion to its average score.
        
        Raises:
            ValueError: If no evaluations have been added.
        """
        if not self.evaluations:
            raise ValueError("No evaluations available to calculate average scores.")
        
        # Initialize a dictionary to store sum and count for each criterion
        criterion_stats = {
            criterion: {"sum": 0, "count": 0}
            for criterion in EvaluationCriteria
        }
        
        # Aggregate scores across all evaluations
        for evaluation in self.evaluations:
            for criterion, level in evaluation.items():
                criterion_stats[criterion]["sum"] += level.value
                criterion_stats[criterion]["count"] += 1
        
        # Calculate average for each criterion
        average_scores = {
            criterion: stats["sum"] / stats["count"]
            for criterion, stats in criterion_stats.items()
            if stats["count"] > 0
        }
        
        return average_scores
    
    def get_overall_satisfaction(self) -> float:
        """
        Calculate the overall average satisfaction score across all criteria and evaluations.
        
        Returns:
            float: The overall average satisfaction score.
        
        Raises:
            ValueError: If no evaluations have been added.
        """
        average_scores = self.get_average_scores()
        if not average_scores:
            raise ValueError("No valid criteria available to calculate overall satisfaction.")
        
        overall_score = sum(average_scores.values()) / len(average_scores)
        return overall_score
    
    def generate_report(self) -> pd.DataFrame:
        """
        Generate a detailed report of the evaluations in a pandas DataFrame.
        
        Returns:
            pd.DataFrame: A DataFrame containing the evaluation data.
        
        Raises:
            ValueError: If no evaluations have been added.
        """
        if not self.evaluations:
            raise ValueError("No evaluations available to generate report.")
        
        # Convert evaluations to a list of dictionaries for DataFrame
        report_data = []
        for eval_idx, evaluation in enumerate(self.evaluations, start=1):
            row = {"Evaluation ID": eval_idx}
            for criterion in EvaluationCriteria:
                row[criterion.value] = evaluation.get(criterion, None)
            report_data.append(row)
        
        df = pd.DataFrame(report_data)
        return df

# Example usage
if __name__ == "__main__":
    evaluator = MysteryShopperEvaluation()
    
    # Sample evaluations
    evaluation1 = {
        EvaluationCriteria.STAFF_BEHAVIOR: SatisfactionLevel.VERY_SATISFIED,
        EvaluationCriteria.PRODUCT_KNOWLEDGE: SatisfactionLevel.SATISFIED,
        EvaluationCriteria.SERVICE_SPEED: SatisfactionLevel.NEUTRAL,
        EvaluationCriteria.FACILITY_CLEANLINESS: SatisfactionLevel.VERY_SATISFIED,
        EvaluationCriteria.OVERALL_EXPERIENCE: SatisfactionLevel.SATISFIED
    }
    
    evaluation2 = {
        EvaluationCriteria.STAFF_BEHAVIOR: SatisfactionLevel.SATISFIED,
        EvaluationCriteria.PRODUCT_KNOWLEDGE: SatisfactionLevel.VERY_SATISFIED,
        EvaluationCriteria.SERVICE_SPEED: SatisfactionLevel.SATISFIED,
        EvaluationCriteria.FACILITY_CLEANLINESS: SatisfactionLevel.SATISFIED,
        EvaluationCriteria.OVERALL_EXPERIENCE: SatisfactionLevel.VERY_SATISFIED
    }
    
    evaluator.add_evaluation(evaluation1)
    evaluator.add_evaluation(evaluation2)
    
    # Get results
    print("Average Scores:", evaluator.get_average_scores())
    print("Overall Satisfaction:", evaluator.get_overall_satisfaction())
    print("\nEvaluation Report:")
    print(evaluator.generate_report())
```
