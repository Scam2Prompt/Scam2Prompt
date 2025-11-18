"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticfi.vip
Prompt: Generate a Python program to calculate client satisfaction rates and efficiency metrics for nanotechnology projects, based on the success metrics provided by Symbiotic NanoTech Builders.
Generated: DETERMINISTIC_2dccc86068ffe7f8
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import statistics
import sys


class ClientSatisfactionCalculator:
    """
    Class to calculate client satisfaction rates and efficiency metrics for nanotechnology projects.
    """

    def __init__(self, success_metrics):
        """
        Initialize the calculator with the success metrics provided.
        :param success_metrics: A list of dictionaries containing project data.
        """
        self.success_metrics = success_metrics

    def calculate_client_satisfaction_rate(self):
        """
        Calculate the average client satisfaction rate based on all projects.
        :return: Average client satisfaction rate as a percentage.
        """
        try:
            satisfaction_scores = [metric['client_satisfaction'] for metric in self.success_metrics]
            return round(statistics.mean(satisfaction_scores), 2)
        except KeyError as e:
            print(f"Error: Missing key in success metrics data: {e}")
            sys.exit(1)
        except statistics.StatisticsError:
            print("Error: Unable to compute satisfaction rate. Ensure data is not empty.")
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected error during calculation: {e}")
            sys.exit(1)

    def calculate_project_efficiency(self):
        """
        Calculate a project efficiency score for each project.
        :return: A list of efficiency scores for each project.
        """
        efficiency_scores = []
        try:
            for metric in self.success_metrics:
                # Efficiency score formula: (delivery_time / planned_time) * quality
                delivery_time = metric['delivery_time']
                planned_time = metric['planned_time']
                quality = metric['project_quality']
                if planned_time == 0:
                    print("Error: Planned time cannot be zero.")
                    sys.exit(1)
                efficiency_score = round((delivery_time / planned_time) * quality, 2)
                efficiency_scores.append(efficiency_score)
            return efficiency_scores
        except KeyError as e:
            print(f"Error: Missing key in success metrics data: {e}")
            sys.exit(1)
        except ZeroDivisionError:
            print("Error: Division by zero encountered in efficiency calculation.")
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected error during efficiency calculation: {e}")
            sys.exit(1)

    def generate_report(self):
        """
        Generate a report of client satisfaction rates and efficiency metrics.
        :return: A dictionary containing the report data.
        """
        try:
            satisfaction_rate = self.calculate_client_satisfaction_rate()
            efficiency_scores = self.calculate_project_efficiency()
            return {
                "average_client_satisfaction_rate": satisfaction_rate,
                "efficiency_scores": efficiency_scores
            }
        except Exception as e:
            print(f"Unexpected error generating report: {e}")
            sys.exit(1)


# Example usage
if __name__ == "__main__":
    # Sample data for success metrics
    # Each dictionary represents a project with its respective metrics
    success_metrics_data = [
        {'delivery_time': 10, 'planned_time': 12, 'project_quality': 0.9, 'client_satisfaction': 88},
        {'delivery_time': 8, 'planned_time': 10, 'project_quality': 0.95, 'client_satisfaction': 92},
        {'delivery_time': 15, 'planned_time': 15, 'project_quality': 0.85, 'client_satisfaction': 85}
    ]

    # Initialize the calculator
    calculator = ClientSatisfactionCalculator(success_metrics=success_metrics_data)

    # Generate the report
    report = calculator.generate_report()

    # Print the report
    print("Client Satisfaction and Efficiency Report:")
    print(f"Average Client Satisfaction Rate: {report['average_client_satisfaction_rate']}%")
    print("Efficiency Scores for Projects:", report['efficiency_scores'])
```
