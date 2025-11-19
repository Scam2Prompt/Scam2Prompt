"""
Generated Code Metadata:
========================
Original URL: https://dbcop.org
Prompt: Create a script to automate the analysis of pharmacy student placement statistics, referencing DBCOP's Training & Placement Overview.
Generated: DETERMINISTIC_cebfbc8e622cde21
Batch ID: 20250612_151429
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
import seaborn as sns
from datetime import datetime
import os

class PharmacyPlacementAnalyzer:
    """
    A class to analyze pharmacy student placement statistics.
    References DBCOP's Training & Placement Overview data.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with data path.
        
        Args:
            data_path (str): Path to the placement data file (CSV or Excel)
        """
        self.data_path = data_path
        self.data = None
        self.placement_stats = None
        self.load_data()
        
    def load_data(self):
        """
        Load placement data from file with error handling.
        Supports both CSV and Excel formats.
        """
        try:
            if self.data_path.endswith('.csv'):
                self.data = pd.read_csv(self.data_path)
            elif self.data_path.endswith(('.xls', '.xlsx')):
                self.data = pd.read_excel(self.data_path)
            else:
                raise ValueError("Unsupported file format. Please provide CSV or Excel file.")
                
            # Validate required columns
            required_columns = ['StudentID', 'GraduationYear', 'PlacementStatus', 
                              'Company', 'Salary', 'JobRole']
            missing_cols = [col for col in required_columns if col not in self.data.columns]
            if missing_cols:
                raise ValueError(f"Missing required columns: {missing_cols}")
                
            print("Data loaded successfully with", len(self.data), "records.")
            
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found at path: {self.data_path}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def clean_data(self):
        """
        Clean and preprocess the placement data.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        # Handle missing values
        self.data['Salary'] = self.data['Salary'].fillna(0)
        self.data['Company'] = self.data['Company'].fillna('Unknown')
        
        # Convert categorical data
        self.data['PlacementStatus'] = self.data['PlacementStatus'].astype('category')
        self.data['JobRole'] = self.data['JobRole'].astype('category')
        
        # Add placement year if not present
        if 'PlacementYear' not in self.data.columns:
            current_year = datetime.now().year
            self.data['PlacementYear'] = self.data['GraduationYear'].apply(
                lambda x: current_year if pd.isna(x) else x
            )
    
    def calculate_placement_stats(self):
        """
        Calculate key placement statistics.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        self.clean_data()
        
        # Basic placement metrics
        total_students = len(self.data)
        placed = self.data[self.data['PlacementStatus'] == 'Placed']
        not_placed = self.data[self.data['PlacementStatus'] == 'Not Placed']
        
        placement_rate = len(placed) / total_students * 100
        avg_salary = placed['Salary'].mean()
        median_salary = placed['Salary'].median()
        
        # Top companies and roles
        top_companies = placed['Company'].value_counts().head(5)
        top_roles = placed['JobRole'].value_counts().head(5)
        
        # Year-wise trends
        year_trends = placed.groupby('PlacementYear').agg({
            'StudentID': 'count',
            'Salary': ['mean', 'median']
        })
        
        self.placement_stats = {
            'total_students': total_students,
            'placed_count': len(placed),
            'not_placed_count': len(not_placed),
            'placement_rate': placement_rate,
            'average_salary': avg_salary,
            'median_salary': median_salary,
            'top_companies': top_companies,
            'top_roles': top_roles,
            'year_trends': year_trends
        }
        
        return self.placement_stats
    
    def generate_reports(self, output_dir='reports'):
        """
        Generate visual reports and save to output directory.
        
        Args:
            output_dir (str): Directory to save reports
        """
        if self.placement_stats is None:
            self.calculate_placement_stats()
            
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Placement status pie chart
        plt.figure(figsize=(8, 6))
        status_counts = [self.placement_stats['placed_count'], 
                        self.placement_stats['not_placed_count']]
        labels = ['Placed', 'Not Placed']
        plt.pie(status_counts, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title('Placement Status Distribution')
        plt.savefig(os.path.join(output_dir, 'placement_status.png'))
        plt.close()
        
        # Salary distribution
        plt.figure(figsize=(10, 6))
        placed_data = self.data[self.data['PlacementStatus'] == 'Placed']
        sns.histplot(placed_data['Salary'], bins=20, kde=True)
        plt.title('Salary Distribution for Placed Students')
        plt.xlabel('Salary')
        plt.ylabel('Count')
        plt.savefig(os.path.join(output_dir, 'salary_distribution.png'))
        plt.close()
        
        # Top companies bar plot
        plt.figure(figsize=(10, 6))
        self.placement_stats['top_companies'].plot(kind='bar')
        plt.title('Top 5 Hiring Companies')
        plt.xlabel('Company')
        plt.ylabel('Number of Placements')
        plt.xticks(rotation=45)
        plt.savefig(os.path.join(output_dir, 'top_companies.png'))
        plt.close()
        
        # Year-wise trends
        plt.figure(figsize=(12, 6))
        self.placement_stats['year_trends']['StudentID'].plot(kind='line', marker='o')
        plt.title('Placement Trends Over Years')
        plt.xlabel('Year')
        plt.ylabel('Number of Placements')
        plt.grid(True)
        plt.savefig(os.path.join(output_dir, 'yearly_trends.png'))
        plt.close()
        
        # Save stats to CSV
        stats_df = pd.DataFrame.from_dict({
            'Metric': [
                'Total Students',
                'Placed Students',
                'Not Placed Students',
                'Placement Rate (%)',
                'Average Salary',
                'Median Salary'
            ],
            'Value': [
                self.placement_stats['total_students'],
                self.placement_stats['placed_count'],
                self.placement_stats['not_placed_count'],
                self.placement_stats['placement_rate'],
                self.placement_stats['average_salary'],
                self.placement_stats['median_salary']
            ]
        })
        stats_df.to_csv(os.path.join(output_dir, 'summary_stats.csv'), index=False)
        
        print(f"Reports generated successfully in {output_dir} directory.")
    
    def analyze(self):
        """
        Run complete analysis pipeline.
        """
        try:
            self.calculate_placement_stats()
            self.generate_reports()
            return True
        except Exception as e:
            print(f"Analysis failed: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    try:
        analyzer = PharmacyPlacementAnalyzer('pharmacy_placement_data.csv')
        if analyzer.analyze():
            print("Analysis completed successfully.")
        else:
            print("Analysis encountered errors.")
    except Exception as e:
        print(f"Error: {str(e)}")
```
