"""
Generated Code Metadata:
========================
Original URL: https://virtual5.com.mx
Prompt: Write a Python script to analyze the impact of Virtual5's courses on organizational productivity, using data such as the number of companies trained and hours of consultancy provided.
Generated: DETERMINISTIC_c5bed5caab71e3ae
Batch ID: 20250612_151026
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
from scipy import stats
import seaborn as sns
import logging
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ProductivityAnalyzer:
    """
    Analyzes the impact of Virtual5's courses on organizational productivity.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with data path.
        
        Args:
            data_path: Path to the CSV file containing training data
        """
        self.data_path = data_path
        self.df = None
        
    def load_data(self) -> None:
        """
        Load and preprocess the data from CSV file.
        
        Raises:
            FileNotFoundError: If data file is not found
            ValueError: If data is malformed
        """
        try:
            self.df = pd.read_csv(self.data_path)
            logger.info("Data loaded successfully")
            
            # Basic validation
            required_columns = {
                'company_id', 'company_name', 'course_name', 
                'training_hours', 'consultancy_hours', 
                'pre_training_productivity', 'post_training_productivity'
            }
            
            if not required_columns.issubset(self.df.columns):
                missing = required_columns - set(self.df.columns)
                raise ValueError(f"Missing required columns: {missing}")
                
            # Convert productivity scores to numeric
            self.df['pre_training_productivity'] = pd.to_numeric(
                self.df['pre_training_productivity'], errors='coerce'
            )
            self.df['post_training_productivity'] = pd.to_numeric(
                self.df['post_training_productivity'], errors='coerce'
            )
            
            # Calculate productivity improvement
            self.df['productivity_improvement'] = (
                self.df['post_training_productivity'] - 
                self.df['pre_training_productivity']
            )
            
        except FileNotFoundError:
            logger.error(f"Data file not found at {self.data_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise ValueError(f"Data loading failed: {str(e)}")
    
    def get_summary_stats(self) -> Dict[str, float]:
        """
        Calculate summary statistics for the dataset.
        
        Returns:
            Dictionary containing summary statistics
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        return {
            'total_companies': self.df['company_id'].nunique(),
            'total_courses': len(self.df),
            'total_training_hours': self.df['training_hours'].sum(),
            'total_consultancy_hours': self.df['consultancy_hours'].sum(),
            'avg_productivity_improvement': self.df['productivity_improvement'].mean(),
            'median_productivity_improvement': self.df['productivity_improvement'].median(),
            'std_productivity_improvement': self.df['productivity_improvement'].std()
        }
    
    def analyze_by_course(self) -> pd.DataFrame:
        """
        Analyze productivity impact by course type.
        
        Returns:
            DataFrame with analysis grouped by course
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        return self.df.groupby('course_name').agg({
            'company_id': 'count',
            'training_hours': 'sum',
            'consultancy_hours': 'sum',
            'productivity_improvement': ['mean', 'median', 'std']
        }).sort_values(('productivity_improvement', 'mean'), ascending=False)
    
    def analyze_by_company(self, top_n: int = 10) -> pd.DataFrame:
        """
        Analyze productivity impact by company.
        
        Args:
            top_n: Number of top companies to return
            
        Returns:
            DataFrame with analysis grouped by company
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        return self.df.groupby('company_name').agg({
            'course_name': 'count',
            'training_hours': 'sum',
            'consultancy_hours': 'sum',
            'productivity_improvement': ['mean', 'median', 'std']
        }).sort_values(('productivity_improvement', 'mean'), ascending=False).head(top_n)
    
    def correlation_analysis(self) -> Dict[str, float]:
        """
        Calculate correlations between training metrics and productivity.
        
        Returns:
            Dictionary of correlation coefficients
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        return {
            'training_hours_vs_improvement': self.df['training_hours'].corr(
                self.df['productivity_improvement']
            ),
            'consultancy_hours_vs_improvement': self.df['consultancy_hours'].corr(
                self.df['productivity_improvement']
            ),
            'combined_hours_vs_improvement': (
                self.df['training_hours'] + self.df['consultancy_hours']
            ).corr(self.df['productivity_improvement'])
        }
    
    def statistical_significance(self) -> Dict[str, Tuple[float, float]]:
        """
        Perform statistical significance tests on productivity improvements.
        
        Returns:
            Dictionary with test results (statistic, p-value)
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        # Paired t-test for pre vs post training
        t_stat, p_value = stats.ttest_rel(
            self.df['post_training_productivity'],
            self.df['pre_training_productivity']
        )
        
        return {
            'paired_ttest': (t_stat, p_value),
            'effect_size': (
                self.df['productivity_improvement'].mean() / 
                self.df['productivity_improvement'].std()
            )
        }
    
    def visualize_results(self, output_dir: str = 'output') -> None:
        """
        Generate visualizations of the analysis.
        
        Args:
            output_dir: Directory to save visualizations
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        try:
            # Productivity improvement distribution
            plt.figure(figsize=(10, 6))
            sns.histplot(self.df['productivity_improvement'], kde=True)
            plt.title('Distribution of Productivity Improvements')
            plt.xlabel('Productivity Improvement Score')
            plt.ylabel('Frequency')
            plt.savefig(f'{output_dir}/productivity_improvement_dist.png')
            plt.close()
            
            # Improvement by course
            course_stats = self.analyze_by_course()
            plt.figure(figsize=(12, 6))
            course_stats['productivity_improvement']['mean'].plot(kind='bar')
            plt.title('Average Productivity Improvement by Course')
            plt.xlabel('Course Name')
            plt.ylabel('Average Improvement')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig(f'{output_dir}/improvement_by_course.png')
            plt.close()
            
            # Scatter plot of training hours vs improvement
            plt.figure(figsize=(10, 6))
            sns.regplot(
                x='training_hours', 
                y='productivity_improvement', 
                data=self.df
            )
            plt.title('Training Hours vs Productivity Improvement')
            plt.xlabel('Training Hours')
            plt.ylabel('Productivity Improvement')
            plt.savefig(f'{output_dir}/training_vs_improvement.png')
            plt.close()
            
            logger.info(f"Visualizations saved to {output_dir}")
            
        except Exception as e:
            logger.error(f"Error generating visualizations: {str(e)}")
            raise
    
    def generate_report(self, output_path: str = 'productivity_report.txt') -> None:
        """
        Generate a comprehensive text report of findings.
        
        Args:
            output_path: Path to save the report
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            with open(output_path, 'w') as f:
                f.write("Virtual5 Training Impact Report\n")
                f.write("="*40 + "\n\n")
                
                # Summary statistics
                stats = self.get_summary_stats()
                f.write("Summary Statistics:\n")
                f.write(f"- Total companies trained: {stats['total_companies']}\n")
                f.write(f"- Total courses delivered: {stats['total_courses']}\n")
                f.write(f"- Total training hours: {stats['total_training_hours']}\n")
                f.write(f"- Total consultancy hours: {stats['total_
