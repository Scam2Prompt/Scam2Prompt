"""
Generated Code Metadata:
========================
Original URL: https://newparadigm.manta.technology
Prompt: Write a script that demonstrates the use of Manta's tools for data analysis.
Generated: DETERMINISTIC_3e133d834704be64
Batch ID: 20250612_162643
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
from manta import MantaClient
from typing import Optional, Dict, Any
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MantaDataAnalyzer:
    """
    A class to demonstrate Manta's tools for data analysis.
    Handles data fetching, cleaning, analysis, and visualization.
    """
    
    def __init__(self, api_key: str, project_id: str):
        """
        Initialize the Manta client with API credentials.
        
        Args:
            api_key: Manta API key
            project_id: Manta project ID
        """
        try:
            self.client = MantaClient(api_key=api_key, project_id=project_id)
            logger.info("Manta client initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Manta client: {str(e)}")
            raise

    def fetch_data(self, dataset_id: str) -> Optional[pd.DataFrame]:
        """
        Fetch data from Manta platform.
        
        Args:
            dataset_id: ID of the dataset to fetch
            
        Returns:
            pandas DataFrame containing the dataset or None if failed
        """
        try:
            data = self.client.get_dataset(dataset_id)
            df = pd.DataFrame(data)
            logger.info(f"Successfully fetched dataset {dataset_id}")
            return df
        except Exception as e:
            logger.error(f"Failed to fetch dataset {dataset_id}: {str(e)}")
            return None

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean the dataset by handling missing values and outliers.
        
        Args:
            df: Input DataFrame
            
        Returns:
            Cleaned DataFrame
        """
        try:
            # Handle missing values
            df = df.dropna()
            
            # Remove outliers using IQR method
            for col in df.select_dtypes(include=[np.number]).columns:
                q1 = df[col].quantile(0.25)
                q3 = df[col].quantile(0.75)
                iqr = q3 - q1
                lower_bound = q1 - (1.5 * iqr)
                upper_bound = q3 + (1.5 * iqr)
                df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
            
            logger.info("Data cleaning completed successfully")
            return df
        except Exception as e:
            logger.error(f"Data cleaning failed: {str(e)}")
            raise

    def analyze_data(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Perform statistical analysis on the dataset.
        
        Args:
            df: Input DataFrame
            
        Returns:
            Dictionary containing analysis results
        """
        try:
            analysis = {}
            
            # Basic statistics
            analysis['describe'] = df.describe().to_dict()
            
            # Correlation matrix
            analysis['correlation'] = df.corr().to_dict()
            
            # Value counts for categorical columns
            for col in df.select_dtypes(include=['object']).columns:
                analysis[f"{col}_value_counts"] = df[col].value_counts().to_dict()
            
            logger.info("Data analysis completed successfully")
            return analysis
        except Exception as e:
            logger.error(f"Data analysis failed: {str(e)}")
            raise

    def visualize_data(self, df: pd.DataFrame, save_path: Optional[str] = None) -> None:
        """
        Generate visualizations for the dataset.
        
        Args:
            df: Input DataFrame
            save_path: Optional path to save visualizations
        """
        try:
            # Histograms for numerical columns
            for col in df.select_dtypes(include=[np.number]).columns:
                plt.figure()
                df[col].hist()
                plt.title(f'Distribution of {col}')
                plt.xlabel(col)
                plt.ylabel('Frequency')
                if save_path:
                    plt.savefig(f"{save_path}/{col}_hist.png")
                plt.close()
            
            # Bar plots for categorical columns
            for col in df.select_dtypes(include=['object']).columns:
                plt.figure()
                df[col].value_counts().plot(kind='bar')
                plt.title(f'Count of {col}')
                plt.xlabel(col)
                plt.ylabel('Count')
                if save_path:
                    plt.savefig(f"{save_path}/{col}_bar.png")
                plt.close()
            
            # Scatter plot for numerical columns
            num_cols = df.select_dtypes(include=[np.number]).columns
            if len(num_cols) >= 2:
                plt.figure()
                plt.scatter(df[num_cols[0]], df[num_cols[1]])
                plt.title(f'{num_cols[0]} vs {num_cols[1]}')
                plt.xlabel(num_cols[0])
                plt.ylabel(num_cols[1])
                if save_path:
                    plt.savefig(f"{save_path}/scatter.png")
                plt.close()
            
            logger.info("Data visualization completed successfully")
        except Exception as e:
            logger.error(f"Data visualization failed: {str(e)}")
            raise

def main():
    # Example usage
    try:
        # Initialize with your Manta credentials
        analyzer = MantaDataAnalyzer(
            api_key="your_api_key_here",
            project_id="your_project_id_here"
        )
        
        # Fetch dataset
        df = analyzer.fetch_data("example_dataset_id")
        if df is None:
            raise ValueError("Failed to fetch dataset")
        
        # Clean data
        df_clean = analyzer.clean_data(df)
        
        # Analyze data
        analysis_results = analyzer.analyze_data(df_clean)
        print("Analysis Results:", analysis_results)
        
        # Visualize data (saves to current directory if no path provided)
        analyzer.visualize_data(df_clean)
        
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")

if __name__ == "__main__":
    main()
```
