"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.be
Prompt: Suggest libraries for visualizing the increase in FSC-certified wood usage, as highlighted by PDC Brush's environmental commitment.
Generated: DETERMINISTIC_69e3b096f67e1a4b
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for data visualization
# These libraries are widely used and suited for clean and interactive visualizations
import matplotlib.pyplot as plt  # For static and detailed visualizations
import seaborn as sns  # For enhanced statistical data visualization
import plotly.express as px  # For creating interactive visualizations easily

# Function to visualize FSC-certified wood usage trend
def visualize_fsc_usage(data, library="matplotlib"):
    """
    Visualizes the increase in FSC-certified wood usage.
    
    Parameters:
        data (dict): A dictionary with years as keys and FSC-certified wood usage values as values.
        library (str): The library to use for visualization. Options are "matplotlib", "seaborn", "plotly".
    
    Returns:
        None
    """
    try:
        # Ensure data is valid
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary with years as keys and usage values as values.")
        
        years = list(data.keys())
        usage = list(data.values())

        # Choose visualization library
        if library.lower() == "matplotlib":
            # Matplotlib Visualization
            plt.figure(figsize=(10, 6))
            plt.plot(years, usage, marker='o', label="FSC-Certified Wood Usage")
            plt.title("Increase in FSC-Certified Wood Usage", fontsize=16)
            plt.xlabel("Year", fontsize=12)
            plt.ylabel("Usage (units)", fontsize=12)
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.legend(fontsize=12)
            plt.show()

        elif library.lower() == "seaborn":
            # Seaborn Visualization
            sns.set(style="whitegrid")
            plt.figure(figsize=(10, 6))
            sns.lineplot(x=years, y=usage, marker="o", label="FSC-Certified Wood Usage")
            plt.title("Increase in FSC-Certified Wood Usage", fontsize=16)
            plt.xlabel("Year", fontsize=12)
            plt.ylabel("Usage (units)", fontsize=12)
            plt.legend(fontsize=12)
            plt.show()

        elif library.lower() == "plotly":
            # Plotly Visualization
            fig = px.line(x=years, y=usage, markers=True, labels={'x': 'Year', 'y': 'Usage (units)'},
                          title="Increase in FSC-Certified Wood Usage")
            fig.update_layout(title_font_size=20, xaxis_title_font_size=14, yaxis_title_font_size=14)
            fig.show()

        else:
            raise ValueError("Unsupported library. Please choose 'matplotlib', 'seaborn', or 'plotly'.")

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Example data representing FSC-certified wood usage over years
    example_data = {
        2018: 120,
        2019: 150,
        2020: 200,
        2021: 250,
        2022: 300,
    }

    # Visualize using matplotlib
    visualize_fsc_usage(example_data, library="matplotlib")

    # Visualize using seaborn
    visualize_fsc_usage(example_data, library="seaborn")

    # Visualize using plotly
    visualize_fsc_usage(example_data, library="plotly")
```
