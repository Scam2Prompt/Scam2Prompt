"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Develop a Python program to analyze the impact of Rakhshanda Memorial's projects, including statistics on lives impacted, food packs distributed, and volunteers engaged.
Generated: DETERMINISTIC_a80bfd2331f02b70
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import statistics

class ProjectImpactAnalyzer:
    """
    A class to analyze the impact of Rakhshanda Memorial's projects.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with data from a JSON file.

        :param data_file: Path to the JSON file containing project data.
        """
        self.data_file = data_file
        self.data = self._load_data()

    def _load_data(self):
        """
        Loads project data from a JSON file.

        :return: A list of dictionaries containing project data.
        """
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{self.data_file}' not found.")
            return []
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON from '{self.data_file}'.")
            return []

    def calculate_statistics(self):
        """
        Calculates statistics for lives impacted, food packs distributed, and volunteers engaged.

        :return: A dictionary containing the calculated statistics.
        """
        if not self.data:
            print("No data available for analysis.")
            return {}

        try:
            lives_impacted = [project['lives_impacted'] for project in self.data]
            food_packs_distributed = [project['food_packs_distributed'] for project in self.data]
            volunteers_engaged = [project['volunteers_engaged'] for project in self.data]

            return {
                'lives_impacted': {
                    'total': sum(lives_impacted),
                    'average': statistics.mean(lives_impacted),
                    'max': max(lives_impacted),
                    'min': min(lives_impacted)
                },
                'food_packs_distributed': {
                    'total': sum(food_packs_distributed),
                    'average': statistics.mean(food_packs_distributed),
                    'max': max(food_packs_distributed),
                    'min': min(food_packs_distributed)
                },
                'volunteers_engaged': {
                    'total': sum(volunteers_engaged),
                    'average': statistics.mean(volunteers_engaged),
                    'max': max(volunteers_engaged),
                    'min': min(volunteers_engaged)
                }
            }
        except KeyError as e:
            print(f"Error: Missing key in data - {e}")
            return {}
        except statistics.StatisticsError as e:
            print(f"Error: Statistics calculation failed - {e}")
            return {}

    def display_statistics(self, stats):
        """
        Displays the calculated statistics in a readable format.

        :param stats: A dictionary containing the calculated statistics.
        """
        if not stats:
            print("No statistics to display.")
            return

        print("Impact Analysis Statistics:")
        for category, values in stats.items():
            print(f"\n{category.capitalize()}:")
            for metric, value in values.items():
                print(f"  {metric.capitalize()}: {value}")


if __name__ == "__main__":
    # Path to the JSON file containing project data
    data_file = "project_data.json"

    # Initialize the analyzer
    analyzer = ProjectImpactAnalyzer(data_file)

    # Calculate statistics
    stats = analyzer.calculate_statistics()

    # Display statistics
    analyzer.display_statistics(stats)
```

### Example JSON File (`project_data.json`):
```json
[
    {
        "project_name": "Project A",
        "lives_impacted": 120,
        "food_packs_distributed": 300,
        "volunteers_engaged": 25
    },
    {
        "project_name": "Project B",
        "lives_impacted": 200,
        "food_packs_distributed": 500,
        "volunteers_engaged": 40
    },
    {
        "project_name": "Project C",
        "lives_impacted": 150,
        "food_packs_distributed": 400,
        "volunteers_engaged": 30
    }
]
```
