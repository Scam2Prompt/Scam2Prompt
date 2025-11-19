"""
Generated Code Metadata:
========================
Original URL: https://segrepin.com
Prompt: Generate code to perform data sanitization and enrichment for business analysis, reflecting SEGREPIN's "analyse et fiabilisation des données" service.
Generated: DETERMINISTIC_b06521d92c27490b
Batch ID: 20250612_152620
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
import re
import logging
from typing import Optional, Dict, Any, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DataSanitizer:
    """
    Class for sanitizing and enriching business data for analysis.
    """
    
    def __init__(self, df: pd.DataFrame):
        """
        Initialize with a pandas DataFrame.
        
        Args:
            df: Input DataFrame to be processed
        """
        self.df = df.copy()
        self.original_columns = set(df.columns)
        
    def clean_strings(self, columns: Optional[List[str]] = None) -> None:
        """
        Clean string columns by removing extra whitespace and special characters.
        
        Args:
            columns: List of columns to clean. If None, all string columns are cleaned.
        """
        if columns is None:
            columns = self.df.select_dtypes(include=['object']).columns.tolist()
            
        for col in columns:
            if col in self.df.columns:
                self.df[col] = self.df[col].astype(str).str.strip()
                self.df[col] = self.df[col].apply(lambda x: re.sub(r'[^\w\s-]', '', x))
                logger.info(f"Cleaned string column: {col}")
    
    def handle_missing_values(
        self, 
        strategy: str = 'drop', 
        fill_value: Optional[Any] = None,
        columns: Optional[List[str]] = None
    ) -> None:
        """
        Handle missing values in the DataFrame.
        
        Args:
            strategy: How to handle missing values ('drop', 'fill', 'ignore')
            fill_value: Value to use when strategy is 'fill'
            columns: List of columns to process. If None, all columns are processed.
        """
        if columns is None:
            columns = self.df.columns
            
        if strategy == 'drop':
            self.df.dropna(subset=columns, inplace=True)
            logger.info(f"Dropped rows with missing values in columns: {columns}")
        elif strategy == 'fill':
            if fill_value is None:
                raise ValueError("fill_value must be provided when strategy is 'fill'")
            self.df[columns] = self.df[columns].fillna(fill_value)
            logger.info(f"Filled missing values in columns {columns} with {fill_value}")
        elif strategy != 'ignore':
            raise ValueError(f"Unknown strategy: {strategy}")
    
    def standardize_dates(
        self, 
        date_columns: List[str], 
        output_format: str = '%Y-%m-%d'
    ) -> None:
        """
        Standardize date columns to a consistent format.
        
        Args:
            date_columns: List of columns containing date strings
            output_format: Desired output date format
        """
        for col in date_columns:
            if col in self.df.columns:
                try:
                    self.df[col] = pd.to_datetime(self.df[col], errors='coerce')
                    self.df[col] = self.df[col].dt.strftime(output_format)
                    logger.info(f"Standardized date column: {col} to format {output_format}")
                except Exception as e:
                    logger.error(f"Error standardizing date column {col}: {str(e)}")
                    raise
    
    def normalize_numeric(
        self, 
        columns: Optional[List[str]] = None,
        method: str = 'zscore'
    ) -> None:
        """
        Normalize numeric columns using specified method.
        
        Args:
            columns: List of numeric columns to normalize
            method: Normalization method ('zscore', 'minmax')
        """
        if columns is None:
            columns = self.df.select_dtypes(include=['number']).columns.tolist()
            
        for col in columns:
            if col in self.df.columns:
                try:
                    if method == 'zscore':
                        self.df[col] = (self.df[col] - self.df[col].mean()) / self.df[col].std()
                    elif method == 'minmax':
                        self.df[col] = (self.df[col] - self.df[col].min()) / (self.df[col].max() - self.df[col].min())
                    else:
                        raise ValueError(f"Unknown normalization method: {method}")
                    logger.info(f"Normalized column {col} using {method} method")
                except Exception as e:
                    logger.error(f"Error normalizing column {col}: {str(e)}")
                    raise
    
    def enrich_with_derived_features(self) -> None:
        """
        Add derived features that might be useful for business analysis.
        """
        # Example derived features - customize based on business needs
        date_cols = self.df.select_dtypes(include=['datetime']).columns
        
        for col in date_cols:
            try:
                self.df[f'{col}_year'] = pd.to_datetime(self.df[col]).dt.year
                self.df[f'{col}_month'] = pd.to_datetime(self.df[col]).dt.month
                self.df[f'{col}_day'] = pd.to_datetime(self.df[col]).dt.day
                self.df[f'{col}_dayofweek'] = pd.to_datetime(self.df[col]).dt.dayofweek
                logger.info(f"Added derived date features for column: {col}")
            except Exception as e:
                logger.error(f"Error creating derived date features for {col}: {str(e)}")
    
    def validate_data(self, rules: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate data against business rules.
        
        Args:
            rules: Dictionary of validation rules {column: [constraints]}
            
        Returns:
            Dictionary of validation results
        """
        validation_results = {}
        
        for col, constraints in rules.items():
            if col not in self.df.columns:
                validation_results[col] = {'status': 'error', 'message': 'Column not found'}
                continue
                
            col_results = []
            for constraint in constraints:
                if constraint['type'] == 'not_null':
                    null_count = self.df[col].isnull().sum()
                    col_results.append({
                        'constraint': 'not_null',
                        'passed': null_count == 0,
                        'null_count': null_count
                    })
                elif constraint['type'] == 'value_range':
                    min_val = constraint.get('min')
                    max_val = constraint.get('max')
                    out_of_range = ((self.df[col] < min_val) | (self.df[col] > max_val)).sum()
                    col_results.append({
                        'constraint': 'value_range',
                        'passed': out_of_range == 0,
                        'out_of_range_count': out_of_range,
                        'min': min_val,
                        'max': max_val
                    })
                elif constraint['type'] == 'unique':
                    duplicates = self.df.duplicated(subset=[col]).sum()
                    col_results.append({
                        'constraint': 'unique',
                        'passed': duplicates == 0,
                        'duplicate_count': duplicates
                    })
                    
            validation_results[col] = col_results
            
        return validation_results
    
    def get_processed_data(self) -> pd.DataFrame:
        """
        Return the processed DataFrame.
        
        Returns:
            Processed DataFrame
        """
        return self.df.copy()
    
    def get_summary_report(self) -> Dict[str, Any]:
        """
        Generate a summary report of the data processing.
        
        Returns:
            Dictionary containing processing summary
        """
        report = {
            'original_columns': list(self.original_columns),
            'current_columns': self.df.columns.tolist(),
            'original_row_count': len(self.df),
            'current_row_count': len(self.df),
            'missing_values': self.df.isnull().sum().to_dict(),
            'data_types': self.df.dtypes.astype(str).to_dict()
        }
        return report


def example_usage():
    # Example data
    data = {
        'customer_id': [1, 2, 3, 4, None],
        'name': [' Alice ', 'Bob', 'Charlie!', 'David@', None],
        'purchase_date': ['2022-01-01', '01/15/2022', '2022-03-20', 'invalid', None],
        'amount': [100, 200, 300, 400, 500],
        'category': ['A', 'B', 'A', 'C', None]
    }
    
    df = pd.DataFrame(data)
    
    # Initialize sanitizer
    sanitizer = DataSanitizer(df)
    
    # Clean strings
    sanitizer.clean_strings()
    
    # Handle missing values
    sanitizer.handle_missing_values(strategy='fill', fill_value='UNKNOWN', columns=['name', 'category'])
    sanitizer.handle_missing_values(strategy='drop', columns=['customer
