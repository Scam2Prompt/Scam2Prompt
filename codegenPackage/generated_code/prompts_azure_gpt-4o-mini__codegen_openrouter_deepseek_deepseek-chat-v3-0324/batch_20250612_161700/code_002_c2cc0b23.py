"""
Generated Code Metadata:
========================
Original URL: https://uni4kashmir.com
Prompt: Write a Python script that analyzes data related to student enrollment in emerging fields such as Artificial Intelligence and Cybersecurity at a university like Uni4Kashmir.
Generated: DETERMINISTIC_c2cc0b236f373867
Batch ID: 20250612_161700
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
from typing import Dict, List, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class StudentEnrollmentAnalyzer:
    """
    A class to analyze student enrollment data in emerging fields.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with data from a CSV file.
        
        Args:
            data_path (str): Path to the CSV file containing enrollment data.
        """
        self.data_path = data_path
        self.data = None
        self.emerging_fields = ['Artificial Intelligence', 'Cybersecurity']
        
    def load_data(self) -> None:
        """
        Load and preprocess the enrollment data.
        
        Raises:
            FileNotFoundError: If the data file is not found.
            ValueError: If the data is malformed or missing required columns.
        """
        try:
            self.data = pd.read_csv(self.data_path)
            logger.info("Data loaded successfully")
            
            # Check required columns
            required_columns = ['student_id', 'program', 'year', 'enrollment_count']
            missing_columns = [col for col in required_columns if col not in self.data.columns]
            
            if missing_columns:
                raise ValueError(f"Missing required columns: {missing_columns}")
                
            # Filter for emerging fields
            self.data = self.data[self.data['program'].isin(self.emerging_fields)]
            
        except FileNotFoundError:
            logger.error(f"Data file not found at path: {self.data_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
            
    def get_enrollment_trends(self) -> Dict[str, Dict[int, int]]:
        """
        Calculate enrollment trends by program and year.
        
        Returns:
            Dict[str, Dict[int, int]]: Dictionary with program as key and 
                year-wise enrollment counts as values.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        trends = {}
        for program in self.emerging_fields:
            program_data = self.data[self.data['program'] == program]
            yearly_counts = program_data.groupby('year')['enrollment_count'].sum().to_dict()
            trends[program] = yearly_counts
            
        return trends
    
    def plot_enrollment_trends(self, output_path: Optional[str] = None) -> None:
        """
        Plot enrollment trends for emerging fields.
        
        Args:
            output_path (Optional[str]): Path to save the plot. If None, plot is displayed.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        plt.figure(figsize=(10, 6))
        sns.lineplot(
            data=self.data,
            x='year',
            y='enrollment_count',
            hue='program',
            marker='o'
        )
        
        plt.title('Student Enrollment Trends in Emerging Fields')
        plt.xlabel('Year')
        plt.ylabel('Number of Students')
        plt.grid(True)
        
        if output_path:
            plt.savefig(output_path, bbox_inches='tight')
            logger.info(f"Plot saved to {output_path}")
        else:
            plt.show()
            
    def get_program_statistics(self) -> Dict[str, Dict[str, float]]:
        """
        Calculate statistics for each program.
        
        Returns:
            Dict[str, Dict[str, float]]: Statistics (mean, median, etc.) for each program.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        stats = {}
        for program in self.emerging_fields:
            program_data = self.data[self.data['program'] == program]['enrollment_count']
            stats[program] = {
                'mean': program_data.mean(),
                'median': program_data.median(),
                'std_dev': program_data.std(),
                'total': program_data.sum()
            }
            
        return stats

# Example usage
if __name__ == "__main__":
    try:
        # Initialize analyzer (replace with actual data path)
        analyzer = StudentEnrollmentAnalyzer('student_enrollment.csv')
        
        # Load and analyze data
        analyzer.load_data()
        
        # Get and print trends
        trends = analyzer.get_enrollment_trends()
        print("Enrollment Trends:")
        for program, yearly_data in trends.items():
            print(f"{program}: {yearly_data}")
        
        # Get and print statistics
        stats = analyzer.get_program_statistics()
        print("\nProgram Statistics:")
        for program, stat_data in stats.items():
            print(f"{program}: {stat_data}")
        
        # Plot trends (save to file or display)
        analyzer.plot_enrollment_trends(output_path='enrollment_trends.png')
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
```
