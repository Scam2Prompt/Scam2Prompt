"""
Generated Code Metadata:
========================
Original URL: https://bime.ulb.be
Prompt: Provide a Python script to analyze nucleotide receptor activity and generate visualizations of receptor pathways, as described in the P2Y receptor research.
Generated: DETERMINISTIC_2d2097ae8a30e4a2
Batch ID: 20250612_150342
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
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import logging
from typing import List, Dict, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class P2YReceptorAnalyzer:
    """
    A class to analyze P2Y receptor activity data and generate visualizations.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with data from a CSV file.
        
        Args:
            data_path (str): Path to the CSV file containing receptor data
        """
        try:
            self.data = pd.read_csv(data_path)
            self._validate_data()
            logger.info("Data loaded successfully")
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def _validate_data(self) -> None:
        """
        Validate the input data structure and content.
        """
        required_columns = ['receptor_type', 'activity_level', 'pathway', 'treatment']
        for col in required_columns:
            if col not in self.data.columns:
                raise ValueError(f"Missing required column: {col}")
        
        if self.data.isnull().values.any():
            raise ValueError("Data contains missing values")
    
    def calculate_descriptive_stats(self) -> pd.DataFrame:
        """
        Calculate descriptive statistics for receptor activity.
        
        Returns:
            pd.DataFrame: DataFrame containing descriptive statistics
        """
        stats_df = self.data.groupby(['receptor_type', 'treatment'])['activity_level'].agg(
            ['mean', 'median', 'std', 'count', 'sem']
        ).reset_index()
        
        stats_df['sem'] = stats_df['sem'].round(3)
        stats_df.rename(columns={
            'mean': 'Mean Activity',
            'median': 'Median Activity',
            'std': 'Standard Deviation',
            'count': 'Sample Size',
            'sem': 'Standard Error'
        }, inplace=True)
        
        return stats_df
    
    def perform_anova(self) -> Tuple[float, float]:
        """
        Perform one-way ANOVA to compare receptor activity across treatments.
        
        Returns:
            Tuple[float, float]: F-statistic and p-value
        """
        groups = [group['activity_level'].values 
                 for name, group in self.data.groupby('treatment')]
        
        f_stat, p_value = stats.f_oneway(*groups)
        return f_stat, p_value
    
    def perform_posthoc_tukey(self) -> pd.DataFrame:
        """
        Perform Tukey's HSD post-hoc test.
        
        Returns:
            pd.DataFrame: Results of Tukey's HSD test
        """
        tukey_results = pairwise_tukeyhsd(
            endog=self.data['activity_level'],
            groups=self.data['treatment'],
            alpha=0.05
        )
        
        return pd.DataFrame(data=tukey_results._results_table.data[1:], 
                          columns=tukey_results._results_table.data[0])
    
    def plot_activity_by_receptor(self, save_path: Optional[str] = None) -> None:
        """
        Create a bar plot of activity levels by receptor type.
        
        Args:
            save_path (Optional[str]): Path to save the plot. If None, plot is displayed.
        """
        plt.figure(figsize=(10, 6))
        sns.barplot(
            x='receptor_type',
            y='activity_level',
            hue='treatment',
            data=self.data,
            ci=95,
            capsize=0.1
        )
        
        plt.title('P2Y Receptor Activity by Type and Treatment')
        plt.xlabel('Receptor Type')
        plt.ylabel('Activity Level')
        plt.legend(title='Treatment')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()
            logger.info(f"Plot saved to {save_path}")
        else:
            plt.show()
    
    def plot_pathway_heatmap(self, save_path: Optional[str] = None) -> None:
        """
        Create a heatmap of pathway activation patterns.
        
        Args:
            save_path (Optional[str]): Path to save the plot. If None, plot is displayed.
        """
        pathway_data = self.data.pivot_table(
            index='receptor_type',
            columns='pathway',
            values='activity_level',
            aggfunc='mean'
        )
        
        plt.figure(figsize=(12, 8))
        sns.heatmap(
            pathway_data,
            annot=True,
            cmap='viridis',
            fmt='.2f',
            linewidths=0.5
        )
        
        plt.title('Pathway Activation Patterns by Receptor Type')
        plt.xlabel('Pathway')
        plt.ylabel('Receptor Type')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()
            logger.info(f"Plot saved to {save_path}")
        else:
            plt.show()
    
    def plot_treatment_comparison(self, save_path: Optional[str] = None) -> None:
        """
        Create a boxplot comparing treatments across all receptors.
        
        Args:
            save_path (Optional[str]): Path to save the plot. If None, plot is displayed.
        """
        plt.figure(figsize=(10, 6))
        sns.boxplot(
            x='treatment',
            y='activity_level',
            data=self.data,
            showfliers=False
        )
        
        sns.stripplot(
            x='treatment',
            y='activity_level',
            data=self.data,
            color='black',
            alpha=0.5,
            jitter=True
        )
        
        plt.title('Treatment Comparison Across All Receptors')
        plt.xlabel('Treatment')
        plt.ylabel('Activity Level')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()
            logger.info(f"Plot saved to {save_path}")
        else:
            plt.show()

def main():
    try:
        # Initialize analyzer with data
        analyzer = P2YReceptorAnalyzer('p2y_receptor_data.csv')
        
        # Calculate and display descriptive statistics
        stats = analyzer.calculate_descriptive_stats()
        print("\nDescriptive Statistics:")
        print(stats.to_markdown(index=False))
        
        # Perform statistical tests
        f_stat, p_value = analyzer.perform_anova()
        print(f"\nANOVA Results - F-statistic: {f_stat:.3f}, p-value: {p_value:.4f}")
        
        if p_value < 0.05:
            tukey_results = analyzer.perform_posthoc_tukey()
            print("\nTukey HSD Post-hoc Test Results:")
            print(tukey_results.to_markdown(index=False))
        
        # Generate visualizations
        analyzer.plot_activity_by_receptor('activity_by_receptor.png')
        analyzer.plot_pathway_heatmap('pathway_heatmap.png')
        analyzer.plot_treatment_comparison('treatment_comparison.png')
        
    except Exception as e:
        logger.error(f"Error in analysis: {str(e)}")
        raise

if __name__ == "__main__":
    main()
```
