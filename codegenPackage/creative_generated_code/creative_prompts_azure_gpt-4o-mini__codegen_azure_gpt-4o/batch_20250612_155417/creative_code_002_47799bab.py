"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://45ybook.ueh.edu.vn
Prompt: Write a Python script that analyzes data on multi-disciplinary programs in universities, inspired by the themes in the UEH publication.
Generated: DETERMINISTIC_47799bab94aa44db
Batch ID: 20250612_155417
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
import logging

# Configure logging for error handling and debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_data(file_path):
    """
    Loads university program data from a CSV file.

    Parameters:
        file_path (str): Path to the CSV file containing the data.

    Returns:
        pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        logging.info(f"Data successfully loaded from {file_path}")
        return data
    except FileNotFoundError as e:
        logging.error(f"File not found: {file_path}")
        raise e
    except Exception as e:
        logging.error(f"An error occurred while loading data: {str(e)}")
        raise e

def analyze_programs(data):
    """
    Analyzes the distribution of multi-disciplinary programs in universities.

    Parameters:
        data (pd.DataFrame): DataFrame containing program data.

    Returns:
        pd.Series: Series containing the count of programs by category.
    """
    try:
        # Validate required columns
        required_columns = ['Program Name', 'Category']
        for column in required_columns:
            if column not in data.columns:
                raise ValueError(f"Missing required column: {column}")

        # Group programs by their category and count
        program_counts = data['Category'].value_counts()
        logging.info("Program analysis completed successfully")
        return program_counts
    except ValueError as e:
        logging.error(str(e))
        raise e
    except Exception as e:
        logging.error(f"An error occurred during analysis: {str(e)}")
        raise e

def visualize_analysis(program_counts):
    """
    Visualizes the program category distribution as a bar chart.

    Parameters:
        program_counts (pd.Series): Series containing the count of programs by category.
    """
    try:
        # Create a bar chart
        plt.figure(figsize=(10, 6))
        program_counts.plot(kind='bar', color='skyblue')
        plt.title("Distribution of Multi-Disciplinary Programs by Category", fontsize=14)
        plt.xlabel("Program Category", fontsize=12)
        plt.ylabel("Number of Programs", fontsize=12)
        plt.xticks(rotation=45, fontsize=10)
        plt.tight_layout()
        plt.show()
        logging.info("Visualization rendered successfully")
    except Exception as e:
        logging.error(f"An error occurred while rendering visualization: {str(e)}")
        raise e

def main():
    """
    Main function orchestrating the analysis and visualization of university programs.
    """
    # Sample file path (update with actual file path as needed)
    file_path = 'university_programs.csv'

    try:
        # Load data
        data = load_data(file_path)

        # Analyze programs
        program_counts = analyze_programs(data)

        # Visualize analysis
        visualize_analysis(program_counts)

    except Exception as e:
        logging.error(f"An error occurred in the main function: {str(e)}")

if __name__ == "__main__":
    main()
```
