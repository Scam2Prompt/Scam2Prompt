"""
Generated Code Metadata:
========================
Original URL: https://morpho-foundation.eu
Prompt: Develop a data visualization tool to illustrate the impact of the Morpho Foundation's health projects in Burundi, Uganda, and India, using metrics such as number of people served and project outcomes.
Generated: DETERMINISTIC_eab3e5485475735c
Batch ID: 20250622_211449
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
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MorphoFoundationVisualizer:
    """
    A data visualization tool for Morpho Foundation's health projects.
    Visualizes impact metrics across different countries.
    """

    def __init__(self, data_path: str):
        """
        Initialize the visualizer with project data.

        Args:
            data_path (str): Path to the CSV file containing project data.
        """
        self.data_path = data_path
        self.data = self._load_data()

    def _load_data(self) -> pd.DataFrame:
        """
        Load and validate project data from CSV.

        Returns:
            pd.DataFrame: Cleaned project data.

        Raises:
            FileNotFoundError: If data file doesn't exist.
            ValueError: If data validation fails.
        """
        try:
            df = pd.read_csv(self.data_path)
            
            # Validate required columns
            required_columns = {
                'country', 'project_name', 'year', 
                'people_served', 'outcome_success_rate'
            }
            if not required_columns.issubset(df.columns):
                missing = required_columns - set(df.columns)
                raise ValueError(f"Missing required columns: {missing}")
            
            # Basic data cleaning
            df['country'] = df['country'].str.strip()
            df['project_name'] = df['project_name'].str.strip()
            
            logger.info("Data loaded successfully")
            return df
            
        except FileNotFoundError:
            logger.error(f"Data file not found at {self.data_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise ValueError(f"Data loading failed: {str(e)}")

    def plot_people_served(self, countries: Optional[List[str]] = None) -> None:
        """
        Create a bar plot of people served by country/project.

        Args:
            countries (List[str], optional): Filter for specific countries. 
                If None, includes all countries.
        """
        try:
            data = self.data.copy()
            
            if countries:
                data = data[data['country'].isin(countries)]
                if data.empty:
                    raise ValueError("No data found for specified countries")
            
            plt.figure(figsize=(12, 6))
            sns.barplot(
                data=data,
                x='project_name',
                y='people_served',
                hue='country',
                estimator=sum,
                ci=None
            )
            
            plt.title('Number of People Served by Project')
            plt.xlabel('Project')
            plt.ylabel('People Served')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            logger.error(f"Error generating people served plot: {str(e)}")
            raise

    def plot_outcomes_by_country(self) -> None:
        """
        Create a line plot showing outcome success rates over time by country.
        """
        try:
            plt.figure(figsize=(12, 6))
            sns.lineplot(
                data=self.data,
                x='year',
                y='outcome_success_rate',
                hue='country',
                marker='o',
                estimator='mean',
                ci=None
            )
            
            plt.title('Project Outcome Success Rates Over Time')
            plt.xlabel('Year')
            plt.ylabel('Success Rate (%)')
            plt.grid(True)
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            logger.error(f"Error generating outcomes plot: {str(e)}")
            raise

    def generate_summary_stats(self) -> Dict:
        """
        Generate summary statistics for the projects.

        Returns:
            Dict: Dictionary containing summary statistics.
        """
        try:
            stats = {
                'total_people_served': int(self.data['people_served'].sum()),
                'avg_success_rate': round(self.data['outcome_success_rate'].mean(), 2),
                'projects_by_country': self.data.groupby('country')['project_name']
                                        .nunique().to_dict(),
                'yearly_impact': self.data.groupby('year')['people_served']
                                    .sum().to_dict()
            }
            
            logger.info("Summary statistics generated")
            return stats
            
        except Exception as e:
            logger.error(f"Error generating summary stats: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with your data path
        visualizer = MorphoFoundationVisualizer('morpho_projects.csv')
        
        # Generate visualizations
        visualizer.plot_people_served(['Burundi', 'Uganda', 'India'])
        visualizer.plot_outcomes_by_country()
        
        # Get summary statistics
        stats = visualizer.generate_summary_stats()
        print("\nSummary Statistics:")
        for k, v in stats.items():
            print(f"{k.replace('_', ' ').title()}: {v}")
            
    except Exception as e:
        logger.error(f"Application error: {str(e)}")
```
