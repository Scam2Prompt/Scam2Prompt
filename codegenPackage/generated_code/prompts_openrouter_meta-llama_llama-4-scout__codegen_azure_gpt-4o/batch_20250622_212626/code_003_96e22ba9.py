"""
Generated Code Metadata:
========================
Original URL: https://labiqc.com
Prompt: What libraries are available for data analysis in laboratory settings, and how can they be used for quality control?
Generated: DETERMINISTIC_96e22ba9adfebd41
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates the use of popular Python libraries for data analysis in laboratory settings,
with a focus on quality control. It uses pandas for data manipulation, numpy for numerical operations,
matplotlib for visualization, and scipy for statistical analysis.
"""

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore

# Function to simulate laboratory data
def generate_lab_data(num_samples=100):
    """
    Generate synthetic laboratory data for demonstration purposes.
    :param num_samples: Number of samples to generate.
    :return: DataFrame containing simulated data.
    """
    np.random.seed(42)  # For reproducibility
    data = {
        "Sample_ID": range(1, num_samples + 1),
        "Measurement": np.random.normal(loc=100, scale=5, size=num_samples),  # Normal distribution
    }
    return pd.DataFrame(data)

# Function to perform quality control analysis
def quality_control_analysis(data, threshold=3):
    """
    Perform quality control analysis on laboratory data.
    :param data: DataFrame containing laboratory data.
    :param threshold: Z-score threshold for identifying outliers.
    :return: DataFrame with outlier information.
    """
    # Calculate Z-scores for the measurements
    data["Z_Score"] = zscore(data["Measurement"])
    
    # Identify outliers based on the threshold
    data["Outlier"] = np.abs(data["Z_Score"]) > threshold
    
    return data

# Function to visualize the data
def visualize_data(data):
    """
    Visualize laboratory data and highlight outliers.
    :param data: DataFrame containing laboratory data.
    """
    plt.figure(figsize=(10, 6))
    
    # Plot measurements
    plt.scatter(data["Sample_ID"], data["Measurement"], label="Measurements", color="blue")
    
    # Highlight outliers
    outliers = data[data["Outlier"]]
    plt.scatter(outliers["Sample_ID"], outliers["Measurement"], label="Outliers", color="red")
    
    # Add labels and legend
    plt.title("Laboratory Data Quality Control")
    plt.xlabel("Sample ID")
    plt.ylabel("Measurement")
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function to execute the workflow
def main():
    """
    Main function to demonstrate data analysis and quality control in laboratory settings.
    """
    try:
        # Generate synthetic laboratory data
        lab_data = generate_lab_data(num_samples=200)
        
        # Perform quality control analysis
        qc_data = quality_control_analysis(lab_data, threshold=3)
        
        # Display summary of outliers
        print("Quality Control Summary:")
        print(qc_data[qc_data["Outlier"]])
        
        # Visualize the data
        visualize_data(qc_data)
    
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
