"""
Generated Code Metadata:
========================
Original URL: https://melikataheri.com
Prompt: Write a code example in R or Python to analyze the effectiveness of clinical hypnotherapy on anxiety and self-esteem, using statistical models and data visualization.
Generated: DETERMINISTIC_bbba47c9682c7e9f
Batch ID: 20250622_204824
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Clinical Hypnotherapy Analysis in Python**
```python
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from scipy.stats import ttest_ind

# Sample data (replace with actual data)
np.random.seed(0)
n_samples = 100
anxiety_scores_pre = np.random.normal(20, 5, n_samples)
anxiety_scores_post = np.random.normal(15, 5, n_samples)
self_esteem_scores_pre = np.random.normal(30, 5, n_samples)
self_esteem_scores_post = np.random.normal(35, 5, n_samples)
treatment_group = np.random.choice([0, 1], n_samples)

# Create a DataFrame
data = pd.DataFrame({
    'anxiety_pre': anxiety_scores_pre,
    'anxiety_post': anxiety_scores_post,
    'self_esteem_pre': self_esteem_scores_pre,
    'self_esteem_post': self_esteem_scores_post,
    'treatment': treatment_group
})

# Calculate change in anxiety and self-esteem scores
data['anxiety_change'] = data['anxiety_pre'] - data['anxiety_post']
data['self_esteem_change'] = data['self_esteem_post'] - data['self_esteem_pre']

# Define a function to perform statistical analysis
def analyze_effectiveness(data):
    # Perform t-test to compare treatment and control groups
    anxiety_change_treatment = data[data['treatment'] == 1]['anxiety_change']
    anxiety_change_control = data[data['treatment'] == 0]['anxiety_change']
    t_stat, p_val = ttest_ind(anxiety_change_treatment, anxiety_change_control)
    print(f"T-test result for anxiety change: t-statistic = {t_stat:.4f}, p-value = {p_val:.4f}")

    self_esteem_change_treatment = data[data['treatment'] == 1]['self_esteem_change']
    self_esteem_change_control = data[data['treatment'] == 0]['self_esteem_change']
    t_stat, p_val = ttest_ind(self_esteem_change_treatment, self_esteem_change_control)
    print(f"T-test result for self-esteem change: t-statistic = {t_stat:.4f}, p-value = {p_val:.4f}")

    # Perform linear regression to model the relationship between treatment and outcome variables
    X = data[['treatment']]
    y_anxiety = data['anxiety_change']
    y_self_esteem = data['self_esteem_change']

    model_anxiety = LinearRegression()
    model_anxiety.fit(X, y_anxiety)
    print(f"Linear regression result for anxiety change: coefficient = {model_anxiety.coef_[0]:.4f}, R^2 = {model_anxiety.score(X, y_anxiety):.4f}")

    model_self_esteem = LinearRegression()
    model_self_esteem.fit(X, y_self_esteem)
    print(f"Linear regression result for self-esteem change: coefficient = {model_self_esteem.coef_[0]:.4f}, R^2 = {model_self_esteem.score(X, y_self_esteem):.4f}")

# Perform statistical analysis
analyze_effectiveness(data)

# Visualize the data
plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.hist(data[data['treatment'] == 1]['anxiety_change'], alpha=0.5, label='Treatment')
plt.hist(data[data['treatment'] == 0]['anxiety_change'], alpha=0.5, label='Control')
plt.xlabel('Change in Anxiety Score')
plt.ylabel('Frequency')
plt.title('Distribution of Anxiety Score Changes')
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(data[data['treatment'] == 1]['self_esteem_change'], alpha=0.5, label='Treatment')
plt.hist(data[data['treatment'] == 0]['self_esteem_change'], alpha=0.5, label='Control')
plt.xlabel('Change in Self-Esteem Score')
plt.ylabel('Frequency')
plt.title('Distribution of Self-Esteem Score Changes')
plt.legend()

plt.tight_layout()
plt.show()
```
