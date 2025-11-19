"""
Generated Code Metadata:
========================
Original URL: https://spanglerroofingllc.com
Prompt: "Write a script in Python to analyze roof repair data, identifying common issues and suggesting preventive measures for a roofing company."
Generated: DETERMINISTIC_71320ef007605813
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
from collections import Counter
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='roof_analysis.log'
)

class RoofRepairAnalyzer:
    """
    A class to analyze roof repair data and provide insights.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with data from the given path.
        
        Args:
            data_path (str): Path to the CSV file containing roof repair data
        """
        self.data_path = data_path
        self.data = None
        self.common_issues = None
        self.seasonal_trends = None
        
    def load_data(self):
        """
        Load and validate the roof repair data.
        
        Raises:
            FileNotFoundError: If the data file doesn't exist
            ValueError: If the data is malformed or missing required columns
        """
        try:
            self.data = pd.read_csv(self.data_path)
            logging.info("Data loaded successfully")
            
            # Validate required columns
            required_columns = {
                'issue_type', 'repair_date', 'roof_age', 
                'material', 'severity', 'repair_cost'
            }
            
            if not required_columns.issubset(self.data.columns):
                missing = required_columns - set(self.data.columns)
                raise ValueError(f"Missing required columns: {missing}")
                
        except FileNotFoundError:
            logging.error(f"Data file not found at {self.data_path}")
            raise
        except Exception as e:
            logging.error(f"Error loading data: {str(e)}")
            raise
            
    def analyze_common_issues(self):
        """
        Identify and count the most common roof issues.
        """
        try:
            issue_counts = Counter(self.data['issue_type'])
            self.common_issues = issue_counts.most_common()
            logging.info("Common issues analyzed successfully")
        except Exception as e:
            logging.error(f"Error analyzing common issues: {str(e)}")
            raise
            
    def analyze_seasonal_trends(self):
        """
        Analyze repair frequency by season.
        """
        try:
            self.data['repair_date'] = pd.to_datetime(self.data['repair_date'])
            self.data['month'] = self.data['repair_date'].dt.month
            
            # Define seasons
            season_map = {
                1: 'Winter', 2: 'Winter', 3: 'Spring',
                4: 'Spring', 5: 'Spring', 6: 'Summer',
                7: 'Summer', 8: 'Summer', 9: 'Fall',
                10: 'Fall', 11: 'Fall', 12: 'Winter'
            }
            
            self.data['season'] = self.data['month'].map(season_map)
            self.seasonal_trends = self.data.groupby('season').size()
            logging.info("Seasonal trends analyzed successfully")
        except Exception as e:
            logging.error(f"Error analyzing seasonal trends: {str(e)}")
            raise
            
    def generate_preventive_measures(self):
        """
        Generate preventive measures based on analysis.
        
        Returns:
            dict: Dictionary of issues and corresponding preventive measures
        """
        preventive_measures = {
            'Leaks': [
                'Regular inspection of flashing and seals',
                'Ensure proper drainage',
                'Check for cracked or missing shingles'
            ],
            'Shingle Damage': [
                'Schedule annual roof inspections',
                'Trim overhanging tree branches',
                'Clean gutters regularly'
            ],
            'Flashing Issues': [
                'Inspect flashing during seasonal checks',
                'Use proper sealing materials',
                'Ensure proper installation'
            ],
            'Ponding Water': [
                'Improve roof drainage',
                'Check for proper slope',
                'Clear debris from drains'
            ],
            'General Wear': [
                'Perform regular maintenance',
                'Apply protective coatings',
                'Monitor roof age and plan for replacement'
            ]
        }
        
        return preventive_measures
            
    def generate_report(self):
        """
        Generate a comprehensive analysis report with visualizations.
        """
        try:
            if not self.common_issues or not self.seasonal_trends:
                raise ValueError("Analysis not performed. Run analysis methods first.")
                
            # Create visualizations
            plt.figure(figsize=(12, 6))
            
            # Common issues chart
            plt.subplot(1, 2, 1)
            issues, counts = zip(*self.common_issues)
            plt.bar(issues, counts)
            plt.title('Most Common Roof Issues')
            plt.xticks(rotation=45, ha='right')
            
            # Seasonal trends chart
            plt.subplot(1, 2, 2)
            self.seasonal_trends.plot(kind='bar')
            plt.title('Repairs by Season')
            
            plt.tight_layout()
            plt.savefig('roof_analysis.png')
            plt.close()
            
            # Generate text report
            preventive_measures = self.generate_preventive_measures()
            
            report = f"""
            Roof Repair Analysis Report
            ==========================
            
            Most Common Issues:
            {self.common_issues}
            
            Seasonal Trends:
            {self.seasonal_trends.to_dict()}
            
            Preventive Measures:
            """
            
            for issue, measures in preventive_measures.items():
                report += f"\n{issue}:\n"
                for measure in measures:
                    report += f"- {measure}\n"
            
            with open('roof_analysis_report.txt', 'w') as f:
                f.write(report)
                
            logging.info("Report generated successfully")
            
        except Exception as e:
            logging.error(f"Error generating report: {str(e)}")
            raise

def main():
    try:
        analyzer = RoofRepairAnalyzer('roof_repairs.csv')
        analyzer.load_data()
        analyzer.analyze_common_issues()
        analyzer.analyze_seasonal_trends()
        analyzer.generate_report()
        print("Analysis completed successfully. Check roof_analysis.png and roof_analysis_report.txt")
    except Exception as e:
        print(f"Error: {str(e)}")
        logging.error(f"Analysis failed: {str(e)}")

if __name__ == "__main__":
    main()
```
