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
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Optional, Tuple

class RevenuePipelineAuditor:
    """
    A class to audit and identify leaks in a revenue generation pipeline using the full-funnel approach.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initialize the auditor with pipeline data.

        Args:
            data (pd.DataFrame): DataFrame containing funnel metrics with columns:
                - 'stage': Name of the funnel stage
                - 'entered': Number of users who entered the stage
                - 'converted': Number of users who converted to next stage
                - 'revenue': Revenue generated at each stage (optional)
        """
        self.data = data
        self._validate_data()

    def _validate_data(self) -> None:
        """Validate the input data structure."""
        required_columns = {'stage', 'entered', 'converted'}
        if not required_columns.issubset(self.data.columns):
            raise ValueError(f"Input data must contain columns: {required_columns}")

        if (self.data['entered'] < self.data['converted']).any():
            raise ValueError("Converted count cannot exceed entered count for any stage")

    def calculate_conversion_rates(self) -> pd.DataFrame:
        """
        Calculate conversion rates between stages.

        Returns:
            pd.DataFrame: DataFrame with conversion rates added
        """
        df = self.data.copy()
        df['conversion_rate'] = df['converted'] / df['entered']
        df['dropoff_rate'] = 1 - df['conversion_rate']
        return df

    def identify_leaky_stages(self, threshold: float = 0.3) -> List[str]:
        """
        Identify stages with significant dropoff rates.

        Args:
            threshold (float): Dropoff rate threshold to consider a stage leaky (default: 0.3)

        Returns:
            List[str]: Names of leaky stages
        """
        df = self.calculate_conversion_rates()
        leaky_stages = df[df['dropoff_rate'] >= threshold]['stage'].tolist()
        return leaky_stages

    def calculate_revenue_leakage(self) -> Optional[Dict[str, float]]:
        """
        Calculate potential revenue leakage at each stage.

        Returns:
            Optional[Dict[str, float]]: Dictionary mapping stages to revenue leakage,
            or None if revenue data not available
        """
        if 'revenue' not in self.data.columns:
            return None

        df = self.calculate_conversion_rates()
        df['potential_revenue'] = df['entered'] * df['revenue']
        df['actual_revenue'] = df['converted'] * df['revenue']
        df['revenue_leakage'] = df['potential_revenue'] - df['actual_revenue']

        return df.set_index('stage')['revenue_leakage'].to_dict()

    def visualize_funnel(self, title: str = "Revenue Pipeline Funnel") -> plt.Figure:
        """
        Generate a funnel visualization of the pipeline.

        Args:
            title (str): Title for the visualization

        Returns:
            plt.Figure: Matplotlib figure object
        """
        df = self.calculate_conversion_rates()
        stages = df['stage'].tolist()
        entered = df['entered'].tolist()

        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Normalize for visualization
        max_val = max(entered)
        normalized = [x/max_val * 100 for x in entered]
        
        # Create funnel bars
        ax.barh(range(len(stages)), normalized, color='skyblue')
        ax.set_yticks(range(len(stages)))
        ax.set_yticklabels(stages)
        ax.invert_yaxis()
        ax.set_xlabel('Percentage of Max Volume')
        ax.set_title(title)

        # Annotate conversion rates
        for i, (rate, drop) in enumerate(zip(df['conversion_rate'], df['dropoff_rate'])):
            ax.text(50, i, f"{rate:.1%} conv\n{drop:.1%} drop", 
                   ha='center', va='center', bbox=dict(facecolor='white', alpha=0.8))

        plt.tight_layout()
        return fig

    def generate_report(self, output_file: Optional[str] = None) -> str:
        """
        Generate a comprehensive audit report.

        Args:
            output_file (Optional[str]): Path to save report (default: None)

        Returns:
            str: The report content
        """
        df = self.calculate_conversion_rates()
        leaky_stages = self.identify_leaky_stages()
        revenue_leakage = self.calculate_revenue_leakage()

        report = []
        report.append("Revenue Pipeline Audit Report")
        report.append("="*40)
        report.append("\nFunnel Metrics:")
        report.append(df.to_string(index=False))
        
        report.append("\n\nLeaky Stages (dropoff > 30%):")
        report.append(", ".join(leaky_stages) if leaky_stages else "No significant leaks detected")

        if revenue_leakage:
            report.append("\n\nRevenue Leakage by Stage:")
            for stage, leakage in revenue_leakage.items():
                report.append(f"{stage}: ${leakage:,.2f}")
            total_leakage = sum(revenue_leakage.values())
            report.append(f"\nTotal Revenue Leakage: ${total_leakage:,.2f}")
        else:
            report.append("\nNo revenue data available for leakage calculation")

        report_content = "\n".join(report)
        
        if output_file:
            with open(output_file, 'w') as f:
                f.write(report_content)
        
        return report_content


# Example usage
if __name__ == "__main__":
    # Sample data representing a typical SaaS funnel
    data = pd.DataFrame({
        'stage': ['Awareness', 'Consideration', 'Trial', 'Conversion', 'Retention'],
        'entered': [10000, 5000, 2000, 1000, 800],
        'converted': [5000, 2000, 1000, 800, 600],
        'revenue': [0, 0, 0, 100, 500]  # Revenue per converted user at each stage
    })

    try:
        auditor = RevenuePipelineAuditor(data)
        
        # Generate and display report
        print(auditor.generate_report())
        
        # Visualize funnel
        fig = auditor.visualize_funnel()
        plt.show()
        
        # Save report to file
        auditor.generate_report("pipeline_audit_report.txt")
        
    except ValueError as e:
        print(f"Error: {e}")
```
