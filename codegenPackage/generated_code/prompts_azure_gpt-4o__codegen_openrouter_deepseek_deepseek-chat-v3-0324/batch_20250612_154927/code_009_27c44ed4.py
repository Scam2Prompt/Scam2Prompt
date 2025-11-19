"""
Generated Code Metadata:
========================
Original URL: https://institutopangoa.edu.pe
Prompt: Write a script to analyze student performance data for technical programs such as "Mecatrónica Automotriz," using the educational focus described on the Instituto Pangoa site.
Generated: DETERMINISTIC_27c44ed47cdc7231
Batch ID: 20250612_154927
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
from scipy import stats

class StudentPerformanceAnalyzer:
    """
    A class to analyze student performance data for technical programs.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with the path to the student data.
        
        Args:
            data_path (str): Path to the CSV file containing student data.
        """
        self.data_path = data_path
        self.df = None
        self.load_data()
        
    def load_data(self):
        """
        Load and preprocess the student performance data.
        """
        try:
            # Load data with specified encoding
            self.df = pd.read_csv(self.data_path, encoding='latin1')
            
            # Basic data cleaning
            self.df.dropna(inplace=True)
            self.df = self.df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
            
            # Convert relevant columns to numeric
            numeric_cols = ['calificacion_final', 'asistencia', 'practicas_aprobadas']
            for col in numeric_cols:
                if col in self.df.columns:
                    self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
            
            print("Data loaded and preprocessed successfully.")
            
        except FileNotFoundError:
            print(f"Error: File not found at {self.data_path}")
        except Exception as e:
            print(f"Error loading data: {str(e)}")
    
    def analyze_program(self, program_name):
        """
        Analyze performance for a specific technical program.
        
        Args:
            program_name (str): Name of the program to analyze.
            
        Returns:
            dict: Dictionary containing analysis results.
        """
        if self.df is None:
            return {"error": "Data not loaded"}
            
        try:
            program_data = self.df[self.df['programa'] == program_name]
            
            if program_data.empty:
                return {"error": f"No data found for program: {program_name}"}
                
            # Basic statistics
            stats = {
                'num_students': len(program_data),
                'avg_final_grade': program_data['calificacion_final'].mean(),
                'median_final_grade': program_data['calificacion_final'].median(),
                'pass_rate': (program_data['calificacion_final'] >= 70).mean() * 100,
                'attendance_rate': program_data['asistencia'].mean(),
                'practice_completion': program_data['practicas_aprobadas'].mean()
            }
            
            return stats
            
        except Exception as e:
            return {"error": f"Analysis error: {str(e)}"}
    
    def visualize_performance(self, program_name):
        """
        Generate visualizations for program performance.
        
        Args:
            program_name (str): Name of the program to visualize.
        """
        if self.df is None:
            print("Data not loaded")
            return
            
        try:
            program_data = self.df[self.df['programa'] == program_name]
            
            if program_data.empty:
                print(f"No data found for program: {program_name}")
                return
                
            plt.figure(figsize=(15, 10))
            
            # Grade distribution
            plt.subplot(2, 2, 1)
            sns.histplot(program_data['calificacion_final'], kde=True)
            plt.title(f'Grade Distribution - {program_name}')
            plt.xlabel('Final Grade')
            plt.ylabel('Count')
            
            # Attendance vs Grade
            plt.subplot(2, 2, 2)
            sns.scatterplot(x='asistencia', y='calificacion_final', data=program_data)
            plt.title('Attendance vs Final Grade')
            plt.xlabel('Attendance (%)')
            plt.ylabel('Final Grade')
            
            # Practice completion
            plt.subplot(2, 2, 3)
            program_data['practicas_aprobadas'].value_counts().plot(kind='bar')
            plt.title('Practice Completion')
            plt.xlabel('Number of Approved Practices')
            plt.ylabel('Count')
            
            # Correlation heatmap
            plt.subplot(2, 2, 4)
            numeric_cols = program_data.select_dtypes(include=[np.number]).columns
            sns.heatmap(program_data[numeric_cols].corr(), annot=True, cmap='coolwarm')
            plt.title('Feature Correlation')
            
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Visualization error: {str(e)}")
    
    def compare_programs(self, program1, program2):
        """
        Compare performance between two programs.
        
        Args:
            program1 (str): First program name
            program2 (str): Second program name
            
        Returns:
            dict: Dictionary containing comparison results.
        """
        if self.df is None:
            return {"error": "Data not loaded"}
            
        try:
            prog1_data = self.df[self.df['programa'] == program1]
            prog2_data = self.df[self.df['programa'] == program2]
            
            if prog1_data.empty or prog2_data.empty:
                return {"error": "One or both programs not found"}
                
            comparison = {
                'program1_stats': self.analyze_program(program1),
                'program2_stats': self.analyze_program(program2),
                'grade_t_test': stats.ttest_ind(
                    prog1_data['calificacion_final'],
                    prog2_data['calificacion_final'],
                    nan_policy='omit'
                ).pvalue
            }
            
            return comparison
            
        except Exception as e:
            return {"error": f"Comparison error: {str(e)}"}

# Example usage
if __name__ == "__main__":
    analyzer = StudentPerformanceAnalyzer("student_data.csv")
    
    # Analyze Mecatrónica Automotriz program
    mecatronica_stats = analyzer.analyze_program("Mecatrónica Automotriz")
    print("\nMecatrónica Automotriz Performance:")
    for k, v in mecatronica_stats.items():
        print(f"{k}: {v}")
    
    # Visualize performance
    analyzer.visualize_performance("Mecatrónica Automotriz")
    
    # Compare with another program
    comparison = analyzer.compare_programs("Mecatrónica Automotriz", "Electrónica Industrial")
    print("\nProgram Comparison:")
    for k, v in comparison.items():
        print(f"{k}: {v}")
```
