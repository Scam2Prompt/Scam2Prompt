"""
Generated Code Metadata:
========================
Original URL: https://www.linea.ai
Prompt: Create an example of how Disarray can help trace issues across a data stack in a machine learning project.
Generated: DETERMINISTIC_ab343e81c21125c9
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import Dict, Any, Optional
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import disarray

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DataPipeline:
    """A simple data pipeline for a machine learning project with Disarray integration."""
    
    def __init__(self):
        """Initialize the pipeline with Disarray tracking."""
        self.df: Optional[pd.DataFrame] = None
        self.X_train: Optional[pd.DataFrame] = None
        self.X_test: Optional[pd.DataFrame] = None
        self.y_train: Optional[pd.Series] = None
        self.y_test: Optional[pd.Series] = None
        self.model: Optional[RandomForestClassifier] = None
        
        # Initialize Disarray
        self.da = disarray.Disarray(project_name="ml_pipeline")
        
    def load_data(self, file_path: str) -> None:
        """Load data from a CSV file and track with Disarray."""
        try:
            self.df = pd.read_csv(file_path)
            logger.info("Data loaded successfully")
            
            # Track data loading with Disarray
            self.da.track(
                operation="load_data",
                metadata={
                    "file_path": file_path,
                    "shape": self.df.shape,
                    "columns": list(self.df.columns),
                    "sample": self.df.head(3).to_dict()
                }
            )
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            self.da.track_error(
                operation="load_data",
                error=str(e),
                metadata={"file_path": file_path}
            )
            raise
    
    def preprocess_data(self) -> None:
        """Preprocess data and track with Disarray."""
        try:
            if self.df is None:
                raise ValueError("No data loaded")
                
            # Simple preprocessing
            self.df = self.df.dropna()
            self.df = pd.get_dummies(self.df, drop_first=True)
            
            logger.info("Data preprocessed successfully")
            
            # Track preprocessing
            self.da.track(
                operation="preprocess_data",
                metadata={
                    "shape_after_preprocessing": self.df.shape,
                    "columns_after_preprocessing": list(self.df.columns),
                    "sample_after_preprocessing": self.df.head(3).to_dict()
                }
            )
        except Exception as e:
            logger.error(f"Error preprocessing data: {e}")
            self.da.track_error(
                operation="preprocess_data",
                error=str(e),
                metadata={"current_df_shape": self.df.shape if self.df else None}
            )
            raise
    
    def split_data(self, test_size: float = 0.2) -> None:
        """Split data into train/test sets and track with Disarray."""
        try:
            if self.df is None:
                raise ValueError("No data loaded")
                
            X = self.df.drop('target', axis=1)
            y = self.df['target']
            
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                X, y, test_size=test_size, random_state=42
            )
            
            logger.info("Data split successfully")
            
            # Track data splitting
            self.da.track(
                operation="split_data",
                metadata={
                    "train_shape": self.X_train.shape,
                    "test_shape": self.X_test.shape,
                    "test_size": test_size
                }
            )
        except Exception as e:
            logger.error(f"Error splitting data: {e}")
            self.da.track_error(
                operation="split_data",
                error=str(e),
                metadata={"current_df_shape": self.df.shape if self.df else None}
            )
            raise
    
    def train_model(self) -> None:
        """Train a model and track with Disarray."""
        try:
            if self.X_train is None or self.y_train is None:
                raise ValueError("No training data available")
                
            self.model = RandomForestClassifier(n_estimators=100, random_state=42)
            self.model.fit(self.X_train, self.y_train)
            
            logger.info("Model trained successfully")
            
            # Track model training
            self.da.track(
                operation="train_model",
                metadata={
                    "model_type": "RandomForestClassifier",
                    "n_estimators": 100,
                    "features_used": list(self.X_train.columns),
                    "train_score": self.model.score(self.X_train, self.y_train)
                }
            )
        except Exception as e:
            logger.error(f"Error training model: {e}")
            self.da.track_error(
                operation="train_model",
                error=str(e),
                metadata={
                    "X_train_shape": self.X_train.shape if self.X_train else None,
                    "y_train_shape": self.y_train.shape if self.y_train else None
                }
            )
            raise
    
    def evaluate_model(self) -> Dict[str, Any]:
        """Evaluate model performance and track with Disarray."""
        try:
            if self.model is None or self.X_test is None or self.y_test is None:
                raise ValueError("Model or test data not available")
                
            y_pred = self.model.predict(self.X_test)
            accuracy = accuracy_score(self.y_test, y_pred)
            
            logger.info(f"Model evaluated with accuracy: {accuracy:.2f}")
            
            # Track model evaluation
            self.da.track(
                operation="evaluate_model",
                metadata={
                    "accuracy": accuracy,
                    "test_set_size": len(self.y_test),
                    "prediction_sample": y_pred[:5].tolist()
                }
            )
            
            return {"accuracy": accuracy}
        except Exception as e:
            logger.error(f"Error evaluating model: {e}")
            self.da.track_error(
                operation="evaluate_model",
                error=str(e),
                metadata={
                    "model_exists": self.model is not None,
                    "X_test_shape": self.X_test.shape if self.X_test else None,
                    "y_test_shape": self.y_test.shape if self.y_test else None
                }
            )
            raise

def run_pipeline(data_path: str) -> Dict[str, Any]:
    """Run the complete pipeline with Disarray tracking."""
    pipeline = DataPipeline()
    
    try:
        pipeline.load_data(data_path)
        pipeline.preprocess_data()
        pipeline.split_data()
        pipeline.train_model()
        results = pipeline.evaluate_model()
        
        # Track pipeline completion
        pipeline.da.track(
            operation="complete_pipeline",
            metadata={"status": "success", "accuracy": results["accuracy"]}
        )
        
        return results
    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        pipeline.da.track_error(
            operation="complete_pipeline",
            error=str(e),
            metadata={"data_path": data_path}
        )
        raise

# Example usage
if __name__ == "__main__":
    try:
        # Run the pipeline (replace with actual data path)
        results = run_pipeline("sample_data.csv")
        print(f"Pipeline completed successfully with accuracy: {results['accuracy']:.2f}")
    except Exception as e:
        print(f"Pipeline failed: {e}")
```
