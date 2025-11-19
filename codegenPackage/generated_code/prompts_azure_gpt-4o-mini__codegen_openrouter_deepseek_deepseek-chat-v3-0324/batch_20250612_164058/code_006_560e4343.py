"""
Generated Code Metadata:
========================
Original URL: https://mercanza.es
Prompt: What tools and libraries does Mercanza suggest for ensuring data quality and management in a business environment?
Generated: DETERMINISTIC_560e4343c964c367
Batch ID: 20250612_164058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide a Python script that demonstrates data quality and management tools and libraries that Mercanza might suggest, following best practices:

```python
import pandas as pd
import numpy as np
from great_expectations import DataContext
from pydqc import DataQualityChecker
from openpyxl import load_workbook
from sqlalchemy import create_engine
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DataQualityManager:
    """
    A class to manage data quality operations using various tools and libraries.
    Implements common data quality checks and management tasks.
    """
    
    def __init__(self, config: Dict):
        """
        Initialize DataQualityManager with configuration.
        
        Args:
            config (Dict): Configuration dictionary containing:
                - great_expectations_config: Path to Great Expectations config
                - database_url: Database connection string
                - data_sources: Dictionary of data sources
        """
        self.config = config
        self.ge_context = DataContext(config['great_expectations_config'])
        self.db_engine = create_engine(config['database_url'])
        
    def validate_data_with_great_expectations(self, dataset_name: str) -> Dict:
        """
        Validate dataset using Great Expectations.
        
        Args:
            dataset_name (str): Name of dataset to validate
            
        Returns:
            Dict: Validation results
        """
        try:
            batch = self.ge_context.get_batch(
                {'dataset': dataset_name}, 
                expectation_suite_name=f"{dataset_name}_suite"
            )
            results = batch.validate()
            return results.to_json_dict()
        except Exception as e:
            logger.error(f"Great Expectations validation failed: {str(e)}")
            raise
            
    def profile_data_with_pandas(self, df: pd.DataFrame) -> Dict:
        """
        Generate basic data profile using pandas.
        
        Args:
            df (pd.DataFrame): Data to profile
            
        Returns:
            Dict: Data profile statistics
        """
        try:
            profile = {
                'row_count': len(df),
                'column_count': len(df.columns),
                'missing_values': df.isnull().sum().to_dict(),
                'data_types': df.dtypes.astype(str).to_dict(),
                'descriptive_stats': df.describe(include='all').to_dict()
            }
            return profile
        except Exception as e:
            logger.error(f"Data profiling failed: {str(e)}")
            raise
            
    def check_data_quality_with_dqc(self, df: pd.DataFrame, rules: List[Dict]) -> Dict:
        """
        Check data quality using Data Quality Checker (DQC).
        
        Args:
            df (pd.DataFrame): Data to check
            rules (List[Dict]): List of quality rules
            
        Returns:
            Dict: Quality check results
        """
        try:
            checker = DataQualityChecker(df)
            results = {}
            
            for rule in rules:
                if rule['type'] == 'missing_values':
                    result = checker.check_missing(rule['columns'])
                elif rule['type'] == 'value_range':
                    result = checker.check_range(
                        rule['column'], 
                        rule.get('min'), 
                        rule.get('max')
                    )
                elif rule['type'] == 'data_type':
                    result = checker.check_type(rule['column'], rule['expected_type'])
                
                results[rule['name']] = result
                
            return results
        except Exception as e:
            logger.error(f"DQC check failed: {str(e)}")
            raise
            
    def load_data_from_source(self, source_name: str) -> pd.DataFrame:
        """
        Load data from configured source.
        
        Args:
            source_name (str): Name of data source from config
            
        Returns:
            pd.DataFrame: Loaded data
        """
        try:
            source = self.config['data_sources'][source_name]
            
            if source['type'] == 'csv':
                return pd.read_csv(source['path'])
            elif source['type'] == 'excel':
                return pd.read_excel(source['path'])
            elif source['type'] == 'database':
                query = source.get('query') or f"SELECT * FROM {source['table']}"
                return pd.read_sql(query, self.db_engine)
            else:
                raise ValueError(f"Unsupported data source type: {source['type']}")
        except Exception as e:
            logger.error(f"Failed to load data from {source_name}: {str(e)}")
            raise
            
    def save_data_to_destination(self, df: pd.DataFrame, destination_name: str) -> None:
        """
        Save data to configured destination.
        
        Args:
            df (pd.DataFrame): Data to save
            destination_name (str): Name of destination from config
        """
        try:
            destination = self.config['data_sources'][destination_name]
            
            if destination['type'] == 'csv':
                df.to_csv(destination['path'], index=False)
            elif destination['type'] == 'excel':
                df.to_excel(destination['path'], index=False)
            elif destination['type'] == 'database':
                df.to_sql(
                    destination['table'], 
                    self.db_engine, 
                    if_exists=destination.get('if_exists', 'replace'),
                    index=False
                )
            else:
                raise ValueError(f"Unsupported destination type: {destination['type']}")
        except Exception as e:
            logger.error(f"Failed to save data to {destination_name}: {str(e)}")
            raise

def example_usage():
    """Example usage of the DataQualityManager class."""
    config = {
        'great_expectations_config': 'great_expectations.yml',
        'database_url': 'postgresql://user:password@localhost:5432/mydb',
        'data_sources': {
            'customers': {
                'type': 'csv',
                'path': 'data/customers.csv'
            },
            'sales_db': {
                'type': 'database',
                'table': 'sales',
                'query': 'SELECT * FROM sales WHERE date > NOW() - INTERVAL \'30 days\''
            },
            'output': {
                'type': 'database',
                'table': 'cleaned_sales',
                'if_exists': 'append'
            }
        }
    }
    
    dqm = DataQualityManager(config)
    
    try:
        # Load data
        customers = dqm.load_data_from_source('customers')
        sales = dqm.load_data_from_source('sales_db')
        
        # Profile data
        customer_profile = dqm.profile_data_with_pandas(customers)
        logger.info(f"Customer profile: {customer_profile}")
        
        # Validate with Great Expectations
        ge_results = dqm.validate_data_with_great_expectations('customers')
        logger.info(f"Great Expectations results: {ge_results}")
        
        # Check data quality
        rules = [
            {'name': 'missing_customer_ids', 'type': 'missing_values', 'columns': ['customer_id']},
            {'name': 'valid_amounts', 'type': 'value_range', 'column': 'amount', 'min': 0}
        ]
        dqc_results = dqm.check_data_quality_with_dqc(sales, rules)
        logger.info(f"DQC results: {dqc_results}")
        
        # Save cleaned data
        cleaned_sales = sales[sales['amount'] >= 0].dropna(subset=['customer_id'])
        dqm.save_data_to_destination(cleaned_sales, 'output')
        
    except Exception as e:
        logger.error(f"Data quality process failed: {str(e)}")
        raise

if __name__ == '__main__':
    example_usage()
```
