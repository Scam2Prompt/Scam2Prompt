"""
Generated Code Metadata:
========================
Original URL: https://dataonmatrix.com
Prompt: Write a Python script that utilizes Azure services for data analytics, as described in the Data on Matrix offerings.
Generated: DETERMINISTIC_6b447272305db0c2
Batch ID: 20250612_160254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import (
    AzureBlobStorageLinkedService,
    AzureSqlDatabaseLinkedService,
    Dataset,
    PipelineResource,
    CopyActivity,
    CopySource,
    CopySink,
    SqlSource,
    BlobSink,
    BlobDataset,
    SqlServerTableDataset
)

class AzureDataAnalyticsPipeline:
    """
    A class to manage Azure Data Analytics pipelines using Azure Data Factory.
    """
    
    def __init__(self, subscription_id, resource_group_name, data_factory_name):
        """
        Initialize the Azure Data Analytics Pipeline with credentials and configuration.
        
        Args:
            subscription_id (str): Azure subscription ID
            resource_group_name (str): Azure resource group name
            data_factory_name (str): Azure Data Factory name
        """
        self.subscription_id = subscription_id
        self.resource_group_name = resource_group_name
        self.data_factory_name = data_factory_name
        
        # Authenticate with Azure
        self.credential = DefaultAzureCredential()
        self.adf_client = DataFactoryManagementClient(
            credential=self.credential,
            subscription_id=subscription_id
        )
    
    def create_blob_linked_service(self, service_name, storage_account_name, container_name):
        """
        Create a linked service for Azure Blob Storage.
        
        Args:
            service_name (str): Name for the linked service
            storage_account_name (str): Azure Storage account name
            container_name (str): Container name in the storage account
            
        Returns:
            AzureBlobStorageLinkedService: The created linked service
        """
        connection_string = f"DefaultEndpointsProtocol=https;AccountName={storage_account_name};AccountKey={os.getenv('AZURE_STORAGE_KEY')}"
        
        blob_linked_service = AzureBlobStorageLinkedService(
            connection_string=connection_string
        )
        
        return self.adf_client.linked_services.create_or_update(
            resource_group_name=self.resource_group_name,
            factory_name=self.data_factory_name,
            linked_service_name=service_name,
            properties=blob_linked_service
        )
    
    def create_sql_linked_service(self, service_name, server_name, database_name):
        """
        Create a linked service for Azure SQL Database.
        
        Args:
            service_name (str): Name for the linked service
            server_name (str): Azure SQL server name
            database_name (str): Database name
            
        Returns:
            AzureSqlDatabaseLinkedService: The created linked service
        """
        connection_string = (
            f"Server=tcp:{server_name}.database.windows.net,1433;"
            f"Database={database_name};"
            f"User ID={os.getenv('AZURE_SQL_USER')};"
            f"Password={os.getenv('AZURE_SQL_PASSWORD')};"
            "Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"
        )
        
        sql_linked_service = AzureSqlDatabaseLinkedService(
            connection_string=connection_string
        )
        
        return self.adf_client.linked_services.create_or_update(
            resource_group_name=self.resource_group_name,
            factory_name=self.data_factory_name,
            linked_service_name=service_name,
            properties=sql_linked_service
        )
    
    def create_blob_dataset(self, dataset_name, linked_service_name, folder_path, file_name):
        """
        Create a dataset for Azure Blob Storage.
        
        Args:
            dataset_name (str): Name for the dataset
            linked_service_name (str): Name of the linked service
            folder_path (str): Path to the folder in the container
            file_name (str): Name of the file
            
        Returns:
            Dataset: The created dataset
        """
        blob_dataset = BlobDataset(
            linked_service_name=linked_service_name,
            folder_path=folder_path,
            file_name=file_name
        )
        
        return self.adf_client.datasets.create_or_update(
            resource_group_name=self.resource_group_name,
            factory_name=self.data_factory_name,
            dataset_name=dataset_name,
            properties=blob_dataset
        )
    
    def create_sql_dataset(self, dataset_name, linked_service_name, table_name):
        """
        Create a dataset for Azure SQL Database.
        
        Args:
            dataset_name (str): Name for the dataset
            linked_service_name (str): Name of the linked service
            table_name (str): Name of the SQL table
            
        Returns:
            Dataset: The created dataset
        """
        sql_dataset = SqlServerTableDataset(
            linked_service_name=linked_service_name,
            table_name=table_name
        )
        
        return self.adf_client.datasets.create_or_update(
            resource_group_name=self.resource_group_name,
            factory_name=self.data_factory_name,
            dataset_name=dataset_name,
            properties=sql_dataset
        )
    
    def create_copy_pipeline(self, pipeline_name, source_dataset_name, sink_dataset_name):
        """
        Create a pipeline with a copy activity.
        
        Args:
            pipeline_name (str): Name for the pipeline
            source_dataset_name (str): Name of the source dataset
            sink_dataset_name (str): Name of the sink dataset
            
        Returns:
            PipelineResource: The created pipeline
        """
        copy_activity = CopyActivity(
            name="CopyData",
            inputs=[{"referenceName": source_dataset_name, "type": "DatasetReference"}],
            outputs=[{"referenceName": sink_dataset_name, "type": "DatasetReference"}],
            source=CopySource(type="SqlSource"),
            sink=CopySink(type="BlobSink")
        )
        
        pipeline = PipelineResource(
            activities=[copy_activity]
        )
        
        return self.adf_client.pipelines.create_or_update(
            resource_group_name=self.resource_group_name,
            factory_name=self.data_factory_name,
            pipeline_name=pipeline_name,
            pipeline=pipeline
        )
    
    def run_pipeline(self, pipeline_name):
        """
        Run a pipeline and return the run ID.
        
        Args:
            pipeline_name (str): Name of the pipeline to run
            
        Returns:
            str: The pipeline run ID
        """
        run_response = self.adf_client.pipelines.create_run(
            resource_group_name=self.resource_group_name,
            factory_name=self.data_factory_name,
            pipeline_name=pipeline_name
        )
        return run_response.run_id
    
    def monitor_pipeline_run(self, run_id):
        """
        Monitor a pipeline run until completion.
        
        Args:
            run_id (str): The pipeline run ID to monitor
            
        Returns:
            dict: The final pipeline run status
        """
        while True:
            run_status = self.adf_client.pipeline_runs.get(
                resource_group_name=self.resource_group_name,
                factory_name=self.data_factory_name,
                run_id=run_id
            )
            
            if run_status.status in ["Succeeded", "Failed", "Cancelled"]:
                return {
                    "status": run_status.status,
                    "message": run_status.message
                }
            
            time.sleep(30)

def main():
    # Configuration
    subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
    resource_group_name = "data-analytics-rg"
    data_factory_name = "matrix-data-factory"
    storage_account_name = "matrixstorage"
    sql_server_name = "matrix-sql-server"
    
    # Initialize the pipeline manager
    pipeline_manager = AzureDataAnalyticsPipeline(
        subscription_id=subscription_id,
        resource_group_name=resource_group_name,
        data_factory_name=data_factory_name
    )
    
    try:
        # Create linked services
        blob_service = pipeline_manager.create_blob_linked_service(
            "BlobStorageLinkedService",
            storage_account_name,
            "raw-data"
        )
        
        sql_service = pipeline_manager.create_sql_linked_service(
            "SqlDbLinkedService",
            sql_server_name,
            "analytics-db"
        )
        
        # Create datasets
        source_dataset = pipeline_manager.create_sql_dataset(
            "SourceSqlDataset",
            "SqlDbLinkedService",
            "sales_data"
        )
        
        sink_dataset = pipeline_manager.create_blob_dataset(
            "SinkBlobDataset",
            "BlobStorageLinkedService",
            "processed-data",
            "sales_processed.csv"
        )
        
        # Create pipeline
        pipeline = pipeline_manager.create_copy_pipeline(
            "SalesDataProcessingPipeline",
            "SourceSqlDataset",
            "SinkBlobDataset"
        )
        
        # Run pipeline
        run_id = pipeline_manager.run_pipeline("SalesDataProcessingPipeline")
        print(f"Pipeline started with run ID: {run_id}")
        
        # Monitor pipeline
        status = pipeline_manager.monitor_pipeline_run(run_id)
        print(f"Pipeline completed with status: {status['status']}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    import time
    main()
```
