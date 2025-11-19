"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: "Write a Python script to analyze the effectiveness of DBT therapy in reducing suicidal ideation and self-harm behaviors in adolescents and adults."
Generated: DETERMINISTIC_7b4c8f0827b6d475
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
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class DBTEffectivenessAnalyzer:
    """
    A class to analyze the effectiveness of Dialectical Behavior Therapy (DBT)
    in reducing suicidal ideation and self-harm behaviors.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with the dataset.
        
        Parameters:
        data_path (str): Path to the CSV file containing the data
        """
        try:
            self.data = pd.read_csv(data_path)
            self._validate_data()
            print("Data loaded successfully.")
        except Exception as e:
            print(f"Error loading data: {e}")
            raise
    
    def _validate_data(self):
        """
        Validate the dataset contains required columns.
        """
        required_columns = {
            'participant_id', 'age', 'gender', 'group', 
            'pre_suicidal_ideation', 'post_suicidal_ideation',
            'pre_self_harm', 'post_self_harm', 'therapy_duration'
        }
        
        if not required_columns.issubset(self.data.columns):
            missing = required_columns - set(self.data.columns)
            raise ValueError(f"Missing required columns: {missing}")
    
    def clean_data(self):
        """
        Clean the dataset by handling missing values and outliers.
        """
        # Drop rows with missing critical values
        self.data.dropna(
            subset=['pre_suicidal_ideation', 'post_suicidal_ideation',
                   'pre_self_harm', 'post_self_harm'],
            inplace=True
        )
        
        # Remove outliers using z-score for continuous variables
        continuous_vars = [
            'pre_suicidal_ideation', 'post_suicidal_ideation',
            'pre_self_harm', 'post_self_harm', 'age', 'therapy_duration'
        ]
        
        for var in continuous_vars:
            z_scores = np.abs(stats.zscore(self.data[var]))
            self.data = self.data[(z_scores < 3)]
    
    def calculate_improvement(self):
        """
        Calculate improvement scores for suicidal ideation and self-harm.
        """
        self.data['suicidal_ideation_change'] = (
            self.data['pre_suicidal_ideation'] - self.data['post_suicidal_ideation']
        )
        self.data['self_harm_change'] = (
            self.data['pre_self_harm'] - self.data['post_self_harm']
        )
    
    def demographic_summary(self):
        """
        Generate demographic summary statistics.
        """
        return self.data[['age', 'gender', 'group', 'therapy_duration']].describe()
    
    def pre_post_comparison(self):
        """
        Compare pre- and post-therapy scores using paired t-tests.
        """
        results = {}
        
        # Suicidal ideation comparison
        t_stat, p_val = stats.ttest_rel(
            self.data['pre_suicidal_ideation'],
            self.data['post_suicidal_ideation']
        )
        results['suicidal_ideation'] = {
            't_statistic': t_stat,
            'p_value': p_val,
            'mean_pre': self.data['pre_suicidal_ideation'].mean(),
            'mean_post': self.data['post_suicidal_ideation'].mean()
        }
        
        # Self-harm comparison
        t_stat, p_val = stats.ttest_rel(
            self.data['pre_self_harm'],
            self.data['post_self_harm']
        )
        results['self_harm'] = {
            't_statistic': t_stat,
            'p_value': p_val,
            'mean_pre': self.data['pre_self_harm'].mean(),
            'mean_post': self.data['post_self_harm'].mean()
        }
        
        return results
    
    def group_comparison(self):
        """
        Compare effectiveness between adolescents and adults.
        """
        results = {}
        
        # Split data into adolescents and adults
        adolescents = self.data[self.data['group'] == 'adolescent']
        adults = self.data[self.data['group'] == 'adult']
        
        # Compare suicidal ideation improvement
        t_stat, p_val = stats.ttest_ind(
            adolescents['suicidal_ideation_change'],
            adults['suicidal_ideation_change'],
            equal_var=False
        )
        results['suicidal_ideation'] = {
            't_statistic': t_stat,
            'p_value': p_val,
            'mean_adolescent': adolescents['suicidal_ideation_change'].mean(),
            'mean_adult': adults['suicidal_ideation_change'].mean()
        }
        
        # Compare self-harm improvement
        t_stat, p_val = stats.ttest_ind(
            adolescents['self_harm_change'],
            adults['self_harm_change'],
            equal_var=False
        )
        results['self_harm'] = {
            't_statistic': t_stat,
            'p_value': p_val,
            'mean_adolescent': adolescents['self_harm_change'].mean(),
            'mean_adult': adults['self_harm_change'].mean()
        }
        
        return results
    
    def duration_analysis(self):
        """
        Analyze relationship between therapy duration and outcomes.
        """
        results = {}
        
        # Suicidal ideation change vs duration
        model = ols(
            'suicidal_ideation_change ~ therapy_duration',
            data=self.data
        ).fit()
        results['suicidal_ideation'] = {
            'r_squared': model.rsquared,
            'p_value': model.f_pvalue,
            'coef': model.params['therapy_duration']
        }
        
        # Self-harm change vs duration
        model = ols(
            'self_harm_change ~ therapy_duration',
            data=self.data
        ).fit()
        results['self_harm'] = {
            'r_squared': model.rsquared,
            'p_value': model.f_pvalue,
            'coef': model.params['therapy_duration']
        }
        
        return results
    
    def visualize_results(self):
        """
        Generate visualizations of the results.
        """
        plt.figure(figsize=(15, 10))
        
        # Pre-post comparison plot
        plt.subplot(2, 2, 1)
        sns.boxplot(data=self.data[['pre_suicidal_ideation', 'post_suicidal_ideation']])
        plt.title('Suicidal Ideation: Pre vs Post Therapy')
        
        plt.subplot(2, 2, 2)
        sns.boxplot(data=self.data[['pre_self_harm', 'post_self_harm']])
        plt.title('Self-Harm: Pre vs Post Therapy')
        
        # Group comparison plot
        plt.subplot(2, 2, 3)
        sns.barplot(
            x='group',
            y='suicidal_ideation_change',
            data=self.data,
            ci=95
        )
        plt.title('Suicidal Ideation Improvement by Age Group')
        
        plt.subplot(2, 2, 4)
        sns.barplot(
            x='group',
            y='self_harm_change',
            data=self.data,
            ci=95
        )
        plt.title('Self-Harm Improvement by Age Group')
        
        plt.tight_layout()
        plt.show()
        
        # Duration relationship plot
        plt.figure(figsize=(12, 5))
        
        plt.subplot(1, 2, 1)
        sns.regplot(
            x='therapy_duration',
            y='suicidal_ideation_change',
            data=self.data
        )
        plt.title('Therapy Duration vs Suicidal Ideation Improvement')
        
        plt.subplot(1, 2, 2)
        sns.regplot(
            x='therapy_duration',
            y='self_harm_change',
            data=self.data
        )
        plt.title('Therapy Duration vs Self-Harm Improvement')
        
        plt.tight_layout()
        plt.show()
    
    def full_analysis(self):
        """
        Run complete analysis pipeline.
        """
        try:
            self.clean_data()
            self.calculate_improvement()
            
            print("\n=== Demographic Summary ===")
            print(self.demographic_summary())
            
            print("\n=== Pre-Post Therapy Comparison ===")
            print(pd.DataFrame(self.pre_post_comparison()))
            
            print("\n=== Age Group Comparison ===")
            print(pd.DataFrame(self.group_comparison()))
            
            print("\n=== Therapy Duration Analysis ===")
            print(pd.DataFrame(self.duration_analysis()))
            
            self.visualize_results()
            
        except Exception as e:
            print(f"Error during analysis: {e}")
            raise


# Example usage
if __name__ == "__main__":
    try:
        analyzer = DBTEffectivenessAnalyzer('dbt_therapy_data.csv')
        analyzer.full_analysis()
    except Exception as e:
        print(f"Analysis failed: {e}")
