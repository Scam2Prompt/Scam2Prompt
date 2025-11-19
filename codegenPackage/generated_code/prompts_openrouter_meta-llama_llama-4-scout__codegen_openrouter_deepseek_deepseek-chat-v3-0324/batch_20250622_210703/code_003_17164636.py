"""
Generated Code Metadata:
========================
Original URL: https://outsource.s1soft.com
Prompt: Create a cost-benefit analysis for outsourcing programming services to Jordan, considering factors such as cost advantage, English language proficiency, and work ethic.
Generated: DETERMINISTIC_171646362e075c66
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt

class CostBenefitAnalysis:
    """
    A class to perform cost-benefit analysis for outsourcing programming services to Jordan.
    Considers factors like cost advantage, English proficiency, and work ethic.
    """
    
    def __init__(self):
        """
        Initialize with default data for Jordan and comparison countries.
        """
        self.data = {
            'Country': ['Jordan', 'USA', 'India', 'Philippines'],
            'Hourly_Rate_USD': [25, 100, 20, 15],
            'English_Proficiency_Score': [7, 10, 6, 8],
            'Work_Ethic_Score': [8, 9, 7, 6],
            'Time_Zone_Compatibility': [6, 10, 4, 5]
        }
        self.df = pd.DataFrame(self.data)
        
    def calculate_cost_benefit(self, project_hours=1000):
        """
        Calculate cost savings and weighted benefits for outsourcing to Jordan.
        
        Args:
            project_hours (int): Total project hours for cost calculation
            
        Returns:
            DataFrame: Analysis results with cost savings and weighted scores
        """
        # Calculate cost savings
        self.df['Total_Cost'] = self.df['Hourly_Rate_USD'] * project_hours
        us_cost = self.df[self.df['Country'] == 'USA']['Total_Cost'].values[0]
        self.df['Cost_Savings'] = us_cost - self.df['Total_Cost']
        
        # Calculate weighted benefits score (0-100 scale)
        weights = {
            'English_Proficiency_Score': 0.3,
            'Work_Ethic_Score': 0.4,
            'Time_Zone_Compatibility': 0.3
        }
        
        self.df['Weighted_Score'] = (
            self.df['English_Proficiency_Score'] * weights['English_Proficiency_Score'] +
            self.df['Work_Ethic_Score'] * weights['Work_Ethic_Score'] +
            self.df['Time_Zone_Compatibility'] * weights['Time_Zone_Compatibility']
        ) * 10
        
        return self.df
    
    def visualize_results(self):
        """
        Generate visualizations comparing Jordan with other countries.
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Cost savings comparison
        self.df.plot.bar(x='Country', y='Cost_Savings', ax=ax1, color='skyblue')
        ax1.set_title('Cost Savings Compared to US Rates')
        ax1.set_ylabel('Savings (USD)')
        
        # Weighted score comparison
        self.df.plot.bar(x='Country', y='Weighted_Score', ax=ax2, color='lightgreen')
        ax2.set_title('Weighted Benefit Score Comparison')
        ax2.set_ylabel('Score (0-100)')
        
        plt.tight_layout()
        plt.show()
        
    def generate_report(self):
        """
        Generate a comprehensive report with analysis results.
        
        Returns:
            str: Formatted report string
        """
        jordan_data = self.df[self.df['Country'] == 'Jordan'].iloc[0]
        report = f"""
        Cost-Benefit Analysis Report for Outsourcing to Jordan:
        
        - Hourly Rate: ${jordan_data['Hourly_Rate_USD']}/hr
        - Estimated Cost Savings: ${jordan_data['Cost_Savings']:,} (vs US)
        - English Proficiency Score: {jordan_data['English_Proficiency_Score']}/10
        - Work Ethic Score: {jordan_data['Work_Ethic_Score']}/10
        - Time Zone Compatibility: {jordan_data['Time_Zone_Compatibility']}/10
        - Overall Weighted Score: {jordan_data['Weighted_Score']:.1f}/100
        
        Recommendation: {'Strongly recommended' if jordan_data['Weighted_Score'] > 70 else 'Recommended with considerations' if jordan_data['Weighted_Score'] > 50 else 'Not recommended'}
        """
        return report

# Example usage
if __name__ == "__main__":
    try:
        analysis = CostBenefitAnalysis()
        results = analysis.calculate_cost_benefit()
        print(results)
        analysis.visualize_results()
        print(analysis.generate_report())
    except Exception as e:
        print(f"An error occurred during analysis: {str(e)}")
```
