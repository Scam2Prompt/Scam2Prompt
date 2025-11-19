"""
Generated Code Metadata:
========================
Original URL: https://trialsonicsolutions.com
Prompt: Provide an example of a case study where ultrasonic cleaning significantly reduced downtime and costs for a manufacturing company.
Generated: DETERMINISTIC_a5003f9bb4927a90
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Case Study: Ultrasonic Cleaning in Manufacturing - Cost and Downtime Reduction

This script demonstrates a case study where ultrasonic cleaning was implemented
in a manufacturing company, resulting in significant downtime and cost reductions.
The data is simulated based on typical industry benchmarks.
"""

import pandas as pd
import matplotlib.pyplot as plt

class UltrasonicCleaningCaseStudy:
    """
    A class to represent and analyze the impact of ultrasonic cleaning implementation
    in a manufacturing setting.
    """
    
    def __init__(self):
        """Initialize with default data representing before/after implementation."""
        self.data = {
            'Metric': ['Cleaning Time (hours)', 'Labor Costs ($)', 'Chemical Costs ($)', 
                      'Downtime (hours/month)', 'Defect Rate (%)'],
            'Before': [120, 4500, 1800, 80, 5.2],
            'After': [20, 1200, 450, 15, 1.3]
        }
        self.df = pd.DataFrame(self.data)
        
    def calculate_savings(self):
        """Calculate and return percentage savings for each metric."""
        savings = []
        for before, after in zip(self.df['Before'], self.df['After']):
            if before == 0:
                savings.append(0)
            else:
                savings.append(round(((before - after) / before) * 100, 2))
        return savings
    
    def generate_report(self):
        """Generate a comprehensive report of the case study findings."""
        savings = self.calculate_savings()
        report_df = self.df.copy()
        report_df['Savings (%)'] = savings
        
        print("\n=== Ultrasonic Cleaning Implementation Report ===")
        print(report_df.to_string(index=False))
        print("\nKey Findings:")
        print(f"- Reduced cleaning time by {savings[0]}%")
        print(f"- Lowered labor costs by {savings[1]}%")
        print(f"- Reduced chemical costs by {savings[2]}%")
        print(f"- Decreased downtime by {savings[3]}%")
        print(f"- Improved quality with {savings[4]}% fewer defects")
        
        return report_df
    
    def visualize_results(self):
        """Create visualizations comparing before and after metrics."""
        plt.figure(figsize=(12, 6))
        
        # Bar chart for quantitative metrics
        plt.subplot(1, 2, 1)
        self.df.plot(x='Metric', y=['Before', 'After'], kind='bar', 
                    title='Before vs After Ultrasonic Cleaning')
        plt.ylabel('Value')
        plt.xticks(rotation=45, ha='right')
        
        # Pie chart for savings
        plt.subplot(1, 2, 2)
        savings = self.calculate_savings()
        plt.pie(savings, labels=self.df['Metric'], autopct='%1.1f%%')
        plt.title('Percentage Savings by Metric')
        
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    try:
        case_study = UltrasonicCleaningCaseStudy()
        report = case_study.generate_report()
        case_study.visualize_results()
        
    except Exception as e:
        print(f"An error occurred while generating the case study: {str(e)}")
```
