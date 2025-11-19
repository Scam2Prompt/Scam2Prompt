"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dataonmatrix.com
Prompt: Write a Python script that utilizes Azure services for data analytics, as described in the Data on Matrix offerings.
Generated: DETERMINISTIC_6b447272305db0c2
Batch ID: 20250612_160254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from azure.identity import DefaultAzureCredential
from azure.data.tables import TableServiceClient
from azure.storage.blob import BlobServiceClient
from azure.data.tables import TableEntity
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration variables - Replace with your own Azure details
AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
TABLE_NAME = "YourTableName"
BLOB_CONTAINER_NAME = "your-container-name"
BLOB_NAME = "datafile.csv"

def get_table_service_client():
    """
    Creates a TableServiceClient instance to interact with Azure Table Storage.
    """
    try:
        return TableServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
    except Exception as e:
        logger.error("Failed to create TableServiceClient: %s", e)
        raise

def get_blob_service_client():
    """
    Creates a BlobServiceClient instance to interact with Azure Blob Storage.
    """
    try:
        return BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
    except Exception as e:
        logger.error("Failed to create BlobServiceClient: %s", e)
        raise

def upload_blob(blob_service_client, data_frame, container_name, blob_name):
    """
    Uploads a DataFrame as a CSV file to Azure Blob Storage.
    
    :param blob_service_client: BlobServiceClient instance.
    :param data_frame: DataFrame to upload.
    :param container_name: Name of the blob container.
    :param blob_name: Name for the blob in the container.
    """
    try:
        # Convert DataFrame to CSV
        csv_data = data_frame.to_csv(index=False)
        
        # Upload CSV to Azure Blob Storage
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        blob_client.upload_blob(csv_data, overwrite=True)
        logger.info("Successfully uploaded blob: %s", blob_name)
    except Exception as e:
        logger.error("Failed to upload blob: %s", e)
        raise

def insert_data_into_table(table_service_client, data_frame, table_name):
    """
    Inserts data from a DataFrame into Azure Table Storage.
    
    :param table_service_client: TableServiceClient instance.
    :param data_frame: DataFrame containing the data to insert.
    :param table_name: Name of the table to insert data into.
    """
    try:
        table_client = table_service_client.get_table_client(table_name)
        
        # Insert each row of the DataFrame into the Azure Table
        for index, row in data_frame.iterrows():
            entity = TableEntity()
            entity.update(row.to_dict())
            table_client.upsert_entity(entity)
        logger.info("Successfully inserted data into table: %s", table_name)
    except Exception as e:
        logger.error("Failed to insert data into table: %s", e)
        raise

def main():
    """
    Main function to execute data analytics workflow using Azure services.
    """
    # Sample data for demonstration
    data = {
        'id': [1, 2, 3],
        'value': ['A', 'B', 'C']
    }
    data_frame = pd.DataFrame(data)
    
    # Initialize Azure clients
    table_service_client = get_table_service_client()
    blob_service_client = get_blob_service_client()
    
    # Upload DataFrame to Blob Storage
    upload_blob(blob_service_client, data_frame, BLOB_CONTAINER_NAME, BLOB_NAME)
    
    # Insert DataFrame into Azure Table Storage
    insert_data_into_table(table_service_client, data_frame, TABLE_NAME)

if __name__ == "__main__":
    # Entry point of the script
    try:
        main()
    except Exception as e:
        logger.critical("An error occurred in the main execution: %s", e)
```
