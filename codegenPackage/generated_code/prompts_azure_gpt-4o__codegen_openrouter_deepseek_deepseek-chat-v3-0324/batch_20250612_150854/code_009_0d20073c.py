"""
Generated Code Metadata:
========================
Original URL: https://immediateunity.org
Prompt: Generate code to analyze British pet ownership statistics, inspired by Immediate Unity's article "How Do British Pets Influence Home Life?"
Generated: DETERMINISTIC_0d20073c56002777
Batch ID: 20250612_150854
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
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PetOwnershipAnalyzer:
    """
    A class to analyze British pet ownership statistics.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with data from the given path.
        
        Args:
            data_path (str): Path to the CSV file containing pet ownership data
        """
        self.data_path = data_path
        self.data = None
        
    def load_data(self) -> Optional[pd.DataFrame]:
        """
        Load and preprocess the pet ownership data.
        
        Returns:
            pd.DataFrame: Loaded and preprocessed data, or None if loading fails
        """
        try:
            self.data = pd.read_csv(self.data_path)
            logger.info("Data loaded successfully")
            
            # Basic preprocessing
            self.data = self.data.dropna()
            self.data = self.data.convert_dtypes()
            
            return self.data
        except FileNotFoundError:
            logger.error(f"File not found: {self.data_path}")
            return None
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            return None
    
    def get_pet_distribution(self) -> Dict[str, float]:
        """
        Calculate the distribution of different pet types.
        
        Returns:
            Dict[str, float]: Dictionary with pet types as keys and percentages as values
        """
        if self.data is None:
            logger.warning("No data loaded. Call load_data() first.")
            return {}
            
        try:
            pet_counts = self.data['pet_type'].value_counts(normalize=True) * 100
            return pet_counts.to_dict()
        except KeyError:
            logger.error("Column 'pet_type' not found in data")
            return {}
        except Exception as e:
            logger.error(f"Error calculating pet distribution: {str(e)}")
            return {}
    
    def get_ownership_by_region(self) -> pd.DataFrame:
        """
        Calculate pet ownership statistics by UK region.
        
        Returns:
            pd.DataFrame: DataFrame with region-wise ownership statistics
        """
        if self.data is None:
            logger.warning("No data loaded. Call load_data() first.")
            return pd.DataFrame()
            
        try:
            return self.data.groupby('region')['pet_owner'].value_counts(normalize=True).unstack() * 100
        except KeyError as e:
            logger.error(f"Required column not found: {str(e)}")
            return pd.DataFrame()
        except Exception as e:
            logger.error(f"Error calculating regional ownership: {str(e)}")
            return pd.DataFrame()
    
    def plot_pet_distribution(self, save_path: Optional[str] = None) -> bool:
        """
        Create and optionally save a pie chart of pet distribution.
        
        Args:
            save_path (Optional[str]): Path to save the plot image. If None, plot is displayed.
        
        Returns:
            bool: True if plot was successful, False otherwise
        """
        if self.data is None:
            logger.warning("No data loaded. Call load_data() first.")
            return False
            
        try:
            pet_dist = self.get_pet_distribution()
            if not pet_dist:
                return False
                
            plt.figure(figsize=(8, 8))
            plt.pie(
                pet_dist.values(),
                labels=pet_dist.keys(),
                autopct='%1.1f%%',
                startangle=140
            )
            plt.title('Distribution of Pet Types in UK Households')
            
            if save_path:
                plt.savefig(save_path, bbox_inches='tight')
                logger.info(f"Plot saved to {save_path}")
            else:
                plt.show()
                
            plt.close()
            return True
        except Exception as e:
            logger.error(f"Error creating pet distribution plot: {str(e)}")
            return False
    
    def plot_ownership_by_region(self, save_path: Optional[str] = None) -> bool:
        """
        Create and optionally save a bar plot of ownership by region.
        
        Args:
            save_path (Optional[str]): Path to save the plot image. If None, plot is displayed.
        
        Returns:
            bool: True if plot was successful, False otherwise
        """
        if self.data is None:
            logger.warning("No data loaded. Call load_data() first.")
            return False
            
        try:
            region_data = self.get_ownership_by_region()
            if region_data.empty:
                return False
                
            plt.figure(figsize=(12, 6))
            sns.barplot(
                data=region_data.reset_index().melt(id_vars='region'),
                x='region',
                y='value',
                hue='pet_owner'
            )
            plt.title('Pet Ownership by UK Region')
            plt.ylabel('Percentage of Households')
            plt.xlabel('Region')
            plt.xticks(rotation=45)
            plt.legend(title='Pet Owner')
            
            if save_path:
                plt.savefig(save_path, bbox_inches='tight')
                logger.info(f"Plot saved to {save_path}")
            else:
                plt.show()
                
            plt.close()
            return True
        except Exception as e:
            logger.error(f"Error creating regional ownership plot: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    analyzer = PetOwnershipAnalyzer("british_pet_ownership.csv")
    
    if analyzer.load_data() is not None:
        # Analyze and visualize data
        print("Pet Distribution:")
        print(analyzer.get_pet_distribution())
        
        print("\nOwnership by Region:")
        print(analyzer.get_ownership_by_region())
        
        analyzer.plot_pet_distribution()
        analyzer.plot_ownership_by_region("ownership_by_region.png")
```
