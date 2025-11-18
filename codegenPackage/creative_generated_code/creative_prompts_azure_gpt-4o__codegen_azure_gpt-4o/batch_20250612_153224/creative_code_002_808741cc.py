"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.slv-valbonne.fr
Prompt: Generate code to analyze and visualize data related to screen time usage and PEGI ratings, inspired by the topics discussed in Sophia Loisirs & Vie's interventions on digital education.
Generated: DETERMINISTIC_808741ccbfe1a742
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
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load and preprocess data
def load_data(file_path):
    """
    Load and preprocess screen time and PEGI ratings data.
    
    Args:
        file_path (str): Path to the CSV file containing the data.
        
    Returns:
        pd.DataFrame: Preprocessed DataFrame ready for analysis.
    """
    try:
        # Load the data
        data = pd.read_csv(file_path)
        
        # Basic data validation
        if data.empty:
            raise ValueError("The data file is empty.")
        if "Screen_Time_Hours" not in data.columns or "PEGI_Rating" not in data.columns:
            raise ValueError("Missing required columns: 'Screen_Time_Hours' or 'PEGI_Rating'.")
        
        # Drop rows with missing or invalid data
        data = data.dropna(subset=["Screen_Time_Hours", "PEGI_Rating"])
        
        # Ensure numeric values for screen time
        data["Screen_Time_Hours"] = pd.to_numeric(data["Screen_Time_Hours"], errors="coerce")
        data = data.dropna(subset=["Screen_Time_Hours"])
        
        # Reset index after cleaning
        data.reset_index(drop=True, inplace=True)
        
        return data
    except Exception as e:
        print(f"Error loading and preprocessing data: {e}")
        return None

# Function to visualize screen time and PEGI ratings
def visualize_data(data):
    """
    Visualize screen time usage and PEGI ratings using bar charts and scatter plots.
    
    Args:
        data (pd.DataFrame): Preprocessed DataFrame containing screen time and PEGI ratings.
    """
    try:
        # Bar plot: Average screen time per PEGI rating
        plt.figure(figsize=(10, 6))
        avg_screen_time = data.groupby("PEGI_Rating")["Screen_Time_Hours"].mean().sort_index()
        avg_screen_time.plot(kind="bar", color="skyblue", edgecolor="black")
        plt.title("Average Screen Time by PEGI Rating")
        plt.xlabel("PEGI Rating")
        plt.ylabel("Average Screen Time (Hours)")
        plt.xticks(rotation=45)
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.tight_layout()
        plt.show()

        # Scatter plot: Screen time vs PEGI ratings
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x="PEGI_Rating", y="Screen_Time_Hours", data=data, hue="PEGI_Rating", palette="viridis")
        plt.title("Screen Time vs PEGI Ratings")
        plt.xlabel("PEGI Rating")
        plt.ylabel("Screen Time (Hours)")
        plt.xticks(rotation=45)
        plt.grid(alpha=0.7)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error visualizing data: {e}")

# Main function to execute the program
def main():
    """
    Main entry point for the program.
    """
    # Define the path to the CSV file
    file_path = "screen_time_pegi_data.csv"  # Update this path as needed
    
    # Load and preprocess data
    data = load_data(file_path)
    
    if data is not None:
        # Visualize the data
        visualize_data(data)
    else:
        print("Failed to process data.")

# Entry point
if __name__ == "__main__":
    main()
```
