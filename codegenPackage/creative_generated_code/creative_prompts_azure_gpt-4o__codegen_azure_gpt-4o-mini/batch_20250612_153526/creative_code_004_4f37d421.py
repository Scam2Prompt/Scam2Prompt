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
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Constants for materials
MATERIALS = {
    'TP304': {
        'carbon_content': '0.08',  # Max carbon content as per ASTM
        'hardness': [90, 90.5, 91, 92, 91.5]  # Example hardness values
    },
    'TP201': {
        'carbon_content': '0.15',  # Max carbon content as per ASTM
        'hardness': [85, 86, 87, 87.5, 88]  # Example hardness values
    }
}

def create_dataset(materials):
    """Create a dataset from materials' carbon content and hardness."""
    data = []
    for material, properties in materials.items():
        carbon = float(properties['carbon_content'])
        for hardness in properties['hardness']:
            data.append({'Material': material, 'Carbon Content': carbon, 'Hardness': hardness})
    
    return pd.DataFrame(data)

def analyze_hardness(df):
    """Analyze the impact of carbon content on hardness using linear regression."""
    # Define features and target variable
    X = df[['Carbon Content']]
    y = df['Hardness']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'Mean Squared Error: {mse:.2f}')
    print(f'R² Score: {r2:.2f}')

    return model.coef_[0], model.intercept_  # Return the slope and intercept

def plot_results(df, slope, intercept):
    """Plot the results of the analysis."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Carbon Content', y='Hardness', hue='Material', style='Material', s=100)

    # Plot the regression line
    x_values = np.linspace(df['Carbon Content'].min(), df['Carbon Content'].max(), 100)
    y_values = slope * x_values + intercept
    plt.plot(x_values, y_values, color='red', label='Regression Line')

    plt.title('Impact of Carbon Content on Hardness of Stainless Steel Pipes')
    plt.xlabel('Carbon Content (%)')
    plt.ylabel('Hardness (HV)')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    """Main function to run the analysis."""
    try:
        # Create dataset
        df = create_dataset(MATERIALS)
        
        # Analyze the hardness
        slope, intercept = analyze_hardness(df)
        
        # Plot the results
        plot_results(df, slope, intercept)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
