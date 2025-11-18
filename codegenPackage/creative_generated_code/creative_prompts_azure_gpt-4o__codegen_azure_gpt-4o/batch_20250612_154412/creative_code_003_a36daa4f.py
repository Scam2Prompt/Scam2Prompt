"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://invictacobrancas.com.br
Prompt: Create a script to analyze debt recovery data and generate performance reports, mimicking the features of the Invicta Cobranças online platform.
Generated: DETERMINISTIC_a36daa4f2511f125
Batch ID: 20250612_154412
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
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("debt_recovery_analysis.log")
    ]
)

# Constants for the script
INPUT_FILE = "debt_recovery_data.csv"
OUTPUT_FILE = "performance_report.csv"


def load_data(file_path):
    """
    Load debt recovery data into a pandas DataFrame.
    
    Parameters:
        file_path (str): Path to the input CSV file.
        
    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        logging.info("Data successfully loaded from %s", file_path)
        return data
    except Exception as e:
        logging.error("Error loading data: %s", str(e))
        raise


def preprocess_data(data):
    """
    Preprocess the debt recovery data by handling missing values and adding necessary fields.
    
    Parameters:
        data (pd.DataFrame): Raw data.
    
    Returns:
        pd.DataFrame: Preprocessed data.
    """
    try:
        # Drop rows with missing values
        data = data.dropna()
        logging.info("Missing values handled by dropping rows.")
        
        # Ensure data types are correct (e.g., convert dates)
        if 'date' in data:
            data['date'] = pd.to_datetime(data['date'])
            logging.info("Date column converted to datetime format.")
        
        return data
    except Exception as e:
        logging.error("Error preprocessing data: %s", str(e))
        raise


def analyze_performance(data):
    """
    Analyze debt recovery data for performance metrics such as recovery rates.
    
    Parameters:
        data (pd.DataFrame): Preprocessed data.
    
    Returns:
        dict: Dictionary containing performance metrics.
    """
    try:
        total_debt = data['total_debt'].sum() if 'total_debt' in data else 0
        recovered_amount = data['recovered_amount'].sum() if 'recovered_amount' in data else 0
        recovery_rate = (recovered_amount / total_debt) * 100 if total_debt > 0 else 0
        
        # Compile metrics into a dictionary
        metrics = {
            'total_debt': total_debt,
            'recovered_amount': recovered_amount,
            'recovery_rate': recovery_rate,
        }
        
        logging.info("Performance metrics calculated: %s", metrics)
        return metrics
    except Exception as e:
        logging.error("Error analyzing performance: %s", str(e))
        raise


def generate_report(metrics, output_file):
    """
    Generate a CSV report for the calculated performance metrics.
    
    Parameters:
        metrics (dict): Dictionary containing performance metrics.
        output_file (str): Path to the output file.
    """
    try:
        report_df = pd.DataFrame([metrics])
        report_df.to_csv(output_file, index=False)
        logging.info("Performance report saved to %s", output_file)
    except Exception as e:
        logging.error("Error generating report: %s", str(e))
        raise


def visualize_data(data):
    """
    Create a visualization of debt and recovery data using matplotlib.

    Parameters:
        data (pd.DataFrame): Preprocessed data.
    """
    try:
        if 'date' in data and 'recovered_amount' in data:
            plt.figure(figsize=(10, 6))
            plt.plot(data['date'], data['recovered_amount'], marker='o', label="Recovered Amount")
            plt.title("Debt Recovery Over Time")
            plt.xlabel("Date")
            plt.ylabel("Recovered Amount")
            plt.legend()
            plt.grid(True)
            plt.tight_layout()
            plt.savefig("recovery_performance_plot.png")
            logging.info("Visualization saved to recovery_performance_plot.png")
        else:
            logging.warning("Required fields for visualization are missing.")
    except Exception as e:
        logging.error("Error creating visualization: %s", str(e))
        raise


def main():
    """
    Main function to orchestrate the script operations.
    """
    try:
        # Load and preprocess data
        data = load_data(INPUT_FILE)
        data = preprocess_data(data)
        
        # Perform analysis
        metrics = analyze_performance(data)
        
        # Generate report
        generate_report(metrics, OUTPUT_FILE)
        
        # Visualize data
        visualize_data(data)
        
        logging.info("Debt recovery analysis completed successfully.")
    except Exception as e:
        logging.critical("An error occurred: %s", str(e))


if __name__ == "__main__":
    main()
```
