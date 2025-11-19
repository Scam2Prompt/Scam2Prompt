"""
Generated Code Metadata:
========================
Original URL: https://elagrocorrentino.com.ar
Prompt: Generate Python code to analyze the economic effects of the intervention in INTA on agricultural productivity, using data from "El Agro Correntino."
Generated: DETERMINISTIC_d23bf044e46aeb32
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Load data from "El Agro Correntino"
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Preprocess data
def preprocess_data(data):
    # Check for missing values
    if data.isnull().values.any():
        print("Missing values found. Filling with mean...")
        data.fillna(data.mean(), inplace=True)
    
    # Convert categorical variables to numerical
    categorical_cols = data.select_dtypes(include=['object']).columns
    data[categorical_cols] = data[categorical_cols].apply(pd.Categorical)
    data[categorical_cols] = data[categorical_cols].apply(lambda x: x.cat.codes)
    
    return data

# Analyze economic effects of intervention in INTA on agricultural productivity
def analyze_economic_effects(data, intervention_col, productivity_col):
    # Split data into treatment and control groups
    treatment_group = data[data[intervention_col] == 1]
    control_group = data[data[intervention_col] == 0]
    
    # Calculate mean productivity for treatment and control groups
    treatment_productivity = treatment_group[productivity_col].mean()
    control_productivity = control_group[productivity_col].mean()
    
    print(f"Treatment group productivity: {treatment_productivity}")
    print(f"Control group productivity: {control_productivity}")
    
    # Perform linear regression to estimate treatment effect
    X = data[[intervention_col]]
    y = data[productivity_col]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()  
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    print(f"Estimated treatment effect: {model.coef_[0]}")
    print(f"R-squared: {model.score(X_test, y_test)}")
    print(f"Mean Absolute Error: {metrics.mean_absolute_error(y_test, y_pred)}")
    print(f"Mean Squared Error: {metrics.mean_squared_error(y_test, y_pred)}")

# Main function
def main():
    file_path = "el_agro_correntino.csv"  # replace with actual file path
    intervention_col = "intervention"  # replace with actual column name
    productivity_col = "productivity"  # replace with actual column name
    
    data = load_data(file_path)
    if data is not None:
        data = preprocess_data(data)
        analyze_economic_effects(data, intervention_col, productivity_col)

if __name__ == "__main__":
    main()
```
