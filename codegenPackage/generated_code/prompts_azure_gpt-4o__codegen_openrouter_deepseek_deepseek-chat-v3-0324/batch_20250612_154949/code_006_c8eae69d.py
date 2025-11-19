"""
Generated Code Metadata:
========================
Original URL: https://romain-rissoan.fr
Prompt: Develop a script to visualize ROI trends for training programs, using insights from Romain Rissoan's consulting practices.
Generated: DETERMINISTIC_c8eae69d63f77422
Batch ID: 20250612_154949
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
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ROITrendVisualizer:
    """
    A class to visualize ROI trends for training programs based on consulting data.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the visualizer with data from a CSV file.
        
        Args:
            data_path (str): Path to the CSV file containing ROI data
        """
        self.data_path = data_path
        self.data = None
        
    def load_data(self) -> None:
        """
        Load and preprocess the ROI data from the CSV file.
        """
        try:
            self.data = pd.read_csv(self.data_path)
            logger.info("Data loaded successfully")
            
            # Basic data validation
            required_columns = ['program_name', 'year', 'roi_percentage', 'investment']
            if not all(col in self.data.columns for col in required_columns):
                raise ValueError(f"Data must contain these columns: {required_columns}")
                
            # Convert year to datetime if it's not already
            if not pd.api.types.is_datetime64_any_dtype(self.data['year']):
                self.data['year'] = pd.to_datetime(self.data['year'], format='%Y')
                
        except FileNotFoundError:
            logger.error(f"File not found at path: {self.data_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
            
    def plot_roi_trends(self, programs: Optional[List[str]] = None, 
                        output_path: Optional[str] = None) -> None:
        """
        Plot ROI trends for specified training programs.
        
        Args:
            programs (List[str], optional): List of program names to plot. 
                If None, plots all programs.
            output_path (str, optional): Path to save the plot. If None, displays plot.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            # Filter data if specific programs are requested
            plot_data = self.data.copy()
            if programs is not None:
                plot_data = plot_data[plot_data['program_name'].isin(programs)]
                
            if plot_data.empty:
                logger.warning("No data available for the specified programs")
                return
                
            # Set up the plot
            plt.figure(figsize=(12, 6))
            sns.set_style("whitegrid")
            
            # Create line plot with markers
            ax = sns.lineplot(
                data=plot_data,
                x='year',
                y='roi_percentage',
                hue='program_name',
                style='program_name',
                markers=True,
                dashes=False,
                linewidth=2.5,
                markersize=10
            )
            
            # Customize plot
            plt.title("ROI Trends for Training Programs", fontsize=16, pad=20)
            plt.xlabel("Year", fontsize=12)
            plt.ylabel("ROI Percentage", fontsize=12)
            plt.xticks(rotation=45)
            plt.legend(title='Program', bbox_to_anchor=(1.05, 1), loc='upper left')
            
            # Add value annotations
            for line in ax.lines:
                for x, y in zip(line.get_xdata(), line.get_ydata()):
                    ax.annotate(
                        f"{y:.1f}%",
                        (x, y),
                        textcoords="offset points",
                        xytext=(0, 10),
                        ha='center'
                    )
            
            # Save or display plot
            if output_path:
                plt.savefig(output_path, bbox_inches='tight', dpi=300)
                logger.info(f"Plot saved to {output_path}")
            else:
                plt.tight_layout()
                plt.show()
                
        except Exception as e:
            logger.error(f"Error generating plot: {str(e)}")
            raise
            
    def plot_investment_vs_roi(self, year: int, output_path: Optional[str] = None) -> None:
        """
        Plot investment vs ROI for a specific year.
        
        Args:
            year (int): Year to analyze
            output_path (str, optional): Path to save the plot. If None, displays plot.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            # Filter data for the specified year
            year_data = self.data[self.data['year'].dt.year == year]
            
            if year_data.empty:
                logger.warning(f"No data available for year {year}")
                return
                
            # Set up the plot
            plt.figure(figsize=(10, 6))
            sns.set_style("whitegrid")
            
            # Create scatter plot with regression line
            ax = sns.regplot(
                data=year_data,
                x='investment',
                y='roi_percentage',
                scatter_kws={'s': 100, 'alpha': 0.7}
            )
            
            # Add program name annotations
            for _, row in year_data.iterrows():
                ax.annotate(
                    row['program_name'],
                    (row['investment'], row['roi_percentage']),
                    textcoords="offset points",
                    xytext=(5, 5),
                    ha='left'
                )
                
            # Customize plot
            plt.title(f"Investment vs ROI for Training Programs ({year})", fontsize=16, pad=20)
            plt.xlabel("Investment Amount", fontsize=12)
            plt.ylabel("ROI Percentage", fontsize=12)
            
            # Save or display plot
            if output_path:
                plt.savefig(output_path, bbox_inches='tight', dpi=300)
                logger.info(f"Plot saved to {output_path}")
            else:
                plt.tight_layout()
                plt.show()
                
        except Exception as e:
            logger.error(f"Error generating investment vs ROI plot: {str(e)}")
            raise


# Example usage
if __name__ == "__main__":
    try:
        # Initialize visualizer with sample data
        visualizer = ROITrendVisualizer("training_roi_data.csv")
        visualizer.load_data()
        
        # Plot ROI trends for all programs
        visualizer.plot_roi_trends(output_path="roi_trends.png")
        
        # Plot investment vs ROI for a specific year
        visualizer.plot_investment_vs_roi(year=2023, output_path="investment_vs_roi_2023.png")
        
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
```
