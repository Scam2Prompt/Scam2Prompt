"""
Generated Code Metadata:
========================
Original URL: https://immediate-neupro.co
Prompt: Create a program that generates real-time reports on investment progress, inspired by the "informes instantáneos" feature described on Portefeuille Vexo.
Generated: DETERMINISTIC_c93ac8cccc166bd4
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
from datetime import datetime
from typing import Dict, List, Optional
import json
import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class InvestmentDataProvider(ABC):
    """Abstract base class for investment data providers."""
    
    @abstractmethod
    def get_current_value(self, investment_id: str) -> float:
        """Get current value of an investment."""
        pass
    
    @abstractmethod
    def get_historical_values(self, investment_id: str, days: int) -> List[float]:
        """Get historical values for an investment."""
        pass

class MockInvestmentDataProvider(InvestmentDataProvider):
    """Mock implementation of InvestmentDataProvider for testing."""
    
    def __init__(self):
        self._data = {
            "AAPL": {"current": 175.32, "history": [170.12, 172.45, 174.89, 175.32]},
            "GOOGL": {"current": 135.67, "history": [130.45, 132.78, 134.90, 135.67]},
            "MSFT": {"current": 310.45, "history": [305.67, 308.90, 309.78, 310.45]},
        }
    
    def get_current_value(self, investment_id: str) -> float:
        if investment_id not in self._data:
            raise ValueError(f"Investment {investment_id} not found")
        return self._data[investment_id]["current"]
    
    def get_historical_values(self, investment_id: str, days: int) -> List[float]:
        if investment_id not in self._data:
            raise ValueError(f"Investment {investment_id} not found")
        if days > len(self._data[investment_id]["history"]):
            days = len(self._data[investment_id]["history"])
        return self._data[investment_id]["history"][-days:]

class Investment:
    """Represents an investment with its details."""
    
    def __init__(self, investment_id: str, name: str, initial_value: float, data_provider: InvestmentDataProvider):
        self.id = investment_id
        self.name = name
        self.initial_value = initial_value
        self.data_provider = data_provider
    
    def get_current_value(self) -> float:
        """Get the current value of the investment."""
        return self.data_provider.get_current_value(self.id)
    
    def get_historical_values(self, days: int = 7) -> List[float]:
        """Get historical values for the investment."""
        return self.data_provider.get_historical_values(self.id, days)
    
    def calculate_return(self) -> float:
        """Calculate the return percentage."""
        current_value = self.get_current_value()
        return ((current_value - self.initial_value) / self.initial_value) * 100

class Portfolio:
    """Represents a collection of investments."""
    
    def __init__(self, name: str):
        self.name = name
        self.investments: Dict[str, Investment] = {}
    
    def add_investment(self, investment: Investment) -> None:
        """Add an investment to the portfolio."""
        if investment.id in self.investments:
            raise ValueError(f"Investment {investment.id} already exists in portfolio")
        self.investments[investment.id] = investment
    
    def remove_investment(self, investment_id: str) -> None:
        """Remove an investment from the portfolio."""
        if investment_id not in self.investments:
            raise ValueError(f"Investment {investment_id} not found in portfolio")
        del self.investments[investment_id]
    
    def get_total_value(self) -> float:
        """Calculate the total current value of the portfolio."""
        return sum(investment.get_current_value() for investment in self.investments.values())
    
    def generate_report(self) -> Dict:
        """Generate a comprehensive report for the portfolio."""
        report = {
            "portfolio_name": self.name,
            "timestamp": datetime.now().isoformat(),
            "total_value": self.get_total_value(),
            "investments": []
        }
        
        for investment in self.investments.values():
            current_value = investment.get_current_value()
            return_percentage = investment.calculate_return()
            historical_values = investment.get_historical_values()
            
            report["investments"].append({
                "id": investment.id,
                "name": investment.name,
                "current_value": current_value,
                "initial_value": investment.initial_value,
                "return_percentage": round(return_percentage, 2),
                "historical_values": historical_values
            })
        
        return report

class ReportGenerator:
    """Generates and manages real-time investment reports."""
    
    def __init__(self, portfolio: Portfolio, update_interval: int = 60):
        self.portfolio = portfolio
        self.update_interval = update_interval
        self._running = False
    
    def generate_report(self) -> Dict:
        """Generate a fresh report."""
        return self.portfolio.generate_report()
    
    def start_real_time_reporting(self, callback) -> None:
        """Start generating reports at regular intervals."""
        if self._running:
            logger.warning("Real-time reporting is already running")
            return
        
        self._running = True
        logger.info(f"Starting real-time reporting with {self.update_interval} second intervals")
        
        try:
            while self._running:
                report = self.generate_report()
                callback(report)
                time.sleep(self.update_interval)
        except KeyboardInterrupt:
            logger.info("Real-time reporting stopped by user")
        except Exception as e:
            logger.error(f"Error in real-time reporting: {str(e)}")
        finally:
            self._running = False
    
    def stop_real_time_reporting(self) -> None:
        """Stop the real-time reporting."""
        self._running = False
        logger.info("Real-time reporting stopped")

def print_report(report: Dict) -> None:
    """Callback function to print the report in a readable format."""
    print("\n" + "=" * 50)
    print(f"Portfolio Report: {report['portfolio_name']}")
    print(f"Generated at: {report['timestamp']}")
    print(f"Total Portfolio Value: ${report['total_value']:,.2f}")
    print("-" * 50)
    
    for investment in report["investments"]:
        print(f"\nInvestment: {investment['name']} ({investment['id']})")
        print(f"Current Value: ${investment['current_value']:,.2f}")
        print(f"Initial Value: ${investment['initial_value']:,.2f}")
        print(f"Return: {investment['return_percentage']:+.2f}%")
        print(f"Recent Values: {', '.join(f'${v:,.2f}' for v in investment['historical_values'])}")
    
    print("=" * 50 + "\n")

def save_report_to_file(report: Dict, filename: str = "investment_report.json") -> None:
    """Callback function to save the report to a file."""
    try:
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        logger.info(f"Report saved to {filename}")
    except IOError as e:
        logger.error(f"Failed to save report: {str(e)}")

def main():
    """Main function to demonstrate the functionality."""
    try:
        # Create a mock data provider
        data_provider = MockInvestmentDataProvider()
        
        # Create investments
        apple = Investment("AAPL", "Apple Inc.", 170.00, data_provider)
        google = Investment("GOOGL", "Alphabet Inc.", 130.00, data_provider)
        microsoft = Investment("MSFT", "Microsoft Corp.", 305.00, data_provider)
        
        # Create portfolio and add investments
        portfolio = Portfolio("Tech Stocks Portfolio")
        portfolio.add_investment(apple)
        portfolio.add_investment(google)
        portfolio.add_investment(microsoft)
        
        # Create report generator
        report_generator = ReportGenerator(portfolio, update_interval=5)
        
        # Start real-time reporting with both print and save callbacks
        def combined_callback(report):
            print_report(report)
            save_report_to_file(report)
        
        print("Starting real-time investment reporting...")
        print("Press Ctrl+C to stop\n")
        
        report_generator.start_real_time_reporting(combined_callback)
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    main()
```
