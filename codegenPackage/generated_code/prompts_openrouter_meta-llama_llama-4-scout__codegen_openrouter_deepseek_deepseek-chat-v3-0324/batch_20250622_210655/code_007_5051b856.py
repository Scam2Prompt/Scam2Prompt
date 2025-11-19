"""
Generated Code Metadata:
========================
Original URL: https://gesec.com.co
Prompt: "Write a Python script to analyze and visualize incident rates in a workplace, helping to identify areas for improvement in the SG-SST implementation."
Generated: DETERMINISTIC_5051b856320e2607
Batch ID: 20250622_210655
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
import seaborn as sns
from datetime import datetime
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('incident_analysis.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

class IncidentAnalyzer:
    """
    A class to analyze and visualize workplace incident rates for SG-SST implementation improvement.
    """

    def __init__(self, data_path):
        """
        Initialize the IncidentAnalyzer with data from the specified path.

        Args:
            data_path (str): Path to the incident data file (CSV or Excel).
        """
        self.data_path = data_path
        self.data = None
        self.logger = logging.getLogger(__name__)

    def load_data(self):
        """
        Load incident data from the specified file.

        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file format is not supported.
        """
        try:
            if self.data_path.endswith('.csv'):
                self.data = pd.read_csv(self.data_path)
            elif self.data_path.endswith(('.xls', '.xlsx')):
                self.data = pd.read_excel(self.data_path)
            else:
                raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")
            
            self.logger.info("Data loaded successfully.")
            
            # Validate required columns
            required_columns = ['date', 'incident_type', 'department', 'severity']
            if not all(col in self.data.columns for col in required_columns):
                raise ValueError(f"Missing required columns. Expected: {required_columns}")
                
        except FileNotFoundError:
            self.logger.error(f"File not found: {self.data_path}")
            raise
        except Exception as e:
            self.logger.error(f"Error loading data: {str(e)}")
            raise

    def preprocess_data(self):
        """
        Preprocess the incident data by cleaning and transforming it.
        """
        try:
            # Convert date column to datetime
            self.data['date'] = pd.to_datetime(self.data['date'], errors='coerce')
            
            # Drop rows with invalid dates
            self.data = self.data.dropna(subset=['date'])
            
            # Extract year and month for time-based analysis
            self.data['year'] = self.data['date'].dt.year
            self.data['month'] = self.data['date'].dt.month_name()
            
            self.logger.info("Data preprocessing completed.")
        except Exception as e:
            self.logger.error(f"Error preprocessing data: {str(e)}")
            raise

    def analyze_incidents(self):
        """
        Analyze incident data and generate insights.

        Returns:
            dict: A dictionary containing analysis results.
        """
        analysis_results = {}
        
        try:
            # Total incidents
            analysis_results['total_incidents'] = len(self.data)
            
            # Incidents by type
            analysis_results['incidents_by_type'] = self.data['incident_type'].value_counts().to_dict()
            
            # Incidents by department
            analysis_results['incidents_by_department'] = self.data['department'].value_counts().to_dict()
            
            # Incidents by severity
            analysis_results['incidents_by_severity'] = self.data['severity'].value_counts().to_dict()
            
            # Monthly trend
            monthly_trend = self.data.groupby(['year', 'month']).size().reset_index(name='count')
            analysis_results['monthly_trend'] = monthly_trend.to_dict('records')
            
            self.logger.info("Incident analysis completed.")
            return analysis_results
            
        except Exception as e:
            self.logger.error(f"Error analyzing incidents: {str(e)}")
            raise

    def visualize_results(self, analysis_results, output_dir='output'):
        """
        Generate visualizations from the analysis results.

        Args:
            analysis_results (dict): Dictionary containing analysis results.
            output_dir (str): Directory to save visualizations.
        """
        try:
            import os
            os.makedirs(output_dir, exist_ok=True)
            
            # Set style
            sns.set_theme(style="whitegrid")
            
            # Incidents by type
            plt.figure(figsize=(10, 6))
            type_data = pd.DataFrame.from_dict(
                analysis_results['incidents_by_type'], 
                orient='index', 
                columns=['count']
            ).reset_index()
            type_data.columns = ['incident_type', 'count']
            sns.barplot(x='count', y='incident_type', data=type_data.sort_values('count', ascending=False))
            plt.title('Incidents by Type')
            plt.tight_layout()
            plt.savefig(f'{output_dir}/incidents_by_type.png')
            plt.close()
            
            # Incidents by department
            plt.figure(figsize=(10, 6))
            dept_data = pd.DataFrame.from_dict(
                analysis_results['incidents_by_department'], 
                orient='index', 
                columns=['count']
            ).reset_index()
            dept_data.columns = ['department', 'count']
            sns.barplot(x='count', y='department', data=dept_data.sort_values('count', ascending=False))
            plt.title('Incidents by Department')
            plt.tight_layout()
            plt.savefig(f'{output_dir}/incidents_by_department.png')
            plt.close()
            
            # Monthly trend
            plt.figure(figsize=(12, 6))
            trend_data = pd.DataFrame(analysis_results['monthly_trend'])
            trend_data['month_year'] = trend_data['month'] + ' ' + trend_data['year'].astype(str)
            sns.lineplot(x='month_year', y='count', data=trend_data, marker='o')
            plt.title('Monthly Incident Trend')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(f'{output_dir}/monthly_trend.png')
            plt.close()
            
            self.logger.info(f"Visualizations saved to {output_dir}")
            
        except Exception as e:
            self.logger.error(f"Error generating visualizations: {str(e)}")
            raise

    def generate_report(self, analysis_results, output_file='incident_report.txt'):
        """
        Generate a text report with key findings.

        Args:
            analysis_results (dict): Dictionary containing analysis results.
            output_file (str): Path to save the report.
        """
        try:
            with open(output_file, 'w') as f:
                f.write("Workplace Incident Analysis Report\n")
                f.write("=================================\n\n")
                
                f.write(f"Total Incidents: {analysis_results['total_incidents']}\n\n")
                
                f.write("Incidents by Type:\n")
                for incident_type, count in analysis_results['incidents_by_type'].items():
                    f.write(f"- {incident_type}: {count}\n")
                
                f.write("\nIncidents by Department:\n")
                for department, count in analysis_results['incidents_by_department'].items():
                    f.write(f"- {department}: {count}\n")
                
                f.write("\nIncidents by Severity:\n")
                for severity, count in analysis_results['incidents_by_severity'].items():
                    f.write(f"- {severity}: {count}\n")
                
                f.write("\nRecommendations:\n")
                f.write("- Focus on departments with highest incident rates\n")
                f.write("- Address most frequent incident types first\n")
                f.write("- Monitor monthly trends for seasonal patterns\n")
            
            self.logger.info(f"Report generated: {output_file}")
            
        except Exception as e:
            self.logger.error(f"Error generating report: {str(e)}")
            raise

def main():
    """
    Main function to execute the incident analysis workflow.
    """
    try:
        # Initialize analyzer with data path
        analyzer = IncidentAnalyzer('incident_data.csv')  # Change to your data file
        
        # Load and preprocess data
        analyzer.load_data()
        analyzer.preprocess_data()
        
        # Analyze data
        results = analyzer.analyze_incidents()
        
        # Visualize results
        analyzer.visualize_results(results)
        
        # Generate report
        analyzer.generate_report(results)
        
    except Exception as e:
        logging.error(f"An error occurred in the main execution: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
```
