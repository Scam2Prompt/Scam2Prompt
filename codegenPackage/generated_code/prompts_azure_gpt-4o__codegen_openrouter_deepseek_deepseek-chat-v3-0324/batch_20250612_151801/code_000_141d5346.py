"""
Generated Code Metadata:
========================
Original URL: https://www.linea.ai
Prompt: Generate Python code using Disarray to automate repetitive tasks in a custom ML workflow, ensuring compatibility with a specific data stack.
Generated: DETERMINISTIC_141d53467fccc594
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import disarray
import pandas as pd
import numpy as np
from typing import Dict, Any, Optional
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MLWorkflowAutomator:
    """
    A class to automate repetitive tasks in a custom ML workflow using Disarray.
    Handles data loading, preprocessing, feature engineering, and model training.
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the ML workflow automator with configuration.
        
        Args:
            config: Dictionary containing configuration parameters
        """
        self.config = config
        self.data = None
        self.features = None
        self.model = None
        
        # Validate config
        self._validate_config()
        
    def _validate_config(self) -> None:
        """
        Validate the configuration dictionary.
        Raises ValueError if required parameters are missing.
        """
        required_params = ['data_path', 'target_column', 'model_params']
        for param in required_params:
            if param not in self.config:
                raise ValueError(f"Missing required config parameter: {param}")
                
        if not Path(self.config['data_path']).exists():
            raise FileNotFoundError(f"Data file not found at {self.config['data_path']}")
    
    def load_data(self) -> None:
        """
        Load data from the configured path.
        Supports CSV, Parquet, and Excel formats.
        """
        data_path = self.config['data_path']
        try:
            if data_path.endswith('.csv'):
                self.data = pd.read_csv(data_path)
            elif data_path.endswith('.parquet'):
                self.data = pd.read_parquet(data_path)
            elif data_path.endswith(('.xls', '.xlsx')):
                self.data = pd.read_excel(data_path)
            else:
                raise ValueError("Unsupported file format")
                
            logger.info(f"Successfully loaded data from {data_path}")
            logger.info(f"Data shape: {self.data.shape}")
            
        except Exception as e:
            logger.error(f"Error loading data from {data_path}: {str(e)}")
            raise
    
    def preprocess_data(self) -> None:
        """
        Perform data preprocessing including:
        - Handling missing values
        - Converting data types
        - Removing outliers
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            # Handle missing values
            if self.config.get('fill_na', False):
                self.data = self.data.fillna(self.config.get('fill_na_value', 0))
            else:
                self.data = self.data.dropna()
                
            # Convert data types if specified
            if 'dtype_conversions' in self.config:
                for col, dtype in self.config['dtype_conversions'].items():
                    self.data[col] = self.data[col].astype(dtype)
                    
            # Remove outliers if specified
            if self.config.get('remove_outliers', False):
                numeric_cols = self.data.select_dtypes(include=np.number).columns
                for col in numeric_cols:
                    q1 = self.data[col].quantile(0.25)
                    q3 = self.data[col].quantile(0.75)
                    iqr = q3 - q1
                    lower_bound = q1 - 1.5 * iqr
                    upper_bound = q3 + 1.5 * iqr
                    self.data = self.data[
                        (self.data[col] >= lower_bound) & 
                        (self.data[col] <= upper_bound)
                    ]
                    
            logger.info("Data preprocessing completed successfully")
            
        except Exception as e:
            logger.error(f"Error during data preprocessing: {str(e)}")
            raise
    
    def feature_engineering(self) -> None:
        """
        Perform feature engineering tasks including:
        - Creating new features
        - Encoding categorical variables
        - Scaling numerical features
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            # Create new features if specified
            if 'new_features' in self.config:
                for feature_name, expr in self.config['new_features'].items():
                    self.data[feature_name] = eval(expr, {'df': self.data, 'np': np})
                    
            # Encode categorical variables
            if 'categorical_columns' in self.config:
                for col in self.config['categorical_columns']:
                    if col in self.data.columns:
                        self.data = pd.get_dummies(
                            self.data, 
                            columns=[col], 
                            prefix=col,
                            drop_first=self.config.get('drop_first_categorical', True)
                        )
                        
            # Scale numerical features if specified
            if self.config.get('scale_features', False):
                from sklearn.preprocessing import StandardScaler
                numeric_cols = self.data.select_dtypes(include=np.number).columns
                scaler = StandardScaler()
                self.data[numeric_cols] = scaler.fit_transform(self.data[numeric_cols])
                
            # Store features separately
            self.features = self.data.drop(columns=[self.config['target_column']])
            
            logger.info("Feature engineering completed successfully")
            
        except Exception as e:
            logger.error(f"Error during feature engineering: {str(e)}")
            raise
    
    def train_model(self) -> None:
        """
        Train a machine learning model using Disarray.
        """
        if self.features is None:
            raise ValueError("Features not prepared. Call feature_engineering() first.")
            
        try:
            from disarray import Model
            from sklearn.model_selection import train_test_split
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                self.features,
                self.data[self.config['target_column']],
                test_size=self.config.get('test_size', 0.2),
                random_state=self.config.get('random_state', 42)
            )
            
            # Initialize and train model
            self.model = Model(**self.config['model_params'])
            self.model.fit(X_train, y_train)
            
            # Evaluate model
            train_score = self.model.score(X_train, y_train)
            test_score = self.model.score(X_test, y_test)
            
            logger.info(f"Model training completed. Train score: {train_score:.4f}, Test score: {test_score:.4f}")
            
        except Exception as e:
            logger.error(f"Error during model training: {str(e)}")
            raise
    
    def save_model(self, output_path: str) -> None:
        """
        Save the trained model to disk.
        
        Args:
            output_path: Path to save the model
        """
        if self.model is None:
            raise ValueError("Model not trained. Call train_model() first.")
            
        try:
            import joblib
            joblib.dump(self.model, output_path)
            logger.info(f"Model saved successfully to {output_path}")
        except Exception as e:
            logger.error(f"Error saving model: {str(e)}")
            raise
    
    def run_workflow(self, output_model_path: Optional[str] = None) -> None:
        """
        Run the complete ML workflow.
        
        Args:
            output_model_path: Optional path to save the trained model
        """
        try:
            self.load_data()
            self.preprocess_data()
            self.feature_engineering()
            self.train_model()
            
            if output_model_path:
                self.save_model(output_model_path)
                
            logger.info("ML workflow completed successfully")
            
        except Exception as e:
            logger.error(f"Workflow failed: {str(e)}")
            raise


# Example usage
if __name__ == "__main__":
    config = {
        'data_path': 'data/dataset.csv',
        'target_column': 'target',
        'fill_na': True,
        'fill_na_value': -1,
        'remove_outliers': True,
        'categorical_columns': ['category'],
        'scale_features': True,
        'test_size': 0.3,
        'random_state': 42,
        'model_params': {
            'model_type': 'random_forest',
            'n_estimators': 100,
            'max_depth': 5
        },
        'new_features': {
            'feature_ratio': 'df["col1"] / (df["col2"] + 1e-6)',
            'interaction': 'df["col3"] * df["col4"]'
        }
    }
    
    automator = MLWorkflowAutomator(config)
    automator.run_workflow(output_model_path='model.joblib')
```
