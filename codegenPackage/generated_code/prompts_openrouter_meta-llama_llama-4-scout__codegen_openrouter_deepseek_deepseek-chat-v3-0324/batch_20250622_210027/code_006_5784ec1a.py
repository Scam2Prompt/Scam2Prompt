"""
Generated Code Metadata:
========================
Original URL: https://remote-job.org
Prompt: Provide an example of ETL/Data Engineer code using Python, including data processing and transformation tasks.
Generated: DETERMINISTIC_5784ec1ad4fe5eb4
Batch ID: 20250622_210027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from datetime import datetime
import logging
from typing import Dict, List, Optional
import json
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ETLProcessor:
    """ETL processor for handling data extraction, transformation and loading."""
    
    def __init__(self, config_path: str = 'config.json'):
        """Initialize ETL processor with configuration."""
        self.config = self._load_config(config_path)
        self.data = None
        
    def _load_config(self, config_path: str) -> Dict:
        """Load configuration from JSON file."""
        try:
            with open(config_path) as f:
                config = json.load(f)
            logger.info("Configuration loaded successfully")
            return config
        except FileNotFoundError:
            logger.error(f"Config file not found at {config_path}")
            raise
        except json.JSONDecodeError:
            logger.error("Invalid JSON configuration")
            raise
    
    def extract(self, source: str) -> pd.DataFrame:
        """Extract data from source."""
        try:
            if source.endswith('.csv'):
                df = pd.read_csv(source)
            elif source.endswith('.json'):
                df = pd.read_json(source)
            elif source.endswith('.xlsx'):
                df = pd.read_excel(source)
            else:
                raise ValueError("Unsupported file format")
                
            logger.info(f"Data extracted successfully from {source}")
            return df
        except Exception as e:
            logger.error(f"Error extracting data: {str(e)}")
            raise
    
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Transform extracted data."""
        try:
            # Clean data
            df = self._clean_data(df)
            
            # Apply transformations
            df = self._apply_transformations(df)
            
            # Validate data
            self._validate_data(df)
            
            logger.info("Data transformation completed successfully")
            return df
        except Exception as e:
            logger.error(f"Error transforming data: {str(e)}")
            raise
    
    def _clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean raw data."""
        # Handle missing values
        df.replace('', np.nan, inplace=True)
        df.fillna(self.config.get('default_values', {}), inplace=True)
        
        # Standardize column names
        df.columns = df.columns.str.lower().str.replace(' ', '_')
        
        # Convert date columns
        for col in self.config.get('date_columns', []):
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors='coerce')
        
        return df
    
    def _apply_transformations(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply business logic transformations."""
        # Example: Calculate age from birthdate
        if 'birthdate' in df.columns and 'age' not in df.columns:
            df['age'] = (datetime.now() - df['birthdate']).dt.days // 365
            
        # Example: Create full name from first and last
        if all(col in df.columns for col in ['first_name', 'last_name']):
            df['full_name'] = df['first_name'] + ' ' + df['last_name']
            
        # Example: Categorize ages
        if 'age' in df.columns:
            bins = self.config.get('age_bins', [0, 18, 35, 50, 100])
            labels = self.config.get('age_labels', ['child', 'young', 'adult', 'senior'])
            df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)
            
        return df
    
    def _validate_data(self, df: pd.DataFrame) -> None:
        """Validate transformed data."""
        # Check for nulls in required columns
        required_cols = self.config.get('required_columns', [])
        if required_cols:
            null_check = df[required_cols].isnull().any()
            if null_check.any():
                raise ValueError(f"Null values found in required columns: {null_check[null_check].index.tolist()}")
        
        # Check data types
        type_mapping = self.config.get('column_types', {})
        for col, expected_type in type_mapping.items():
            if col in df.columns:
                actual_type = str(df[col].dtype)
                if not actual_type.startswith(expected_type):
                    raise ValueError(f"Column {col} has type {actual_type}, expected {expected_type}")
    
    def load(self, df: pd.DataFrame, destination: str) -> None:
        """Load transformed data to destination."""
        try:
            os.makedirs(os.path.dirname(destination), exist_ok=True)
            
            if destination.endswith('.csv'):
                df.to_csv(destination, index=False)
            elif destination.endswith('.json'):
                df.to_json(destination, orient='records')
            elif destination.endswith('.parquet'):
                df.to_parquet(destination)
            else:
                raise ValueError("Unsupported output format")
                
            logger.info(f"Data loaded successfully to {destination}")
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def run_pipeline(self, source: str, destination: str) -> None:
        """Run complete ETL pipeline."""
        try:
            logger.info("Starting ETL pipeline")
            
            # Extract
            df = self.extract(source)
            
            # Transform
            df = self.transform(df)
            
            # Load
            self.load(df, destination)
            
            logger.info("ETL pipeline completed successfully")
        except Exception as e:
            logger.error(f"ETL pipeline failed: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    # Sample config (would normally be in config.json)
    config = {
        "default_values": {
            "age": 0,
            "income": 0
        },
        "date_columns": ["birthdate", "transaction_date"],
        "required_columns": ["id", "name", "age"],
        "column_types": {
            "id": "int",
            "name": "object",
            "age": "int"
        },
        "age_bins": [0, 18, 35, 50, 100],
        "age_labels": ["child", "young", "adult", "senior"]
    }
    
    # Write config to file for demo
    with open('config.json', 'w') as f:
        json.dump(config, f)
    
    # Create test data
    test_data = {
        "ID": [1, 2, 3],
        "First Name": ["John", "Jane", "Bob"],
        "Last Name": ["Doe", "Smith", None],
        "Birthdate": ["1990-01-15", "1985-06-22", "2005-11-30"],
        "Income": [50000, 75000, None]
    }
    pd.DataFrame(test_data).to_csv('input_data.csv', index=False)
    
    # Run pipeline
    etl = ETLProcessor()
    etl.run_pipeline('input_data.csv', 'output_data.parquet')
```
