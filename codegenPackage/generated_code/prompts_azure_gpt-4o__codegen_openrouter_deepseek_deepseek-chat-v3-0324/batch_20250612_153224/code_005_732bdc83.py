"""
Generated Code Metadata:
========================
Original URL: https://brosbel.pe
Prompt: Develop a program to track the performance of Brosbel Agro's bioestimulantes, such as "Algakelp," in improving the health of orange and avocado crops, based on field data.
Generated: DETERMINISTIC_732bdc83667efafc
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
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import logging
import os
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BioestimulantTracker:
    """
    A class to track and analyze the performance of bioestimulants on crops.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the tracker with data path.
        
        Args:
            data_path (str): Path to the CSV file containing field data.
        """
        self.data_path = data_path
        self.data = None
        self.models = {}
        self.load_data()
        
    def load_data(self) -> None:
        """
        Load and preprocess the field data.
        """
        try:
            self.data = pd.read_csv(self.data_path)
            logger.info("Data loaded successfully")
            
            # Basic data validation
            required_columns = {
                'crop_type', 'bioestimulant', 'application_rate', 
                'yield', 'health_score', 'date'
            }
            if not required_columns.issubset(self.data.columns):
                missing = required_columns - set(self.data.columns)
                raise ValueError(f"Missing required columns: {missing}")
                
            # Convert date to datetime
            self.data['date'] = pd.to_datetime(self.data['date'])
            
            # Add additional features
            self.data['days_since_application'] = (
                (self.data['date'] - self.data['date'].min()).dt.days
            )
            
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise
            
    def analyze_performance(self, crop_type: str, bioestimulant: str) -> Dict:
        """
        Analyze the performance of a specific bioestimulant on a crop.
        
        Args:
            crop_type (str): Type of crop (e.g., 'orange', 'avocado')
            bioestimulant (str): Name of bioestimulant (e.g., 'Algakelp')
            
        Returns:
            Dict: Analysis results including metrics and plots
        """
        try:
            # Filter data
            mask = (
                (self.data['crop_type'] == crop_type) & 
                (self.data['bioestimulant'] == bioestimulant)
            )
            filtered_data = self.data[mask]
            
            if len(filtered_data) == 0:
                raise ValueError(
                    f"No data found for {bioestimulant} on {crop_type}"
                )
                
            # Prepare features and target
            X = filtered_data[['application_rate', 'days_since_application']]
            y_yield = filtered_data['yield']
            y_health = filtered_data['health_score']
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y_yield, test_size=0.2, random_state=42
            )
            
            # Train model for yield
            yield_model = LinearRegression()
            yield_model.fit(X_train, y_train)
            y_pred = yield_model.predict(X_test)
            
            # Calculate metrics
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            
            # Store model
            self.models[f"{crop_type}_{bioestimulant}_yield"] = yield_model
            
            # Generate plots
            plot_path = self._generate_plots(
                crop_type, bioestimulant, filtered_data
            )
            
            return {
                'crop_type': crop_type,
                'bioestimulant': bioestimulant,
                'yield_model_metrics': {
                    'mse': mse,
                    'r2': r2,
                    'coefficients': yield_model.coef_.tolist(),
                    'intercept': yield_model.intercept_
                },
                'plots': plot_path
            }
            
        except Exception as e:
            logger.error(f"Error analyzing performance: {e}")
            raise
            
    def _generate_plots(
        self, 
        crop_type: str, 
        bioestimulant: str, 
        data: pd.DataFrame
    ) -> str:
        """
        Generate performance plots and save to file.
        
        Args:
            crop_type (str): Type of crop
            bioestimulant (str): Name of bioestimulant
            data (pd.DataFrame): Filtered data for the analysis
            
        Returns:
            str: Path to the saved plot image
        """
        try:
            os.makedirs('plots', exist_ok=True)
            filename = f"plots/{crop_type}_{bioestimulant}_performance.png"
            
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
            
            # Yield vs Application Rate
            ax1.scatter(
                data['application_rate'], 
                data['yield'], 
                alpha=0.5
            )
            ax1.set_xlabel('Application Rate')
            ax1.set_ylabel('Yield')
            ax1.set_title(f'Yield vs Application Rate\n{crop_type} - {bioestimulant}')
            
            # Health Score vs Days Since Application
            ax2.scatter(
                data['days_since_application'], 
                data['health_score'], 
                alpha=0.5
            )
            ax2.set_xlabel('Days Since Application')
            ax2.set_ylabel('Health Score')
            ax2.set_title(f'Health Score vs Days Since Application\n{crop_type} - {bioestimulant}')
            
            plt.tight_layout()
            plt.savefig(filename)
            plt.close()
            
            return filename
            
        except Exception as e:
            logger.error(f"Error generating plots: {e}")
            raise
            
    def predict_yield(
        self, 
        crop_type: str, 
        bioestimulant: str, 
        application_rate: float, 
        days_since_application: int
    ) -> float:
        """
        Predict yield based on model.
        
        Args:
            crop_type (str): Type of crop
            bioestimulant (str): Name of bioestimulant
            application_rate (float): Application rate of bioestimulant
            days_since_application (int): Days since application
            
        Returns:
            float: Predicted yield
        """
        try:
            model_key = f"{crop_type}_{bioestimulant}_yield"
            if model_key not in self.models:
                raise ValueError(
                    f"No model found for {bioestimulant} on {crop_type}"
                )
                
            model = self.models[model_key]
            prediction = model.predict(
                [[application_rate, days_since_application]]
            )
            return prediction[0]
            
        except Exception as e:
            logger.error(f"Error predicting yield: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize tracker with sample data
        tracker = BioestimulantTracker("field_data.csv")
        
        # Analyze Algakelp performance on oranges
        results = tracker.analyze_performance("orange", "Algakelp")
        print("Analysis Results:")
        print(results)
        
        # Predict yield for specific conditions
        predicted_yield = tracker.predict_yield(
            "orange", "Algakelp", 2.5, 30
        )
        print(f"\nPredicted yield: {predicted_yield:.2f}")
        
    except Exception as e:
        logger.error(f"Error in main execution: {e}")
```
