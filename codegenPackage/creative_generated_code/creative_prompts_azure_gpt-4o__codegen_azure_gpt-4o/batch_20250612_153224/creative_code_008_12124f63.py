"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uranpres.sk
Prompt: Write a Python script to analyze geological survey data for identifying mineral deposits, inspired by the historical uranium exploration activities of URANPRES.
Generated: DETERMINISTIC_12124f63f01fb355
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
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import logging

# Configure logging for error tracking and debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("geological_analysis.log"), logging.StreamHandler()]
)

def load_data(file_path):
    """
    Load geological survey data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing survey data.

    Returns:
        pd.DataFrame: DataFrame containing the survey data.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If the file cannot be parsed.
    """
    try:
        logging.info("Loading geological survey data from %s", file_path)
        data = pd.read_csv(file_path)
        logging.info("Data loaded successfully. Shape of the data: %s", data.shape)
        return data
    except FileNotFoundError:
        logging.error("File not found: %s", file_path)
        raise
    except pd.errors.EmptyDataError:
        logging.error("The file is empty: %s", file_path)
        raise
    except pd.errors.ParserError:
        logging.error("Error parsing the file: %s", file_path)
        raise

def preprocess_data(data):
    """
    Preprocess the geological survey data by handling missing values and normalizing numeric columns.

    Args:
        data (pd.DataFrame): Raw survey data.

    Returns:
        pd.DataFrame: Preprocessed survey data.
    """
    logging.info("Preprocessing data...")
    # Drop rows with missing values
    data_cleaned = data.dropna()
    logging.info("Dropped rows with missing values. Remaining rows: %d", len(data_cleaned))

    # Normalize numeric columns
    numeric_columns = data_cleaned.select_dtypes(include=[np.number]).columns
    data_cleaned[numeric_columns] = (data_cleaned[numeric_columns] - data_cleaned[numeric_columns].mean()) / data_cleaned[numeric_columns].std()
    logging.info("Normalized numeric columns.")

    return data_cleaned

def cluster_data(data, n_clusters=3):
    """
    Perform K-Means clustering on the survey data to identify potential mineral deposit zones.

    Args:
        data (pd.DataFrame): Preprocessed survey data.
        n_clusters (int): Number of clusters for K-Means.

    Returns:
        np.ndarray: Cluster labels for each sample.
    """
    logging.info("Clustering data using K-Means with %d clusters...", n_clusters)
    numeric_data = data.select_dtypes(include=[np.number]).values

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(numeric_data)
    logging.info("Clustering completed.")

    return cluster_labels

def visualize_clusters(data, cluster_labels):
    """
    Visualize the clustering results using a scatter plot.

    Args:
        data (pd.DataFrame): Preprocessed survey data.
        cluster_labels (np.ndarray): Cluster labels from K-Means.
    """
    logging.info("Visualizing clusters...")
    plt.figure(figsize=(10, 6))

    # Assuming the first two numeric columns are used for visualization
    column_names = data.select_dtypes(include=[np.number]).columns
    plt.scatter(data[column_names[0]], data[column_names[1]], c=cluster_labels, cmap='viridis', s=50)

    plt.xlabel(column_names[0])
    plt.ylabel(column_names[1])
    plt.title("Geological Survey Data Clustering")
    plt.colorbar(label='Cluster')
    plt.grid(True)
    plt.show()
    logging.info("Visualization complete.")

def main():
    """
    Main function to run the geological survey data analysis pipeline.
    """
    try:
        # Define the file path for survey data
        file_path = "geological_survey_data.csv"

        # Load the data
        survey_data = load_data(file_path)

        # Preprocess the data
        processed_data = preprocess_data(survey_data)

        # Cluster the data
        cluster_labels = cluster_data(processed_data, n_clusters=5)

        # Visualize the results
        visualize_clusters(processed_data, cluster_labels)
        
    except Exception as e:
        logging.error("An error occurred during execution: %s", str(e))
        raise

# Entry point of the script
if __name__ == "__main__":
    main()
```
