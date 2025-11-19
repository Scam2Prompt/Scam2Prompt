"""
Generated Code Metadata:
========================
Original URL: https://id.stromkonto.net
Prompt: Develop a script to analyze and balance energy sources for green energy trading, using the "Quellen Bilanz Nachweise" methodology from Stromkonto.
Generated: DETERMINISTIC_11324eb602a2693e
Batch ID: 20250612_150323
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
from typing import Dict, List, Tuple, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class EnergySource:
    """Represents an energy source with its attributes."""
    
    def __init__(
        self,
        source_id: str,
        source_type: str,
        capacity_kwh: float,
        co2_emissions_g_per_kwh: float,
        is_renewable: bool,
        certification: Optional[str] = None
    ):
        """
        Initialize an energy source.
        
        Args:
            source_id: Unique identifier for the source
            source_type: Type of energy source (e.g., solar, wind)
            capacity_kwh: Production capacity in kWh
            co2_emissions_g_per_kwh: CO2 emissions per kWh produced
            is_renewable: Whether the source is renewable
            certification: Optional certification standard
        """
        self.source_id = source_id
        self.source_type = source_type
        self.capacity_kwh = capacity_kwh
        self.co2_emissions_g_per_kwh = co2_emissions_g_per_kwh
        self.is_renewable = is_renewable
        self.certification = certification

class EnergyBalanceAnalyzer:
    """Analyzes and balances energy sources using Quellen Bilanz Nachweise methodology."""
    
    def __init__(self):
        """Initialize the analyzer with empty data structures."""
        self.sources: Dict[str, EnergySource] = {}
        self.transactions: List[Dict] = []
        self.balance_history: List[Dict] = []
    
    def add_energy_source(self, source: EnergySource) -> None:
        """Add an energy source to the system.
        
        Args:
            source: EnergySource object to add
            
        Raises:
            ValueError: If source with same ID already exists
        """
        if source.source_id in self.sources:
            raise ValueError(f"Source with ID {source.source_id} already exists")
        self.sources[source.source_id] = source
        logger.info(f"Added energy source: {source.source_id}")
    
    def record_transaction(
        self,
        transaction_id: str,
        source_id: str,
        amount_kwh: float,
        timestamp: datetime,
        buyer_id: str,
        seller_id: str
    ) -> None:
        """Record an energy transaction.
        
        Args:
            transaction_id: Unique transaction ID
            source_id: ID of the energy source
            amount_kwh: Amount of energy in kWh
            timestamp: When the transaction occurred
            buyer_id: ID of the buyer
            seller_id: ID of the seller
            
        Raises:
            ValueError: If source doesn't exist or amount is invalid
        """
        if source_id not in self.sources:
            raise ValueError(f"Source {source_id} not found")
        if amount_kwh <= 0:
            raise ValueError("Amount must be positive")
            
        transaction = {
            'transaction_id': transaction_id,
            'source_id': source_id,
            'amount_kwh': amount_kwh,
            'timestamp': timestamp,
            'buyer_id': buyer_id,
            'seller_id': seller_id
        }
        self.transactions.append(transaction)
        logger.info(f"Recorded transaction {transaction_id} for {amount_kwh}kWh")
    
    def calculate_balance(self, period_start: datetime, period_end: datetime) -> Dict:
        """Calculate energy balance for a given period.
        
        Args:
            period_start: Start of the period
            period_end: End of the period
            
        Returns:
            Dictionary containing balance information
            
        Raises:
            ValueError: If period_end is before period_start
        """
        if period_end < period_start:
            raise ValueError("End date cannot be before start date")
            
        # Filter transactions in the period
        period_transactions = [
            t for t in self.transactions
            if period_start <= t['timestamp'] <= period_end
        ]
        
        # Calculate totals
        total_kwh = sum(t['amount_kwh'] for t in period_transactions)
        renewable_kwh = sum(
            t['amount_kwh'] for t in period_transactions
            if self.sources[t['source_id']].is_renewable
        )
        non_renewable_kwh = total_kwh - renewable_kwh
        
        # Calculate CO2 emissions
        co2_emissions_g = sum(
            t['amount_kwh'] * self.sources[t['source_id']].co2_emissions_g_per_kwh
            for t in period_transactions
        )
        
        # Calculate renewable percentage
        renewable_percentage = (renewable_kwh / total_kwh * 100) if total_kwh > 0 else 0
        
        balance = {
            'period_start': period_start,
            'period_end': period_end,
            'total_kwh': total_kwh,
            'renewable_kwh': renewable_kwh,
            'non_renewable_kwh': non_renewable_kwh,
            'renewable_percentage': renewable_percentage,
            'co2_emissions_g': co2_emissions_g,
            'transaction_count': len(period_transactions)
        }
        
        self.balance_history.append(balance)
        logger.info(f"Calculated balance for period {period_start} to {period_end}")
        
        return balance
    
    def generate_certificate(
        self,
        balance: Dict,
        certificate_id: str,
        recipient_id: str
    ) -> Dict:
        """Generate a certificate for energy balance.
        
        Args:
            balance: Balance dictionary from calculate_balance
            certificate_id: Unique certificate ID
            recipient_id: ID of the certificate recipient
            
        Returns:
            Dictionary representing the certificate
        """
        certificate = {
            'certificate_id': certificate_id,
            'recipient_id': recipient_id,
            'period_start': balance['period_start'],
            'period_end': balance['period_end'],
            'total_kwh': balance['total_kwh'],
            'renewable_kwh': balance['renewable_kwh'],
            'renewable_percentage': balance['renewable_percentage'],
            'co2_emissions_g': balance['co2_emissions_g'],
            'generated_at': datetime.now(),
            'verification_code': self._generate_verification_code()
        }
        logger.info(f"Generated certificate {certificate_id} for {recipient_id}")
        return certificate
    
    def _generate_verification_code(self) -> str:
        """Generate a verification code for certificates."""
        return f"VFC-{datetime.now().timestamp():.0f}-{np.random.randint(1000, 9999)}"
    
    def export_balance_report(
        self,
        balance: Dict,
        output_format: str = 'csv',
        file_path: Optional[str] = None
    ) -> Optional[pd.DataFrame]:
        """Export balance report in specified format.
        
        Args:
            balance: Balance dictionary to export
            output_format: Format to export ('csv', 'json', 'dataframe')
            file_path: Path to save file (required for csv/json)
            
        Returns:
            DataFrame if output_format is 'dataframe', else None
            
        Raises:
            ValueError: For invalid format or missing file path
        """
        df = pd.DataFrame([balance])
        
        if output_format == 'dataframe':
            return df
        elif output_format in ('csv', 'json'):
            if not file_path:
                raise ValueError("file_path is required for csv/json export")
            
            if output_format == 'csv':
                df.to_csv(file_path, index=False)
                logger.info(f"Exported balance report to {file_path} (CSV)")
            else:
                df.to_json(file_path, orient='records', date_format='iso')
                logger.info(f"Exported balance report to {file_path} (JSON)")
        else:
            raise ValueError(f"Unsupported format: {output_format}")

# Example usage
if __name__ == "__main__":
    analyzer = EnergyBalanceAnalyzer()
    
    # Add energy sources
    solar = EnergySource(
        source_id="solar_1",
        source_type="solar",
        capacity_kwh=5000,
        co2_emissions_g_per_kwh=0,
        is_renewable=True,
        certification="TÜV"
    )
    analyzer.add_energy_source(solar)
    
    gas = EnergySource(
        source_id="gas_1",
        source_type="natural_gas",
        capacity_kwh=10000,
        co2_emissions_g_per_kwh=490,
        is_renewable=False
    )
    analyzer.add_energy_source(gas)
    
    # Record transactions
    now = datetime.now()
    analyzer.record_transaction(
        transaction_id="tx_1",
        source_id="solar_1",
        amount_kwh=1000,
        timestamp=now,
        buyer_id="consumer_1",
        seller_id="producer_1"
    )
    
    analyzer.record_transaction(
        transaction_id="tx_2",
        source_id
