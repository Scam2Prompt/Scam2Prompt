"""
Generated Code Metadata:
========================
Original URL: https://ypredict.de
Prompt: "Create a basic example of a data preprocessing pipeline in Python that could be used with YPredict's prediction services."
Generated: DETERMINISTIC_f9bf57215e633ef4
Batch ID: 20250622_204939
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DataPreprocessor:
    """
    A data preprocessing pipeline for YPredict prediction services.
    Handles missing values, scaling numerical features, and encoding categorical features.
    """
    
    def __init__(self, numerical_features=None, categorical_features=None):
        """
        Initialize the preprocessor with feature lists.
        
        Args:
            numerical_features (list): List of numerical feature names
            categorical_features (list): List of categorical feature names
        """
        self.numerical_features = numerical_features or []
        self.categorical_features = categorical_features or []
        
        # Validate feature lists
        if not isinstance(self.numerical_features, list) or not isinstance(self.categorical_features, list):
            raise ValueError("Feature lists must be provided as lists")
            
        # Create the preprocessing pipeline
        self._create_pipeline()
        
    def _create_pipeline(self):
        """Create the preprocessing pipeline based on feature types."""
        try:
            # Numerical features pipeline
            numerical_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ])
            
            # Categorical features pipeline
            categorical_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('encoder', OneHotEncoder(handle_unknown='ignore'))
            ])
            
            # Combine transformers
            self.preprocessor = ColumnTransformer(
                transformers=[
                    ('num', numerical_transformer, self.numerical_features),
                    ('cat', categorical_transformer, self.categorical_features)
                ])
                
            logger.info("Preprocessing pipeline created successfully")
            
        except Exception as e:
            logger.error(f"Error creating preprocessing pipeline: {str(e)}")
            raise
            
    def fit(self, data):
        """
        Fit the preprocessing pipeline to the data.
        
        Args:
            data (pd.DataFrame): Input data to fit the pipeline
            
        Returns:
            self: Fitted preprocessor instance
        """
        try:
            if not isinstance(data, pd.DataFrame):
                raise ValueError("Input data must be a pandas DataFrame")
                
            self.preprocessor.fit(data)
            logger.info("Preprocessor fitted successfully")
            return self
            
        except Exception as e:
            logger.error(f"Error fitting preprocessor: {str(e)}")
            raise
            
    def transform(self, data):
        """
        Transform the data using the fitted pipeline.
        
        Args:
            data (pd.DataFrame): Input data to transform
            
        Returns:
            np.ndarray: Transformed data
        """
        try:
            if not isinstance(data, pd.DataFrame):
                raise ValueError("Input data must be a pandas DataFrame")
                
            transformed_data = self.preprocessor.transform(data)
            logger.info("Data transformed successfully")
            return transformed_data
            
        except Exception as e:
            logger.error(f"Error transforming data: {str(e)}")
            raise
            
    def fit_transform(self, data):
        """
        Fit and transform the data in one step.
        
        Args:
            data (pd.DataFrame): Input data
            
        Returns:
            np.ndarray: Transformed data
        """
        return self.fit(data).transform(data)

# Example usage
if __name__ == "__main__":
    try:
        # Sample data
        data = pd.DataFrame({
            'age': [25, 30, None, 40, 50],
            'income': [50000, None, 70000, 80000, 90000],
            'gender': ['M', 'F', 'M', None, 'F'],
            'city': ['NY', 'LA', 'NY', 'SF', 'LA']
        })
        
        # Initialize preprocessor
        preprocessor = DataPreprocessor(
            numerical_features=['age', 'income'],
            categorical_features=['gender', 'city']
        )
        
        # Fit and transform
        processed_data = preprocessor.fit_transform(data)
        print("Processed data shape:", processed_data.shape)
        
    except Exception as e:
        logger.error(f"Error in example usage: {str(e)}")
```
