"""
Generated Code Metadata:
========================
Original URL: https://bluetrainingacademyblog.com
Prompt: Create a Python script to analyze PPE maintenance data, focusing on arc flash protection, as outlined in Blue Training Academy's article on PPE maintenance.
Generated: DETERMINISTIC_9432babe8775b012
Batch ID: 20250612_152924
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
import os

class PPEAnalyzer:
    """
    A class to analyze PPE maintenance data with a focus on arc flash protection.
    """
    
    def __init__(self, data_path):
        """
        Initialize the PPEAnalyzer with data from the specified path.
        
        Args:
            data_path (str): Path to the PPE maintenance data file (CSV or Excel).
        """
        self.data_path = data_path
        self.data = None
        self.load_data()
        
    def load_data(self):
        """
        Load PPE maintenance data from the specified file.
        Supports CSV and Excel formats.
        """
        try:
            if self.data_path.endswith('.csv'):
                self.data = pd.read_csv(self.data_path)
            elif self.data_path.endswith(('.xls', '.xlsx')):
                self.data = pd.read_excel(self.data_path)
            else:
                raise ValueError("Unsupported file format. Please provide CSV or Excel file.")
            
            # Validate required columns
            required_columns = ['PPE_ID', 'Type', 'Last_Inspection', 'Condition', 'Arc_Flash_Rating']
            missing_cols = [col for col in required_columns if col not in self.data.columns]
            if missing_cols:
                raise ValueError(f"Missing required columns: {missing_cols}")
                
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found at path: {self.data_path}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def clean_data(self):
        """
        Clean and preprocess the PPE maintenance data.
        """
        try:
            # Convert date columns to datetime
            self.data['Last_Inspection'] = pd.to_datetime(self.data['Last_Inspection'], errors='coerce')
            
            # Clean condition data
            self.data['Condition'] = self.data['Condition'].str.strip().str.upper()
            
            # Clean arc flash rating
            self.data['Arc_Flash_Rating'] = pd.to_numeric(
                self.data['Arc_Flash_Rating'].str.extract(r'(\d+)')[0], 
                errors='coerce'
            )
            
            # Drop rows with critical missing data
            self.data.dropna(subset=['PPE_ID', 'Type', 'Last_Inspection', 'Arc_Flash_Rating'], inplace=True)
            
        except Exception as e:
            raise Exception(f"Error cleaning data: {str(e)}")
    
    def analyze_arc_flash_protection(self):
        """
        Analyze arc flash protection data and generate insights.
        
        Returns:
            dict: Dictionary containing analysis results.
        """
        try:
            self.clean_data()
            
            analysis = {}
            
            # Basic statistics
            analysis['total_items'] = len(self.data)
            analysis['avg_arc_flash_rating'] = self.data['Arc_Flash_Rating'].mean()
            analysis['min_arc_flash_rating'] = self.data['Arc_Flash_Rating'].min()
            analysis['max_arc_flash_rating'] = self.data['Arc_Flash_Rating'].max()
            
            # Condition analysis
            condition_counts = self.data['Condition'].value_counts().to_dict()
            analysis['condition_distribution'] = condition_counts
            
            # Expired PPE (assuming inspection should be done annually)
            today = datetime.now()
            self.data['Days_Since_Inspection'] = (today - self.data['Last_Inspection']).dt.days
            expired_count = len(self.data[self.data['Days_Since_Inspection'] > 365])
            analysis['expired_items'] = expired_count
            
            # PPE types with insufficient arc flash protection (assuming threshold of 8 cal/cm²)
            insufficient_protection = self.data[self.data['Arc_Flash_Rating'] < 8]
            analysis['insufficient_protection'] = {
                'count': len(insufficient_protection),
                'items': insufficient_protection[['PPE_ID', 'Type', 'Arc_Flash_Rating']].to_dict('records')
            }
            
            return analysis
            
        except Exception as e:
            raise Exception(f"Error analyzing arc flash protection: {str(e)}")
    
    def generate_report(self, output_dir='reports'):
        """
        Generate a visual report of the PPE analysis.
        
        Args:
            output_dir (str): Directory to save the report.
        """
        try:
            analysis = self.analyze_arc_flash_protection()
            
            # Create output directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)
            
            # Generate plots
            plt.figure(figsize=(12, 8))
            
            # Condition distribution pie chart
            plt.subplot(2, 2, 1)
            self.data['Condition'].value_counts().plot.pie(
                autopct='%1.1f%%',
                title='PPE Condition Distribution'
            )
            
            # Arc flash rating histogram
            plt.subplot(2, 2, 2)
            self.data['Arc_Flash_Rating'].plot.hist(
                bins=10,
                title='Arc Flash Rating Distribution',
                xlabel='Rating (cal/cm²)'
            )
            
            # Days since inspection histogram
            plt.subplot(2, 2, 3)
            self.data['Days_Since_Inspection'].plot.hist(
                bins=20,
                title='Days Since Last Inspection',
                xlabel='Days'
            )
            
            # PPE type bar chart
            plt.subplot(2, 2, 4)
            self.data['Type'].value_counts().plot.bar(
                title='PPE Type Distribution'
            )
            
            plt.tight_layout()
            report_path = os.path.join(output_dir, 'ppe_analysis_report.png')
            plt.savefig(report_path)
            plt.close()
            
            # Save analysis summary to CSV
            summary_path = os.path.join(output_dir, 'ppe_analysis_summary.csv')
            summary_df = pd.DataFrame.from_dict(analysis, orient='index')
            summary_df.to_csv(summary_path)
            
            return {
                'report_path': report_path,
                'summary_path': summary_path
            }
            
        except Exception as e:
            raise Exception(f"Error generating report: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize analyzer with data path
        analyzer = PPEAnalyzer('ppe_data.csv')
        
        # Generate and save report
        report_info = analyzer.generate_report()
        print(f"Report generated successfully at: {report_info['report_path']}")
        print(f"Summary saved at: {report_info['summary_path']}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
