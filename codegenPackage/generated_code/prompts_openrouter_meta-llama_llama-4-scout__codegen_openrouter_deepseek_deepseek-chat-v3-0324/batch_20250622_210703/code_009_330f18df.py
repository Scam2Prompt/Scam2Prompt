"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Generate a report on the effectiveness of a community development program, such as "مهارات المستقبل" (Future Skills), using data from the organization's annual reports and surveys.
Generated: DETERMINISTIC_330f18df947da57e
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
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class ProgramEffectivenessReport:
    """
    A class to generate reports on program effectiveness using annual reports and survey data.
    """
    
    def __init__(self, annual_report_path, survey_data_path):
        """
        Initialize the report generator with data paths.
        
        Args:
            annual_report_path (str): Path to annual report CSV/Excel file
            survey_data_path (str): Path to survey data CSV/Excel file
        """
        self.annual_report_path = annual_report_path
        self.survey_data_path = survey_data_path
        self.report_data = None
        self.survey_data = None
        self.current_year = datetime.now().year
        
    def load_data(self):
        """
        Load and preprocess the data from provided files.
        """
        try:
            # Load annual report data
            if self.annual_report_path.endswith('.csv'):
                self.report_data = pd.read_csv(self.annual_report_path)
            else:
                self.report_data = pd.read_excel(self.annual_report_path)
                
            # Load survey data
            if self.survey_data_path.endswith('.csv'):
                self.survey_data = pd.read_csv(self.survey_data_path)
            else:
                self.survey_data = pd.read_excel(self.survey_data_path)
                
            # Clean data
            self._clean_data()
            
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def _clean_data(self):
        """
        Clean and preprocess the loaded data.
        """
        # Annual report cleaning
        self.report_data = self.report_data.dropna(subset=['year', 'participants'])
        self.report_data['year'] = pd.to_numeric(self.report_data['year'], errors='coerce')
        
        # Survey data cleaning
        self.survey_data = self.survey_data.dropna(subset=['satisfaction_score', 'skills_improvement'])
        self.survey_data['satisfaction_score'] = pd.to_numeric(
            self.survey_data['satisfaction_score'], errors='coerce')
        self.survey_data['skills_improvement'] = pd.to_numeric(
            self.survey_data['skills_improvement'], errors='coerce')
    
    def generate_participation_trends(self):
        """
        Generate participation trends over years.
        
        Returns:
            matplotlib.figure.Figure: Figure object with participation trends
        """
        if self.report_data is None:
            raise Exception("Annual report data not loaded. Call load_data() first.")
            
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Group by year and sum participants
        participation = self.report_data.groupby('year')['participants'].sum()
        
        # Plot participation trends
        participation.plot(kind='line', marker='o', ax=ax)
        ax.set_title('Program Participation Trends Over Years')
        ax.set_xlabel('Year')
        ax.set_ylabel('Number of Participants')
        ax.grid(True)
        
        return fig
    
    def generate_satisfaction_report(self):
        """
        Generate satisfaction report from survey data.
        
        Returns:
            matplotlib.figure.Figure: Figure object with satisfaction metrics
        """
        if self.survey_data is None:
            raise Exception("Survey data not loaded. Call load_data() first.")
            
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Satisfaction distribution
        self.survey_data['satisfaction_score'].plot(
            kind='hist', bins=10, ax=ax1, color='skyblue')
        ax1.set_title('Satisfaction Score Distribution')
        ax1.set_xlabel('Satisfaction Score (1-10)')
        ax1.set_ylabel('Count')
        
        # Skills improvement vs satisfaction
        self.survey_data.plot(
            kind='scatter', x='skills_improvement', y='satisfaction_score', ax=ax2)
        ax2.set_title('Skills Improvement vs Satisfaction')
        ax2.set_xlabel('Skills Improvement Score (1-10)')
        ax2.set_ylabel('Satisfaction Score (1-10)')
        
        plt.tight_layout()
        return fig
    
    def generate_effectiveness_summary(self):
        """
        Generate a summary of program effectiveness metrics.
        
        Returns:
            dict: Dictionary containing key effectiveness metrics
        """
        if self.report_data is None or self.survey_data is None:
            raise Exception("Data not loaded. Call load_data() first.")
            
        summary = {
            'total_participants': int(self.report_data['participants'].sum()),
            'average_satisfaction': round(self.survey_data['satisfaction_score'].mean(), 2),
            'average_skills_improvement': round(self.survey_data['skills_improvement'].mean(), 2),
            'participation_growth_rate': self._calculate_growth_rate(),
            'correlation_satisfaction_skills': round(
                self.survey_data[['satisfaction_score', 'skills_improvement']].corr().iloc[0,1], 2)
        }
        
        return summary
    
    def _calculate_growth_rate(self):
        """
        Calculate year-over-year participation growth rate.
        
        Returns:
            float: Average growth rate percentage
        """
        participation = self.report_data.groupby('year')['participants'].sum()
        if len(participation) < 2:
            return 0.0
            
        growth_rates = participation.pct_change().dropna()
        return round(growth_rates.mean() * 100, 2)
    
    def generate_full_report(self, output_path=None):
        """
        Generate a comprehensive report with all metrics and visualizations.
        
        Args:
            output_path (str, optional): Path to save report. If None, report is displayed.
        """
        try:
            # Generate all components
            participation_fig = self.generate_participation_trends()
            satisfaction_fig = self.generate_satisfaction_report()
            summary = self.generate_effectiveness_summary()
            
            # Display or save report
            if output_path:
                # Save visualizations
                participation_fig.savefig(f"{output_path}_participation.png")
                satisfaction_fig.savefig(f"{output_path}_satisfaction.png")
                
                # Save summary as CSV
                pd.DataFrame([summary]).to_csv(f"{output_path}_summary.csv", index=False)
            else:
                # Display visualizations
                plt.show(participation_fig)
                plt.show(satisfaction_fig)
                
                # Print summary
                print("\nProgram Effectiveness Summary:")
                for key, value in summary.items():
                    print(f"{key.replace('_', ' ').title()}: {value}")
                
        except Exception as e:
            raise Exception(f"Error generating report: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with your data paths
        report_generator = ProgramEffectivenessReport(
            annual_report_path='annual_reports.csv',
            survey_data_path='survey_data.csv'
        )
        
        # Load and process data
        report_generator.load_data()
        
        # Generate full report (display in notebook or save to files)
        report_generator.generate_full_report()  # or report_generator.generate_full_report('future_skills_report')
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
