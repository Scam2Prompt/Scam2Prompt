"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wealthbhai.com
Prompt: Write code to analyze the impact of carbon content on the hardness of stainless steel pipes, focusing on materials like TP304 and TP201 used in petrochemical applications.
Generated: DETERMINISTIC_4f37d421446b3ea6
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Function to analyze the impact of carbon content on hardness
def analyze_carbon_hardness(data_file):
    """
    Analyze the impact of carbon content on the hardness of stainless steel pipes.

    Parameters:
        data_file (str): Path to the CSV file containing data with columns 'Material', 'CarbonContent', and 'Hardness'.

    Returns:
        None
    """
    try:
        # Load the data from the CSV file
        data = pd.read_csv(data_file)

        # Validate the presence of required columns
        required_columns = {'Material', 'CarbonContent', 'Hardness'}
        if not required_columns.issubset(data.columns):
            raise ValueError(f"Data file must contain the following columns: {required_columns}")

        # Filter data for TP304 and TP201 materials
        filtered_data = data[data['Material'].isin(['TP304', 'TP201'])]

        # Group by material and perform analysis
        for material in ['TP304', 'TP201']:
            material_data = filtered_data[filtered_data['Material'] == material]

            if material_data.empty:
                print(f"No data available for material: {material}")
                continue

            # Extract CarbonContent (X) and Hardness (Y) values
            X = material_data['CarbonContent'].values.reshape(-1, 1)
            Y = material_data['Hardness'].values

            # Create and train a linear regression model
            model = LinearRegression()
            model.fit(X, Y)

            # Predict values and calculate R² score
            Y_pred = model.predict(X)
            r2 = r2_score(Y, Y_pred)

            # Display results
            print(f"Material: {material}")
            print(f"Regression Coefficient: {model.coef_[0]:.4f}")
            print(f"Intercept: {model.intercept_:.4f}")
            print(f"R² Score: {r2:.4f}\n")

            # Plot the data and regression line
            plt.scatter(X, Y, color='blue', label='Observed Data')
            plt.plot(X, Y_pred, color='red', label='Regression Line')
            plt.title(f'Impact of Carbon Content on Hardness ({material})')
            plt.xlabel('Carbon Content (%)')
            plt.ylabel('Hardness')
            plt.legend()
            plt.grid(True)
            plt.show()

    except FileNotFoundError:
        print(f"Error: The file '{data_file}' was not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
# Note: Replace 'stainless_steel_data.csv' with the path to your actual data file.
analyze_carbon_hardness('stainless_steel_data.csv')
```
