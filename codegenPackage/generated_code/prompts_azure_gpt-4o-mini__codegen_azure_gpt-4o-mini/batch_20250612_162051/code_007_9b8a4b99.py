"""
Generated Code Metadata:
========================
Original URL: https://lexuscertifications.com
Prompt: Write a function that evaluates the effectiveness of a company's ISO 45001 Occupational Health and Safety Management System based on performance metrics.
Generated: DETERMINISTIC_9b8a4b99381ad914
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ISO45001Evaluator:
    """
    A class to evaluate the effectiveness of a company's ISO 45001 Occupational Health and Safety Management System.
    """

    def __init__(self, incident_rate, training_hours, employee_satisfaction, audits_passed):
        """
        Initializes the evaluator with performance metrics.

        :param incident_rate: Number of incidents per 100 employees
        :param training_hours: Total hours of training provided
        :param employee_satisfaction: Employee satisfaction score (0-100)
        :param audits_passed: Number of successful audits
        """
        self.incident_rate = incident_rate
        self.training_hours = training_hours
        self.employee_satisfaction = employee_satisfaction
        self.audits_passed = audits_passed

    def evaluate_effectiveness(self):
        """
        Evaluates the effectiveness of the ISO 45001 system based on the provided metrics.

        :return: A string indicating the effectiveness level
        """
        try:
            # Validate input metrics
            self._validate_metrics()

            # Define thresholds for evaluation
            if self.incident_rate < 2 and self.training_hours > 20 and self.employee_satisfaction > 75 and self.audits_passed > 2:
                return "Highly Effective"
            elif self.incident_rate < 5 and self.training_hours > 10 and self.employee_satisfaction > 60 and self.audits_passed > 1:
                return "Moderately Effective"
            else:
                return "Needs Improvement"

        except ValueError as e:
            return f"Error in evaluation: {str(e)}"

    def _validate_metrics(self):
        """
        Validates the input metrics to ensure they are within acceptable ranges.

        :raises ValueError: If any metric is out of range
        """
        if self.incident_rate < 0:
            raise ValueError("Incident rate cannot be negative.")
        if self.training_hours < 0:
            raise ValueError("Training hours cannot be negative.")
        if not (0 <= self.employee_satisfaction <= 100):
            raise ValueError("Employee satisfaction must be between 0 and 100.")
        if self.audits_passed < 0:
            raise ValueError("Number of audits passed cannot be negative.")

# Example usage
if __name__ == "__main__":
    evaluator = ISO45001Evaluator(incident_rate=1.5, training_hours=25, employee_satisfaction=80, audits_passed=3)
    effectiveness = evaluator.evaluate_effectiveness()
    print(f"ISO 45001 System Effectiveness: {effectiveness}")
```
