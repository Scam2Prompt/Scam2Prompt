"""
Generated Code Metadata:
========================
Original URL: https://labiqc.com
Prompt: How can I integrate LIMS (Laboratory Information Management System) data with quality control software using Python?
Generated: DETERMINISTIC_abfba28d9ea3a716
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from typing import Dict, List, Optional
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, exc
import requests
from requests.exceptions import RequestException
from pydantic import BaseModel, ValidationError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class LIMSDataModel(BaseModel):
    sample_id: str
    test_name: str
    result_value: float
    unit: str
    date_analyzed: str
    analyst: str
    status: str

class QCDataModel(BaseModel):
    sample_id: str
    parameter: str
    measured_value: float
    expected_value: float
    deviation: float
    status: str

class LIMSIntegration:
    def __init__(self, lims_config: Dict, qc_config: Dict):
        """
        Initialize LIMS integration with configuration for both LIMS and QC systems.
        
        Args:
            lims_config: Dictionary containing LIMS connection parameters
            qc_config: Dictionary containing QC system connection parameters
        """
        self.lims_config = lims_config
        self.qc_config = qc_config
        self.lims_engine = None
        self.qc_engine = None
        
    def connect_to_lims(self) -> bool:
        """Establish connection to LIMS database."""
        try:
            connection_string = (
                f"postgresql://{self.lims_config['username']}:{self.lims_config['password']}@"
                f"{self.lims_config['host']}:{self.lims_config['port']}/{self.lims_config['database']}"
            )
            self.lims_engine = create_engine(connection_string)
            logger.info("Successfully connected to LIMS database")
            return True
        except exc.SQLAlchemyError as e:
            logger.error(f"Error connecting to LIMS database: {str(e)}")
            return False
            
    def connect_to_qc_system(self) -> bool:
        """Establish connection to QC system."""
        try:
            connection_string = (
                f"mysql://{self.qc_config['username']}:{self.qc_config['password']}@"
                f"{self.qc_config['host']}:{self.qc_config['port']}/{self.qc_config['database']}"
            )
            self.qc_engine = create_engine(connection_string)
            logger.info("Successfully connected to QC system")
            return True
        except exc.SQLAlchemyError as e:
            logger.error(f"Error connecting to QC system: {str(e)}")
            return False
            
    def fetch_lims_data(self, query: str) -> Optional[pd.DataFrame]:
        """Fetch data from LIMS system."""
        if not self.lims_engine:
            logger.error("LIMS connection not established")
            return None
            
        try:
            df = pd.read_sql(query, self.lims_engine)
            logger.info(f"Retrieved {len(df)} records from LIMS")
            return df
        except exc.SQLAlchemyError as e:
            logger.error(f"Error fetching LIMS data: {str(e)}")
            return None
            
    def validate_lims_data(self, data: pd.DataFrame) -> List[LIMSDataModel]:
        """Validate LIMS data against expected schema."""
        validated_data = []
        errors = []
        
        for _, row in data.iterrows():
            try:
                validated_item = LIMSDataModel(**row.to_dict())
                validated_data.append(validated_item)
            except ValidationError as e:
                errors.append(f"Row {_}: {str(e)}")
                
        if errors:
            logger.warning(f"Validation errors found: {errors}")
            
        return validated_data
        
    def transform_to_qc_format(self, lims_data: List[LIMSDataModel]) -> List[QCDataModel]:
        """Transform LIMS data to QC system format."""
        qc_data = []
        
        for item in lims_data:
            try:
                qc_item = QCDataModel(
                    sample_id=item.sample_id,
                    parameter=item.test_name,
                    measured_value=item.result_value,
                    expected_value=self._get_expected_value(item.test_name),
                    deviation=self._calculate_deviation(
                        item.result_value,
                        self._get_expected_value(item.test_name)
                    ),
                    status=self._determine_status(
                        item.result_value,
                        self._get_expected_value(item.test_name)
                    )
                )
                qc_data.append(qc_item)
            except Exception as e:
                logger.error(f"Error transforming data for sample {item.sample_id}: {str(e)}")
                
        return qc_data
        
    def _get_expected_value(self, test_name: str) -> float:
        """Get expected value for a test (mock implementation)."""
        # In a real implementation, this would query reference values
        expected_values = {
            "pH": 7.0,
            "Conductivity": 500.0,
            "Turbidity": 1.0
        }
        return expected_values.get(test_name, 0.0)
        
    def _calculate_deviation(self, measured: float, expected: float) -> float:
        """Calculate deviation between measured and expected values."""
        if expected == 0:
            return 0.0
        return ((measured - expected) / expected) * 100
        
    def _determine_status(self, measured: float, expected: float) -> str:
        """Determine QC status based on deviation."""
        deviation = self._calculate_deviation(measured, expected)
        
        if abs(deviation) < 5:
            return "PASS"
        elif abs(deviation) < 10:
            return "WARNING"
        else:
            return "FAIL"
            
    def send_to_qc_system(self, qc_data: List[QCDataModel]) -> bool:
        """Send transformed data to QC system."""
        if not self.qc_engine:
            logger.error("QC system connection not established")
            return False
            
        try:
            df = pd.DataFrame([item.dict() for item in qc_data])
            df.to_sql(
                'qc_results',
                self.qc_engine,
                if_exists='append',
                index=False
            )
            logger.info(f"Successfully sent {len(df)} records to QC system")
            return True
        except exc.SQLAlchemyError as e:
            logger.error(f"Error sending data to QC system: {str(e)}")
            return False
            
    def integrate(self, lims_query: str) -> bool:
        """Full integration pipeline."""
        if not self.connect_to_lims():
            return False
            
        if not self.connect_to_qc_system():
            return False
            
        lims_df = self.fetch_lims_data(lims_query)
        if lims_df is None:
            return False
            
        validated_data = self.validate_lims_data(lims_df)
        if not validated_data:
            logger.error("No valid data to process")
            return False
            
        qc_data = self.transform_to_qc_format(validated_data)
        if not qc_data:
            logger.error("No QC data generated")
            return False
            
        return self.send_to_qc_system(qc_data)

class RESTLIMSIntegration:
    def __init__(self, lims_api_config: Dict, qc_api_config: Dict):
        """
        Initialize REST-based LIMS integration.
        
        Args:
            lims_api_config: Dictionary containing LIMS API configuration
            qc_api_config: Dictionary containing QC API configuration
        """
        self.lims_api_config = lims_api_config
        self.qc_api_config = qc_api_config
        
    def fetch_lims_data(self, endpoint: str, params: Dict = None) -> Optional[List[Dict]]:
        """Fetch data from LIMS REST API."""
        url = f"{self.lims_api_config['base_url']}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.lims_api_config['api_key']}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.get(
                url,
                headers=headers,
                params=params,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            logger.error(f"Error fetching data from LIMS API: {str(e)}")
            return None
            
    def send_to_qc_system(self, qc_data: List[Dict]) -> bool:
        """Send data to QC system via REST API."""
        url = f"{self.qc_api_config['base_url']}/api/qc/results"
        headers = {
            "Authorization": f"Bearer {self.qc_api_config['api_key']}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(
                url,
                json=qc_data,
                headers=headers,
                timeout=30
            )
            response.raise_for_status()
            return True
        except RequestException as e:
            logger.error(f"Error sending data to QC API: {str(e
