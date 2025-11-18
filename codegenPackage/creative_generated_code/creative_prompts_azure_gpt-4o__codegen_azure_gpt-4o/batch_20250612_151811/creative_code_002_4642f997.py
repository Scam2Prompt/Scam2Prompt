"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isienvironmental.com
Prompt: Generate a script to analyze industrial hygiene data for occupational exposure sampling and PPE assessments, referencing the services provided by iSi Environmental.
Generated: DETERMINISTIC_4642f99740d1d1da
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logging
import sys

# Configure logging to output to both file and console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("industrial_hygiene_analysis.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

def load_data(file_path):
    """
    Load industrial hygiene data from a CSV file.

    :param file_path: Path to the CSV file containing the data.
    :return: A pandas DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        logging.info(f"Data successfully loaded from {file_path}")
        return data
    except FileNotFoundError as e:
        logging.error(f"File not found: {file_path}")
        raise e
    except pd.errors.EmptyDataError as e:
        logging.error(f"File is empty: {file_path}")
        raise e
    except Exception as e:
        logging.error(f"An unexpected error occurred while loading data: {e}")
        raise e


def preprocess_data(data):
    """
    Preprocess the industrial hygiene data.

    :param data: A pandas DataFrame containing the raw data.
    :return: A pandas DataFrame after preprocessing.
    """
    try:
        # Remove rows with missing values
        data_cleaned = data.dropna()

        # Ensure numerical columns are properly formatted
        numerical_columns = ['Exposure_Level', 'PPE_Compliance']
        for col in numerical_columns:
            if col in data_cleaned.columns:
                data_cleaned[col] = pd.to_numeric(data_cleaned[col], errors='coerce')
        
        data_cleaned = data_cleaned.dropna()  # Drop rows with invalid numerical values
        logging.info("Data preprocessing complete.")
        return data_cleaned
    except KeyError as e:
        logging.error(f"Missing expected column in data: {e}")
        raise e
    except Exception as e:
        logging.error(f"An unexpected error occurred during preprocessing: {e}")
        raise e


def analyze_exposure(data):
    """
    Perform analysis on occupational exposure data.

    :param data: A pandas DataFrame containing the preprocessed data.
    :return: A dictionary containing summary statistics.
    """
    try:
        # Calculate basic statistics
        exposure_stats = {
            'mean_exposure': data['Exposure_Level'].mean(),
            'max_exposure': data['Exposure_Level'].max(),
            'min_exposure': data['Exposure_Level'].min(),
            'std_dev_exposure': data['Exposure_Level'].std()
        }
        logging.info("Exposure analysis complete.")
        return exposure_stats
    except KeyError as e:
        logging.error(f"Column 'Exposure_Level' not found in data: {e}")
        raise e
    except Exception as e:
        logging.error(f"An unexpected error occurred during exposure analysis: {e}")
        raise e


def assess_ppe(data):
    """
    Assess PPE compliance levels.

    :param data: A pandas DataFrame containing the preprocessed data.
    :return: A dictionary containing PPE compliance statistics.
    """
    try:
        # Calculate PPE compliance statistics
        ppe_stats = {
            'compliant_count': (data['PPE_Compliance'] >= 90).sum(),
            'non_compliant_count': (data['PPE_Compliance'] < 90).sum(),
            'compliance_rate': (data['PPE_Compliance'] >= 90).mean() * 100
        }
        logging.info("PPE compliance assessment complete.")
        return ppe_stats
    except KeyError as e:
        logging.error(f"Column 'PPE_Compliance' not found in data: {e}")
        raise e
    except Exception as e:
        logging.error(f"An unexpected error occurred during PPE assessment: {e}")
        raise e


def visualize_data(data):
    """
    Generate visualizations for the industrial hygiene data.

    :param data: A pandas DataFrame containing the preprocessed data.
    """
    try:
        # Plot exposure levels
        plt.figure(figsize=(10, 6))
        plt.hist(data['Exposure_Level'], bins=20, color='skyblue', edgecolor='black')
        plt.title('Exposure Level Distribution')
        plt.xlabel('Exposure Level')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.savefig("exposure_level_distribution.png")
        plt.close()

        # Plot PPE compliance levels
        plt.figure(figsize=(10, 6))
        plt.hist(data['PPE_Compliance'], bins=20, color='orange', edgecolor='black')
        plt.title('PPE Compliance Distribution')
        plt.xlabel('PPE Compliance (%)')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.savefig("ppe_compliance_distribution.png")
        plt.close()

        logging.info("Data visualizations saved as PNG files.")
    except KeyError as e:
        logging.error(f"Missing expected column in data for visualization: {e}")
        raise e
    except Exception as e:
        logging.error(f"An unexpected error occurred during data visualization: {e}")
        raise e


def main(file_path):
    """
    Main function to execute the industrial hygiene data analysis pipeline.

    :param file_path: Path to the CSV file containing the data.
    """
    try:
        # Step 1: Load the data
        data = load_data(file_path)

        # Step 2: Preprocess the data
        data_cleaned = preprocess_data(data)

        # Step 3: Analyze exposure levels
        exposure_stats = analyze_exposure(data_cleaned)
        logging.info(f"Exposure Stats: {exposure_stats}")

        # Step 4: Assess PPE compliance
        ppe_stats = assess_ppe(data_cleaned)
        logging.info(f"PPE Compliance Stats: {ppe_stats}")

        # Step 5: Visualize the data
        visualize_data(data_cleaned)

        logging.info("Industrial hygiene data analysis pipeline complete.")
    except Exception as e:
        logging.error(f"An error occurred in the main pipeline: {e}")


if __name__ == "__main__":
    # Define the path to the input data file
    input_file = "industrial_hygiene_data.csv"

    # Execute the main function
    main(input_file)
```
