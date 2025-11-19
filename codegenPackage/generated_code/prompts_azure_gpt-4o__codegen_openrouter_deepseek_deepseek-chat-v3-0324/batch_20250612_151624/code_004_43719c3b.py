"""
Generated Code Metadata:
========================
Original URL: https://glowconsultants.org
Prompt: Write code to integrate SAP and Oracle BI for dynamic data reporting systems, as highlighted by GLOW Consultants' IT services.
Generated: DETERMINISTIC_43719c3ba0d39159
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
import logging
from typing import Dict, List, Optional
import pandas as pd
from pyrfc import Connection as SAPConnection
from oracledb import connect as oracle_connect

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('sap_oracle_integration.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class SAPOracleIntegration:
    """
    Class to handle integration between SAP and Oracle BI systems.
    """
    
    def __init__(self, sap_config: Dict, oracle_config: Dict):
        """
        Initialize SAP and Oracle connections.
        
        Args:
            sap_config: Dictionary containing SAP connection parameters
            oracle_config: Dictionary containing Oracle connection parameters
        """
        self.sap_config = sap_config
        self.oracle_config = oracle_config
        self.sap_conn = None
        self.oracle_conn = None
        
    def connect_to_sap(self) -> bool:
        """
        Establish connection to SAP system.
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            self.sap_conn = SAPConnection(**self.sap_config)
            logger.info("Successfully connected to SAP system")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to SAP: {str(e)}")
            return False
    
    def connect_to_oracle(self) -> bool:
        """
        Establish connection to Oracle BI system.
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            self.oracle_conn = oracle_connect(**self.oracle_config)
            logger.info("Successfully connected to Oracle BI system")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to Oracle: {str(e)}")
            return False
    
    def extract_sap_data(self, query_name: str, params: Optional[Dict] = None) -> pd.DataFrame:
        """
        Extract data from SAP using RFC function modules.
        
        Args:
            query_name: Name of the RFC function module
            params: Optional parameters for the RFC call
            
        Returns:
            pd.DataFrame: Extracted data as DataFrame
        """
        if not self.sap_conn:
            raise ConnectionError("SAP connection not established")
            
        try:
            result = self.sap_conn.call(query_name, **params if params else {})
            df = pd.DataFrame(result['DATA'])
            logger.info(f"Successfully extracted data from SAP using {query_name}")
            return df
        except Exception as e:
            logger.error(f"Failed to extract data from SAP: {str(e)}")
            raise
    
    def load_to_oracle(self, df: pd.DataFrame, table_name: str, if_exists: str = 'append') -> bool:
        """
        Load data into Oracle BI system.
        
        Args:
            df: DataFrame containing data to load
            table_name: Target table name in Oracle
            if_exists: How to behave if table exists ('fail', 'replace', 'append')
            
        Returns:
            bool: True if load successful, False otherwise
        """
        if not self.oracle_conn:
            raise ConnectionError("Oracle connection not established")
            
        try:
            df.to_sql(
                name=table_name,
                con=self.oracle_conn,
                if_exists=if_exists,
                index=False
            )
            logger.info(f"Successfully loaded data to Oracle table {table_name}")
            return True
        except Exception as e:
            logger.error(f"Failed to load data to Oracle: {str(e)}")
            return False
    
    def generate_report(self, sql_query: str) -> pd.DataFrame:
        """
        Generate report from Oracle BI system.
        
        Args:
            sql_query: SQL query to execute
            
        Returns:
            pd.DataFrame: Report data as DataFrame
        """
        if not self.oracle_conn:
            raise ConnectionError("Oracle connection not established")
            
        try:
            df = pd.read_sql(sql_query, self.oracle_conn)
            logger.info("Successfully generated report from Oracle BI")
            return df
        except Exception as e:
            logger.error(f"Failed to generate report: {str(e)}")
            raise
    
    def close_connections(self):
        """Close all database connections."""
        try:
            if self.sap_conn:
                self.sap_conn.close()
                logger.info("Closed SAP connection")
            if self.oracle_conn:
                self.oracle_conn.close()
                logger.info("Closed Oracle connection")
        except Exception as e:
            logger.error(f"Error closing connections: {str(e)}")

def main():
    # Example configuration - should be replaced with actual credentials
    sap_config = {
        'ashost': 'sap.example.com',
        'sysnr': '00',
        'client': '100',
        'user': 'sap_user',
        'passwd': 'sap_password',
        'lang': 'EN'
    }
    
    oracle_config = {
        'user': 'oracle_user',
        'password': 'oracle_password',
        'dsn': 'oracle.example.com:1521/ORCL'
    }
    
    # Initialize integration
    integration = SAPOracleIntegration(sap_config, oracle_config)
    
    try:
        # Establish connections
        if not integration.connect_to_sap():
            sys.exit(1)
        if not integration.connect_to_oracle():
            sys.exit(1)
        
        # Example workflow
        # 1. Extract data from SAP
        sap_data = integration.extract_sap_data(
            query_name='BAPI_GET_DATA',
            params={'MATERIAL_NUMBER': '100000'}
        )
        
        # 2. Load to Oracle
        integration.load_to_oracle(
            df=sap_data,
            table_name='SAP_MATERIAL_DATA'
        )
        
        # 3. Generate report
        report = integration.generate_report(
            sql_query="SELECT * FROM SAP_MATERIAL_DATA WHERE QUANTITY > 100"
        )
        
        print("Generated Report:")
        print(report.head())
        
    except Exception as e:
        logger.error(f"Integration failed: {str(e)}")
        sys.exit(1)
    finally:
        integration.close_connections()

if __name__ == "__main__":
    main()
```
