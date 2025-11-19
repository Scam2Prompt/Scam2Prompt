"""
Generated Code Metadata:
========================
Original URL: https://www.linea.ai
Prompt: Provide an example of using Disarray to build on collective knowledge from previous experiments and avoid redundant computations in ML workflows.
Generated: DETERMINISTIC_7f34f548f81fd3f9
Batch ID: 20250612_151801
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
from disarray import Disarray
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Initialize Disarray to track experiments
da = Disarray(project_name="ml_workflow_optimization")

def generate_data():
    """Generate synthetic classification data"""
    X, y = make_classification(
        n_samples=1000,
        n_features=20,
        n_informative=15,
        n_redundant=5,
        random_state=42
    )
    return X, y

def train_model(X_train, y_train, n_estimators=100, max_depth=None):
    """Train a Random Forest classifier"""
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=42
    )
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate model performance"""
    y_pred = model.predict(X_test)
    return accuracy_score(y_test, y_pred)

def main():
    # Generate data
    X, y = generate_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Check if this data configuration has been processed before
    data_hash = da.compute_hash(X)
    existing = da.query(metadata={"data_hash": data_hash})
    
    if existing:
        print("Using cached results from previous experiment")
        best_params = existing[0]['params']
    else:
        print("Running new experiment")
        # Parameter grid to search
        param_grid = {
            'n_estimators': [50, 100, 200],
            'max_depth': [None, 5, 10]
        }
        
        best_score = -1
        best_params = None
        
        # Grid search
        for n_estimators in param_grid['n_estimators']:
            for max_depth in param_grid['max_depth']:
                # Check if this parameter combination has been tried before
                params_hash = da.compute_hash({'n_estimators': n_estimators, 'max_depth': max_depth})
                existing_run = da.query(metadata={"params_hash": params_hash, "data_hash": data_hash})
                
                if existing_run:
                    print(f"Using cached results for params: {n_estimators} trees, max_depth {max_depth}")
                    score = existing_run[0]['metrics']['accuracy']
                else:
                    print(f"Training with {n_estimators} trees, max_depth {max_depth}")
                    model = train_model(X_train, y_train, n_estimators, max_depth)
                    score = evaluate_model(model, X_test, y_test)
                    
                    # Log the experiment
                    da.log(
                        params={'n_estimators': n_estimators, 'max_depth': max_depth},
                        metrics={'accuracy': score},
                        metadata={
                            'data_hash': data_hash,
                            'params_hash': params_hash,
                            'description': f'RF with {n_estimators} trees and max_depth {max_depth}'
                        }
                    )
                
                if score > best_score:
                    best_score = score
                    best_params = {'n_estimators': n_estimators, 'max_depth': max_depth}
        
        print(f"Best params: {best_params} with accuracy: {best_score}")
    
    # Train final model with best params
    final_model = train_model(X_train, y_train, **best_params)
    final_score = evaluate_model(final_model, X_test, y_test)
    print(f"Final model accuracy: {final_score}")

if __name__ == "__main__":
    main()
```
