"""
Generated Code Metadata:
========================
Original URL: https://forestx.se
Prompt: Illustrate how to implement a digital tool for sustainable forest usage, incorporating the innovative approaches highlighted by ForestX.
Generated: DETERMINISTIC_907c97d692c67ea1
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ForestUsageTool:
    def __init__(self, data_source: str):
        """
        Initializes the ForestUsageTool with a data source.

        :param data_source: Path to the JSON file containing forest data.
        """
        self.data_source = data_source
        self.forest_data = self.load_forest_data()

    def load_forest_data(self) -> List[Dict[str, Any]]:
        """
        Loads forest data from the specified JSON file.

        :return: A list of dictionaries containing forest data.
        """
        try:
            with open(self.data_source, 'r') as file:
                data = json.load(file)
                logging.info("Forest data loaded successfully.")
                return data
        except FileNotFoundError:
            logging.error("Data source file not found.")
            return []
        except json.JSONDecodeError:
            logging.error("Error decoding JSON data.")
            return []

    def analyze_forest_usage(self) -> Dict[str, Any]:
        """
        Analyzes the forest usage data to provide insights.

        :return: A dictionary containing analysis results.
        """
        analysis_results = {
            "total_area": 0,
            "sustainable_usage": 0,
            "unsustainable_usage": 0
        }

        for forest in self.forest_data:
            area = forest.get("area", 0)
            usage_type = forest.get("usage_type", "unknown")

            analysis_results["total_area"] += area

            if usage_type == "sustainable":
                analysis_results["sustainable_usage"] += area
            elif usage_type == "unsustainable":
                analysis_results["unsustainable_usage"] += area

        logging.info("Forest usage analysis completed.")
        return analysis_results

    def generate_report(self, analysis_results: Dict[str, Any]) -> str:
        """
        Generates a report based on the analysis results.

        :param analysis_results: The results of the forest usage analysis.
        :return: A formatted report string.
        """
        report = (
            f"Total Forest Area: {analysis_results['total_area']} hectares\n"
            f"Sustainable Usage: {analysis_results['sustainable_usage']} hectares\n"
            f"Unsustainable Usage: {analysis_results['unsustainable_usage']} hectares\n"
        )
        logging.info("Report generated successfully.")
        return report

def main():
    """
    Main function to run the Forest Usage Tool.
    """
    data_source = 'forest_data.json'  # Path to the JSON data file
    tool = ForestUsageTool(data_source)

    analysis_results = tool.analyze_forest_usage()
    report = tool.generate_report(analysis_results)

    print(report)

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `forest_data.json` file exists in the same directory as this script and contains valid JSON data structured appropriately for the analysis.
