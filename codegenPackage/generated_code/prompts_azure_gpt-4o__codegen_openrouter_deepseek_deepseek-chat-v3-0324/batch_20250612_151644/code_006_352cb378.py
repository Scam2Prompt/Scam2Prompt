"""
Generated Code Metadata:
========================
Original URL: https://complyaml.com
Prompt: Write code to analyze transaction data for AML compliance in real estate businesses, leveraging principles from ComplyAML's consultancy services.
Generated: DETERMINISTIC_352cb3786cbea284
Batch ID: 20250612_151644
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
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple
import logging
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('aml_compliance.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class RiskLevel(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class TransactionType(Enum):
    PURCHASE = 1
    SALE = 2
    LEASE = 3
    TRANSFER = 4

class TransactionAnalyzer:
    """
    Analyzes real estate transactions for AML compliance risks.
    """
    
    def __init__(self, config: Optional[Dict] = None):
        """
        Initialize the analyzer with optional configuration.
        
        Args:
            config: Dictionary containing configuration parameters
        """
        self.config = config or {
            'high_risk_threshold': 1000000,  # USD
            'medium_risk_threshold': 500000,  # USD
            'suspicious_countries': ['IR', 'KP', 'SY', 'CU', 'SD'],
            'pep_check': True,
            'watchlist_check': True
        }
        self.watchlist = self._load_watchlist()
        
    def _load_watchlist(self) -> pd.DataFrame:
        """
        Load watchlist data from file or database.
        
        Returns:
            DataFrame containing watchlist entries
        """
        try:
            # In production, this would connect to a database or API
            return pd.DataFrame(columns=['name', 'country', 'type'])
        except Exception as e:
            logger.error(f"Failed to load watchlist: {str(e)}")
            return pd.DataFrame()
    
    def analyze_transactions(self, transactions: pd.DataFrame) -> pd.DataFrame:
        """
        Analyze a batch of transactions for AML risks.
        
        Args:
            transactions: DataFrame containing transaction data
            
        Returns:
            DataFrame with risk assessments for each transaction
        """
        if transactions.empty:
            logger.warning("Empty transaction dataset provided")
            return pd.DataFrame()
            
        try:
            # Apply risk assessment functions
            transactions['amount_risk'] = transactions['amount'].apply(self._assess_amount_risk)
            transactions['country_risk'] = transactions['country'].apply(self._assess_country_risk)
            transactions['pep_risk'] = transactions['buyer_name'].apply(self._check_pep)
            transactions['watchlist_risk'] = transactions['buyer_name'].apply(self._check_watchlist)
            
            # Calculate overall risk
            transactions['overall_risk'] = transactions.apply(self._calculate_overall_risk, axis=1)
            
            # Flag suspicious transactions
            transactions['is_suspicious'] = transactions['overall_risk'] >= RiskLevel.HIGH.value
            
            return transactions
            
        except Exception as e:
            logger.error(f"Error analyzing transactions: {str(e)}")
            raise
    
    def _assess_amount_risk(self, amount: float) -> int:
        """
        Assess risk based on transaction amount.
        
        Args:
            amount: Transaction amount in USD
            
        Returns:
            RiskLevel enum value
        """
        if amount >= self.config['high_risk_threshold']:
            return RiskLevel.HIGH.value
        elif amount >= self.config['medium_risk_threshold']:
            return RiskLevel.MEDIUM.value
        return RiskLevel.LOW.value
    
    def _assess_country_risk(self, country: str) -> int:
        """
        Assess risk based on country.
        
        Args:
            country: 2-letter country code
            
        Returns:
            RiskLevel enum value
        """
        if country in self.config['suspicious_countries']:
            return RiskLevel.HIGH.value
        return RiskLevel.LOW.value
    
    def _check_pep(self, name: str) -> int:
        """
        Check if individual is a politically exposed person (PEP).
        
        Args:
            name: Individual's name
            
        Returns:
            RiskLevel enum value
        """
        if not self.config['pep_check']:
            return RiskLevel.LOW.value
            
        # In production, this would query a PEP database
        return RiskLevel.LOW.value
    
    def _check_watchlist(self, name: str) -> int:
        """
        Check if individual is on watchlist.
        
        Args:
            name: Individual's name
            
        Returns:
            RiskLevel enum value
        """
        if not self.config['watchlist_check'] or self.watchlist.empty:
            return RiskLevel.LOW.value
            
        # Simple name matching - in production would use fuzzy matching
        if name in self.watchlist['name'].values:
            return RiskLevel.HIGH.value
        return RiskLevel.LOW.value
    
    def _calculate_overall_risk(self, row: pd.Series) -> int:
        """
        Calculate overall risk score based on individual risk factors.
        
        Args:
            row: Transaction data row
            
        Returns:
            Overall risk score (1-3)
        """
        risks = [
            row['amount_risk'],
            row['country_risk'],
            row['pep_risk'],
            row['watchlist_risk']
        ]
        return max(risks)
    
    def generate_sar_report(self, suspicious_transactions: pd.DataFrame) -> Dict:
        """
        Generate a Suspicious Activity Report (SAR) for filing.
        
        Args:
            suspicious_transactions: DataFrame of suspicious transactions
            
        Returns:
            Dictionary containing SAR data
        """
        if suspicious_transactions.empty:
            return {}
            
        try:
            report = {
                'report_date': datetime.now().isoformat(),
                'total_transactions': len(suspicious_transactions),
                'total_amount': suspicious_transactions['amount'].sum(),
                'transactions': suspicious_transactions.to_dict('records')
            }
            return report
        except Exception as e:
            logger.error(f"Error generating SAR report: {str(e)}")
            raise

class RealTimeMonitor:
    """
    Monitors real-time transaction streams for AML compliance.
    """
    
    def __init__(self, analyzer: TransactionAnalyzer):
        self.analyzer = analyzer
        self.suspicious_activities = []
        
    def process_transaction(self, transaction: Dict) -> Optional[Dict]:
        """
        Process a single transaction in real-time.
        
        Args:
            transaction: Dictionary containing transaction data
            
        Returns:
            Risk assessment if suspicious, None otherwise
        """
        try:
            df = pd.DataFrame([transaction])
            analyzed = self.analyzer.analyze_transactions(df)
            
            if analyzed.iloc[0]['is_suspicious']:
                self.suspicious_activities.append(transaction)
                return {
                    'transaction_id': transaction.get('id'),
                    'risk_level': analyzed.iloc[0]['overall_risk'],
                    'reasons': self._get_risk_reasons(analyzed.iloc[0])
                }
            return None
        except Exception as e:
            logger.error(f"Error processing transaction: {str(e)}")
            return None
    
    def _get_risk_reasons(self, transaction: pd.Series) -> List[str]:
        """
        Get reasons for risk assessment.
        
        Args:
            transaction: Transaction data row
            
        Returns:
            List of risk reasons
        """
        reasons = []
        if transaction['amount_risk'] == RiskLevel.HIGH.value:
            reasons.append(f"High amount: ${transaction['amount']}")
        if transaction['country_risk'] == RiskLevel.HIGH.value:
            reasons.append(f"High-risk country: {transaction['country']}")
        if transaction['pep_risk'] == RiskLevel.HIGH.value:
            reasons.append("Politically exposed person")
        if transaction['watchlist_risk'] == RiskLevel.HIGH.value:
            reasons.append("Match found in watchlist")
        return reasons
    
    def generate_daily_report(self) -> Dict:
        """
        Generate daily suspicious activity report.
        
        Returns:
            Dictionary containing daily report data
        """
        if not self.suspicious_activities:
            return {}
            
        try:
            df = pd.DataFrame(self.suspicious_activities)
            report = self.analyzer.generate_sar_report(df)
            self.suspicious_activities = []  # Reset after reporting
            return report
        except Exception as e:
            logger.error(f"Error generating daily report: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    # Sample transaction data
    sample_data = {
        'id': [1, 2, 3],
        'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'amount': [250000, 1500000, 750000],
        'country': ['US', 'IR', 'CA'],
        'buyer_name': ['John Doe', 'Ali Reza', 'Jane Smith'],
        'property_type': ['Residential', 'Commercial', 'Land']
    }
    
    analyzer = TransactionAnalyzer()
    transactions_df =
