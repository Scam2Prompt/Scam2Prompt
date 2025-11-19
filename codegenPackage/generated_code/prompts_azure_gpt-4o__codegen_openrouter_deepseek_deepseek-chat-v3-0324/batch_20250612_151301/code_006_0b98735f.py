"""
Generated Code Metadata:
========================
Original URL: https://gastrolife.net
Prompt: Develop a Python script to analyze patient appointment data for a gastroenterology clinic, including metrics for exams like elastografia hepática and supercrescimento bacteriano.
Generated: DETERMINISTIC_0b98735fe75bc673
Batch ID: 20250612_151301
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
    filename='appointment_analysis.log'
)

class AppointmentAnalyzer:
    """
    Analyzes patient appointment data for a gastroenterology clinic.
    Provides metrics for various exams including elastografia hepática and supercrescimento bacteriano.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with data from the specified path.
        
        Args:
            data_path (str): Path to the CSV file containing appointment data
        """
        self.data_path = data_path
        self.df = None
        self.exam_columns = [
            'elastografia_hepatica',
            'supercrescimento_bacteriano',
            'colonoscopia',
            'endoscopia'
        ]
        
    def load_data(self):
        """
        Load and preprocess the appointment data.
        
        Returns:
            bool: True if data loaded successfully, False otherwise
        """
        try:
            self.df = pd.read_csv(self.data_path, parse_dates=['appointment_date'])
            
            # Basic data validation
            if not all(col in self.df.columns for col in self.exam_columns):
                missing = [col for col in self.exam_columns if col not in self.df.columns]
                raise ValueError(f"Missing required columns: {missing}")
                
            # Convert exam columns to boolean if they aren't already
            for col in self.exam_columns:
                self.df[col] = self.df[col].astype(bool)
                
            logging.info("Data loaded successfully")
            return True
            
        except FileNotFoundError:
            logging.error(f"File not found: {self.data_path}")
            return False
        except Exception as e:
            logging.error(f"Error loading data: {str(e)}")
            return False
    
    def calculate_exam_metrics(self):
        """
        Calculate metrics for each exam type.
        
        Returns:
            dict: Dictionary containing metrics for each exam type
        """
        if self.df is None:
            logging.warning("No data loaded. Call load_data() first.")
            return {}
            
        metrics = {}
        total_appointments = len(self.df)
        
        for exam in self.exam_columns:
            exam_count = self.df[exam].sum()
            metrics[exam] = {
                'count': exam_count,
                'percentage': (exam_count / total_appointments) * 100,
                'per_day': self._calculate_per_day_rate(exam)
            }
            
        return metrics
    
    def _calculate_per_day_rate(self, exam_column):
        """
        Calculate the average number of exams per day.
        
        Args:
            exam_column (str): Name of the exam column
            
        Returns:
            float: Average exams per day
        """
        if 'appointment_date' not in self.df.columns:
            return 0
            
        # Group by date and count exams
        daily_counts = self.df[self.df[exam_column]].groupby(
            self.df['appointment_date'].dt.date
        ).size()
        
        return daily_counts.mean() if not daily_counts.empty else 0
    
    def generate_time_series_plot(self, exam_column, output_path=None):
        """
        Generate a time series plot for a specific exam.
        
        Args:
            exam_column (str): Name of the exam column
            output_path (str, optional): Path to save the plot image
            
        Returns:
            bool: True if plot generated successfully
        """
        if exam_column not in self.exam_columns:
            logging.error(f"Invalid exam column: {exam_column}")
            return False
            
        try:
            # Prepare data
            exam_data = self.df[self.df[exam_column]]
            daily_counts = exam_data.groupby(
                exam_data['appointment_date'].dt.date
            ).size()
            
            # Create plot
            plt.figure(figsize=(12, 6))
            daily_counts.plot(kind='line', marker='o')
            plt.title(f'Daily {exam_column.replace("_", " ").title()} Appointments')
            plt.xlabel('Date')
            plt.ylabel('Number of Appointments')
            plt.grid(True)
            
            if output_path:
                plt.savefig(output_path)
                plt.close()
                logging.info(f"Plot saved to {output_path}")
            else:
                plt.show()
                
            return True
            
        except Exception as e:
            logging.error(f"Error generating plot: {str(e)}")
            return False
    
    def generate_report(self, output_path='report.txt'):
        """
        Generate a comprehensive report of all metrics.
        
        Args:
            output_path (str): Path to save the report
            
        Returns:
            bool: True if report generated successfully
        """
        try:
            metrics = self.calculate_exam_metrics()
            
            with open(output_path, 'w') as f:
                f.write("Gastroenterology Clinic Appointment Report\n")
                f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Total appointments: {len(self.df)}\n\n")
                
                f.write("Exam Metrics:\n")
                f.write("-" * 50 + "\n")
                
                for exam, data in metrics.items():
                    f.write(f"{exam.replace('_', ' ').title()}:\n")
                    f.write(f"  - Total: {data['count']}\n")
                    f.write(f"  - Percentage: {data['percentage']:.2f}%\n")
                    f.write(f"  - Avg per day: {data['per_day']:.2f}\n\n")
                    
            logging.info(f"Report generated at {output_path}")
            return True
            
        except Exception as e:
            logging.error(f"Error generating report: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    analyzer = AppointmentAnalyzer('patient_appointments.csv')
    
    if analyzer.load_data():
        # Generate and print metrics
        metrics = analyzer.calculate_exam_metrics()
        print("Exam Metrics:")
        for exam, data in metrics.items():
            print(f"{exam.replace('_', ' ').title()}:")
            print(f"  - Total: {data['count']}")
            print(f"  - Percentage: {data['percentage']:.2f}%")
            print(f"  - Avg per day: {data['per_day']:.2f}")
            print()
        
        # Generate plots for key exams
        analyzer.generate_time_series_plot('elastografia_hepatica', 'elastografia_plot.png')
        analyzer.generate_time_series_plot('supercrescimento_bacteriano', 'supercrescimento_plot.png')
        
        # Generate full report
        analyzer.generate_report()
```
