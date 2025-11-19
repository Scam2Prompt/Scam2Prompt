"""
Generated Code Metadata:
========================
Original URL: https://araform.org
Prompt: "Develop a short Python program to analyze course completion rates and job placement statistics for graduates of programs similar to those on araform.org."
Generated: DETERMINISTIC_24ef1d34793a8447
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Optional
import json
import os


class CourseAnalyzer:
    """
    Analyzes course completion rates and job placement statistics.
    """

    def __init__(self, data_path: str):
        """
        Initialize the analyzer with data from a JSON file.

        Args:
            data_path (str): Path to the JSON file containing course data.
        """
        self.data_path = data_path
        self.data = self._load_data()

    def _load_data(self) -> List[Dict]:
        """
        Load and validate the course data from JSON file.

        Returns:
            List[Dict]: List of course data dictionaries.

        Raises:
            FileNotFoundError: If the data file does not exist.
            ValueError: If the JSON data is malformed or missing required fields.
        """
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Data file not found at {self_data_path}")

        with open(self.data_path, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON data: {e}")

        if not isinstance(data, list):
            raise ValueError("Data should be a list of courses")

        required_fields = {'name', 'completion_rate', 'job_placement_rate', 'graduates'}
        for course in data:
            if not all(field in course for field in required_fields):
                raise ValueError(f"Missing required fields in course data: {required_fields}")

        return data

    def calculate_stats(self) -> Dict[str, Dict[str, float]]:
        """
        Calculate statistics for completion and job placement rates.

        Returns:
            Dict[str, Dict[str, float]]: Statistics including mean, median, and std dev.
        """
        completion_rates = [course['completion_rate'] for course in self.data]
        job_rates = [course['job_placement_rate'] for course in self.data]

        stats = {
            'completion_rate': {
                'mean': np.mean(completion_rates),
                'median': np.median(completion_rates),
                'std_dev': np.std(completion_rates)
            },
            'job_placement_rate': {
                'mean': np.mean(job_rates),
                'median': np.median(job_rates),
                'std_dev': np.std(job_rates)
            }
        }

        return stats

    def plot_rates(self, save_path: Optional[str] = None) -> None:
        """
        Plot completion and job placement rates.

        Args:
            save_path (Optional[str]): If provided, saves the plot to this path.
        """
        names = [course['name'] for course in self.data]
        completion = [course['completion_rate'] for course in self.data]
        job_placement = [course['job_placement_rate'] for course in self.data]

        x = np.arange(len(names))
        width = 0.35

        fig, ax = plt.subplots(figsize=(12, 6))
        rects1 = ax.bar(x - width/2, completion, width, label='Completion Rate')
        rects2 = ax.bar(x + width/2, job_placement, width, label='Job Placement Rate')

        ax.set_ylabel('Rate (%)')
        ax.set_title('Course Completion and Job Placement Rates')
        ax.set_xticks(x)
        ax.set_xticklabels(names, rotation=45, ha='right')
        ax.legend()

        fig.tight_layout()

        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
        else:
            plt.show()

    def get_top_courses(self, metric: str, top_n: int = 3) -> List[Dict]:
        """
        Get top courses based on specified metric.

        Args:
            metric (str): 'completion_rate' or 'job_placement_rate'.
            top_n (int): Number of top courses to return.

        Returns:
            List[Dict]: Top courses sorted by the metric.

        Raises:
            ValueError: If invalid metric is provided.
        """
        if metric not in ['completion_rate', 'job_placement_rate']:
            raise ValueError("Metric must be 'completion_rate' or 'job_placement_rate'")

        sorted_courses = sorted(
            self.data,
            key=lambda x: x[metric],
            reverse=True
        )
        return sorted_courses[:top_n]


# Example usage
if __name__ == "__main__":
    try:
        analyzer = CourseAnalyzer('course_data.json')
        
        # Calculate and print statistics
        stats = analyzer.calculate_stats()
        print("Statistics:")
        print(json.dumps(stats, indent=2))
        
        # Plot rates
        analyzer.plot_rates('rates_plot.png')
        
        # Get top courses
        top_completion = analyzer.get_top_courses('completion_rate')
        print("\nTop courses by completion rate:")
        for course in top_completion:
            print(f"{course['name']}: {course['completion_rate']}%")
            
        top_job_placement = analyzer.get_top_courses('job_placement_rate')
        print("\nTop courses by job placement rate:")
        for course in top_job_placement:
            print(f"{course['name']}: {course['job_placement_rate']}%")
            
    except Exception as e:
        print(f"Error: {e}")
```
