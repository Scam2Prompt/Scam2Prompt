"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.icyd.org
Prompt: Generate code using a library like Pandas to visualize data on youth health and social competence, inspired by the objectives of ICYD.org.
Generated: DETERMINISTIC_46f609068e4f236c
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
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset: Youth health and social competence data
# In production, replace this with actual data from a file or database
data = {
    'Youth ID': [1, 2, 3, 4, 5],
    'Physical Activity (hrs/wk)': [5, 3, 6, 2, 7],
    'Sleep Hours (hrs/night)': [8, 6, 7, 5, 8],
    'Social Competence Score': [80, 75, 90, 70, 85],
    'Mental Health Rating (1-10)': [8, 7, 9, 6, 8]
}

# Convert the dataset into a pandas DataFrame
df = pd.DataFrame(data)

# Check if the data is loaded properly
print("Data Preview:")
print(df.head())

# Set up the visualization style
sns.set_style("whitegrid")
plt.figure(figsize=(12, 8))

# Create subplots for better visualization of relationships
plt.subplot(2, 2, 1)
sns.barplot(x='Youth ID', y='Physical Activity (hrs/wk)', data=df, palette="Blues_d")
plt.title('Physical Activity by Youth ID')
plt.xlabel('Youth ID')
plt.ylabel('Physical Activity (hrs/wk)')

plt.subplot(2, 2, 2)
sns.scatterplot(x='Sleep Hours (hrs/night)', y='Social Competence Score', data=df, hue='Mental Health Rating (1-10)', palette="coolwarm", size='Mental Health Rating (1-10)', sizes=(50, 200))
plt.title('Social Competence vs. Sleep Hours')
plt.xlabel('Sleep Hours (hrs/night)')
plt.ylabel('Social Competence Score')

plt.subplot(2, 2, 3)
sns.boxplot(x='Mental Health Rating (1-10)', y='Physical Activity (hrs/wk)', data=df, palette="pastel")
plt.title('Physical Activity by Mental Health Rating')
plt.xlabel('Mental Health Rating (1-10)')
plt.ylabel('Physical Activity (hrs/wk)')

plt.subplot(2, 2, 4)
sns.lineplot(x='Youth ID', y='Social Competence Score', marker='o', data=df, label='Social Competence')
sns.lineplot(x='Youth ID', y='Mental Health Rating (1-10)', marker='o', data=df, label='Mental Health Rating')
plt.title('Youth Social Competence & Mental Health Over IDs')
plt.xlabel('Youth ID')
plt.ylabel('Scores')
plt.legend()

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the visualizations
plt.show()

# Save visualizations as output files
try:
    plt.savefig("youth_health_social_competence_visualizations.png")
    print("Visualization successfully saved as 'youth_health_social_competence_visualizations.png'.")
except Exception as e:
    print(f"Error occurred while saving the visualization: {str(e)}")
```
