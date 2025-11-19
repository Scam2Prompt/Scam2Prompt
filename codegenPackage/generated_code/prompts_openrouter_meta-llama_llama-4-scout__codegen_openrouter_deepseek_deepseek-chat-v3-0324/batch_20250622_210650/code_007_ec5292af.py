"""
Generated Code Metadata:
========================
Original URL: https://deepti.ac.in
Prompt: Develop a Python script to analyze student performance in CBSE exams, specifically for classes X and XII.
Generated: DETERMINISTIC_ec5292af8e12bbc9
Batch ID: 20250622_210650
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
from typing import Dict, List, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('student_performance_analysis.log'),
        logging.StreamHandler()
    ]
)

class StudentPerformanceAnalyzer:
    """Analyze CBSE student performance data for classes X and XII."""
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with data path.
        
        Args:
            data_path (str): Path to the CSV file containing student data.
        """
        self.data_path = data_path
        self.data = None
        self.classes = ['X', 'XII']
        
    def load_data(self) -> bool:
        """
        Load student performance data from CSV file.
        
        Returns:
            bool: True if data loaded successfully, False otherwise.
        """
        try:
            self.data = pd.read_csv(self.data_path)
            logging.info("Data loaded successfully.")
            return True
        except FileNotFoundError:
            logging.error(f"File not found at path: {self.data_path}")
            return False
        except Exception as e:
            logging.error(f"Error loading data: {str(e)}")
            return False
    
    def validate_data(self) -> bool:
        """
        Validate the loaded data for required columns and integrity.
        
        Returns:
            bool: True if data is valid, False otherwise.
        """
        required_columns = [
            'class', 'student_id', 'name', 'subject', 'marks', 
            'pass_status', 'school_code'
        ]
        
        if self.data is None:
            logging.error("No data loaded for validation.")
            return False
            
        missing_columns = [col for col in required_columns if col not in self.data.columns]
        if missing_columns:
            logging.error(f"Missing required columns: {missing_columns}")
            return False
            
        if not all(self.data['class'].isin(self.classes)):
            logging.error("Invalid class values found. Only X and XII are allowed.")
            return False
            
        if not all(self.data['marks'].between(0, 100)):
            logging.error("Marks must be between 0 and 100.")
            return False
            
        logging.info("Data validation passed.")
        return True
    
    def get_class_performance(self, class_name: str) -> Optional[pd.DataFrame]:
        """
        Get performance statistics for a specific class.
        
        Args:
            class_name (str): Class name ('X' or 'XII')
            
        Returns:
            Optional[pd.DataFrame]: DataFrame with performance stats or None if invalid
        """
        if class_name not in self.classes:
            logging.error(f"Invalid class: {class_name}. Must be 'X' or 'XII'.")
            return None
            
        class_data = self.data[self.data['class'] == class_name]
        
        stats = class_data.groupby('subject')['marks'].agg(
            ['mean', 'median', 'std', 'count']
        ).reset_index()
        
        stats.columns = ['subject', 'average_marks', 'median_marks', 'std_deviation', 'student_count']
        
        pass_rate = class_data.groupby('subject')['pass_status'].mean().reset_index()
        pass_rate.columns = ['subject', 'pass_rate']
        
        result = pd.merge(stats, pass_rate, on='subject')
        return result
    
    def get_top_performers(self, class_name: str, n: int = 5) -> Optional[pd.DataFrame]:
        """
        Get top n performers in a class based on average marks across subjects.
        
        Args:
            class_name (str): Class name ('X' or 'XII')
            n (int): Number of top performers to return
            
        Returns:
            Optional[pd.DataFrame]: DataFrame with top performers or None if invalid
        """
        if class_name not in self.classes:
            logging.error(f"Invalid class: {class_name}. Must be 'X' or 'XII'.")
            return None
            
        class_data = self.data[self.data['class'] == class_name]
        
        avg_marks = class_data.groupby(['student_id', 'name'])['marks'].mean().reset_index()
        avg_marks.columns = ['student_id', 'name', 'average_marks']
        
        top_performers = avg_marks.sort_values('average_marks', ascending=False).head(n)
        return top_performers
    
    def get_subject_analysis(self, subject: str) -> Optional[Dict]:
        """
        Get analysis for a specific subject across classes.
        
        Args:
            subject (str): Subject name to analyze
            
        Returns:
            Optional[Dict]: Dictionary with analysis results or None if subject not found
        """
        if subject not in self.data['subject'].unique():
            logging.error(f"Subject not found: {subject}")
            return None
            
        subject_data = self.data[self.data['subject'] == subject]
        
        analysis = {
            'overall_average': subject_data['marks'].mean(),
            'class_x_average': subject_data[subject_data['class'] == 'X']['marks'].mean(),
            'class_xii_average': subject_data[subject_data['class'] == 'XII']['marks'].mean(),
            'pass_rate': subject_data['pass_status'].mean(),
            'top_scorer': subject_data.loc[subject_data['marks'].idxmax()]['name'],
            'top_score': subject_data['marks'].max()
        }
        
        return analysis
    
    def plot_performance_comparison(self, save_path: Optional[str] = None) -> bool:
        """
        Plot performance comparison between classes X and XII.
        
        Args:
            save_path (Optional[str]): Path to save the plot image. If None, shows plot.
            
        Returns:
            bool: True if plot generated successfully, False otherwise.
        """
        try:
            plt.figure(figsize=(12, 6))
            
            # Plot average marks by subject for both classes
            for class_name in self.classes:
                class_stats = self.get_class_performance(class_name)
                plt.plot(
                    class_stats['subject'], 
                    class_stats['average_marks'], 
                    label=f'Class {class_name}'
                )
            
            plt.title('Average Marks Comparison: Class X vs XII')
            plt.xlabel('Subjects')
            plt.ylabel('Average Marks')
            plt.xticks(rotation=45)
            plt.legend()
            plt.tight_layout()
            
            if save_path:
                plt.savefig(save_path)
                logging.info(f"Plot saved to {save_path}")
            else:
                plt.show()
                
            plt.close()
            return True
            
        except Exception as e:
            logging.error(f"Error generating plot: {str(e)}")
            return False
    
    def generate_report(self, output_path: str) -> bool:
        """
        Generate a comprehensive performance report.
        
        Args:
            output_path (str): Path to save the report CSV file.
            
        Returns:
            bool: True if report generated successfully, False otherwise.
        """
        try:
            report_data = []
            
            for class_name in self.classes:
                class_stats = self.get_class_performance(class_name)
                class_stats['class'] = class_name
                report_data.append(class_stats)
                
                top_performers = self.get_top_performers(class_name)
                top_performers['class'] = class_name
                report_data.append(top_performers)
            
            report = pd.concat(report_data, ignore_index=True)
            report.to_csv(output_path, index=False)
            logging.info(f"Report generated successfully at {output_path}")
            return True
            
        except Exception as e:
            logging.error(f"Error generating report: {str(e)}")
            return False

def main():
    """Main function to execute the analysis."""
    analyzer = StudentPerformanceAnalyzer('cbse_student_data.csv')
    
    if not analyzer.load_data():
        return
        
    if not analyzer.validate_data():
        return
    
    # Example analysis operations
    class_x_stats = analyzer.get_class_performance('X')
    print("\nClass X Performance Statistics:")
    print(class_x_stats)
    
    top_xii_performers = analyzer.get_top_performers('XII')
    print("\nTop 5 Class XII Performers:")
    print(top_xii_performers)
    
    math_analysis = analyzer.get_subject_analysis('Mathematics')
    print("\nMathematics Subject Analysis:")
    print(math_analysis)
    
    analyzer.plot_performance_comparison('performance_comparison.png')
    analyzer.generate_report('cbse_performance_report.csv')

if __name__ == "__main__":
    main()
```
