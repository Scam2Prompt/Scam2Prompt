"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dataonmatrix.com
Prompt: Provide a Python script for data engineering tasks using Agile DataOps, based on the data analytics and BI solutions mentioned on the Data on Matrix website.
Generated: DETERMINISTIC_7bb5977146a88438
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python Script for Data Engineering Tasks using Agile DataOps principles.
This script implements ETL (Extract, Transform, Load) pipeline processes
aligned with best practices for data analytics and BI solutions.

Requirements:
- pandas: Python library for data manipulation
- sqlalchemy: SQL toolkit and Object Relational Mapper
"""

import pandas as pd
from sqlalchemy import create_engine
import logging

# Initialize logging for error tracking and debugging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("data_engineering.log"),
        logging.StreamHandler()
    ]
)

def extract_data(source_type, connection_details):
    """
    Extract data from the given source based on type and connection details.

    Args:
        source_type (str): Type of source (e.g., 'csv', 'sql', 'api').
        connection_details (dict): Connection details for the source.

    Returns:
        pd.DataFrame: Data extracted from the source.

    Raises:
        ValueError: If source_type is not supported.
    """
    logging.info("Starting data extraction...")
    try:
        if source_type == "csv":
            filepath = connection_details.get("filepath")
            if not filepath:
                raise ValueError("Filepath is required for CSV extraction.")
            data = pd.read_csv(filepath)
        elif source_type == "sql":
            db_url = connection_details.get("db_url")
            query = connection_details.get("query")
            if not db_url or not query:
                raise ValueError("Database URL and query are required for SQL extraction.")
            engine = create_engine(db_url)
            data = pd.read_sql_query(query, engine)
        elif source_type == "api":
            # Placeholder for API extraction. Implement API logic per your needs.
            raise NotImplementedError("API extraction is not implemented.")
        else:
            raise ValueError(f"Unsupported source type: {source_type}")
        logging.info("Data extraction completed successfully.")
        return data
    except Exception as e:
        logging.error(f"Error during data extraction: {e}")
        raise

def transform_data(data, transformations):
    """
    Transform the data based on the specified transformations.

    Args:
        data (pd.DataFrame): Input data to transform.
        transformations (dict): Transformations to apply.

    Returns:
        pd.DataFrame: Transformed data.

    Raises:
        ValueError: If transformations dict is invalid.
    """
    logging.info("Starting data transformation...")
    try:
        for transformation in transformations:
            operation = transformation.get("operation")
            params = transformation.get("params", {})
            if operation == "filter_rows":
                condition = params.get("condition")
                if not condition:
                    raise ValueError("Condition is required for row filtering.")
                data = data.query(condition)
            elif operation == "rename_columns":
                rename_mapping = params.get("rename_mapping")
                if not rename_mapping:
                    raise ValueError("Rename mapping is required for renaming columns.")
                data = data.rename(columns=rename_mapping)
            elif operation == "add_column":
                column_name = params.get("column_name")
                default_value = params.get("default_value", None)
                if not column_name:
                    raise ValueError("Column name is required for adding columns.")
                data[column_name] = default_value
            else:
                raise ValueError(f"Unsupported transformation operation: {operation}")
        logging.info("Data transformation completed successfully.")
        return data
    except Exception as e:
        logging.error(f"Error during data transformation: {e}")
        raise

def load_data(data, target_type, connection_details):
    """
    Load data into the specified target based on type and connection details.

    Args:
        data (pd.DataFrame): Data to load into the target.
        target_type (str): Type of target (e.g., 'csv', 'sql').
        connection_details (dict): Connection details for the target.

    Raises:
        ValueError: If target_type is not supported.
    """
    logging.info("Starting data loading...")
    try:
        if target_type == "csv":
            filepath = connection_details.get("filepath")
            if not filepath:
                raise ValueError("Filepath is required for CSV loading.")
            data.to_csv(filepath, index=False)
        elif target_type == "sql":
            db_url = connection_details.get("db_url")
            table_name = connection_details.get("table_name")
            if not db_url or not table_name:
                raise ValueError("Database URL and table name are required for SQL loading.")
            engine = create_engine(db_url)
            data.to_sql(table_name, engine, if_exists="replace", index=False)
        else:
            raise ValueError(f"Unsupported target type: {target_type}")
        logging.info("Data loading completed successfully.")
    except Exception as e:
        logging.error(f"Error during data loading: {e}")
        raise

if __name__ == "__main__":
    """
    Main function for the ETL pipeline.
    """
    logging.info("ETL pipeline started.")

    try:
        # Example configuration for ETL process
        source_config = {
            "source_type": "csv",
            "connection_details": {
                "filepath": "input_data.csv"
            }
        }
        
        transformation_config = [
            {"operation": "filter_rows", "params": {"condition": "age > 30"}},
            {"operation": "rename_columns", "params": {"rename_mapping": {"name": "full_name"}}},
            {"operation": "add_column", "params": {"column_name": "processed_date", "default_value": pd.Timestamp.now()}}
        ]
        
        target_config = {
            "target_type": "csv",
            "connection_details": {
                "filepath": "output_data.csv"
            }
        }

        # Step 1: Extract
        extracted_data = extract_data(**source_config)

        # Step 2: Transform
        transformed_data = transform_data(extracted_data, transformation_config)

        # Step 3: Load
        load_data(transformed_data, **target_config)

        logging.info("ETL pipeline completed successfully.")
    except Exception as e:
        logging.error(f"ETL pipeline failed: {e}")
```
