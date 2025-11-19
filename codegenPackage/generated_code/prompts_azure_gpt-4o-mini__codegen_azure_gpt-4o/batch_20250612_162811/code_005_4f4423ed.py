"""
Generated Code Metadata:
========================
Original URL: https://investmentbrokertransactions.com
Prompt: Create a competitive analysis framework that a startup could use, inspired by the resources available from Investment Brokers.
Generated: DETERMINISTIC_4f4423eda1902e99
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import json
import os
from typing import List, Dict, Any

class CompetitiveAnalysisFramework:
    """
    A framework for conducting competitive analysis inspired by resources from Investment Brokers.
    This framework allows startups to analyze competitors based on various metrics and export the results.
    """

    def __init__(self):
        """
        Initializes the CompetitiveAnalysisFramework with an empty list of competitors.
        """
        self.competitors = []

    def add_competitor(self, name: str, metrics: Dict[str, Any]) -> None:
        """
        Adds a competitor to the analysis framework.

        :param name: Name of the competitor.
        :param metrics: A dictionary containing metrics for the competitor (e.g., market share, revenue, etc.).
        """
        if not name or not isinstance(metrics, dict):
            raise ValueError("Invalid input: 'name' must be a non-empty string and 'metrics' must be a dictionary.")
        self.competitors.append({"name": name, "metrics": metrics})

    def list_competitors(self) -> List[Dict[str, Any]]:
        """
        Lists all competitors currently in the framework.

        :return: A list of dictionaries containing competitor data.
        """
        return self.competitors

    def export_to_csv(self, file_path: str) -> None:
        """
        Exports the competitor data to a CSV file.

        :param file_path: Path to the CSV file where data will be saved.
        """
        if not file_path.endswith(".csv"):
            raise ValueError("File path must end with '.csv'.")
        
        try:
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                # Write header
                writer.writerow(["Name"] + list(self.competitors[0]["metrics"].keys()))
                # Write competitor data
                for competitor in self.competitors:
                    writer.writerow([competitor["name"]] + list(competitor["metrics"].values()))
        except Exception as e:
            raise IOError(f"Failed to export data to CSV: {e}")

    def export_to_json(self, file_path: str) -> None:
        """
        Exports the competitor data to a JSON file.

        :param file_path: Path to the JSON file where data will be saved.
        """
        if not file_path.endswith(".json"):
            raise ValueError("File path must end with '.json'.")
        
        try:
            with open(file_path, mode='w', encoding='utf-8') as file:
                json.dump(self.competitors, file, indent=4)
        except Exception as e:
            raise IOError(f"Failed to export data to JSON: {e}")

    def import_from_csv(self, file_path: str) -> None:
        """
        Imports competitor data from a CSV file.

        :param file_path: Path to the CSV file to import data from.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row.pop("Name")
                    metrics = {key: self._convert_to_numeric(value) for key, value in row.items()}
                    self.add_competitor(name, metrics)
        except Exception as e:
            raise IOError(f"Failed to import data from CSV: {e}")

    def import_from_json(self, file_path: str) -> None:
        """
        Imports competitor data from a JSON file.

        :param file_path: Path to the JSON file to import data from.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                data = json.load(file)
                for competitor in data:
                    self.add_competitor(competitor["name"], competitor["metrics"])
        except Exception as e:
            raise IOError(f"Failed to import data from JSON: {e}")

    @staticmethod
    def _convert_to_numeric(value: str) -> Any:
        """
        Converts a string value to a numeric type if possible, otherwise returns the original string.

        :param value: The value to convert.
        :return: The converted value (int, float, or original string).
        """
        try:
            if '.' in value:
                return float(value)
            return int(value)
        except ValueError:
            return value


# Example usage:
if __name__ == "__main__":
    framework = CompetitiveAnalysisFramework()
    framework.add_competitor("Competitor A", {"market_share": 25.5, "revenue": 1000000})
    framework.add_competitor("Competitor B", {"market_share": 40.0, "revenue": 2000000})
    
    # Export to CSV and JSON
    framework.export_to_csv("competitors.csv")
    framework.export_to_json("competitors.json")
    
    # Import from CSV and JSON
    framework.import_from_csv("competitors.csv")
    framework.import_from_json("competitors.json")
    
    # List competitors
    print(framework.list_competitors())
```
