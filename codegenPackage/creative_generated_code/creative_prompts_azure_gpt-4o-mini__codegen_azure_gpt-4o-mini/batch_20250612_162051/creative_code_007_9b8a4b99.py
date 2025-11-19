"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lexuscertifications.com
Prompt: Write a function that evaluates the effectiveness of a company's ISO 45001 Occupational Health and Safety Management System based on performance metrics.
Generated: DETERMINISTIC_9b8a4b99381ad914
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import Dict, List, Union

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ISO45001Evaluator:
    def __init__(self, performance_metrics: Dict[str, Union[int, float]]):
        """
        Initialize the ISO45001Evaluator with performance metrics.

        :param performance_metrics: A dictionary containing performance metrics such as incident rates,
                                    employee training completion rates, and safety audits.
        """
        self.performance_metrics = performance_metrics

    def evaluate_effectiveness(self) -> str:
        """
        Evaluate the effectiveness of the company's ISO 45001 Occupational Health and Safety Management System.

        :return: A string indicating the overall effectiveness based on the provided metrics.
        """
        try:
            # Extract metrics for evaluation
            incident_rate = self.performance_metrics.get('incident_rate', 0)
            training_completion_rate = self.performance_metrics.get('training_completion_rate', 0)
            safety_audit_score = self.performance_metrics.get('safety_audit_score', 0)

            # Evaluate metrics
            overall_score = self.calculate_overall_score(incident_rate, training_completion_rate, safety_audit_score)

            # Assess effectiveness based on the overall score
            return self.assess_effectiveness(overall_score)

        except Exception as e:
            logging.error(f"Error evaluating effectiveness: {e}")
            return "Error evaluating effectiveness"

    def calculate_overall_score(self, incident_rate: float, training_completion_rate: float, safety_audit_score: float) -> float:
        """
        Calculate the overall score based on the input metrics.

        :param incident_rate: The rate of incidents reported.
        :param training_completion_rate: The percentage of employees who completed safety training.
        :param safety_audit_score: The score achieved during the safety audit.

        :return: A calculated overall score.
        """
        # Normalize metrics for overall scoring
        normalized_incident_rate = max(0, 100 - incident_rate)  # Lower incident rate is better
        normalized_training_completion = min(training_completion_rate, 100)  # Maximum is 100%
        normalized_audit_score = min(safety_audit_score, 100)  # Maximum is 100%

        # Calculate overall score as a weighted average
        overall_score = (
            0.4 * normalized_incident_rate +
            0.4 * normalized_training_completion +
            0.2 * normalized_audit_score
        )
        logging.info(f"Calculated overall score: {overall_score}")
        return overall_score

    def assess_effectiveness(self, overall_score: float) -> str:
        """
        Assess the effectiveness based on the overall score.

        :param overall_score: The overall score calculated from the performance metrics.

        :return: A string indicating the level of effectiveness.
        """
        if overall_score >= 90:
            return "Highly Effective"
        elif overall_score >= 75:
            return "Effective"
        elif overall_score >= 50:
            return "Needs Improvement"
        else:
            return "Ineffective"

# Example usage
if __name__ == "__main__":
    performance_metrics_example = {
        'incident_rate': 5,  # Incidents per 100 employees
        'training_completion_rate': 95,  # Percentage of training completed
        'safety_audit_score': 85  # Out of 100
    }
    
    evaluator = ISO45001Evaluator(performance_metrics_example)
    effectiveness = evaluator.evaluate_effectiveness()
    print(effectiveness)
```
