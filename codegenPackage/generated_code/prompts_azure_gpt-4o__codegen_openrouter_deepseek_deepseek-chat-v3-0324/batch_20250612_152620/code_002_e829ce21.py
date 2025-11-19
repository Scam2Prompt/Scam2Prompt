"""
Generated Code Metadata:
========================
Original URL: https://scimar.ca
Prompt: Generate code to analyze clinical trial data for hepatalin-based treatments using Python libraries like Pandas and SciPy. Include functionality to visualize trends in metabolic health improvements.
Generated: DETERMINISTIC_e829ce213cb17dc5
Batch ID: 20250612_152620
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
from scipy.stats import ttest_ind
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class ClinicalTrialAnalyzer:
    """
    A class to analyze clinical trial data for hepatalin-based treatments.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with clinical trial data.
        
        Args:
            data_path (str): Path to the clinical trial data file (CSV or Excel)
        """
        try:
            if data_path.endswith('.csv'):
                self.data = pd.read_csv(data_path)
            elif data_path.endswith(('.xls', '.xlsx')):
                self.data = pd.read_excel(data_path)
            else:
                raise ValueError("Unsupported file format. Please provide CSV or Excel file.")
            
            # Validate required columns
            required_columns = ['patient_id', 'treatment_group', 'baseline_metabolic_score', 
                              'post_treatment_metabolic_score', 'treatment_duration']
            missing_cols = [col for col in required_columns if col not in self.data.columns]
            if missing_cols:
                raise ValueError(f"Missing required columns: {missing_cols}")
                
            print("Data loaded successfully with shape:", self.data.shape)
            
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            raise
    
    def clean_data(self):
        """
        Clean the clinical trial data by handling missing values and outliers.
        """
        try:
            # Drop duplicates
            self.data = self.data.drop_duplicates()
            
            # Handle missing values
            self.data = self.data.dropna(subset=['baseline_metabolic_score', 
                                               'post_treatment_metabolic_score'])
            
            # Remove outliers using IQR method
            for col in ['baseline_metabolic_score', 'post_treatment_metabolic_score']:
                Q1 = self.data[col].quantile(0.25)
                Q3 = self.data[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                self.data = self.data[(self.data[col] >= lower_bound) & 
                                    (self.data[col] <= upper_bound)]
            
            print("Data cleaning completed. New shape:", self.data.shape)
            return self.data
            
        except Exception as e:
            print(f"Error during data cleaning: {str(e)}")
            raise
    
    def calculate_improvement(self):
        """
        Calculate metabolic health improvement metrics.
        """
        try:
            # Calculate absolute and percentage improvement
            self.data['absolute_improvement'] = (
                self.data['post_treatment_metabolic_score'] - 
                self.data['baseline_metabolic_score']
            )
            
            self.data['percentage_improvement'] = (
                (self.data['absolute_improvement'] / 
                 self.data['baseline_metabolic_score']) * 100
            )
            
            return self.data
            
        except Exception as e:
            print(f"Error calculating improvement metrics: {str(e)}")
            raise
    
    def analyze_treatment_groups(self):
        """
        Perform statistical analysis between treatment groups.
        """
        try:
            # Group statistics
            group_stats = self.data.groupby('treatment_group').agg({
                'baseline_metabolic_score': ['mean', 'std', 'count'],
                'post_treatment_metabolic_score': ['mean', 'std'],
                'absolute_improvement': ['mean', 'std', 'min', 'max'],
                'percentage_improvement': ['mean', 'std']
            })
            
            # T-test between treatment groups
            groups = self.data['treatment_group'].unique()
            if len(groups) == 2:
                group1 = self.data[self.data['treatment_group'] == groups[0]]['absolute_improvement']
                group2 = self.data[self.data['treatment_group'] == groups[1]]['absolute_improvement']
                t_stat, p_value = ttest_ind(group1, group2)
                print(f"\nT-test results between {groups[0]} and {groups[1]}:")
                print(f"T-statistic: {t_stat:.4f}, P-value: {p_value:.4f}")
            
            return group_stats
            
        except Exception as e:
            print(f"Error during group analysis: {str(e)}")
            raise
    
    def visualize_improvements(self, save_path=None):
        """
        Visualize metabolic health improvements.
        
        Args:
            save_path (str, optional): Path to save the visualization. If None, plot is displayed.
        """
        try:
            plt.figure(figsize=(15, 10))
            
            # Plot 1: Distribution of improvements
            plt.subplot(2, 2, 1)
            sns.histplot(data=self.data, x='absolute_improvement', hue='treatment_group', 
                        kde=True, element='step', stat='density', common_norm=False)
            plt.title('Distribution of Metabolic Score Improvements')
            plt.xlabel('Absolute Improvement')
            
            # Plot 2: Boxplot of improvements by group
            plt.subplot(2, 2, 2)
            sns.boxplot(data=self.data, x='treatment_group', y='absolute_improvement')
            plt.title('Improvement by Treatment Group')
            plt.xlabel('Treatment Group')
            plt.ylabel('Absolute Improvement')
            
            # Plot 3: Scatter plot of baseline vs post-treatment
            plt.subplot(2, 2, 3)
            sns.scatterplot(data=self.data, x='baseline_metabolic_score', 
                           y='post_treatment_metabolic_score', hue='treatment_group')
            plt.plot([self.data['baseline_metabolic_score'].min(), 
                      self.data['baseline_metabolic_score'].max()],
                    [self.data['baseline_metabolic_score'].min(), 
                     self.data['baseline_metabolic_score'].max()], 
                    'k--')
            plt.title('Baseline vs Post-Treatment Scores')
            plt.xlabel('Baseline Metabolic Score')
            plt.ylabel('Post-Treatment Metabolic Score')
            
            # Plot 4: Improvement vs treatment duration
            plt.subplot(2, 2, 4)
            sns.regplot(data=self.data, x='treatment_duration', y='absolute_improvement')
            plt.title('Improvement vs Treatment Duration')
            plt.xlabel('Treatment Duration')
            plt.ylabel('Absolute Improvement')
            
            plt.tight_layout()
            
            if save_path:
                plt.savefig(save_path, dpi=300, bbox_inches='tight')
                print(f"Visualization saved to {save_path}")
            else:
                plt.show()
                
        except Exception as e:
            print(f"Error during visualization: {str(e)}")
            raise
    
    def run_full_analysis(self, save_path=None):
        """
        Run complete analysis pipeline.
        
        Args:
            save_path (str, optional): Path to save visualization. If None, plot is displayed.
        """
        try:
            self.clean_data()
            self.calculate_improvement()
            stats = self.analyze_treatment_groups()
            self.visualize_improvements(save_path)
            return stats
        except Exception as e:
            print(f"Error during full analysis: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize analyzer (replace with actual data path)
        analyzer = ClinicalTrialAnalyzer('hepatalin_trial_data.csv')
        
        # Run full analysis
        analysis_results = analyzer.run_full_analysis(save_path='hepatalin_analysis.png')
        
        # Print summary statistics
        print("\nSummary Statistics:")
        print(analysis_results)
        
    except Exception as e:
        print(f"Error in analysis: {str(e)}")
```
