"""
Generated Code Metadata:
========================
Original URL: https://amirinternationalcharity.org
Prompt: Write a script to analyze the impact of charity programs like those offered by Amir International Charity Organization, using metrics such as number of people served, donations received, and volunteer hours logged.
Generated: DETERMINISTIC_79f27c29ce7d6808
Batch ID: 20250622_210348
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

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='charity_analysis.log'
)

class CharityAnalyzer:
    """
    A class to analyze charity program impact metrics.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with data from a CSV file.
        
        Args:
            data_path (str): Path to the CSV file containing charity data
        """
        self.data_path = data_path
        self.data = None
        self.logger = logging.getLogger(__name__)
        
    def load_data(self):
        """
        Load and preprocess charity data from CSV.
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.data = pd.read_csv(self.data_path)
            
            # Basic data validation
            required_columns = ['program_name', 'people_served', 'donations_received', 
                               'volunteer_hours', 'start_date', 'end_date']
            for col in required_columns:
                if col not in self.data.columns:
                    raise ValueError(f"Missing required column: {col}")
            
            # Convert dates to datetime
            self.data['start_date'] = pd.to_datetime(self.data['start_date'])
            self.data['end_date'] = pd.to_datetime(self.data['end_date'])
            
            # Calculate program duration in days
            self.data['duration_days'] = (self.data['end_date'] - self.data['start_date']).dt.days
            
            self.logger.info("Data loaded successfully")
            return True
            
        except FileNotFoundError:
            self.logger.error(f"File not found: {self.data_path}")
            return False
        except Exception as e:
            self.logger.error(f"Error loading data: {str(e)}")
            return False
    
    def calculate_metrics(self):
        """
        Calculate key metrics for charity programs.
        
        Returns:
            dict: Dictionary containing calculated metrics
        """
        if self.data is None:
            self.logger.error("Data not loaded. Call load_data() first.")
            return None
        
        try:
            metrics = {
                'total_people_served': self.data['people_served'].sum(),
                'total_donations': self.data['donations_received'].sum(),
                'total_volunteer_hours': self.data['volunteer_hours'].sum(),
                'avg_people_per_program': self.data['people_served'].mean(),
                'avg_donation_per_program': self.data['donations_received'].mean(),
                'avg_volunteer_hours_per_program': self.data['volunteer_hours'].mean(),
                'program_count': len(self.data)
            }
            
            self.logger.info("Metrics calculated successfully")
            return metrics
            
        except Exception as e:
            self.logger.error(f"Error calculating metrics: {str(e)}")
            return None
    
    def visualize_impact(self, output_path='impact_visualization.png'):
        """
        Generate visualizations of charity impact metrics.
        
        Args:
            output_path (str): Path to save the visualization image
            
        Returns:
            bool: True if successful, False otherwise
        """
        if self.data is None:
            self.logger.error("Data not loaded. Call load_data() first.")
            return False
        
        try:
            plt.figure(figsize=(15, 10))
            
            # Create subplots
            plt.subplot(2, 2, 1)
            sns.barplot(x='program_name', y='people_served', data=self.data)
            plt.title('People Served by Program')
            plt.xticks(rotation=45)
            
            plt.subplot(2, 2, 2)
            sns.barplot(x='program_name', y='donations_received', data=self.data)
            plt.title('Donations Received by Program')
            plt.xticks(rotation=45)
            
            plt.subplot(2, 2, 3)
            sns.barplot(x='program_name', y='volunteer_hours', data=self.data)
            plt.title('Volunteer Hours by Program')
            plt.xticks(rotation=45)
            
            plt.subplot(2, 2, 4)
            sns.scatterplot(x='donations_received', y='people_served', 
                            hue='program_name', data=self.data, s=100)
            plt.title('Donations vs People Served')
            
            plt.tight_layout()
            plt.savefig(output_path)
            plt.close()
            
            self.logger.info(f"Visualization saved to {output_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error generating visualization: {str(e)}")
            return False
    
    def generate_report(self, output_path='charity_report.txt'):
        """
        Generate a text report summarizing charity impact.
        
        Args:
            output_path (str): Path to save the report
            
        Returns:
            bool: True if successful, False otherwise
        """
        if self.data is None:
            self.logger.error("Data not loaded. Call load_data() first.")
            return False
        
        try:
            metrics = self.calculate_metrics()
            if metrics is None:
                return False
            
            report_date = datetime.now().strftime('%Y-%m-%d')
            
            with open(output_path, 'w') as f:
                f.write(f"Charity Program Impact Report - {report_date}\n")
                f.write("="*50 + "\n\n")
                
                f.write("Summary Metrics:\n")
                f.write(f"- Total People Served: {metrics['total_people_served']:,}\n")
                f.write(f"- Total Donations Received: ${metrics['total_donations']:,.2f}\n")
                f.write(f"- Total Volunteer Hours: {metrics['total_volunteer_hours']:,}\n")
                f.write(f"- Number of Programs: {metrics['program_count']}\n\n")
                
                f.write("Average Per Program:\n")
                f.write(f"- People Served: {metrics['avg_people_per_program']:,.1f}\n")
                f.write(f"- Donations Received: ${metrics['avg_donation_per_program']:,.2f}\n")
                f.write(f"- Volunteer Hours: {metrics['avg_volunteer_hours_per_program']:,.1f}\n\n")
                
                f.write("Program Details:\n")
                for _, row in self.data.iterrows():
                    f.write(f"\nProgram: {row['program_name']}\n")
                    f.write(f"- People Served: {row['people_served']:,}\n")
                    f.write(f"- Donations: ${row['donations_received']:,.2f}\n")
                    f.write(f"- Volunteer Hours: {row['volunteer_hours']:,}\n")
                    f.write(f"- Duration: {row['duration_days']} days\n")
            
            self.logger.info(f"Report generated at {output_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error generating report: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    analyzer = CharityAnalyzer('charity_data.csv')
    
    if analyzer.load_data():
        analyzer.visualize_impact()
        analyzer.generate_report()
        
        metrics = analyzer.calculate_metrics()
        if metrics:
            print("\nCharity Program Impact Summary:")
            print(f"Total People Served: {metrics['total_people_served']:,}")
            print(f"Total Donations: ${metrics['total_donations']:,.2f}")
            print(f"Total Volunteer Hours: {metrics['total_volunteer_hours']:,}")
```
