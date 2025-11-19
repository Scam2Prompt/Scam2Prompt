"""
Generated Code Metadata:
========================
Original URL: https://skaizengroup.eu
Prompt: "Write a code example for a financial data processing pipeline using big data technologies, as applied in SKAIZen Lab's projects and solutions."
Generated: DETERMINISTIC_4316fe6c11c3be41
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, sum
from pyspark.sql.utils import AnalysisException

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("FinancialDataProcessingPipeline") \
    .getOrCreate()

# Function to load financial data from a CSV file
def load_financial_data(file_path: str):
    """
    Load financial data from a CSV file into a Spark DataFrame.

    :param file_path: Path to the CSV file
    :return: DataFrame containing the financial data
    """
    try:
        df = spark.read.csv(file_path, header=True, inferSchema=True)
        return df
    except AnalysisException as e:
        print(f"Error loading data: {e}")
        return None

# Function to process financial data
def process_financial_data(df):
    """
    Process the financial data to calculate total and average values.

    :param df: DataFrame containing the financial data
    :return: DataFrame with processed financial metrics
    """
    if df is None:
        print("DataFrame is None, cannot process data.")
        return None

    # Group by 'category' and calculate total and average amounts
    processed_df = df.groupBy("category").agg(
        sum("amount").alias("total_amount"),
        avg("amount").alias("average_amount")
    )
    
    return processed_df

# Function to save processed data to a specified output path
def save_processed_data(df, output_path: str):
    """
    Save the processed DataFrame to a specified output path in Parquet format.

    :param df: DataFrame to save
    :param output_path: Path to save the output data
    """
    if df is None:
        print("DataFrame is None, cannot save data.")
        return

    try:
        df.write.mode("overwrite").parquet(output_path)
        print(f"Data saved successfully to {output_path}")
    except Exception as e:
        print(f"Error saving data: {e}")

# Main function to run the data processing pipeline
def main():
    # Define file paths
    input_file_path = "path/to/financial_data.csv"
    output_file_path = "path/to/processed_financial_data.parquet"

    # Load financial data
    financial_data_df = load_financial_data(input_file_path)

    # Process financial data
    processed_data_df = process_financial_data(financial_data_df)

    # Save processed data
    save_processed_data(processed_data_df, output_file_path)

# Entry point for the script
if __name__ == "__main__":
    main()

# Stop the Spark session
spark.stop()
```
