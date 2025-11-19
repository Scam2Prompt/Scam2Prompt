"""
Generated Code Metadata:
========================
Original URL: https://brandsoutlet.qa
Prompt: "Create a size chart comparison tool for men's and women's clothing, incorporating data from various fashion brands like those found on Brands Outlet."
Generated: DETERMINISTIC_8fb8fbe4868e915d
Batch ID: 20250622_205529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class SizeChartComparisonTool:
    """
    A tool to compare size charts for men's and women's clothing across various fashion brands.
    """

    def __init__(self):
        """
        Initialize the tool with an empty size chart database.
        """
        self.size_charts = {}

    def load_size_chart(self, brand_name, gender, size_chart):
        """
        Load a size chart for a specific brand and gender.

        :param brand_name: Name of the fashion brand (e.g., "Brand Outlet").
        :param gender: Gender category ("Men" or "Women").
        :param size_chart: Dictionary containing size chart data.
        """
        if brand_name not in self.size_charts:
            self.size_charts[brand_name] = {}
        self.size_charts[brand_name][gender] = size_chart

    def compare_sizes(self, brand1, brand2, gender, size):
        """
        Compare a specific size across two brands for a given gender.

        :param brand1: Name of the first brand.
        :param brand2: Name of the second brand.
        :param gender: Gender category ("Men" or "Women").
        :param size: Size to compare (e.g., "M", "L").
        :return: Comparison result as a dictionary.
        """
        try:
            size_chart1 = self.size_charts[brand1][gender]
            size_chart2 = self.size_charts[brand2][gender]

            if size not in size_chart1 or size not in size_chart2:
                raise ValueError(f"Size '{size}' not found in one or both brands.")

            return {
                "Brand1": {
                    "Name": brand1,
                    "Size": size,
                    "Measurements": size_chart1[size]
                },
                "Brand2": {
                    "Name": brand2,
                    "Size": size,
                    "Measurements": size_chart2[size]
                }
            }
        except KeyError as e:
            raise ValueError(f"Invalid brand or gender specified: {e}")
        except ValueError as e:
            raise ValueError(f"Error during comparison: {e}")

    def save_size_charts_to_file(self, file_path):
        """
        Save the size charts to a JSON file.

        :param file_path: Path to the file where size charts will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.size_charts, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving size charts to file: {e}")

    def load_size_charts_from_file(self, file_path):
        """
        Load size charts from a JSON file.

        :param file_path: Path to the file containing size charts.
        """
        try:
            with open(file_path, 'r') as file:
                self.size_charts = json.load(file)
        except IOError as e:
            raise IOError(f"Error loading size charts from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON file: {e}")


# Example usage
if __name__ == "__main__":
    tool = SizeChartComparisonTool()

    # Load size charts for two brands
    tool.load_size_chart("Brand Outlet", "Men", {
        "S": {"Chest": 36, "Waist": 30},
        "M": {"Chest": 38, "Waist": 32},
        "L": {"Chest": 40, "Waist": 34}
    })
    tool.load_size_chart("Fashion Co.", "Men", {
        "S": {"Chest": 35, "Waist": 29},
        "M": {"Chest": 37, "Waist": 31},
        "L": {"Chest": 39, "Waist": 33}
    })

    # Compare sizes
    try:
        comparison = tool.compare_sizes("Brand Outlet", "Fashion Co.", "Men", "M")
        print("Comparison Result:")
        print(json.dumps(comparison, indent=4))
    except ValueError as e:
        print(f"Error: {e}")

    # Save size charts to file
    try:
        tool.save_size_charts_to_file("size_charts.json")
        print("Size charts saved successfully.")
    except IOError as e:
        print(f"Error: {e}")

    # Load size charts from file
    try:
        tool.load_size_charts_from_file("size_charts.json")
        print("Size charts loaded successfully.")
    except (IOError, ValueError) as e:
        print(f"Error: {e}")
```
