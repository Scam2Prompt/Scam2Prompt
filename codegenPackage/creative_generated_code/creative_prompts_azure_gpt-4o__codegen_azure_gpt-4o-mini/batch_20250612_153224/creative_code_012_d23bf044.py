"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elagrocorrentino.com.ar
Prompt: Generate Python code to analyze the economic effects of the intervention in INTA on agricultural productivity, using data from "El Agro Correntino."
Generated: DETERMINISTIC_d23bf044e46aeb32
Batch ID: 20250612_153224
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
from statsmodels.formula.api import ols
import logging

# Set up logging for debugging purposes
logging.basicConfig(level=logging.INFO)

def load_data(file_path):
    """
    Load agricultural productivity data from a CSV file.
    
    Parameters:
    file_path (str): The path to the CSV file containing the data.

    Returns:
    pd.DataFrame: A DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        logging.info("Data loaded successfully.")
        return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except pd.errors.EmptyDataError:
        logging.error("No data found in the file.")
        raise
    except Exception as e:
        logging.error(f"An error occurred while loading data: {e}")
        raise

def preprocess_data(df):
    """
    Preprocess the data for analysis.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the data to preprocess.

    Returns:
    pd.DataFrame: A DataFrame containing the preprocessed data.
    """
    # Check for missing values and fill or drop them as needed
    df = df.dropna(subset=['productivity', 'intervention', 'year'])
    logging.info("Preprocessing complete. Missing values handled.")

    return df

def analyze_productivity(df):
    """
    Analyze the economic effects of the intervention on agricultural productivity.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the preprocessed data.
    
    Returns:
    None
    """
    # Perform linear regression analysis
    model = ols('productivity ~ intervention + year', data=df).fit()
    logging.info("Regression analysis complete.")

    # Print the summary of the regression model
    print(model.summary())

def plot_results(df):
    """
    Plot the results of the analysis.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the data to plot.
    
    Returns:
    None
    """
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='intervention', y='productivity', data=df)
    plt.title('Effect of Intervention on Agricultural Productivity')
    plt.xlabel('Intervention')
    plt.ylabel('Productivity')
    plt.grid()
    plt.show()
    logging.info("Results plotted successfully.")

def main(file_path):
    """
    Main function to orchestrate the analysis.
    
    Parameters:
    file_path (str): The path to the CSV file containing the data.
    
    Returns:
    None
    """
    # Load the data
    df = load_data(file_path)

    # Preprocess the data
    df = preprocess_data(df)

    # Analyze productivity
    analyze_productivity(df)

    # Plot the results
    plot_results(df)

if __name__ == "__main__":
    # Example usage
    file_path = 'el_agro_correntino_data.csv'  # Update with the actual path to your data
    main(file_path)
```
