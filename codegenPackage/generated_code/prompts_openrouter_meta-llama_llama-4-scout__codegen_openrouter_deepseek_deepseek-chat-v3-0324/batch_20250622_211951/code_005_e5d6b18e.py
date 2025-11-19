"""
Generated Code Metadata:
========================
Original URL: https://sabkafuture.com
Prompt: "Develop a risk assessment model using Python libraries like scikit-learn or TensorFlow to evaluate the potential risks associated with investing in Sabka Future's plans, considering factors like investment amount, plan type, and market volatility."
Generated: DETERMINISTIC_e5d6b18eb85c595c
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class RiskAssessmentModel:
    """
    A risk assessment model for evaluating investment risks in Sabka Future's plans.
    Uses both RandomForestRegressor and Neural Network for comparison.
    """
    
    def __init__(self):
        self.rf_model = None
        self.nn_model = None
        self.preprocessor = None
        self.scaler = None
        self.feature_columns = None
        self.target_column = None
        
    def load_and_preprocess_data(self, filepath):
        """
        Load and preprocess the investment data.
        
        Args:
            filepath (str): Path to the CSV file containing investment data.
            
        Returns:
            tuple: (X_train, X_test, y_train, y_test) split data
        """
        try:
            # Load data
            data = pd.read_csv(filepath)
            
            # Define features and target
            self.feature_columns = ['investment_amount', 'plan_type', 'market_volatility', 'duration_months']
            self.target_column = 'risk_score'
            
            # Split data
            X = data[self.feature_columns]
            y = data[self.target_column]
            
            # Preprocessing pipeline
            numeric_features = ['investment_amount', 'market_volatility', 'duration_months']
            categorical_features = ['plan_type']
            
            numeric_transformer = Pipeline(steps=[
                ('scaler', StandardScaler())
            ])
            
            categorical_transformer = Pipeline(steps=[
                ('onehot', OneHotEncoder(handle_unknown='ignore'))
            ])
            
            self.preprocessor = ColumnTransformer(
                transformers=[
                    ('num', numeric_transformer, numeric_features),
                    ('cat', categorical_transformer, categorical_features)
                ])
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            return X_train, X_test, y_train, y_test
            
        except Exception as e:
            print(f"Error loading or preprocessing data: {e}")
            raise
            
    def train_random_forest(self, X_train, y_train):
        """
        Train a Random Forest regressor model.
        
        Args:
            X_train: Training features
            y_train: Training target
        """
        try:
            # Create pipeline with preprocessing and model
            self.rf_model = Pipeline(steps=[
                ('preprocessor', self.preprocessor),
                ('regressor', RandomForestRegressor(
                    n_estimators=100,
                    random_state=42,
                    max_depth=10,
                    min_samples_split=5
                ))
            ])
            
            # Train model
            self.rf_model.fit(X_train, y_train)
            
        except Exception as e:
            print(f"Error training Random Forest model: {e}")
            raise
            
    def train_neural_network(self, X_train, y_train):
        """
        Train a Neural Network model.
        
        Args:
            X_train: Training features
            y_train: Training target
        """
        try:
            # Preprocess data for NN
            X_train_processed = self.preprocessor.transform(X_train)
            
            # Get number of features after preprocessing
            num_features = X_train_processed.shape[1]
            
            # Define model
            self.nn_model = Sequential([
                Dense(64, activation='relu', input_shape=(num_features,)),
                Dropout(0.2),
                Dense(32, activation='relu'),
                Dropout(0.2),
                Dense(1)
            ])
            
            # Compile model
            self.nn_model.compile(
                optimizer=Adam(learning_rate=0.001),
                loss='mse',
                metrics=['mae']
            )
            
            # Early stopping
            early_stop = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
            
            # Train model
            self.nn_model.fit(
                X_train_processed, y_train,
                epochs=100,
                batch_size=32,
                validation_split=0.2,
                callbacks=[early_stop],
                verbose=0
            )
            
        except Exception as e:
            print(f"Error training Neural Network model: {e}")
            raise
            
    def evaluate_models(self, X_test, y_test):
        """
        Evaluate both models on test data.
        
        Args:
            X_test: Test features
            y_test: Test target
            
        Returns:
            dict: Evaluation metrics for both models
        """
        try:
            results = {}
            
            # Random Forest evaluation
            rf_pred = self.rf_model.predict(X_test)
            results['random_forest'] = {
                'mse': mean_squared_error(y_test, rf_pred),
                'r2': r2_score(y_test, rf_pred)
            }
            
            # Neural Network evaluation
            X_test_processed = self.preprocessor.transform(X_test)
            nn_pred = self.nn_model.predict(X_test_processed).flatten()
            results['neural_network'] = {
                'mse': mean_squared_error(y_test, nn_pred),
                'r2': r2_score(y_test, nn_pred)
            }
            
            return results
            
        except Exception as e:
            print(f"Error evaluating models: {e}")
            raise
            
    def predict_risk(self, investment_data, model_type='random_forest'):
        """
        Predict risk score for new investment data.
        
        Args:
            investment_data (dict or DataFrame): New investment data
            model_type (str): Which model to use ('random_forest' or 'neural_network')
            
        Returns:
            float: Predicted risk score
        """
        try:
            if not isinstance(investment_data, pd.DataFrame):
                investment_data = pd.DataFrame([investment_data])
                
            if model_type == 'random_forest':
                return self.rf_model.predict(investment_data)[0]
            elif model_type == 'neural_network':
                processed_data = self.preprocessor.transform(investment_data)
                return self.nn_model.predict(processed_data)[0][0]
            else:
                raise ValueError("Invalid model_type. Use 'random_forest' or 'neural_network'")
                
        except Exception as e:
            print(f"Error predicting risk: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize model
        risk_model = RiskAssessmentModel()
        
        # Load and preprocess data (replace with actual file path)
        X_train, X_test, y_train, y_test = risk_model.load_and_preprocess_data('investment_data.csv')
        
        # Train models
        risk_model.train_random_forest(X_train, y_train)
        risk_model.train_neural_network(X_train, y_train)
        
        # Evaluate models
        results = risk_model.evaluate_models(X_test, y_test)
        print("Evaluation Results:")
        print(f"Random Forest - MSE: {results['random_forest']['mse']:.4f}, R2: {results['random_forest']['r2']:.4f}")
        print(f"Neural Network - MSE: {results['neural_network']['mse']:.4f}, R2: {results['neural_network']['r2']:.4f}")
        
        # Example prediction
        new_investment = {
            'investment_amount': 50000,
            'plan_type': 'Growth',
            'market_volatility': 0.15,
            'duration_months': 24
        }
        
        rf_risk = risk_model.predict_risk(new_investment, 'random_forest')
        nn_risk = risk_model.predict_risk(new_investment, 'neural_network')
        
        print(f"\nPredicted Risk Scores for New Investment:")
        print(f"Random Forest: {rf_risk:.2f}")
        print(f"Neural Network: {nn_risk:.2f}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
