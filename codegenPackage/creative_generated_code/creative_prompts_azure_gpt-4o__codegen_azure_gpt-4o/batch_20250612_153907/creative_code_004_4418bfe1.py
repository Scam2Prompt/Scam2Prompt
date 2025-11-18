"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inchclub.xyz
Prompt: Create a Python script to process and visualize data related to new material creation, as mentioned in the "AI仅用17天独自创建41种新材料" section of the webpage.
Generated: DETERMINISTIC_4418bfe1a95366b8
Batch ID: 20250612_153907
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
import os

# Define constants
DATA_FILE = "new_materials.csv"  # Expected CSV file containing material data
OUTPUT_DIR = "output_visualizations"

# Ensure output directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def load_data(file_path):
    """
    Load data from a CSV file.
    
    Parameters:
        file_path (str): Path to the CSV file to load.
    
    Returns:
        pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        exit(1)
    except pd.errors.EmptyDataError:
        print("Error: Provided file is empty.")
        exit(1)
    except pd.errors.ParserError:
        print("Error: Failed to parse CSV file.")
        exit(1)


def visualize_material_data(df):
    """
    Generate visualizations for material creation data.
    
    Parameters:
        df (pd.DataFrame): DataFrame containing material data.
    """
    try:
        # Check if required columns exist
        if 'Material' not in df.columns or 'CreationTime' not in df.columns:
            print("Error: Missing required columns 'Material' or 'CreationTime'.")
            exit(1)

        # Group data by creation time
        creation_counts = df.groupby('CreationTime')['Material'].count()

        # Plot a bar chart
        plt.figure(figsize=(10, 6))
        creation_counts.plot(kind='bar', color='skyblue', edgecolor='black')
        plt.title("Number of Materials Created Over Time", fontsize=16)
        plt.xlabel("Creation Time", fontsize=14)
        plt.ylabel("Number of Materials", fontsize=14)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save the plot
        output_file = os.path.join(OUTPUT_DIR, "materials_creation_over_time.png")
        plt.savefig(output_file)
        print(f"Visualization saved to {output_file}")
        plt.close()

    except KeyError as e:
        print(f"Error: Missing key data - {e}")
        exit(1)
    except Exception as e:
        print(f"An unexpected error occurred during visualization: {e}")
        exit(1)


def main():
    """
    Main function to execute the script logic.
    """
    print("Starting data processing...")
    
    # Load data
    data = load_data(DATA_FILE)
    print("Data loaded successfully.")

    # Visualize data
    visualize_material_data(data)
    print("Data visualization completed.")

if __name__ == "__main__":
    main()
```
