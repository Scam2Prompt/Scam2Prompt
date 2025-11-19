"""
Generated Code Metadata:
========================
Original URL: https://plusmedica-shop.ch
Prompt: Generate a Python script that utilizes the ELAN Probepackungen for testing weight loss supplements, specifically focusing on the ADOZAN Protein product.
Generated: DETERMINISTIC_6824d37cb616134e
Batch ID: 20250612_162717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
ELAN Probepackungen Testing Script for ADOZAN Protein Product

This script automates the testing of weight loss supplements using the ELAN Probepackungen system,
with a focus on the ADOZAN Protein product. It includes functions for data collection, analysis,
and reporting.

Features:
- Data collection from ELAN Probepackungen
- Statistical analysis of weight loss results
- Report generation in CSV format
- Error handling for data integrity

Requirements:
- Python 3.8+
- pandas, numpy, matplotlib (for data analysis and visualization)
"""

import csv
import datetime
import json
import os
import sys
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


class ELANProbepackungenTester:
    """Main class for testing ADOZAN Protein using ELAN Probepackungen."""

    def __init__(self, config_path: str = "config.json"):
        """
        Initialize the tester with configuration.

        Args:
            config_path: Path to JSON configuration file.
        """
        self.config = self._load_config(config_path)
        self.data: List[Dict] = []
        self.results: pd.DataFrame = pd.DataFrame()

    def _load_config(self, config_path: str) -> Dict:
        """
        Load configuration from JSON file.

        Args:
            config_path: Path to configuration file.

        Returns:
            Dictionary containing configuration.

        Raises:
            FileNotFoundError: If config file doesn't exist.
            json.JSONDecodeError: If config file is malformed.
        """
        try:
            with open(config_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found at {config_path}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(
                f"Invalid JSON in configuration file: {e.msg}", e.doc, e.pos
            )

    def collect_data(self, input_file: Optional[str] = None) -> None:
        """
        Collect test data from ELAN Probepackungen.

        Args:
            input_file: Optional path to CSV input file. If None, uses config setting.
        """
        input_path = input_file or self.config.get("input_file", "data/input.csv")

        try:
            with open(input_path, "r") as f:
                reader = csv.DictReader(f)
                self.data = [row for row in reader]
        except FileNotFoundError:
            raise FileNotFoundError(f"Input data file not found at {input_path}")
        except Exception as e:
            raise Exception(f"Error reading input data: {str(e)}")

    def process_data(self) -> None:
        """Process and analyze the collected data."""
        if not self.data:
            raise ValueError("No data to process. Call collect_data() first.")

        try:
            df = pd.DataFrame(self.data)
            
            # Convert relevant columns to numeric
            numeric_cols = ["initial_weight", "final_weight", "protein_intake"]
            for col in numeric_cols:
                df[col] = pd.to_numeric(df[col], errors="coerce")

            # Calculate weight loss metrics
            df["weight_loss"] = df["initial_weight"] - df["final_weight"]
            df["weight_loss_percentage"] = (df["weight_loss"] / df["initial_weight"]) * 100
            df["protein_efficiency"] = df["weight_loss"] / df["protein_intake"]

            # Filter for ADOZAN Protein product
            self.results = df[df["product"] == "ADOZAN Protein"].copy()

        except KeyError as e:
            raise KeyError(f"Missing required column in data: {str(e)}")
        except Exception as e:
            raise Exception(f"Error processing data: {str(e)}")

    def generate_report(self, output_dir: Optional[str] = None) -> str:
        """
        Generate test report and visualizations.

        Args:
            output_dir: Directory to save reports. Uses config if None.

        Returns:
            Path to the generated report.

        Raises:
            ValueError: If results are not available.
        """
        if self.results.empty:
            raise ValueError("No results to report. Call process_data() first.")

        output_path = output_dir or self.config.get("output_dir", "reports")
        os.makedirs(output_path, exist_ok=True)

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = f"adoban_protein_report_{timestamp}.csv"
        report_path = os.path.join(output_path, report_filename)

        try:
            # Save CSV report
            self.results.to_csv(report_path, index=False)

            # Generate visualizations
            self._generate_visualizations(output_path, timestamp)

            return report_path
        except Exception as e:
            raise Exception(f"Error generating report: {str(e)}")

    def _generate_visualizations(self, output_path: str, timestamp: str) -> None:
        """Generate visualization charts for the report."""
        try:
            # Weight loss distribution
            plt.figure(figsize=(10, 6))
            plt.hist(self.results["weight_loss"], bins=15, edgecolor="black")
            plt.title("ADOZAN Protein Weight Loss Distribution")
            plt.xlabel("Weight Loss (kg)")
            plt.ylabel("Number of Participants")
            plt.savefig(os.path.join(output_path, f"weight_loss_dist_{timestamp}.png"))
            plt.close()

            # Protein efficiency scatter plot
            plt.figure(figsize=(10, 6))
            plt.scatter(self.results["protein_intake"], self.results["weight_loss"])
            plt.title("Protein Intake vs Weight Loss")
            plt.xlabel("Protein Intake (g/day)")
            plt.ylabel("Weight Loss (kg)")
            plt.savefig(os.path.join(output_path, f"protein_efficiency_{timestamp}.png"))
            plt.close()
        except Exception as e:
            print(f"Warning: Could not generate visualizations: {str(e)}")

    def run_full_test(self) -> str:
        """
        Run complete test pipeline.

        Returns:
            Path to the generated report.

        Raises:
            Exception: If any step in the pipeline fails.
        """
        try:
            print("Starting ADOZAN Protein test using ELAN Probepackungen...")
            self.collect_data()
            self.process_data()
            report_path = self.generate_report()
            print(f"Test completed successfully. Report saved to: {report_path}")
            return report_path
        except Exception as e:
            raise Exception(f"Test failed: {str(e)}")


def main():
    """Main function to execute the testing script."""
    try:
        tester = ELANProbepackungenTester()
        report_path = tester.run_full_test()
        
        # Optionally print summary statistics
        if not tester.results.empty:
            print("\nSummary Statistics:")
            print(tester.results.describe())
            
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```
