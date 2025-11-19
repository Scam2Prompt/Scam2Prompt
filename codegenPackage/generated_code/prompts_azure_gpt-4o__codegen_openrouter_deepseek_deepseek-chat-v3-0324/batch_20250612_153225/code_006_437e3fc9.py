"""
Generated Code Metadata:
========================
Original URL: https://scienceartthinking.de
Prompt: Suggest APIs or libraries for analyzing "Big Data vs. Small Data" in AI systems, as discussed in the "KI und Intelligenz" article on ScienceArtThinking.de. Provide code examples for comparing data efficiency.
Generated: DETERMINISTIC_437e3fc9fc99048f
Batch ID: 20250612_153225
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
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.datasets import make_regression
from time import time
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

def generate_data(sample_size, features):
    """
    Generate synthetic regression data with specified sample size and features.
    Args:
        sample_size (int): Number of samples
        features (int): Number of features
    Returns:
        X, y: Features and target values
    """
    return make_regression(n_samples=sample_size, n_features=features, noise=0.1, random_state=42)

def train_and_evaluate(X, y):
    """
    Train a linear regression model and evaluate its performance.
    Args:
        X: Feature matrix
        y: Target values
    Returns:
        mse: Mean squared error
        training_time: Time taken to train the model
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    
    start_time = time()
    model.fit(X_train, y_train)
    training_time = time() - start_time
    
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    
    return mse, training_time

def compare_data_efficiency():
    """
    Compare model performance between big data and small data scenarios.
    Prints and plots the comparison results.
    """
    # Define data scenarios
    scenarios = [
        ('Small Data', 1000, 10),
        ('Medium Data', 10000, 20),
        ('Big Data', 100000, 50)
    ]
    
    results = []
    
    for name, samples, features in scenarios:
        X, y = generate_data(samples, features)
        mse, time_taken = train_and_evaluate(X, y)
        results.append({
            'Scenario': name,
            'Samples': samples,
            'Features': features,
            'MSE': mse,
            'Training Time (s)': time_taken
        })
    
    # Create results dataframe
    results_df = pd.DataFrame(results)
    print("\nPerformance Comparison:")
    print(results_df.to_string(index=False))
    
    # Plot results
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # MSE plot
    ax1.bar(results_df['Scenario'], results_df['MSE'], color=['blue', 'orange', 'green'])
    ax1.set_title('Model Accuracy (MSE)')
    ax1.set_ylabel('Mean Squared Error')
    ax1.set_yscale('log')
    
    # Training time plot
    ax2.bar(results_df['Scenario'], results_df['Training Time (s)'], color=['blue', 'orange', 'green'])
    ax2.set_title('Training Time')
    ax2.set_ylabel('Seconds')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    compare_data_efficiency()
```
