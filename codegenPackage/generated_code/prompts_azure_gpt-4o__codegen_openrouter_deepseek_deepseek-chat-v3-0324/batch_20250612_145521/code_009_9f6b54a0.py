"""
Generated Code Metadata:
========================
Original URL: https://stronglp.com
Prompt: Suggest machine learning models to predict athletic performance improvements based on training data and metrics used in Blaise Strong's programs.
Generated: DETERMINISTIC_9f6b54a01984c91a
Batch ID: 20250612_145521
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
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class PerformancePredictor:
    """
    A machine learning model selector for predicting athletic performance improvements.
    Uses various regression models to find the best fit for the given training data.
    """
    
    def __init__(self, data_path=None, df=None):
        """
        Initialize the PerformancePredictor with either a file path or DataFrame.
        
        Args:
            data_path (str, optional): Path to CSV file containing training data.
            df (pd.DataFrame, optional): DataFrame containing training data.
        """
        if data_path:
            self.df = pd.read_csv(data_path)
        elif df is not None:
            self.df = df.copy()
        else:
            raise ValueError("Either data_path or df must be provided")
            
        self.X_train, self.X_test, self.y_train, self.y_test = None, None, None, None
        self.models = {}
        self.best_model = None
        self.scaler = StandardScaler()
        
    def preprocess_data(self, target_column, test_size=0.2, random_state=42):
        """
        Preprocess the data by splitting into features and target, and scaling.
        
        Args:
            target_column (str): Name of the column containing target values.
            test_size (float, optional): Proportion of data for testing. Defaults to 0.2.
            random_state (int, optional): Random seed for reproducibility. Defaults to 42.
        """
        if target_column not in self.df.columns:
            raise ValueError(f"Target column '{target_column}' not found in data")
            
        X = self.df.drop(columns=[target_column])
        y = self.df[target_column]
        
        # Convert categorical variables if any
        X = pd.get_dummies(X)
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )
        
        # Scale features
        self.X_train = self.scaler.fit_transform(self.X_train)
        self.X_test = self.scaler.transform(self.X_test)
        
    def train_models(self):
        """
        Train and evaluate multiple regression models to find the best performer.
        Stores trained models in self.models and sets the best model.
        """
        if self.X_train is None:
            raise ValueError("Data not preprocessed. Call preprocess_data() first.")
            
        # Define models to evaluate
        model_list = [
            ('Linear Regression', LinearRegression()),
            ('Ridge Regression', Ridge()),
            ('Lasso Regression', Lasso()),
            ('Random Forest', RandomForestRegressor(random_state=42)),
            ('Gradient Boosting', GradientBoostingRegressor(random_state=42)),
            ('Support Vector Regression', SVR()),
            ('Neural Network', MLPRegressor(random_state=42, max_iter=1000))
        ]
        
        best_score = -np.inf
        self.best_model = None
        
        for name, model in model_list:
            try:
                # Train model
                model.fit(self.X_train, self.y_train)
                
                # Evaluate on test set
                y_pred = model.predict(self.X_test)
                r2 = r2_score(self.y_test, y_pred)
                mse = mean_squared_error(self.y_test, y_pred)
                
                # Store model and metrics
                self.models[name] = {
                    'model': model,
                    'r2_score': r2,
                    'mse': mse
                }
                
                # Update best model
                if r2 > best_score:
                    best_score = r2
                    self.best_model = (name, model)
                    
            except Exception as e:
                print(f"Error training {name}: {str(e)}")
                continue
                
    def tune_best_model(self, param_grid=None):
        """
        Perform hyperparameter tuning on the best performing model.
        
        Args:
            param_grid (dict, optional): Custom parameter grid for GridSearchCV.
                                        If None, uses default grids.
        """
        if self.best_model is None:
            raise ValueError("No models trained. Call train_models() first.")
            
        best_name, best_model = self.best_model
        
        # Default parameter grids
        default_grids = {
            'Random Forest': {
                'n_estimators': [50, 100, 200],
                'max_depth': [None, 10, 20],
                'min_samples_split': [2, 5, 10]
            },
            'Gradient Boosting': {
                'n_estimators': [50, 100, 200],
                'learning_rate': [0.01, 0.1, 0.2],
                'max_depth': [3, 5, 7]
            },
            'Support Vector Regression': {
                'C': [0.1, 1, 10],
                'kernel': ['linear', 'rbf'],
                'gamma': ['scale', 'auto']
            },
            'Neural Network': {
                'hidden_layer_sizes': [(50,), (100,), (50, 50)],
                'activation': ['relu', 'tanh'],
                'alpha': [0.0001, 0.001, 0.01]
            }
        }
        
        # Use custom grid if provided, otherwise default
        grid = param_grid if param_grid else default_grids.get(best_name, {})
        
        if not grid:
            print(f"No parameter grid defined for {best_name}. Skipping tuning.")
            return
            
        # Create pipeline with scaler and model
        pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('model', best_model)
        ])
        
        # Adjust param grid for pipeline
        grid = {f'model__{key}': value for key, value in grid.items()}
        
        # Perform grid search
        grid_search = GridSearchCV(
            pipeline,
            grid,
            cv=5,
            scoring='r2',
            n_jobs=-1,
            verbose=1
        )
        
        # Fit on the full training data (not just X_train)
        X = np.vstack([self.X_train, self.X_test])
        y = np.concatenate([self.y_train, self.y_test])
        
        grid_search.fit(X, y)
        
        # Update best model
        self.best_model = (f"Tuned {best_name}", grid_search.best_estimator_)
        self.models[f"Tuned {best_name}"] = {
            'model': grid_search.best_estimator_,
            'r2_score': grid_search.best_score_,
            'mse': None  # Will be calculated when needed
        }
        
    def predict(self, new_data):
        """
        Make predictions using the best model.
        
        Args:
            new_data (pd.DataFrame): New data for prediction.
            
        Returns:
            np.array: Predicted performance improvements.
        """
        if self.best_model is None:
            raise ValueError("No models trained. Call train_models() first.")
            
        _, model = self.best_model
        
        # Preprocess new data to match training format
        new_data = pd.get_dummies(new_data)
        
        # Ensure columns match training data
        missing_cols = set(self.df.columns) - set(new_data.columns)
        for col in missing_cols:
            new_data[col] = 0
            
        # Reorder columns to match training data
        new_data = new_data[self.df.drop(columns=[self.y_train.name]).columns]
        
        # Scale features
        new_data = self.scaler.transform(new_data)
        
        return model.predict(new_data)
        
    def get_model_performance(self):
        """
        Get performance metrics for all trained models.
        
        Returns:
            dict: Dictionary with model names as keys and metrics as values.
        """
        return {
            name: {
                'r2_score': metrics['r2_score'],
                'mse': metrics['mse']
            }
            for name, metrics in self.models.items()
        }
        
    def get_best_model(self):
        """
        Get the best performing model and its metrics.
        
        Returns:
            tuple: (model_name, model_object, metrics_dict)
        """
        if self.best_model is None:
            return None
            
        name, model = self.best_model
        return name, model, self.models[name]
```
