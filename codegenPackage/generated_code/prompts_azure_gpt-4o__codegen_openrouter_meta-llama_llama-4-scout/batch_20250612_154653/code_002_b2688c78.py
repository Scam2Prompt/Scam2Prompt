"""
Generated Code Metadata:
========================
Original URL: https://csl-seqirus.co.uk
Prompt: Generate code to analyze clinical trial data for hereditary angioedema (HAE) treatment, incorporating insights from the CSL Seqirus team's presentation at #EAACI2024.
Generated: DETERMINISTIC_b2688c78240380df
Batch ID: 20250612_154653
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
from scipy import stats
import matplotlib.pyplot as plt

# Define a function to analyze clinical trial data for HAE treatment
def analyze_hae_clinical_trial(data):
    """
    Analyze clinical trial data for hereditary angioedema (HAE) treatment.

    Parameters:
    data (pandas.DataFrame): Clinical trial data with columns for patient ID, treatment, and outcome measures.

    Returns:
    dict: Dictionary containing summary statistics and analysis results.
    """

    # Check if input data is a pandas DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame")

    # Ensure required columns exist in the data
    required_columns = ['patient_id', 'treatment', 'attack_frequency', 'attack_severity']
    if not all(column in data.columns for column in required_columns):
        raise ValueError("Input data must contain required columns: patient_id, treatment, attack_frequency, attack_severity")

    # Calculate summary statistics for attack frequency and severity
    summary_stats = {
        'attack_frequency': {
            'mean': data['attack_frequency'].mean(),
            'std': data['attack_frequency'].std(),
            'min': data['attack_frequency'].min(),
            'max': data['attack_frequency'].max()
        },
        'attack_severity': {
            'mean': data['attack_severity'].mean(),
            'std': data['attack_severity'].std(),
            'min': data['attack_severity'].min(),
            'max': data['attack_severity'].max()
        }
    }

    # Perform between-group comparisons for treatment efficacy
    treatment_groups = data['treatment'].unique()
    comparisons = {}
    for i in range(len(treatment_groups)):
        for j in range(i + 1, len(treatment_groups)):
            group1 = data[data['treatment'] == treatment_groups[i]]
            group2 = data[data['treatment'] == treatment_groups[j]]

            # Compare attack frequency between treatment groups
            freq_t_stat, freq_p_val = stats.ttest_ind(group1['attack_frequency'], group2['attack_frequency'])
            comparisons[f"{treatment_groups[i]} vs {treatment_groups[j]}"] = {
                'attack_frequency': {
                    't_stat': freq_t_stat,
                    'p_val': freq_p_val
                }
            }

            # Compare attack severity between treatment groups
            sev_t_stat, sev_p_val = stats.ttest_ind(group1['attack_severity'], group2['attack_severity'])
            comparisons[f"{treatment_groups[i]} vs {treatment_groups[j]}"]['attack_severity'] = {
                't_stat': sev_t_stat,
                'p_val': sev_p_val
            }

    # Visualize distribution of attack frequency and severity by treatment group
    plt.figure(figsize=(10, 6))
    for treatment in treatment_groups:
        group_data = data[data['treatment'] == treatment]
        plt.hist(group_data['attack_frequency'], alpha=0.5, label=treatment)
    plt.xlabel('Attack Frequency')
    plt.ylabel('Frequency')
    plt.title('Distribution of Attack Frequency by Treatment Group')
    plt.legend()
    plt.show()

    # Return summary statistics, comparisons, and plots
    return {
        'summary_stats': summary_stats,
        'comparisons': comparisons
    }

# Example usage
if __name__ == "__main__":
    # Sample clinical trial data
    data = pd.DataFrame({
        'patient_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'treatment': ['Treatment A', 'Treatment A', 'Treatment A', 'Treatment B', 'Treatment B', 'Treatment B', 'Treatment C', 'Treatment C', 'Treatment C', 'Treatment C'],
        'attack_frequency': [2.5, 3.1, 2.8, 1.9, 2.2, 2.1, 3.5, 3.8, 3.2, 3.6],
        'attack_severity': [6.2, 5.8, 6.5, 4.9, 5.1, 4.8, 6.8, 7.1, 6.9, 7.3]
    })

    # Analyze clinical trial data
    results = analyze_hae_clinical_trial(data)

    # Print summary statistics
    print("Summary Statistics:")
    for outcome, stats in results['summary_stats'].items():
        print(outcome)
        for stat, value in stats.items():
            print(f"{stat.capitalize()}: {value:.2f}")
        print()

    # Print between-group comparisons
    print("Between-Group Comparisons:")
    for comparison, results in results['comparisons'].items():
        print(comparison)
        for outcome, stats in results.items():
            print(outcome)
            print(f"t-statistic: {stats['t_stat']:.2f}, p-value: {stats['p_val']:.4f}")
        print()
```
