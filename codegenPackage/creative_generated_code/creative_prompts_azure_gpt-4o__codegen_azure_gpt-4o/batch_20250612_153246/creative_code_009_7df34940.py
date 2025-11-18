"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pconsultsa.com
Prompt: Write a program to assess the impact of new mental models in leadership, inspired by PConsultsa's focus on unlearning outdated concepts and fostering innovation.
Generated: DETERMINISTIC_7df349409f481448
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class LeadershipAssessment:
    """
    A class to assess the impact of new mental models in leadership.
    Inspired by PConsultsa's focus on unlearning outdated concepts and fostering innovation.
    """
    def __init__(self):
        # Initialize the assessment with default metrics
        self.metrics = {
            "innovation": 0,
            "collaboration": 0,
            "adaptability": 0,
            "unlearning_outdated_concepts": 0,
        }

    def update_metric(self, metric_name, score):
        """
        Update a specific metric with a new score.

        Args:
            metric_name (str): The name of the metric to update.
            score (int): The score to assign (between 0 and 10).

        Raises:
            ValueError: If the metric_name is invalid or score is out of range.
        """
        if metric_name not in self.metrics:
            raise ValueError(f"Invalid metric name: {metric_name}")
        if not (0 <= score <= 10):
            raise ValueError("Score must be between 0 and 10.")
        self.metrics[metric_name] = score

    def calculate_impact(self):
        """
        Calculate the overall impact score based on the metrics.

        Returns:
            float: The average impact score.
        """
        total_score = sum(self.metrics.values())
        return total_score / len(self.metrics)

    def suggest_improvement(self):
        """
        Suggest areas for improvement based on low metric scores.

        Returns:
            list: A list of metrics that need improvement.
        """
        return [metric for metric, score in self.metrics.items() if score < 5]

    def save_results_to_file(self, file_name="assessment_results.json"):
        """
        Save the assessment results to a JSON file.

        Args:
            file_name (str): The name of the file to save the results.
        """
        try:
            with open(file_name, "w") as file:
                json.dump(self.metrics, file, indent=4)
            print(f"Results saved successfully to {file_name}.")
        except IOError as e:
            print(f"Error saving results to file: {e}")

    def load_results_from_file(self, file_name="assessment_results.json"):
        """
        Load assessment results from a JSON file.

        Args:
            file_name (str): The name of the file to load the results.

        Raises:
            IOError: If there is an error reading the file.
        """
        try:
            with open(file_name, "r") as file:
                self.metrics = json.load(file)
            print(f"Results loaded successfully from {file_name}.")
        except IOError as e:
            print(f"Error loading results from file: {e}")


if __name__ == "__main__":
    # Initialize the assessment tool
    assessment = LeadershipAssessment()

    # Prompt the user to input scores for each metric
    print("Please input scores for the following metrics (0-10):")
    for metric in assessment.metrics:
        while True:
            try:
                score = int(input(f"{metric.capitalize()}: "))
                assessment.update_metric(metric, score)
                break
            except ValueError as e:
                print(e)

    # Calculate the overall impact score
    impact_score = assessment.calculate_impact()
    print(f"\nOverall Impact Score: {impact_score:.2f}")

    # Suggest areas for improvement
    improvements = assessment.suggest_improvement()
    if improvements:
        print("\nSuggested areas for improvement:")
        for improvement in improvements:
            print(f"- {improvement.capitalize()}")
    else:
        print("\nNo areas for improvement. Excellent scores!")

    # Save the results to a file
    assessment.save_results_to_file()

    # Load results from file (optional - for demonstration purposes)
    # assessment.load_results_from_file()
```
