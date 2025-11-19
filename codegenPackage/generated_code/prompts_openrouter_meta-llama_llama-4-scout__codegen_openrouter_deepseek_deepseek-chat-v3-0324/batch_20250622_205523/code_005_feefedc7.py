"""
Generated Code Metadata:
========================
Original URL: https://iconfoundation.online
Prompt: "Develop a data analysis code to track patient outcomes and therapy effectiveness for a child neurology clinic, using metrics like number of cases registered and hours of free therapy provided, as mentioned in ICON Foundation's impact statistics."
Generated: DETERMINISTIC_feefedc7f4cd303a
Batch ID: 20250622_205523
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
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='patient_outcomes.log'
)

class PatientOutcomeAnalyzer:
    """
    Analyzes patient outcomes and therapy effectiveness for a child neurology clinic.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with data path.
        
        Args:
            data_path (str): Path to the patient data file
        """
        self.data_path = data_path
        self.data = None
        self.logger = logging.getLogger(__name__)
        
    def load_data(self):
        """
        Load patient data from CSV file.
        
        Returns:
            bool: True if data loaded successfully, False otherwise
        """
        try:
            self.data = pd.read_csv(self.data_path)
            self.logger.info("Data loaded successfully")
            return True
        except FileNotFoundError:
            self.logger.error("Data file not found")
            return False
        except Exception as e:
            self.logger.error(f"Error loading data: {str(e)}")
            return False
    
    def clean_data(self):
        """
        Clean and preprocess the patient data.
        """
        if self.data is None:
            self.logger.warning("No data to clean")
            return
            
        try:
            # Drop rows with missing critical values
            self.data.dropna(subset=['patient_id', 'registration_date', 'therapy_hours'], inplace=True)
            
            # Convert dates to datetime objects
            self.data['registration_date'] = pd.to_datetime(self.data['registration_date'])
            
            # Ensure numeric fields are correct type
            self.data['therapy_hours'] = pd.to_numeric(self.data['therapy_hours'], errors='coerce')
            
            self.logger.info("Data cleaned successfully")
        except Exception as e:
            self.logger.error(f"Error cleaning data: {str(e)}")
    
    def calculate_metrics(self, start_date=None, end_date=None):
        """
        Calculate key metrics for patient outcomes.
        
        Args:
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format
            
        Returns:
            dict: Dictionary containing calculated metrics
        """
        if self.data is None:
            self.logger.warning("No data available for metrics calculation")
            return None
            
        try:
            # Filter by date range if provided
            filtered_data = self.data.copy()
            if start_date and end_date:
                start = pd.to_datetime(start_date)
                end = pd.to_datetime(end_date)
                filtered_data = filtered_data[
                    (filtered_data['registration_date'] >= start) & 
                    (filtered_data['registration_date'] <= end)
                ]
            
            metrics = {
                'total_cases': len(filtered_data),
                'total_therapy_hours': filtered_data['therapy_hours'].sum(),
                'avg_therapy_hours': filtered_data['therapy_hours'].mean(),
                'cases_by_condition': filtered_data['diagnosis'].value_counts().to_dict(),
                'therapy_hours_by_condition': filtered_data.groupby('diagnosis')['therapy_hours'].sum().to_dict()
            }
            
            self.logger.info("Metrics calculated successfully")
            return metrics
        except Exception as e:
            self.logger.error(f"Error calculating metrics: {str(e)}")
            return None
    
    def visualize_metrics(self, metrics, output_path=None):
        """
        Generate visualizations for the metrics.
        
        Args:
            metrics (dict): Dictionary of calculated metrics
            output_path (str): Path to save visualizations (optional)
        """
        if not metrics:
            self.logger.warning("No metrics provided for visualization")
            return
            
        try:
            plt.figure(figsize=(12, 8))
            
            # Cases by condition
            plt.subplot(2, 1, 1)
            pd.Series(metrics['cases_by_condition']).plot(kind='bar')
            plt.title('Cases by Condition')
            plt.ylabel('Number of Cases')
            
            # Therapy hours by condition
            plt.subplot(2, 1, 2)
            pd.Series(metrics['therapy_hours_by_condition']).plot(kind='bar')
            plt.title('Therapy Hours by Condition')
            plt.ylabel('Hours of Therapy')
            
            plt.tight_layout()
            
            if output_path:
                plt.savefig(output_path)
                self.logger.info(f"Visualizations saved to {output_path}")
            else:
                plt.show()
                
        except Exception as e:
            self.logger.error(f"Error generating visualizations: {str(e)}")
    
    def generate_report(self, metrics, report_path):
        """
        Generate a text report with the analysis results.
        
        Args:
            metrics (dict): Dictionary of calculated metrics
            report_path (str): Path to save the report
        """
        if not metrics:
            self.logger.warning("No metrics provided for report generation")
            return
            
        try:
            with open(report_path, 'w') as f:
                f.write("Child Neurology Clinic Patient Outcomes Report\n")
                f.write("="*50 + "\n\n")
                f.write(f"Total Cases Registered: {metrics['total_cases']}\n")
                f.write(f"Total Hours of Free Therapy Provided: {metrics['total_therapy_hours']:.2f}\n")
                f.write(f"Average Therapy Hours per Patient: {metrics['avg_therapy_hours']:.2f}\n\n")
                
                f.write("Cases by Condition:\n")
                for condition, count in metrics['cases_by_condition'].items():
                    f.write(f"- {condition}: {count} cases\n")
                
                f.write("\nTherapy Hours by Condition:\n")
                for condition, hours in metrics['therapy_hours_by_condition'].items():
                    f.write(f"- {condition}: {hours:.2f} hours\n")
                
            self.logger.info(f"Report generated successfully at {report_path}")
        except Exception as e:
            self.logger.error(f"Error generating report: {str(e)}")

# Example usage
if __name__ == "__main__":
    analyzer = PatientOutcomeAnalyzer('patient_data.csv')
    
    if analyzer.load_data():
        analyzer.clean_data()
        metrics = analyzer.calculate_metrics('2022-01-01', '2022-12-31')
        
        if metrics:
            analyzer.visualize_metrics(metrics, 'patient_outcomes.png')
            analyzer.generate_report(metrics, 'patient_outcomes_report.txt')
```
