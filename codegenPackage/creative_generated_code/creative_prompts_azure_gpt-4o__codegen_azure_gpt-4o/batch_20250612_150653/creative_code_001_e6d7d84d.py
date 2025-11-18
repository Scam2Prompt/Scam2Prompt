"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sautikenya.com
Prompt: Recommend libraries or APIs for visualizing advocacy impact data, such as the number of women trained in peace and governance initiatives across specific counties (e.g., Kisumu, Nairobi, Mombasa).
Generated: DETERMINISTIC_e6d7d84dabf4eeed
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to visualize advocacy impact data using Python.
This script demonstrates libraries suitable for visualizing data such as the number of women trained 
in peace and governance initiatives across different counties.

Libraries:
- pandas: For data manipulation
- matplotlib: For data visualization
- seaborn: For enhanced plotting
- plotly: For interactive visualizations
"""

# Import necessary libraries
import pandas as pd  # For data manipulation
import matplotlib.pyplot as plt  # For static data visualization
import seaborn as sns  # For enhanced plotting
import plotly.express as px  # For interactive data visualization

# Sample data: Advocacy impact data across counties
data = {
    "County": ["Kisumu", "Nairobi", "Mombasa", "Kakamega", "Eldoret"],
    "Women_Trained": [120, 250, 180, 90, 140],
}

# Create a DataFrame from the sample data
try:
    df = pd.DataFrame(data)
except Exception as e:
    print(f"Error creating DataFrame: {e}")

# Function to visualize data using Matplotlib
def visualize_with_matplotlib(df):
    """
    Visualize advocacy impact data using Matplotlib.

    Parameters:
    df (pandas.DataFrame): DataFrame containing the data.
    """
    try:
        # Bar chart for women trained by county
        plt.figure(figsize=(8, 6))
        plt.bar(df["County"], df["Women_Trained"], color="skyblue")
        plt.title("Women Trained in Peace & Governance Initiatives by County", fontsize=14)
        plt.xlabel("County", fontsize=12)
        plt.ylabel("Number of Women Trained", fontsize=12)
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error visualizing with Matplotlib: {e}")

# Function to visualize data using Seaborn
def visualize_with_seaborn(df):
    """
    Visualize advocacy impact data using Seaborn.

    Parameters:
    df (pandas.DataFrame): DataFrame containing the data.
    """
    try:
        # Bar chart for women trained by county using Seaborn
        plt.figure(figsize=(8, 6))
        sns.barplot(x="County", y="Women_Trained", data=df, palette="Blues_d")
        plt.title("Women Trained in Peace & Governance Initiatives by County", fontsize=14)
        plt.xlabel("County", fontsize=12)
        plt.ylabel("Number of Women Trained", fontsize=12)
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error visualizing with Seaborn: {e}")

# Function to visualize data using Plotly
def visualize_with_plotly(df):
    """
    Visualize advocacy impact data using Plotly.

    Parameters:
    df (pandas.DataFrame): DataFrame containing the data.
    """
    try:
        # Interactive bar chart for women trained by county using Plotly
        fig = px.bar(
            df,
            x="County",
            y="Women_Trained",
            color="County",
            title="Women Trained in Peace & Governance Initiatives by County",
            labels={"County": "County", "Women_Trained": "Number of Women Trained"},
        )
        fig.update_layout(
            xaxis_title="County",
            yaxis_title="Number of Women Trained",
            template="plotly_white",
        )
        fig.show()
    except Exception as e:
        print(f"Error visualizing with Plotly: {e}")

# Main execution block
if __name__ == "__main__":
    print("Advocacy Impact Data Visualization")

    # Visualize using Matplotlib
    print("\nVisualizing with Matplotlib...")
    visualize_with_matplotlib(df)

    # Visualize using Seaborn
    print("\nVisualizing with Seaborn...")
    visualize_with_seaborn(df)

    # Visualize using Plotly
    print("\nVisualizing with Plotly...")
    visualize_with_plotly(df)
```

This code showcases libraries for visualizing advocacy impact data, such as training statistics across counties. It includes static visualizations using Matplotlib and Seaborn, and interactive visualizations using Plotly. Error handling ensures robust execution.
