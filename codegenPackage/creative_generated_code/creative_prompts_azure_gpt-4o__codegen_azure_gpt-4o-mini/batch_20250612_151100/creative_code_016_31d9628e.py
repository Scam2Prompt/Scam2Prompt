"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptrongurgaon.in
Prompt: Create a Hadoop-based big data processing pipeline, referencing APTRON Gurgaon’s Big Data Hadoop training.
Generated: DETERMINISTIC_31d9628e8e65ea0a
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.utils import AnalysisException

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("BigDataProcessingPipeline") \
    .getOrCreate()

# Function to read data from HDFS
def read_data_from_hdfs(file_path: str):
    """
    Read data from HDFS into a Spark DataFrame.

    Parameters:
    file_path (str): The HDFS path to the input data file.

    Returns:
    DataFrame: A Spark DataFrame containing the data.
    """
    try:
        df = spark.read.csv(file_path, header=True, inferSchema=True)
        print(f"Data read successfully from {file_path}")
        return df
    except AnalysisException as e:
        print(f"Error reading data from {file_path}: {e}")
        return None

# Function to process the data
def process_data(df):
    """
    Process the input DataFrame by filtering and transforming data.

    Parameters:
    df (DataFrame): The input Spark DataFrame.

    Returns:
    DataFrame: A Spark DataFrame after processing.
    """
    if df is None:
        print("No data to process.")
        return None

    # Example transformation: Filter out rows where 'value' is less than 0
    processed_df = df.filter(col("value") >= 0)

    # Additional transformations can be applied here

    print("Data processed successfully.")
    return processed_df

# Function to write processed data back to HDFS
def write_data_to_hdfs(df, output_path: str):
    """
    Write the processed DataFrame to HDFS.

    Parameters:
    df (DataFrame): The processed Spark DataFrame.
    output_path (str): The HDFS path to write the output data file.
    """
    if df is None:
        print("No data to write.")
        return

    try:
        df.write.csv(output_path, mode='overwrite', header=True)
        print(f"Data written successfully to {output_path}")
    except Exception as e:
        print(f"Error writing data to {output_path}: {e}")

# Main execution flow
if __name__ == "__main__":
    # Define HDFS paths
    input_hdfs_path = "hdfs://path/to/input/data.csv"
    output_hdfs_path = "hdfs://path/to/output/processed_data.csv"
    
    # Step 1: Read data from HDFS
    data_df = read_data_from_hdfs(input_hdfs_path)

    # Step 2: Process the data
    processed_df = process_data(data_df)

    # Step 3: Write the processed data back to HDFS
    write_data_to_hdfs(processed_df, output_hdfs_path)

    # Stop the Spark session
    spark.stop()
```
