"""
Generated Code Metadata:
========================
Original URL: https://gizatech1.vercel.app
Prompt: How do I leverage curated onchain datasets for building machine learning models on the Giza platform?
Generated: DETERMINISTIC_87a5661f37c6e228
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import pandas as pd
import numpy as np
from giza import GizaModel
from giza.datasets import OnChainDataset
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class OnChainMLModel:
    """
    A class to build machine learning models using curated on-chain datasets from Giza platform.
    """
    
    def __init__(self, dataset_name: str, api_key: str = None):
        """
        Initialize the OnChainMLModel with dataset name and API key.
        
        Args:
            dataset_name (str): Name of the on-chain dataset to load
            api_key (str, optional): Giza API key. Defaults to None (reads from env)
        """
        self.dataset_name = dataset_name
        self.api_key = api_key or os.getenv('GIZA_API_KEY')
        if not self.api_key:
            raise ValueError("Giza API key not provided and not found in environment variables")
        
        self.giza_model = GizaModel(api_key=self.api_key)
        self.dataset = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.model = None
        self.scaler = StandardScaler()
    
    def load_dataset(self) -> None:
        """
        Load the specified on-chain dataset from Giza platform.
        """
        try:
            self.dataset = OnChainDataset.load(
                name=self.dataset_name,
                api_key=self.api_key
            )
            print(f"Successfully loaded dataset: {self.dataset_name}")
        except Exception as e:
            raise Exception(f"Failed to load dataset: {str(e)}")
    
    def preprocess_data(self, target_column: str, test_size: float = 0.2) -> None:
        """
        Preprocess the dataset by splitting into features and target, and scaling features.
        
        Args:
            target_column (str): Name of the target column
            test_size (float, optional): Size of test split. Defaults to 0.2
        """
        if self.dataset is None:
            raise ValueError("Dataset not loaded. Call load_dataset() first.")
            
        try:
            # Convert to pandas DataFrame
            df = self.dataset.to_pandas()
            
            # Separate features and target
            X = df.drop(columns=[target_column])
            y = df[target_column]
            
            # Split data
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                X, y, test_size=test_size, random_state=42
            )
            
            # Scale features
            self.X_train = self.scaler.fit_transform(self.X_train)
            self.X_test = self.scaler.transform(self.X_test)
            
        except Exception as e:
            raise Exception(f"Data preprocessing failed: {str(e)}")
    
    def train_model(self, model_params: dict = None) -> None:
        """
        Train a Random Forest classifier on the preprocessed data.
        
        Args:
            model_params (dict, optional): Parameters for the model. Defaults to None
        """
        if self.X_train is None or self.y_train is None:
            raise ValueError("Data not preprocessed. Call preprocess_data() first.")
            
        try:
            # Initialize model with default or provided parameters
            params = model_params or {
                'n_estimators': 100,
                'max_depth': 5,
                'random_state': 42
            }
            
            self.model = RandomForestClassifier(**params)
            self.model.fit(self.X_train, self.y_train)
            print("Model training completed successfully")
            
        except Exception as e:
            raise Exception(f"Model training failed: {str(e)}")
    
    def evaluate_model(self) -> float:
        """
        Evaluate the trained model on test data.
        
        Returns:
            float: Accuracy score of the model
        """
        if self.model is None:
            raise ValueError("Model not trained. Call train_model() first.")
            
        try:
            y_pred = self.model.predict(self.X_test)
            accuracy = accuracy_score(self.y_test, y_pred)
            print(f"Model accuracy: {accuracy:.4f}")
            return accuracy
        except Exception as e:
            raise Exception(f"Model evaluation failed: {str(e)}")
    
    def deploy_to_giza(self, model_name: str) -> str:
        """
        Deploy the trained model to Giza platform.
        
        Args:
            model_name (str): Name to give the deployed model
            
        Returns:
            str: Deployment ID
        """
        if self.model is None:
            raise ValueError("Model not trained. Call train_model() first.")
            
        try:
            deployment = self.giza_model.deploy(
                model=self.model,
                name=model_name,
                framework="sklearn"
            )
            print(f"Model deployed successfully with ID: {deployment.id}")
            return deployment.id
        except Exception as e:
            raise Exception(f"Model deployment failed: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with your dataset name
        ml_pipeline = OnChainMLModel(dataset_name="ethereum_transactions")
        
        # Load dataset
        ml_pipeline.load_dataset()
        
        # Preprocess data (specify your target column)
        ml_pipeline.preprocess_data(target_column="is_fraud")
        
        # Train model
        ml_pipeline.train_model()
        
        # Evaluate model
        accuracy = ml_pipeline.evaluate_model()
        
        # Deploy model (optional)
        # deployment_id = ml_pipeline.deploy_to_giza("fraud_detection_model")
        
    except Exception as e:
        print(f"Error in pipeline execution: {str(e)}")
```
