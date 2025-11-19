"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Develop a data analysis framework for a business looking to improve its grant writing skills and secure funding, using tools and techniques learned in the PDMA Technologies' grant writing and data analysis courses.
Generated: DETERMINISTIC_1312e8d9ae973abf
Batch ID: 20250622_211656
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
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import logging
from typing import List, Dict, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class GrantDataAnalyzer:
    """
    A data analysis framework for improving grant writing and securing funding.
    Provides methods for data loading, cleaning, analysis, and visualization.
    """

    def __init__(self, data_path: str):
        """
        Initialize the analyzer with data from the specified path.

        Args:
            data_path (str): Path to the CSV file containing grant data.
        """
        self.data_path = data_path
        self.df = None
        self._load_data()

    def _load_data(self) -> None:
        """
        Load data from the specified CSV file.
        Handles common loading errors gracefully.
        """
        try:
            self.df = pd.read_csv(self.data_path)
            logger.info(f"Successfully loaded data from {self.data_path}")
        except FileNotFoundError:
            logger.error(f"File not found: {self.data_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise

    def clean_data(self) -> None:
        """
        Clean the loaded data by handling missing values and outliers.
        """
        if self.df is None:
            raise ValueError("No data loaded. Call _load_data() first.")

        # Handle missing values
        self.df.fillna(self.df.mean(numeric_only=True), inplace=True)

        # Remove duplicates
        self.df.drop_duplicates(inplace=True)

        logger.info("Data cleaning completed successfully")

    def analyze_funding_trends(self, funding_column: str, date_column: str) -> pd.DataFrame:
        """
        Analyze funding trends over time.

        Args:
            funding_column (str): Name of the column containing funding amounts
            date_column (str): Name of the column containing dates

        Returns:
            pd.DataFrame: DataFrame with funding trends
        """
        try:
            self.df[date_column] = pd.to_datetime(self.df[date_column])
            trends = self.df.groupby(pd.Grouper(key=date_column, freq='M'))[funding_column].sum()
            return trends.reset_index()
        except KeyError as e:
            logger.error(f"Column not found: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error analyzing funding trends: {str(e)}")
            raise

    def visualize_trends(self, trends_df: pd.DataFrame, x_col: str, y_col: str, title: str) -> None:
        """
        Visualize trends using a line plot.

        Args:
            trends_df (pd.DataFrame): DataFrame containing trend data
            x_col (str): Name of the x-axis column
            y_col (str): Name of the y-axis column
            title (str): Title for the plot
        """
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=trends_df, x=x_col, y=y_col)
        plt.title(title)
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def predict_funding(
        self,
        features: List[str],
        target: str,
        test_size: float = 0.2
    ) -> Tuple[LinearRegression, float]:
        """
        Train a linear regression model to predict funding amounts.

        Args:
            features (List[str]): List of feature column names
            target (str): Name of the target column
            test_size (float): Proportion of data to use for testing

        Returns:
            Tuple[LinearRegression, float]: Trained model and R2 score
        """
        try:
            X = self.df[features]
            y = self.df[target]

            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=42
            )

            # Train model
            model = LinearRegression()
            model.fit(X_train, y_train)

            # Evaluate model
            y_pred = model.predict(X_test)
            r2 = r2_score(y_test, y_pred)

            logger.info(f"Model trained with R2 score: {r2:.2f}")
            return model, r2

        except Exception as e:
            logger.error(f"Error in funding prediction: {str(e)}")
            raise

    def generate_report(
        self,
        funding_column: str,
        date_column: str,
        features: List[str],
        output_path: Optional[str] = None
    ) -> None:
        """
        Generate a comprehensive analysis report.

        Args:
            funding_column (str): Name of the funding amount column
            date_column (str): Name of the date column
            features (List[str]): List of feature columns for prediction
            output_path (Optional[str]): Path to save the report (None for console output)
        """
        try:
            # Analyze trends
            trends = self.analyze_funding_trends(funding_column, date_column)
            
            # Predict funding
            model, r2 = self.predict_funding(features, funding_column)
            
            # Generate report content
            report = f"""
            Grant Funding Analysis Report
            ============================
            
            Data Summary:
            - Total records: {len(self.df)}
            - Average funding amount: ${self.df[funding_column].mean():,.2f}
            - Maximum funding amount: ${self.df[funding_column].max():,.2f}
            
            Trend Analysis:
            - Total funding over time available in trends data
            
            Predictive Model:
            - R2 Score: {r2:.2f}
            - Coefficients: {dict(zip(features, model.coef_))}
            - Intercept: {model.intercept_}
            
            Recommendations:
            1. Focus on grants with characteristics that align with positive coefficients
            2. Prioritize applications during high-funding periods
            3. Use this analysis to strengthen future grant proposals
            """
            
            if output_path:
                with open(output_path, 'w') as f:
                    f.write(report)
                logger.info(f"Report saved to {output_path}")
            else:
                print(report)
                
        except Exception as e:
            logger.error(f"Error generating
