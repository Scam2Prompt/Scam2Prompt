"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: Generate a Python script to analyze student performance data for a coaching academy like Potencia Academy, focusing on JEE and NEET preparation.
Generated: DETERMINISTIC_ed55983f9662d950
Batch ID: 20250612_155654
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
import warnings
from typing import Dict, List, Tuple, Optional

warnings.filterwarnings('ignore')

class StudentPerformanceAnalyzer:
    """
    A class to analyze student performance data for coaching academies.
    Handles data loading, cleaning, analysis, and visualization.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with data path.
        
        Args:
            data_path (str): Path to the student performance data file
        """
        self.data_path = data_path
        self.df = None
        self.load_data()
        
    def load_data(self) -> None:
        """
        Load data from CSV file and perform initial checks.
        """
        try:
            self.df = pd.read_csv(self.data_path)
            print("Data loaded successfully with shape:", self.df.shape)
            
            # Basic data validation
            if self.df.empty:
                raise ValueError("Loaded data is empty")
                
            required_columns = ['student_id', 'name', 'exam_type', 'physics', 'chemistry', 'maths/biology', 'total_marks']
            for col in required_columns:
                if col not in self.df.columns:
                    raise ValueError(f"Missing required column: {col}")
                    
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at path: {self.data_path}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def clean_data(self) -> None:
        """
        Clean the dataset by handling missing values and outliers.
        """
        # Handle missing values
        self.df.dropna(subset=['total_marks'], inplace=True)
        
        # Fill missing subject marks with median
        subjects = ['physics', 'chemistry', 'maths/biology']
        for subject in subjects:
            self.df[subject].fillna(self.df[subject].median(), inplace=True)
        
        # Remove duplicate student records
        self.df.drop_duplicates(subset=['student_id'], keep='last', inplace=True)
        
        # Remove extreme outliers (beyond 3 standard deviations)
        for subject in subjects + ['total_marks']:
            z_scores = np.abs(stats.zscore(self.df[subject]))
            self.df = self.df[z_scores < 3]
    
    def analyze_performance(self) -> Dict[str, Dict]:
        """
        Analyze overall performance metrics.
        
        Returns:
            Dict: Dictionary containing performance metrics
        """
        analysis = {}
        
        # Overall statistics
        analysis['overall'] = {
            'mean_score': self.df['total_marks'].mean(),
            'median_score': self.df['total_marks'].median(),
            'std_dev': self.df['total_marks'].std(),
            'pass_percentage': (self.df['total_marks'] >= 40).mean() * 100
        }
        
        # Exam type comparison
        for exam in self.df['exam_type'].unique():
            exam_data = self.df[self.df['exam_type'] == exam]
            analysis[exam] = {
                'mean_score': exam_data['total_marks'].mean(),
                'median_score': exam_data['total_marks'].median(),
                'std_dev': exam_data['total_marks'].std(),
                'pass_percentage': (exam_data['total_marks'] >= 40).mean() * 100,
                'count': len(exam_data)
            }
        
        # Subject-wise analysis
        subjects = ['physics', 'chemistry', 'maths/biology']
        analysis['subjects'] = {}
        for subject in subjects:
            analysis['subjects'][subject] = {
                'mean': self.df[subject].mean(),
                'median': self.df[subject].median(),
                'std_dev': self.df[subject].std(),
                'weak_students': len(self.df[self.df[subject] < 40]),
                'strong_students': len(self.df[self.df[subject] >= 75])
            }
        
        return analysis
    
    def identify_top_students(self, n: int = 10) -> pd.DataFrame:
        """
        Identify top performing students.
        
        Args:
            n (int): Number of top students to return
            
        Returns:
            pd.DataFrame: DataFrame containing top students
        """
        return self.df.nlargest(n, 'total_marks')[['student_id', 'name', 'exam_type', 'total_marks']]
    
    def identify_weak_students(self, threshold: int = 40) -> pd.DataFrame:
        """
        Identify students performing below threshold.
        
        Args:
            threshold (int): Marks threshold for weak performance
            
        Returns:
            pd.DataFrame: DataFrame containing weak students
        """
        return self.df[self.df['total_marks'] < threshold][['student_id', 'name', 'exam_type', 'total_marks']]
    
    def plot_performance_distribution(self, save_path: Optional[str] = None) -> None:
        """
        Plot distribution of total marks.
        
        Args:
            save_path (str, optional): Path to save the plot. If None, plot is displayed.
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(data=self.df, x='total_marks', kde=True, hue='exam_type', multiple='stack')
        plt.title('Distribution of Total Marks by Exam Type')
        plt.xlabel('Total Marks')
        plt.ylabel('Number of Students')
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
            plt.close()
        else:
            plt.show()
    
    def plot_subject_comparison(self, save_path: Optional[str] = None) -> None:
        """
        Plot comparison of subject scores.
        
        Args:
            save_path (str, optional): Path to save the plot. If None, plot is displayed.
        """
        subjects = ['physics', 'chemistry', 'maths/biology']
        melted_df = self.df.melt(id_vars=['exam_type'], value_vars=subjects, 
                                var_name='subject', value_name='marks')
        
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=melted_df, x='subject', y='marks', hue='exam_type')
        plt.title('Subject-wise Performance Comparison')
        plt.xlabel('Subject')
        plt.ylabel('Marks')
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
            plt.close()
        else:
            plt.show()
    
    def generate_report(self, report_path: str) -> None:
        """
        Generate a comprehensive performance report.
        
        Args:
            report_path (str): Path to save the report
        """
        analysis = self.analyze_performance()
        
        with open(report_path, 'w') as f:
            f.write("STUDENT PERFORMANCE ANALYSIS REPORT\n")
            f.write("="*50 + "\n\n")
            
            # Overall performance
            f.write("OVERALL PERFORMANCE:\n")
            f.write(f"- Mean Score: {analysis['overall']['mean_score']:.2f}\n")
            f.write(f"- Median Score: {analysis['overall']['median_score']:.2f}\n")
            f.write(f"- Standard Deviation: {analysis['overall']['std_dev']:.2f}\n")
            f.write(f"- Pass Percentage: {analysis['overall']['pass_percentage']:.2f}%\n\n")
            
            # Exam-wise performance
            f.write("EXAM-WISE PERFORMANCE:\n")
            for exam in self.df['exam_type'].unique():
                f.write(f"{exam.upper()}:\n")
                f.write(f"  - Number of Students: {analysis[exam]['count']}\n")
                f.write(f"  - Mean Score: {analysis[exam]['mean_score']:.2f}\n")
                f.write(f"  - Pass Percentage: {analysis[exam]['pass_percentage']:.2f}%\n\n")
            
            # Subject-wise performance
            f.write("SUBJECT-WISE PERFORMANCE:\n")
            for subject, stats in analysis['subjects'].items():
                f.write(f"{subject.upper()}:\n")
                f.write(f"  - Mean: {stats['mean']:.2f}\n")
                f.write(f"  - Weak Students (<40 marks): {stats['weak_students']}\n")
                f.write(f"  - Strong Students (>=75 marks): {stats['strong_students']}\n\n")
            
            # Top students
            top_students = self.identify_top_students(5)
            f.write("TOP PERFORMING STUDENTS:\n")
            for _, row in top_students.iterrows():
                f.write(f"- {row['name']} ({row['exam_type']}): {row['total_marks']} marks\n")
            
            # Weak students
            weak_students = self.identify_weak_students()
            f.write(f"\nSTUDENTS NEEDING ATTENTION (Total:
