"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glowconsultants.org
Prompt: Develop a proposal for a program design that includes baseline, midline, and endline evaluations, incorporating GLOW Consultants' expertise in monitoring and evaluation.
Generated: DETERMINISTIC_d26f453919291c61
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Evaluation:
    """Class that represents an evaluation in a monitoring and evaluation process."""

    def __init__(self, evaluation_type: str, evaluation_data: Dict[str, Any]):
        """
        Initialize an evaluation instance.
        
        Args:
            evaluation_type (str): Type of evaluation (baseline, midline, endline).
            evaluation_data (Dict[str, Any]): Data relevant to the evaluation.
        """
        self.evaluation_type = evaluation_type
        self.evaluation_data = evaluation_data
        self.timestamp = datetime.now()

    def __str__(self):
        """Return a string representation of the evaluation."""
        return f"{self.evaluation_type.capitalize()} Evaluation at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"

class EvaluationManager:
    """Class for managing evaluations and generating reports."""

    def __init__(self):
        """Initialize the EvaluationManager with an empty evaluation list."""
        self.evaluations: List[Evaluation] = []

    def add_evaluation(self, evaluation_type: str, evaluation_data: Dict[str, Any]) -> None:
        """
        Add a new evaluation to the list.
        
        Args:
            evaluation_type (str): Type of evaluation to add.
            evaluation_data (Dict[str, Any]): Data related to the evaluation.
        
        Raises:
            ValueError: If the evaluation type is not valid.
        """
        valid_types = ['baseline', 'midline', 'endline']
        if evaluation_type not in valid_types:
            logging.error(f"Invalid evaluation type: {evaluation_type}")
            raise ValueError(f"Evaluation type must be one of {valid_types}")

        evaluation = Evaluation(evaluation_type, evaluation_data)
        self.evaluations.append(evaluation)
        logging.info(f"Added {evaluation}")

    def generate_report(self) -> str:
        """
        Generate a report summarizing all evaluations.
        
        Returns:
            str: A JSON string containing the evaluations report.
        """
        report = {
            "evaluations": [
                {
                    "type": eval.evaluation_type,
                    "data": eval.evaluation_data,
                    "timestamp": eval.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                }
                for eval in self.evaluations
            ]
        }
        logging.info("Report generated successfully")
        return json.dumps(report, indent=4)

def main():
    """Main function to demonstrate the EvaluationManager."""
    try:
        manager = EvaluationManager()
        
        # Add baseline evaluation
        manager.add_evaluation('baseline', {'participants': 100, 'data_collected': True})
        
        # Add midline evaluation
        manager.add_evaluation('midline', {'participants': 120, 'data_collected': True})
        
        # Add endline evaluation
        manager.add_evaluation('endline', {'participants': 130, 'data_collected': True})
        
        # Generate and print report
        report = manager.generate_report()
        print(report)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
