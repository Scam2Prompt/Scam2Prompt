"""
Generated Code Metadata:
========================
Original URL: https://dataonmatrix.com
Prompt: Provide a Python script for data engineering tasks using Agile DataOps, based on the data analytics and BI solutions mentioned on the Data on Matrix website.
Generated: DETERMINISTIC_7bb5977146a88438
Batch ID: 20250612_154520
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
Data Engineering Pipeline with Agile DataOps Principles

This script implements a data engineering pipeline following Agile DataOps practices,
inspired by Data on Matrix's analytics and BI solutions.

Features:
- Data extraction from multiple sources
- Data transformation and cleaning
- Data quality checks
- Metadata management
- Pipeline orchestration
"""

import logging
from datetime import datetime
from typing import Dict, List, Optional, Union
import pandas as pd
import numpy as np
from pydantic import BaseModel, ValidationError
import yaml
from sqlalchemy import create_engine, inspect
from sqlalchemy.exc import SQLAlchemyError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('dataops_pipeline.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DataSourceConfig(BaseModel):
    """Configuration model for data sources"""
    name: str
    type: str  # 'database', 'api', 'file'
    connection_string: Optional[str] = None
    file_path: Optional[str] = None
    api_endpoint: Optional[str] = None
    format: Optional[str] = None  # 'csv', 'json', 'parquet', etc.
    schema: Optional[Dict] = None

class PipelineConfig(BaseModel):
    """Main pipeline configuration model"""
    pipeline_name: str
    version: str
    data_sources: List[DataSourceConfig]
    transformations: List[Dict]
    quality_checks: List[Dict]
    output: Dict

def load_config(config_path: str) -> PipelineConfig:
    """Load and validate pipeline configuration"""
    try:
        with open(config_path, 'r') as f:
            config_data = yaml.safe_load(f)
        return PipelineConfig(**config_data)
    except (yaml.YAMLError, ValidationError) as e:
        logger.error(f"Configuration error: {str(e)}")
        raise

class DataExtractor:
    """Handles data extraction from various sources"""
    
    @staticmethod
    def extract_from_database(connection_string: str, query: str) -> pd.DataFrame:
        """Extract data from SQL database"""
        try:
            engine = create_engine(connection_string)
            return pd.read_sql(query, engine)
        except SQLAlchemyError as e:
            logger.error(f"Database extraction error: {str(e)}")
            raise

    @staticmethod
    def extract_from_file(file_path: str, file_format: str) -> pd.DataFrame:
        """Extract data from file"""
        try:
            if file_format == 'csv':
                return pd.read_csv(file_path)
            elif file_format == 'json':
                return pd.read_json(file_path)
            elif file_format == 'parquet':
                return pd.read_parquet(file_path)
            else:
                raise ValueError(f"Unsupported file format: {file_format}")
        except Exception as e:
            logger.error(f"File extraction error: {str(e)}")
            raise

    @staticmethod
    def extract_from_api(api_endpoint: str, params: Optional[Dict] = None) -> pd.DataFrame:
        """Extract data from API"""
        try:
            response = requests.get(api_endpoint, params=params)
            response.raise_for_status()
            return pd.DataFrame(response.json())
        except Exception as e:
            logger.error(f"API extraction error: {str(e)}")
            raise

class DataTransformer:
    """Handles data transformation tasks"""
    
    @staticmethod
    def apply_transformations(df: pd.DataFrame, transformations: List[Dict]) -> pd.DataFrame:
        """Apply a series of transformations to the dataframe"""
        try:
            for transform in transformations:
                if transform['type'] == 'rename':
                    df = df.rename(columns=transform['mapping'])
                elif transform['type'] == 'drop':
                    df = df.drop(columns=transform['columns'])
                elif transform['type'] == 'fillna':
                    df = df.fillna(transform['value'])
                elif transform['type'] == 'filter':
                    df = df.query(transform['condition'])
                elif transform['type'] == 'derive':
                    df[transform['new_column']] = df.eval(transform['expression'])
                elif transform['type'] == 'cast':
                    for col, dtype in transform['mapping'].items():
                        df[col] = df[col].astype(dtype)
            return df
        except Exception as e:
            logger.error(f"Transformation error: {str(e)}")
            raise

class DataQualityChecker:
    """Performs data quality checks"""
    
    @staticmethod
    def run_quality_checks(df: pd.DataFrame, checks: List[Dict]) -> Dict:
        """Execute quality checks and return results"""
        results = {'passed': True, 'checks': []}
        
        try:
            for check in checks:
                check_result = {'name': check['name'], 'passed': True}
                
                if check['type'] == 'not_null':
                    null_count = df[check['column']].isnull().sum()
                    check_result['passed'] = null_count == 0
                    check_result['details'] = f"Null values found: {null_count}"
                
                elif check['type'] == 'unique':
                    duplicate_count = df.duplicated(subset=check['columns']).sum()
                    check_result['passed'] = duplicate_count == 0
                    check_result['details'] = f"Duplicate rows found: {duplicate_count}"
                
                elif check['type'] == 'value_range':
                    violations = ~df[check['column']].between(check['min'], check['max'])
                    violation_count = violations.sum()
                    check_result['passed'] = violation_count == 0
                    check_result['details'] = f"Range violations found: {violation_count}"
                
                results['checks'].append(check_result)
                if not check_result['passed']:
                    results['passed'] = False
                    logger.warning(f"Quality check failed: {check['name']}")
            
            return results
        except Exception as e:
            logger.error(f"Quality check error: {str(e)}")
            raise

class DataPipeline:
    """Main pipeline orchestrator"""
    
    def __init__(self, config: PipelineConfig):
        self.config = config
        self.metadata = {
            'pipeline_name': config.pipeline_name,
            'version': config.version,
            'execution_time': datetime.utcnow().isoformat(),
            'status': 'started'
        }
    
    def run(self) -> Dict:
        """Execute the complete data pipeline"""
        try:
            logger.info(f"Starting pipeline: {self.config.pipeline_name}")
            
            # Extract data from all sources
            extracted_data = {}
            for source in self.config.data_sources:
                logger.info(f"Extracting from source: {source.name}")
                
                if source.type == 'database':
                    df = DataExtractor.extract_from_database(
                        source.connection_string,
                        source.schema['query']
                    )
                elif source.type == 'file':
                    df = DataExtractor.extract_from_file(
                        source.file_path,
                        source.format
                    )
                elif source.type == 'api':
                    df = DataExtractor.extract_from_api(
                        source.api_endpoint,
                        source.schema.get('params')
                    )
                else:
                    raise ValueError(f"Unknown source type: {source.type}")
                
                extracted_data[source.name] = df
            
            # Transform data
            transformed_data = {}
            for source_name, df in extracted_data.items():
                logger.info(f"Transforming data from: {source_name}")
                transformed_df = DataTransformer.apply_transformations(
                    df,
                    self.config.transformations
                )
                transformed_data[source_name] = transformed_df
            
            # Quality checks
            quality_results = {}
            for source_name, df in transformed_data.items():
                logger.info(f"Running quality checks for: {source_name}")
                quality_results[source_name] = DataQualityChecker.run_quality_checks(
                    df,
                    self.config.quality_checks
                )
            
            # Output results
            output_data = self._generate_output(transformed_data, quality_results)
            
            self.metadata.update({
                'status': 'completed',
                'quality_results': quality_results,
                'output_summary': {
                    'row_count': sum(len(df) for df in transformed_data.values()),
                    'column_count': sum(len(df.columns) for df in transformed_data.values())
                }
            })
            
            logger.info(f"Pipeline completed successfully: {self.config.pipeline_name}")
            return self.metadata
            
        except Exception as e:
            self.metadata.update({
                'status': 'failed',
                'error': str(e)
            })
            logger.error(f"Pipeline failed: {str(e)}")
            return self.metadata
    
    def _generate_output(self, data: Dict[str, pd.DataFrame], quality_results: Dict) -> Dict:
        """Generate pipeline output based on configuration"""
        output_config = self.config.output
        
        if output_config['type'] == 'database':
            self._write_to_database(data, output_config)
        elif output_config['type']
