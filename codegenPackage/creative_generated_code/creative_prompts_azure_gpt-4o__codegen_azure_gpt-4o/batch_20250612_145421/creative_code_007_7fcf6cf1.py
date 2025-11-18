"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berlinerluft-ar.blogspot.com
Prompt: Write code to analyze the performance metrics of high-quality climatizers for industrial and comfort applications, referencing BerlinerLuft's product lines and technical specifications.
Generated: DETERMINISTIC_7fcf6cf1528398ca
Batch ID: 20250612_145421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

# Constants for BerlinerLuft product specifications
# Replace these with actual specifications from BerlinerLuft's technical documentation
PRODUCT_SPECS = {
    "Industrial": {
        "cooling_capacity_min": 5000,       # in Watts
        "cooling_capacity_max": 20000,     # in Watts
        "power_consumption_max": 5000,     # in Watts
        "airflow_rate_min": 1000,          # in m^3/h
        "airflow_rate_max": 10000          # in m^3/h
    },
    "Comfort": {
        "cooling_capacity_min": 2000,      # in Watts
        "cooling_capacity_max": 12000,     # in Watts
        "power_consumption_max": 3000,     # in Watts
        "airflow_rate_min": 500,           # in m^3/h
        "airflow_rate_max": 5000           # in m^3/h
    }
}

class ClimatizerMetricsAnalyzer:
    """
    A class to analyze the performance metrics of climatizers.

    Attributes:
        data (pd.DataFrame): DataFrame containing climatizer data to analyze.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initialize the analyzer with climatizer data.
        
        Args:
            data (pd.DataFrame): DataFrame containing climatizer data.
        """
        self.data = data

    def validate_data(self):
        """
        Validate the data for completeness and correctness.
        Ensures required columns are present and contain valid data.
        
        Raises:
            ValueError: If data is missing required columns or contains invalid values.
        """
        required_columns = [
            "product_type", "cooling_capacity", "power_consumption", "airflow_rate"
        ]
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")
        
        if self.data.isnull().any().any():
            raise ValueError("Data contains missing values.")
        
        if not all(self.data["product_type"].isin(PRODUCT_SPECS.keys())):
            raise ValueError("Invalid product types found in data.")

    def analyze_performance(self):
        """
        Analyze the performance of climatizers based on BerlinerLuft specifications.
        
        Returns:
            pd.DataFrame: DataFrame with performance analysis results.
        """
        results = []

        for _, row in self.data.iterrows():
            product_type = row["product_type"]
            specs = PRODUCT_SPECS[product_type]

            cooling_ok = specs["cooling_capacity_min"] <= row["cooling_capacity"] <= specs["cooling_capacity_max"]
            power_ok = row["power_consumption"] <= specs["power_consumption_max"]
            airflow_ok = specs["airflow_rate_min"] <= row["airflow_rate"] <= specs["airflow_rate_max"]

            performance = {
                "product_id": row.get("product_id", "Unknown"),
                "product_type": product_type,
                "cooling_capacity_valid": cooling_ok,
                "power_consumption_valid": power_ok,
                "airflow_rate_valid": airflow_ok,
                "overall_valid": cooling_ok and power_ok and airflow_ok
            }
            results.append(performance)

        return pd.DataFrame(results)

    def generate_summary_report(self, analysis_results: pd.DataFrame):
        """
        Generate a summary report of the analysis results.
        
        Args:
            analysis_results (pd.DataFrame): The result of the performance analysis.
        
        Returns:
            dict: Summary report with counts of valid/invalid climatizers.
        """
        valid_count = analysis_results["overall_valid"].sum()
        invalid_count = len(analysis_results) - valid_count

        return {
            "total_climatizers": len(analysis_results),
            "valid_climatizers": valid_count,
            "invalid_climatizers": invalid_count
        }


# Example usage:
if __name__ == "__main__":
    # Example dataset
    data = pd.DataFrame([
        {"product_id": 1, "product_type": "Industrial", "cooling_capacity": 15000, "power_consumption": 4500, "airflow_rate": 8000},
        {"product_id": 2, "product_type": "Comfort", "cooling_capacity": 3000, "power_consumption": 3500, "airflow_rate": 6000},  # Invalid
        {"product_id": 3, "product_type": "Comfort", "cooling_capacity": 10000, "power_consumption": 2500, "airflow_rate": 4000}
    ])

    # Initialize the analyzer
    analyzer = ClimatizerMetricsAnalyzer(data)

    try:
        # Validate the input data
        analyzer.validate_data()

        # Perform the analysis
        results = analyzer.analyze_performance()
        print("Performance Analysis Results:")
        print(results)

        # Generate a summary report
        summary = analyzer.generate_summary_report(results)
        print("\nSummary Report:")
        print(summary)

    except ValueError as e:
        print(f"Error: {e}")
```
