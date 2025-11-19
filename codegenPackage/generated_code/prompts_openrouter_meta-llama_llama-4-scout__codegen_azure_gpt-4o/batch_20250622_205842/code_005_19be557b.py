"""
Generated Code Metadata:
========================
Original URL: https://trindademota.adv.br
Prompt: "Develop a code snippet for generating statistics on jurisprudence using specialized technological resources, as mentioned in the services of Trindade & Mota Advocacia."
Generated: DETERMINISTIC_19be557bb45ff8c9
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from collections import Counter

class JurisprudenceStatistics:
    """
    A class to generate statistics on jurisprudence using specialized technological resources.
    """

    def __init__(self, data_source):
        """
        Initialize the class with a data source.

        :param data_source: Path to the JSON file containing jurisprudence data.
        """
        self.data_source = data_source
        self.data = []

    def load_data(self):
        """
        Load jurisprudence data from the specified JSON file.

        :raises FileNotFoundError: If the data source file does not exist.
        :raises json.JSONDecodeError: If the file content is not valid JSON.
        """
        if not os.path.exists(self.data_source):
            raise FileNotFoundError(f"Data source file '{self.data_source}' not found.")
        
        try:
            with open(self.data_source, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse JSON data: {e}")

    def generate_statistics(self):
        """
        Generate statistics based on the loaded jurisprudence data.

        :return: A dictionary containing statistics such as case counts by category.
        """
        if not self.data:
            raise ValueError("No data loaded. Please load data before generating statistics.")
        
        # Example: Count cases by category
        case_categories = [case.get('category', 'Unknown') for case in self.data]
        category_counts = Counter(case_categories)

        # Example: Count cases by year
        case_years = [case.get('year', 'Unknown') for case in self.data]
        year_counts = Counter(case_years)

        return {
            "total_cases": len(self.data),
            "cases_by_category": dict(category_counts),
            "cases_by_year": dict(year_counts)
        }

    def save_statistics(self, output_path, statistics):
        """
        Save the generated statistics to a JSON file.

        :param output_path: Path to the output JSON file.
        :param statistics: Dictionary containing the statistics to save.
        :raises IOError: If there is an error writing to the file.
        """
        try:
            with open(output_path, 'w', encoding='utf-8') as file:
                json.dump(statistics, file, indent=4, ensure_ascii=False)
        except IOError as e:
            raise IOError(f"Failed to write statistics to file: {e}")


# Example usage
if __name__ == "__main__":
    # Path to the input data file (replace with actual path)
    input_data_path = "jurisprudence_data.json"
    # Path to the output statistics file (replace with actual path)
    output_statistics_path = "jurisprudence_statistics.json"

    try:
        # Initialize the statistics generator
        stats_generator = JurisprudenceStatistics(input_data_path)
        
        # Load the data
        stats_generator.load_data()
        
        # Generate statistics
        statistics = stats_generator.generate_statistics()
        
        # Save the statistics to a file
        stats_generator.save_statistics(output_statistics_path, statistics)
        
        print("Statistics generated and saved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
