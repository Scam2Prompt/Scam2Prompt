"""
Generated Code Metadata:
========================
Original URL: https://edukacija.net
Prompt: Write a Python script for data wrangling, incorporating techniques from the "Data Wrangling in Python Live Course" mentioned on edukacija.net.
Generated: DETERMINISTIC_aab89eafcc765aaf
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Data Wrangling Script
Inspired by techniques from "Data Wrangling in Python Live Course"
"""

import pandas as pd
import numpy as np
import re
from datetime import datetime
import warnings
import logging
from typing import Union, List, Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('data_wrangling.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Suppress pandas warnings
warnings.filterwarnings('ignore')

class DataWrangler:
    """
    A class for performing common data wrangling operations.
    """
    
    def __init__(self, df: pd.DataFrame = None):
        """
        Initialize the DataWrangler with a DataFrame.
        
        Args:
            df (pd.DataFrame): Input DataFrame to wrangle
        """
        self.df = df.copy() if df is not None else None
    
    def load_data(self, file_path: str, **kwargs) -> pd.DataFrame:
        """
        Load data from various file formats.
        
        Args:
            file_path (str): Path to the data file
            **kwargs: Additional arguments for pandas read functions
            
        Returns:
            pd.DataFrame: Loaded DataFrame
        """
        try:
            if file_path.endswith('.csv'):
                self.df = pd.read_csv(file_path, **kwargs)
            elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
                self.df = pd.read_excel(file_path, **kwargs)
            elif file_path.endswith('.json'):
                self.df = pd.read_json(file_path, **kwargs)
            elif file_path.endswith('.parquet'):
                self.df = pd.read_parquet(file_path, **kwargs)
            else:
                raise ValueError("Unsupported file format")
                
            logger.info(f"Successfully loaded data from {file_path}")
            return self.df
            
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def clean_column_names(self) -> pd.DataFrame:
        """
        Standardize column names by:
        - Converting to lowercase
        - Replacing spaces with underscores
        - Removing special characters
        
        Returns:
            pd.DataFrame: DataFrame with cleaned column names
        """
        if self.df is None:
            raise ValueError("No DataFrame loaded")
            
        self.df.columns = (
            self.df.columns
            .str.lower()
            .str.replace(' ', '_')
            .str.replace('[^a-z0-9_]', '', regex=True)
        )
        logger.info("Column names cleaned")
        return self.df
    
    def handle_missing_values(self, strategy: str = 'drop', **kwargs) -> pd.DataFrame:
        """
        Handle missing values in the DataFrame.
        
        Args:
            strategy (str): Strategy for handling missing values ('drop', 'fill', 'interpolate')
            **kwargs: Additional arguments for the strategy
            
        Returns:
            pd.DataFrame: DataFrame with handled missing values
        """
        if self.df is None:
            raise ValueError("No DataFrame loaded")
            
        if strategy == 'drop':
            self.df = self.df.dropna(**kwargs)
        elif strategy == 'fill':
            fill_value = kwargs.get('fill_value', 0)
            self.df = self.df.fillna(fill_value)
        elif strategy == 'interpolate':
            self.df = self.df.interpolate(**kwargs)
        else:
            raise ValueError("Invalid strategy. Choose 'drop', 'fill', or 'interpolate'")
            
        logger.info(f"Missing values handled using {strategy} strategy")
        return self.df
    
    def convert_data_types(self, column_type_map: Dict[str, str]) -> pd.DataFrame:
        """
        Convert columns to specified data types.
        
        Args:
            column_type_map (Dict[str, str]): Dictionary mapping column names to target types
            
        Returns:
            pd.DataFrame: DataFrame with converted data types
        """
        if self.df is None:
            raise ValueError("No DataFrame loaded")
            
        for col, dtype in column_type_map.items():
            try:
                if dtype == 'datetime':
                    self.df[col] = pd.to_datetime(self.df[col])
                elif dtype == 'category':
                    self.df[col] = self.df[col].astype('category')
                else:
                    self.df[col] = self.df[col].astype(dtype)
            except Exception as e:
                logger.warning(f"Could not convert column {col} to {dtype}: {str(e)}")
                
        logger.info("Data types converted according to column_type_map")
        return self.df
    
    def remove_duplicates(self, subset: List[str] = None, keep: str = 'first') -> pd.DataFrame:
        """
        Remove duplicate rows from the DataFrame.
        
        Args:
            subset (List[str]): Columns to consider for identifying duplicates
            keep (str): Which duplicates to keep ('first', 'last', False)
            
        Returns:
            pd.DataFrame: DataFrame with duplicates removed
        """
        if self.df is None:
            raise ValueError("No DataFrame loaded")
            
        self.df = self.df.drop_duplicates(subset=subset, keep=keep)
        logger.info(f"Duplicates removed (keep={keep})")
        return self.df
    
    def normalize_text(self, columns: Union[str, List[str]]) -> pd.DataFrame:
        """
        Normalize text data in specified columns.
        
        Args:
            columns (Union[str, List[str]]): Column(s) to normalize
            
        Returns:
            pd.DataFrame: DataFrame with normalized text
        """
        if self.df is None:
            raise ValueError("No DataFrame loaded")
            
        if isinstance(columns, str):
            columns = [columns]
            
        for col in columns:
            if col in self.df.columns:
                self.df[col] = (
                    self.df[col]
                    .str.lower()
                    .str.strip()
                    .str.normalize('NFKD')
                    .str.encode('ascii', errors='ignore')
                    .str.decode('utf-8')
                )
                
        logger.info(f"Text normalized in columns: {columns}")
        return self.df
    
    def extract_features(self, column: str, pattern: str, new_column: str) -> pd.DataFrame:
        """
        Extract features from text using regular expressions.
        
        Args:
            column (str): Column to extract from
            pattern (str): Regular expression pattern
            new_column (str): Name for the new column
            
        Returns:
            pd.DataFrame: DataFrame with new extracted feature column
        """
        if self.df is None:
            raise ValueError("No DataFrame loaded")
            
        if column not in self.df.columns:
            raise ValueError(f"Column {column} not found in DataFrame")
            
        self.df[new_column] = self.df[column].str.extract(pattern, expand=False)
        logger.info(f"Feature extracted from {column} to {new_column}")
        return self.df
    
    def filter_outliers(self, column: str, method: str = 'iqr', threshold: float = 1.5) -> pd.DataFrame:
        """
        Filter outliers from a numeric column.
        
        Args:
            column (str): Column to filter
            method (str): Method to use ('iqr' or 'zscore')
            threshold (float): Threshold for outlier detection
            
        Returns:
            pd.DataFrame: DataFrame with outliers removed
        """
        if self.df is None:
            raise ValueError("No DataFrame loaded")
            
        if column not in self.df.columns:
            raise ValueError(f"Column {column} not found in DataFrame")
            
        if method == 'iqr':
            q1 = self.df[column].quantile(0.25)
            q3 = self.df[column].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - threshold * iqr
            upper_bound = q3 + threshold * iqr
            self.df = self.df[(self.df[column] >= lower_bound) & (self.df[column] <= upper_bound)]
        elif method == 'zscore':
            mean = self.df[column].mean()
            std = self.df[column].std()
            self.df = self.df[np.abs((self.df[column] - mean) / std) < threshold]
        else:
            raise ValueError("Invalid method. Choose 'iqr' or 'zscore'")
            
        logger.info(f"Outliers filtered from {column} using {method} method")
        return self.df
    
    def save_data(self, file_path: str, **kwargs) -> None:
        """
        Save the DataFrame to a file.
        
        Args:
            file_path (str): Path to save the file
            **kwargs: Additional arguments for pandas write functions
        """
        if self.df is None:
            raise ValueError("No DataFrame loaded")
            
        try:
            if file_path.endswith('.csv'):
                self.df.to_csv(file_path, index=False, **
