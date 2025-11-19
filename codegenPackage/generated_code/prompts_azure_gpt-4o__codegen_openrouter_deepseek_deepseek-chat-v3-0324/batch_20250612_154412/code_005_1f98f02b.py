"""
Generated Code Metadata:
========================
Original URL: https://invictacobrancas.com.br
Prompt: Provide code examples for implementing a debt conversion agent that tracks daily conversions and calculates engagement metrics, inspired by Invicta Cobranças' approach.
Generated: DETERMINISTIC_1f98f02b30d8567d
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from dataclasses import dataclass
from typing import List, Dict, Optional
import csv
import json
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class Debt:
    """Represents a debt to be converted."""
    debt_id: str
    original_amount: float
    current_amount: float
    debtor_name: str
    status: str  # e.g., "active", "converted", "written_off"
    conversion_date: Optional[datetime.date] = None

@dataclass
class ConversionRecord:
    """Tracks a single conversion event."""
    conversion_id: str
    debt_id: str
    converted_amount: float
    conversion_date: datetime.date
    agent_id: str
    conversion_type: str  # e.g., "cash", "installment", "settlement"

class DebtConversionAgent:
    """Manages debt conversions and calculates engagement metrics."""
    
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.conversion_records: List[ConversionRecord] = []
        self.debts: Dict[str, Debt] = {}
        
    def add_debt(self, debt: Debt) -> None:
        """Add a debt to be tracked."""
        if debt.debt_id in self.debts:
            raise ValueError(f"Debt with ID {debt.debt_id} already exists")
        self.debts[debt.debt_id] = debt
        
    def record_conversion(self, conversion: ConversionRecord) -> None:
        """Record a conversion event and update the associated debt."""
        if conversion.debt_id not in self.debts:
            raise ValueError(f"Debt with ID {conversion.debt_id} not found")
            
        debt = self.debts[conversion.debt_id]
        
        if conversion.converted_amount > debt.current_amount:
            raise ValueError("Converted amount exceeds current debt amount")
            
        debt.current_amount -= conversion.converted_amount
        if debt.current_amount <= 0:
            debt.status = "converted"
        debt.conversion_date = conversion.conversion_date
        
        self.conversion_records.append(conversion)
        logger.info(f"Recorded conversion {conversion.conversion_id} for debt {debt.debt_id}")
        
    def get_daily_conversions(self, date: datetime.date) -> List[ConversionRecord]:
        """Get all conversions for a specific date."""
        return [
            record for record in self.conversion_records 
            if record.conversion_date == date
        ]
        
    def calculate_daily_engagement(self, date: datetime.date) -> Dict[str, float]:
        """Calculate engagement metrics for a specific day."""
        daily_conversions = self.get_daily_conversions(date)
        total_converted = sum(c.converted_amount for c in daily_conversions)
        conversion_count = len(daily_conversions)
        
        return {
            "date": date.isoformat(),
            "total_converted": total_converted,
            "conversion_count": conversion_count,
            "average_conversion": total_converted / conversion_count if conversion_count else 0,
            "agent_id": self.agent_id
        }
        
    def save_conversions_to_csv(self, file_path: Path) -> None:
        """Save conversion records to a CSV file."""
        try:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=vars(ConversionRecord("", "", 0, datetime.date.today(), "", "")).keys())
                writer.writeheader()
                for record in self.conversion_records:
                    writer.writerow(vars(record))
            logger.info(f"Saved {len(self.conversion_records)} conversions to {file_path}")
        except Exception as e:
            logger.error(f"Failed to save conversions to CSV: {e}")
            raise
            
    def load_conversions_from_csv(self, file_path: Path) -> None:
        """Load conversion records from a CSV file."""
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    conversion = ConversionRecord(
                        conversion_id=row['conversion_id'],
                        debt_id=row['debt_id'],
                        converted_amount=float(row['converted_amount']),
                        conversion_date=datetime.date.fromisoformat(row['conversion_date']),
                        agent_id=row['agent_id'],
                        conversion_type=row['conversion_type']
                    )
                    self.conversion_records.append(conversion)
            logger.info(f"Loaded {len(self.conversion_records)} conversions from {file_path}")
        except Exception as e:
            logger.error(f"Failed to load conversions from CSV: {e}")
            raise
            
    def generate_engagement_report(self, start_date: datetime.date, end_date: datetime.date) -> Dict:
        """Generate an engagement report for a date range."""
        report = {
            "agent_id": self.agent_id,
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "daily_metrics": [],
            "total_converted": 0,
            "total_conversions": 0
        }
        
        current_date = start_date
        while current_date <= end_date:
            daily_metrics = self.calculate_daily_engagement(current_date)
            report["daily_metrics"].append(daily_metrics)
            report["total_converted"] += daily_metrics["total_converted"]
            report["total_conversions"] += daily_metrics["conversion_count"]
            current_date += datetime.timedelta(days=1)
            
        return report
    
    def save_engagement_report(self, report: Dict, file_path: Path) -> None:
        """Save engagement report to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump(report, file, indent=2)
            logger.info(f"Saved engagement report to {file_path}")
        except Exception as e:
            logger.error(f"Failed to save engagement report: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Initialize agent
    agent = DebtConversionAgent(agent_id="agent_123")
    
    # Add some debts
    debt1 = Debt(
        debt_id="debt_001",
        original_amount=1000.0,
        current_amount=1000.0,
        debtor_name="John Doe",
        status="active"
    )
    debt2 = Debt(
        debt_id="debt_002",
        original_amount=500.0,
        current_amount=500.0,
        debtor_name="Jane Smith",
        status="active"
    )
    agent.add_debt(debt1)
    agent.add_debt(debt2)
    
    # Record some conversions
    today = datetime.date.today()
    conversion1 = ConversionRecord(
        conversion_id="conv_001",
        debt_id="debt_001",
        converted_amount=300.0,
        conversion_date=today,
        agent_id="agent_123",
        conversion_type="cash"
    )
    conversion2 = ConversionRecord(
        conversion_id="conv_002",
        debt_id="debt_002",
        converted_amount=200.0,
        conversion_date=today,
        agent_id="agent_123",
        conversion_type="installment"
    )
    agent.record_conversion(conversion1)
    agent.record_conversion(conversion2)
    
    # Generate and save reports
    report = agent.generate_engagement_report(today, today)
    print(json.dumps(report, indent=2))
    
    # Save data to files
    agent.save_conversions_to_csv(Path("conversions.csv"))
    agent.save_engagement_report(report, Path("engagement_report.json"))
```
