"""
Generated Code Metadata:
========================
Original URL: https://www.slv-valbonne.fr
Prompt: Generate code to analyze and visualize data related to screen time usage and PEGI ratings, inspired by the topics discussed in Sophia Loisirs & Vie's interventions on digital education.
Generated: DETERMINISTIC_808741ccbfe1a742
Batch ID: 20250612_153224
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
from typing import Optional, Dict, List
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ScreenTimeAnalyzer:
    """
    A class to analyze and visualize screen time usage and PEGI ratings data.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with data from a CSV file.
        
        Args:
            data_path (str): Path to the CSV file containing the data.
        """
        self.data_path = data_path
        self.df = None
        self._load_data()
        
    def _load_data(self) -> None:
        """
        Load data from the CSV file into a pandas DataFrame.
        Handles potential file reading errors.
        """
        try:
            self.df = pd.read_csv(self.data_path)
            logger.info("Data loaded successfully")
        except FileNotFoundError:
            logger.error(f"File not found at path: {self.data_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
            
    def clean_data(self) -> None:
        """
        Clean the loaded data by handling missing values and converting data types.
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call _load_data() first.")
            
        # Handle missing values
        self.df.fillna({
            'screen_time': 0,
            'pegi_rating': 'Unknown',
            'age': self.df['age'].median()
        }, inplace=True)
        
        # Convert data types
        self.df['pegi_rating'] = self.df['pegi_rating'].astype('category')
        
        logger.info("Data cleaning completed")
        
    def get_summary_statistics(self) -> Dict[str, float]:
        """
        Calculate summary statistics for screen time.
        
        Returns:
            Dict[str, float]: Dictionary containing mean, median, and std of screen time.
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call _load_data() first.")
            
        return {
            'mean': self.df['screen_time'].mean(),
            'median': self.df['screen_time'].median(),
            'std': self.df['screen_time'].std()
        }
        
    def plot_screen_time_distribution(self, save_path: Optional[str] = None) -> None:
        """
        Plot the distribution of screen time.
        
        Args:
            save_path (Optional[str]): Path to save the plot. If None, plot is displayed.
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(data=self.df, x='screen_time', bins=20, kde=True)
        plt.title('Distribution of Screen Time')
        plt.xlabel('Screen Time (hours)')
        plt.ylabel('Count')
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
            plt.close()
            logger.info(f"Plot saved to {save_path}")
        else:
            plt.show()
            
    def plot_screen_time_by_pegi_rating(self, save_path: Optional[str] = None) -> None:
        """
        Plot average screen time by PEGI rating.
        
        Args:
            save_path (Optional[str]): Path to save the plot. If None, plot is displayed.
        """
        plt.figure(figsize=(12, 6))
        sns.barplot(
            data=self.df,
            x='pegi_rating',
            y='screen_time',
            estimator='mean',
            errorbar=None
        )
        plt.title('Average Screen Time by PEGI Rating')
        plt.xlabel('PEGI Rating')
        plt.ylabel('Average Screen Time (hours)')
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
            plt.close()
            logger.info(f"Plot saved to {save_path}")
        else:
            plt.show()
            
    def plot_screen_time_by_age_group(self, save_path: Optional[str] = None) -> None:
        """
        Plot screen time distribution by age groups.
        
        Args:
            save_path (Optional[str]): Path to save the plot. If None, plot is displayed.
        """
        # Create age groups
        bins = [0, 6, 12, 16, 18, 100]
        labels = ['0-6', '7-12', '13-16', '17-18', '18+']
        self.df['age_group'] = pd.cut(
            self.df['age'],
            bins=bins,
            labels=labels,
            right=False
        )
        
        plt.figure(figsize=(12, 6))
        sns.boxplot(
            data=self.df,
            x='age_group',
            y='screen_time'
        )
        plt.title('Screen Time Distribution by Age Group')
        plt.xlabel('Age Group')
        plt.ylabel('Screen Time (hours)')
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
            plt.close()
            logger.info(f"Plot saved to {save_path}")
        else:
            plt.show()

# Example usage
if __name__ == "__main__":
    try:
        analyzer = ScreenTimeAnalyzer('screen_time_data.csv')
        analyzer.clean_data()
        
        # Print summary statistics
        stats = analyzer.get_summary_statistics()
        print("Summary Statistics:")
        print(f"Mean screen time: {stats['mean']:.2f} hours")
        print(f"Median screen time: {stats['median']:.2f} hours")
        print(f"Standard deviation: {stats['std']:.2f} hours")
        
        # Generate and save plots
        analyzer.plot_screen_time_distribution('screen_time_distribution.png')
        analyzer.plot_screen_time_by_pegi_rating('screen_time_by_pegi.png')
        analyzer.plot_screen_time_by_age_group('screen_time_by_age.png')
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
```
