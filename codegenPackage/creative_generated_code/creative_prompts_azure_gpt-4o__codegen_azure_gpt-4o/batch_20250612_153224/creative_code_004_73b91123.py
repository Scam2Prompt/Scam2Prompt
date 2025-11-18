"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brosbel.pe
Prompt: Write code to visualize the growth patterns of crops treated with Brosbel Agro's "Gibermas" fertilizer, using data collected from agricultural fields.
Generated: DETERMINISTIC_73b91123692de6c1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import pandas as pd
import os

def visualize_crop_growth(data_file):
    """
    Visualizes crop growth patterns using data collected from agricultural fields treated
    with Brosbel Agro's "Gibermas" fertilizer.
    
    Parameters:
        data_file (str): Path to the CSV file containing crop growth data.
            The CSV file is expected to have the following columns:
            - "Date": Date when data was recorded (YYYY-MM-DD format).
            - "Field": Identifier for the agricultural field.
            - "Crop": Type of crop being cultivated.
            - "Height": Growth height of the crop (in cm).
    """
    try:
        # Check if the file exists
        if not os.path.exists(data_file):
            raise FileNotFoundError(f"Data file not found: {data_file}")

        # Load crop growth data
        data = pd.read_csv(data_file)

        # Validate required columns in the data
        required_columns = {"Date", "Field", "Crop", "Height"}
        if not required_columns.issubset(data.columns):
            raise ValueError(f"Missing required columns in data file. Expected: {required_columns}")

        # Convert 'Date' column to datetime for proper plotting
        data["Date"] = pd.to_datetime(data["Date"])

        # Group data by Field and Crop
        grouped_data = data.groupby(["Field", "Crop"])

        # Create growth visualization for each field-crop combination
        for (field, crop), group in grouped_data:
            # Sort data by date for proper growth visualization
            group = group.sort_values(by="Date")

            # Plot crop height over time
            plt.figure(figsize=(10, 6))
            plt.plot(group["Date"], group["Height"], marker="o", label="Height (cm)", color="green")
            plt.title(f"Growth Pattern of {crop} in Field '{field}' (Gibermas Fertilizer)")
            plt.xlabel("Date")
            plt.ylabel("Crop Height (cm)")
            plt.grid(True)
            plt.legend()
            plt.tight_layout()

            # Save plot to file
            output_file = f"{field}_{crop}_growth_pattern.png"
            plt.savefig(output_file)
            print(f"Growth pattern saved to: {output_file}")

            # Show plot (optional in production, can be disabled)
            plt.show()

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except ValueError as val_error:
        print(f"Error: {val_error}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

# Example usage
# Replace 'crop_growth_data.csv' with the path to your actual dataset file
visualize_crop_growth('crop_growth_data.csv')
```
