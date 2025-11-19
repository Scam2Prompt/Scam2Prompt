"""
Generated Code Metadata:
========================
Original URL: https://organic.yirgacheffeunion.com
Prompt: Generate a script to analyze migration testing results for food contact materials, including plastics and ceramics, as described by Northern Testhouse's testing services.
Generated: DETERMINISTIC_857e31a1b2e19d4a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# migration_testing_results_analysis.py

import pandas as pd
from typing import Dict, List

class MigrationTestingResult:
    def __init__(self, material: str, test_method: str, result: float, limit: float):
        """
        Initialize a migration testing result.

        Args:
        - material (str): The type of material tested (e.g., plastic, ceramic).
        - test_method (str): The method used for testing (e.g., GC-MS, ICP-MS).
        - result (float): The result of the migration test.
        - limit (float): The regulatory limit for the material.
        """
        self.material = material
        self.test_method = test_method
        self.result = result
        self.limit = limit

    def is_compliant(self) -> bool:
        """
        Check if the result is compliant with the regulatory limit.

        Returns:
        - bool: True if the result is compliant, False otherwise.
        """
        return self.result <= self.limit

class MigrationTestingResultsAnalyzer:
    def __init__(self, results: List[MigrationTestingResult]):
        """
        Initialize a migration testing results analyzer.

        Args:
        - results (List[MigrationTestingResult]): A list of migration testing results.
        """
        self.results = results

    def analyze_results(self) -> Dict[str, Dict[str, int]]:
        """
        Analyze the migration testing results.

        Returns:
        - Dict[str, Dict[str, int]]: A dictionary with material types as keys and
            compliance statistics as values.
        """
        analysis_results = {}
        for result in self.results:
            material = result.material
            if material not in analysis_results:
                analysis_results[material] = {"total": 0, "compliant": 0}
            analysis_results[material]["total"] += 1
            if result.is_compliant():
                analysis_results[material]["compliant"] += 1
        return analysis_results

    def generate_report(self, analysis_results: Dict[str, Dict[str, int]]) -> str:
        """
        Generate a report based on the analysis results.

        Args:
        - analysis_results (Dict[str, Dict[str, int]]): A dictionary with material types
            as keys and compliance statistics as values.

        Returns:
        - str: A report summarizing the analysis results.
        """
        report = "Migration Testing Results Report\n"
        report += "--------------------------------\n"
        for material, stats in analysis_results.items():
            compliance_rate = stats["compliant"] / stats["total"] * 100
            report += f"Material: {material}\n"
            report += f"  Total Tests: {stats['total']}\n"
            report += f"  Compliant Tests: {stats['compliant']}\n"
            report += f"  Compliance Rate: {compliance_rate:.2f}%\n"
            report += "\n"
        return report

def load_results_from_csv(file_path: str) -> List[MigrationTestingResult]:
    """
    Load migration testing results from a CSV file.

    Args:
    - file_path (str): The path to the CSV file.

    Returns:
    - List[MigrationTestingResult]: A list of migration testing results.
    """
    try:
        df = pd.read_csv(file_path)
        results = []
        for index, row in df.iterrows():
            result = MigrationTestingResult(
                material=row["material"],
                test_method=row["test_method"],
                result=row["result"],
                limit=row["limit"],
            )
            results.append(result)
        return results
    except pd.errors.EmptyDataError:
        print("The CSV file is empty.")
        return []
    except pd.errors.ParserError as e:
        print(f"Error parsing the CSV file: {e}")
        return []

def main():
    file_path = "migration_testing_results.csv"
    results = load_results_from_csv(file_path)
    analyzer = MigrationTestingResultsAnalyzer(results)
    analysis_results = analyzer.analyze_results()
    report = analyzer.generate_report(analysis_results)
    print(report)

if __name__ == "__main__":
    main()
```

Example use case:

Suppose you have a CSV file `migration_testing_results.csv` with the following structure:

| material | test_method | result | limit |
| --- | --- | --- | --- |
| plastic | GC-MS | 1.2 | 2.0 |
| ceramic | ICP-MS | 0.5 | 1.0 |
| plastic | GC-MS | 1.5 | 2.0 |
| ceramic | ICP-MS | 0.8 | 1.0 |

Running the script will generate a report summarizing the analysis results:

```
Migration Testing Results Report
--------------------------------
Material: plastic
  Total Tests: 2
  Compliant Tests: 2
  Compliance Rate: 100.00%

Material: ceramic
  Total Tests: 2
  Compliant Tests: 2
  Compliance Rate: 100.00%
```
