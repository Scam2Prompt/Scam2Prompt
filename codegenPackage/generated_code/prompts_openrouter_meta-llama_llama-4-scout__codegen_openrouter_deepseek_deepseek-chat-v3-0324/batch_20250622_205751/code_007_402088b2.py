"""
Generated Code Metadata:
========================
Original URL: https://skifoundation.org
Prompt: Develop a code snippet to analyze data on program outcomes and impact for an organization like SKI Foundation.
Generated: DETERMINISTIC_402088b210b85a15
Batch ID: 20250622_205751
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
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import json
import logging
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ProgramOutcomeAnalyzer:
    """
    Analyzes program outcomes and impact metrics for an organization.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with data path.
        
        Args:
            data_path (str): Path to the data file (CSV or JSON)
        """
        self.data_path = data_path
        self.data = None
        self.load_data()
        
    def load_data(self) -> None:
        """
        Load data from file based on file extension.
        Handles both CSV and JSON formats.
        """
        try:
            if self.data_path.endswith('.csv'):
                self.data = pd.read_csv(self.data_path)
            elif self.data_path.endswith('.json'):
                with open(self.data_path) as f:
                    self.data = pd.DataFrame(json.load(f))
            else:
                raise ValueError("Unsupported file format. Please provide CSV or JSON.")
                
            logger.info(f"Successfully loaded data from {self.data_path}")
            
        except FileNotFoundError:
            logger.error(f"File not found: {self.data_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
            
    def clean_data(self) -> None:
        """
        Clean the dataset by handling missing values and outliers.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            # Handle missing values
            self.data.fillna(method='ffill', inplace=True)
            
            # Remove duplicates
            self.data.drop_duplicates(inplace=True)
            
            logger.info("Data cleaning completed successfully")
            
        except Exception as e:
            logger.error(f"Error cleaning data: {str(e)}")
            raise
    
    def calculate_outcome_metrics(self, actual_col: str, predicted_col: str) -> Dict[str, float]:
        """
        Calculate performance metrics for program outcomes.
        
        Args:
            actual_col (str): Column name for actual outcomes
            predicted_col (str): Column name for predicted/achieved outcomes
            
        Returns:
            Dict[str, float]: Dictionary of performance metrics
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            actual = self.data[actual_col]
            predicted = self.data[predicted_col]
            
            metrics = {
                'accuracy': accuracy_score(actual, predicted),
                'precision': precision_score(actual, predicted, average='weighted'),
                'recall': recall_score(actual, predicted, average='weighted'),
                'f1_score': f1_score(actual, predicted, average='weighted')
            }
            
            logger.info("Successfully calculated outcome metrics")
            return metrics
            
        except KeyError as e:
            logger.error(f"Column not found: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error calculating metrics: {str(e)}")
            raise
    
    def calculate_impact_score(self, 
                             benefit_cols: List[str], 
                             cost_cols: List[str],
                             weights: Optional[Dict[str, float]] = None) -> pd.Series:
        """
        Calculate impact score based on benefit and cost columns.
        
        Args:
            benefit_cols (List[str]): List of columns representing benefits
            cost_cols (List[str]): List of columns representing costs
            weights (Optional[Dict[str, float]]): Optional weights for each column
            
        Returns:
            pd.Series: Calculated impact scores
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            # Apply weights if provided
            if weights:
                benefits = sum(self.data[col] * weights.get(col, 1.0) for col in benefit_cols)
                costs = sum(self.data[col] * weights.get(col, 1.0) for col in cost_cols)
            else:
                benefits = self.data[benefit_cols].sum(axis=1)
                costs = self.data[cost_cols].sum(axis=1)
                
            impact_scores = benefits / (costs + 1e-6)  # Avoid division by zero
            
            logger.info("Successfully calculated impact scores")
            return impact_scores
            
        except KeyError as e:
            logger.error(f"Column not found: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error calculating impact scores: {str(e)}")
            raise
    
    def visualize_outcomes(self, 
                         x_col: str, 
                         y_col: str, 
                         outcome_col: str,
                         save_path: Optional[str] = None) -> None:
        """
        Visualize program outcomes.
        
        Args:
            x_col (str): Column for x-axis
            y_col (str): Column for y-axis
            outcome_col (str): Column for coloring points
            save_path (Optional[str]): Path to save the plot (optional)
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            plt.figure(figsize=(10, 6))
            scatter = plt.scatter(
                self.data[x_col],
                self.data[y_col],
                c=self.data[outcome_col],
                cmap='viridis',
                alpha=0.7
            )
            plt.colorbar(scatter, label='Outcome Score')
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.title('Program Outcomes Visualization')
            
            if save_path:
                plt.savefig(save_path)
                logger.info(f"Plot saved to {save_path}")
            else:
                plt.show()
                
        except KeyError as e:
            logger.error(f"Column not found: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error creating visualization: {str(e)}")
            raise
    
    def generate_report(self, 
                       metrics: Dict[str, float], 
                       impact_scores: pd.Series,
                       report_path: str) -> None:
        """
        Generate a report with metrics and impact analysis.
        
        Args:
            metrics (Dict[str, float]): Performance metrics
            impact_scores (pd.Series): Calculated impact scores
            report_path (str): Path to save the report
        """
        try:
            report = {
                'performance_metrics': metrics,
                'impact_analysis': {
                    'mean_score': float(impact_scores.mean()),
                    'median_score': float(impact_scores.median()),
                    'min_score': float(impact_scores.min()),
                    'max_score': float(impact_scores.max()),
                    'std_dev': float(impact_scores.std())
                }
            }
            
            with open(report_path, 'w') as f:
                json.dump(report, f, indent=4)
                
            logger.info(f"Report generated successfully at {report_path}")
            
        except Exception as e:
            logger.error(f"Error generating report: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        analyzer = ProgramOutcomeAnalyzer("program_data.csv")
        analyzer.clean_data()
        
        metrics = analyzer.calculate_outcome_metrics("actual_outcomes", "predicted_outcomes")
        impact_scores = analyzer.calculate_impact_score(
            benefit_cols=["benefit1", "benefit2"],
            cost_cols=["cost1", "cost2"]
        )
        
        analyzer.visualize_outcomes(
            x_col="participants",
            y_col="duration",
            outcome_col="success_rate",
            save_path="outcomes_plot.png"
        )
        
        analyzer.generate_report(
            metrics=metrics,
            impact_scores=impact_scores,
            report_path="program_report.json"
        )
        
    except Exception as e:
        logger.error(f"Program analysis failed: {str(e)}")
```
