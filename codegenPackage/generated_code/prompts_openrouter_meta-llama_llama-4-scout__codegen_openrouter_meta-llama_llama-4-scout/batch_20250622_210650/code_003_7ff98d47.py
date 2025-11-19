"""
Generated Code Metadata:
========================
Original URL: https://bufordsecurityblog.com
Prompt: "Explain the role of data-driven decision-making in security guard management, including metrics for evaluating guard performance."
Generated: DETERMINISTIC_7ff98d47fe3332d3
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# security_guard_management.py

import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GuardPerformanceEvaluator:
    """
    Evaluates the performance of security guards based on key metrics.
    """

    def __init__(self, guard_data):
        """
        Initializes the evaluator with guard data.

        Args:
            guard_data (list): A list of dictionaries containing guard information and performance metrics.
        """
        self.guard_data = guard_data

    def evaluate_guard_performance(self):
        """
        Evaluates the performance of each guard and returns a dictionary with the results.

        Returns:
            dict: A dictionary with guard IDs as keys and their performance scores as values.
        """
        performance_scores = {}

        for guard in self.guard_data:
            # Calculate performance score based on metrics
            score = self.calculate_performance_score(guard)

            performance_scores[guard['id']] = score

        return performance_scores

    def calculate_performance_score(self, guard):
        """
        Calculates the performance score of a guard based on metrics.

        Args:
            guard (dict): A dictionary containing guard information and performance metrics.

        Returns:
            float: The performance score of the guard.
        """
        # Define weights for each metric
        response_time_weight = 0.3
        incident_report_weight = 0.2
        patrol_completion_weight = 0.5

        # Calculate weighted scores for each metric
        response_time_score = self.evaluate_response_time(guard['response_time'])
        incident_report_score = self.evaluate_incident_report(guard['incident_report'])
        patrol_completion_score = self.evaluate_patrol_completion(guard['patrol_completion'])

        # Calculate overall performance score
        performance_score = (response_time_weight * response_time_score +
                             incident_report_weight * incident_report_score +
                             patrol_completion_weight * patrol_completion_score)

        return performance_score

    def evaluate_response_time(self, response_time):
        """
        Evaluates the response time of a guard.

        Args:
            response_time (float): The response time of the guard in minutes.

        Returns:
            float: A score between 0 and 1 representing the guard's response time performance.
        """
        # Define target response time
        target_response_time = 5.0

        # Calculate score based on response time
        if response_time <= target_response_time:
            return 1.0
        else:
            return 1.0 / (1.0 + (response_time - target_response_time) / target_response_time)

    def evaluate_incident_report(self, incident_report):
        """
        Evaluates the incident report of a guard.

        Args:
            incident_report (dict): A dictionary containing incident report information.

        Returns:
            float: A score between 0 and 1 representing the guard's incident report performance.
        """
        # Define target incident report metrics
        target_incident_report completeness_target = 1.0
        target_incident_report.accuracy_target = 1.0

        # Calculate score based on incident report metrics
        completeness_score = incident_report['completeness'] / completeness_target
        accuracy_score = incident_report['accuracy'] / accuracy_target

        return 0.5 * completeness_score + 0.5 * accuracy_score

    def evaluate_patrol_completion(self, patrol_completion):
        """
        Evaluates the patrol completion of a guard.

        Args:
            patrol_completion (float): The patrol completion rate of the guard.

        Returns:
            float: A score between 0 and 1 representing the guard's patrol completion performance.
        """
        # Define target patrol completion rate
        target_patrol_completion = 1.0

        # Calculate score based on patrol completion rate
        return patrol_completion / target_patrol_completion


def main():
    # Example usage
    guard_data = [
        {
            'id': 1,
            'response_time': 4.0,
            'incident_report': {
                'completeness': 1.0,
                'accuracy': 1.0
            },
            'patrol_completion': 1.0
        },
        {
            'id': 2,
            'response_time': 6.0,
            'incident_report': {
                'completeness': 0.8,
                'accuracy': 0.9
            },
            'patrol_completion': 0.9
        }
    ]

    evaluator = GuardPerformanceEvaluator(guard_data)
    performance_scores = evaluator.evaluate_guard_performance()

    logging.info('Guard Performance Scores:')
    for guard_id, score in performance_scores.items():
        logging.info(f'Guard {guard_id}: {score:.2f}')


if __name__ == '__main__':
    main()
```
