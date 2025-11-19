"""
Generated Code Metadata:
========================
Original URL: https://morpho-foundation.eu
Prompt: Develop a data visualization tool to illustrate the impact of the Morpho Foundation's health projects in Burundi, Uganda, and India, using metrics such as number of people served and project outcomes.
Generated: DETERMINISTIC_eab3e5485475735c
Batch ID: 20250622_211449
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
import matplotlib.pyplot as plt
import seaborn as sns

# Define the data for visualization
data = {
    "Country": ["Burundi", "Uganda", "India"],
    "People_Served": [50000, 120000, 250000],
    "Project_Outcomes": [85, 90, 95]  # Outcomes as percentage of success
}

# Convert data into a pandas DataFrame
df = pd.DataFrame(data)

# Function to visualize the data
def visualize_health_projects(dataframe):
    """
    Visualizes the impact of health projects using bar charts and scatter plots.

    Parameters:
        dataframe (pd.DataFrame): DataFrame containing the data to visualize.

    Returns:
        None
    """
    try:
        # Set the style for the plots
        sns.set(style="whitegrid")

        # Create a bar chart for the number of people served
        plt.figure(figsize=(10, 6))
        sns.barplot(x="Country", y="People_Served", data=dataframe, palette="viridis")
        plt.title("Number of People Served by Health Projects", fontsize=16)
        plt.xlabel("Country", fontsize=14)
        plt.ylabel("People Served", fontsize=14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.tight_layout()
        plt.show()

        # Create a scatter plot for project outcomes
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x="Country", y="Project_Outcomes", data=dataframe, s=100, color="blue")
        plt.title("Project Outcomes by Country", fontsize=16)
        plt.xlabel("Country", fontsize=14)
        plt.ylabel("Project Outcomes (%)", fontsize=14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occurred while visualizing the data: {e}")

# Call the visualization function
visualize_health_projects(df)
```
