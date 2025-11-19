"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: "Write a Python script to analyze the effectiveness of DBT therapy in reducing suicidal ideation and self-harm behaviors in adolescents and adults."
Generated: DETERMINISTIC_7b4c8f0827b6d475
Batch ID: 20250622_210650
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
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Define constants
DATA_FILE = "dbt_therapy_data.csv"  # Path to the dataset file
OUTPUT_FILE = "analysis_results.txt"  # Path to save the analysis results

def load_data(file_path):
    """
    Load the dataset from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: Loaded dataset.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        raise
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        raise
    except Exception as e:
        print(f"Error loading data: {e}")
        raise

def preprocess_data(data):
    """
    Preprocess the dataset by handling missing values and filtering relevant columns.
    
    Args:
        data (pd.DataFrame): Raw dataset.
    
    Returns:
        pd.DataFrame: Preprocessed dataset.
    """
    # Drop rows with missing values in key columns
    data = data.dropna(subset=["Group", "Suicidal_Ideation_Score", "Self_Harm_Score"])
    
    # Ensure scores are numeric
    data["Suicidal_Ideation_Score"] = pd.to_numeric(data["Suicidal_Ideation_Score"], errors="coerce")
    data["Self_Harm_Score"] = pd.to_numeric(data["Self_Harm_Score"], errors="coerce")
    
    # Drop rows with invalid scores
    data = data.dropna(subset=["Suicidal_Ideation_Score", "Self_Harm_Score"])
    
    return data

def analyze_effectiveness(data):
    """
    Analyze the effectiveness of DBT therapy in reducing suicidal ideation and self-harm behaviors.
    
    Args:
        data (pd.DataFrame): Preprocessed dataset.
    
    Returns:
        dict: Analysis results containing statistical metrics.
    """
    # Split data into groups
    dbt_group = data[data["Group"] == "DBT"]
    control_group = data[data["Group"] == "Control"]
    
    # Perform t-tests for suicidal ideation scores
    ttest_suicidal = ttest_ind(dbt_group["Suicidal_Ideation_Score"], control_group["Suicidal_Ideation_Score"])
    
    # Perform t-tests for self-harm scores
    ttest_self_harm = ttest_ind(dbt_group["Self_Harm_Score"], control_group["Self_Harm_Score"])
    
    # Compile results
    results = {
        "Suicidal_Ideation_TTest": {
            "Statistic": ttest_suicidal.statistic,
            "P-Value": ttest_suicidal.pvalue
        },
        "Self_Harm_TTest": {
            "Statistic": ttest_self_harm.statistic,
            "P-Value": ttest_self_harm.pvalue
        }
    }
    
    return results

def save_results(results, file_path):
    """
    Save the analysis results to a text file.
    
    Args:
        results (dict): Analysis results.
        file_path (str): Path to the output file.
    """
    try:
        with open(file_path, "w") as f:
            f.write("DBT Therapy Effectiveness Analysis Results\n")
            f.write("=" * 50 + "\n\n")
            for key, value in results.items():
                f.write(f"{key}:\n")
                for sub_key, sub_value in value.items():
                    f.write(f"  {sub_key}: {sub_value}\n")
                f.write("\n")
        print(f"Results saved to {file_path}")
    except Exception as e:
        print(f"Error saving results: {e}")
        raise

def plot_results(data):
    """
    Generate box plots to visualize the scores for DBT and Control groups.
    
    Args:
        data (pd.DataFrame): Preprocessed dataset.
    """
    try:
        # Box plot for Suicidal Ideation Scores
        plt.figure(figsize=(10, 5))
        data.boxplot(column="Suicidal_Ideation_Score", by="Group", grid=False)
        plt.title("Suicidal Ideation Scores by Group")
        plt.suptitle("")  # Remove default title
        plt.xlabel("Group")
        plt.ylabel("Score")
        plt.show()
        
        # Box plot for Self-Harm Scores
        plt.figure(figsize=(10, 5))
        data.boxplot(column="Self_Harm_Score", by="Group", grid=False)
        plt.title("Self-Harm Scores by Group")
        plt.suptitle("")  # Remove default title
        plt.xlabel("Group")
        plt.ylabel("Score")
        plt.show()
    except Exception as e:
        print(f"Error generating plots: {e}")
        raise

def main():
    """
    Main function to execute the analysis pipeline.
    """
    try:
        # Load and preprocess data
        data = load_data(DATA_FILE)
        data = preprocess_data(data)
        
        # Analyze effectiveness
        results = analyze_effectiveness(data)
        
        # Save results
        save_results(results, OUTPUT_FILE)
        
        # Plot results
        plot_results(data)
    except Exception as e:
        print(f"An error occurred during execution: {e}")

if __name__ == "__main__":
    main()
```
