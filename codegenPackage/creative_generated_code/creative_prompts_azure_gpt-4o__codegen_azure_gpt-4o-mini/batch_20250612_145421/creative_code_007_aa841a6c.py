"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.icyd.org
Prompt: Write code to analyze the effectiveness of youth development programs using statistical libraries like SciPy or Statsmodels, referencing ICYD.org's focus areas.
Generated: DETERMINISTIC_aa841a6c70a292e4
Batch ID: 20250612_145421
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
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for seaborn
sns.set(style="whitegrid")

# Function to load and preprocess data
def load_data(file_path):
    """
    Load and preprocess data from a CSV file.
    
    Parameters:
        file_path (str): The path to the CSV file containing the data.
    
    Returns:
        pd.DataFrame: A cleaned DataFrame with relevant columns.
    """
    try:
        # Load the dataset
        data = pd.read_csv(file_path)
        
        # Drop rows with missing values
        data.dropna(inplace=True)
        
        # Ensure relevant columns are present
        required_columns = ['Program_Effectiveness', 'Youth_Age', 'Participation_Level', 'Community_Engagement']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing columns in data: {', '.join(missing_columns)}")
        
        return data[required_columns]
    
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        raise
    except Exception as e:
        print(f"An error occurred while loading data: {str(e)}")
        raise

# Function to perform linear regression analysis
def analyze_program_effectiveness(data):
    """
    Analyze the effectiveness of youth development programs using linear regression.
    
    Parameters:
        data (pd.DataFrame): The DataFrame containing the relevant data for analysis.
    
    Returns:
        results: The regression results summary.
    """
    # Define the independent variables (features) and dependent variable (target)
    X = data[['Youth_Age', 'Participation_Level', 'Community_Engagement']]
    y = data['Program_Effectiveness']
    
    # Add a constant to the model (intercept)
    X = sm.add_constant(X)
    
    # Fit the regression model
    model = sm.OLS(y, X).fit()
    
    return model

# Function to visualize the results
def plot_results(model):
    """
    Plot the regression results and diagnostics.
    
    Parameters:
        model: The fitted regression model.
    """
    # Create a summary of the model
    print(model.summary())
    
    # Plotting the residuals
    plt.figure(figsize=(10, 6))
    sns.residplot(x=model.fittedvalues, y=model.resid, lowess=True, 
                  line_kws={'color': 'red', 'lw': 1})
    plt.xlabel('Fitted Values')
    plt.ylabel('Residuals')
    plt.title('Residuals vs Fitted Values')
    plt.axhline(0, linestyle='--', color='grey', lw=2)
    plt.show()

# Main function to execute the analysis
def main():
    # Path to the data file
    file_path = 'youth_program_data.csv'  # Change this to your actual file path
    
    # Load and preprocess the data
    data = load_data(file_path)
    
    # Analyze program effectiveness
    model = analyze_program_effectiveness(data)
    
    # Plot results
    plot_results(model)

# Entry point of the script
if __name__ == "__main__":
    main()
```
