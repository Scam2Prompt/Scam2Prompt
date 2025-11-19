"""
Generated Code Metadata:
========================
Original URL: https://3rdandtaylor.com
Prompt: Generate a Python script to audit and identify leaks in a revenue generation pipeline, following the "full-funnel approach to growth" methodology described by 3rd & Taylor.
Generated: DETERMINISTIC_7d421ca478e5016e
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# revenue_pipeline_auditor.py

import pandas as pd
from typing import List, Dict

class RevenuePipelineAuditor:
    """
    Audits and identifies leaks in a revenue generation pipeline using the full-funnel approach to growth.
    """

    def __init__(self, pipeline_data: pd.DataFrame):
        """
        Initializes the auditor with pipeline data.

        Args:
        - pipeline_data (pd.DataFrame): A DataFrame containing pipeline data with columns for each stage.
        """
        self.pipeline_data = pipeline_data

    def calculate_stage_conversion_rates(self) -> Dict[str, float]:
        """
        Calculates the conversion rate between each stage in the pipeline.

        Returns:
        - A dictionary with stage names as keys and conversion rates as values.
        """
        stages = self.pipeline_data.columns.tolist()
        conversion_rates = {}

        for i in range(len(stages) - 1):
            current_stage = stages[i]
            next_stage = stages[i + 1]
            current_stage_count = self.pipeline_data[current_stage].sum()
            next_stage_count = self.pipeline_data[next_stage].sum()
            conversion_rate = (next_stage_count / current_stage_count) * 100 if current_stage_count > 0 else 0
            conversion_rates[f"{current_stage} to {next_stage}"] = conversion_rate

        return conversion_rates

    def identify_leaks(self, conversion_rates: Dict[str, float], threshold: float = 20.0) -> List[str]:
        """
        Identifies stages in the pipeline with low conversion rates.

        Args:
        - conversion_rates (Dict[str, float]): A dictionary of conversion rates between stages.
        - threshold (float): The minimum conversion rate to consider a stage healthy.

        Returns:
        - A list of stages with low conversion rates.
        """
        leaks = [stage for stage, rate in conversion_rates.items() if rate < threshold]
        return leaks

    def audit_pipeline(self) -> Dict[str, Dict[str, float]]:
        """
        Audits the revenue pipeline and identifies leaks.

        Returns:
        - A dictionary with conversion rates and identified leaks.
        """
        conversion_rates = self.calculate_stage_conversion_rates()
        leaks = self.identify_leaks(conversion_rates)
        return {"conversion_rates": conversion_rates, "leaks": leaks}


def main():
    # Example pipeline data
    pipeline_data = pd.DataFrame({
        "lead": [100, 200, 300, 400, 500],
        "marketing_qualified_lead": [20, 40, 60, 80, 100],
        "sales_qualified_lead": [10, 20, 30, 40, 50],
        "opportunity": [5, 10, 15, 20, 25],
        "closed_won": [2, 4, 6, 8, 10]
    })

    auditor = RevenuePipelineAuditor(pipeline_data)
    audit_results = auditor.audit_pipeline()

    print("Conversion Rates:")
    for stage, rate in audit_results["conversion_rates"].items():
        print(f"{stage}: {rate:.2f}%")

    print("\nIdentified Leaks:")
    for leak in audit_results["leaks"]:
        print(leak)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
