"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: "Suggest a suitable machine learning model for analyzing polygraph test data, including features for model training and evaluation metrics."
Generated: DETERMINISTIC_d29ef54eabcd4a80
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

# Load and preprocess polygraph data
def load_and_preprocess_data(filepath):
    """
    Load and preprocess polygraph test data.
    
    Args:
        filepath (str): Path to the CSV file containing polygraph data
        
    Returns:
        tuple: (X, y) - Features and labels
    """
    try:
        data = pd.read_csv(filepath)
        
        # Assuming the data has these columns (adjust based on actual data)
        # Features: physiological measurements
        X = data[['respiration_rate', 'heart_rate', 'blood_pressure', 'galvanic_skin_response']]
        
        # Target: truthfulness (0 for truthful, 1 for deceptive)
        y = data['truthfulness']
        
        return X, y
    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None

# Train and evaluate model
def train_and_evaluate(X, y):
    """
    Train and evaluate machine learning models on polygraph data.
    
    Args:
        X (pd.DataFrame): Features
        y (pd.Series): Labels
        
    Returns:
        dict: Evaluation metrics for best model
    """
    if X is None or y is None:
        return {"error": "Invalid input data"}
    
    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create preprocessing and model pipeline
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', RandomForestClassifier(random_state=42))
    ])
    
    # Define parameter grid for hyperparameter tuning
    param_grid = {
        'classifier__n_estimators': [50, 100, 200],
        'classifier__max_depth': [None, 10, 20],
        'classifier__min_samples_split': [2, 5, 10]
    }
    
    # Perform grid search with cross-validation
    grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='f1', n_jobs=-1)
    grid_search.fit(X_train, y_train)
    
    # Get best model
    best_model = grid_search.best_estimator_
    
    # Make predictions
    y_pred = best_model.predict(X_test)
    
    # Calculate evaluation metrics
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred),
        'recall': recall_score(y_test, y_pred),
        'f1_score': f1_score(y_test, y_pred),
        'confusion_matrix': confusion_matrix(y_test, y_pred).tolist(),
        'classification_report': classification_report(y_test, y_pred, output_dict=True),
        'best_params': grid_search.best_params_
    }
    
    return metrics

# Main execution
if __name__ == "__main__":
    # Example usage
    X, y = load_and_preprocess_data('polygraph_data.csv')
    
    if X is not None and y is not None:
        results = train_and_evaluate(X, y)
        print("Model Evaluation Results:")
        print(f"Accuracy: {results['accuracy']:.4f}")
        print(f"Precision: {results['precision']:.4f}")
        print(f"Recall: {results['recall']:.4f}")
        print(f"F1 Score: {results['f1_score']:.4f}")
        print("\nConfusion Matrix:")
        print(np.array(results['confusion_matrix']))
        print("\nClassification Report:")
        print(pd.DataFrame(results['classification_report']).transpose())
        print("\nBest Hyperparameters:")
        print(results['best_params'])
```
