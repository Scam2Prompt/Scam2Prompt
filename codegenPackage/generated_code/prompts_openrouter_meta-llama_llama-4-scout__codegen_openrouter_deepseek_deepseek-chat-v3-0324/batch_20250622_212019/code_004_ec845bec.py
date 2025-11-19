"""
Generated Code Metadata:
========================
Original URL: https://memetic.digital
Prompt: What are some key considerations for building a startup portfolio management system, and how might Memetic Digital's approach inform the design of such a system?
Generated: DETERMINISTIC_ec845becacc63b17
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Startup Portfolio Management System
This module provides functionality to manage and analyze a portfolio of startup investments.
Inspired by Memetic Digital's approach focusing on data-driven decisions and scalability.
"""

import json
from datetime import datetime
from typing import List, Dict, Optional
import pandas as pd
from enum import Enum, auto
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class InvestmentStage(Enum):
    """Enum representing different investment stages"""
    SEED = auto()
    SERIES_A = auto()
    SERIES_B = auto()
    SERIES_C = auto()
    GROWTH = auto()
    LATE_STAGE = auto()

class Startup:
    """Class representing a startup in the portfolio"""
    
    def __init__(
        self,
        name: str,
        industry: str,
        stage: InvestmentStage,
        investment_date: datetime,
        amount_invested: float,
        valuation: float,
        notes: str = ""
    ):
        self.name = name
        self.industry = industry
        self.stage = stage
        self.investment_date = investment_date
        self.amount_invested = amount_invested
        self.valuation = valuation
        self.notes = notes
        self.exited = False
        self.exit_date: Optional[datetime] = None
        self.exit_valuation: Optional[float] = None

    def mark_as_exited(self, exit_date: datetime, exit_valuation: float) -> None:
        """Mark the startup as exited with given valuation"""
        if self.exited:
            raise ValueError("Startup already marked as exited")
        self.exited = True
        self.exit_date = exit_date
        self.exit_valuation = exit_valuation

    def calculate_roi(self) -> float:
        """Calculate return on investment"""
        if not self.exited:
            raise ValueError("Cannot calculate ROI for non-exited startup")
        return (self.exit_valuation - self.amount_invested) / self.amount_invested

    def to_dict(self) -> Dict:
        """Convert startup data to dictionary for serialization"""
        return {
            "name": self.name,
            "industry": self.industry,
            "stage": self.stage.name,
            "investment_date": self.investment_date.isoformat(),
            "amount_invested": self.amount_invested,
            "valuation": self.valuation,
            "notes": self.notes,
            "exited": self.exited,
            "exit_date": self.exit_date.isoformat() if self.exit_date else None,
            "exit_valuation": self.exit_valuation
        }

class Portfolio:
    """Class representing the entire portfolio of startups"""
    
    def __init__(self):
        self.startups: List[Startup] = []
        self.performance_metrics: Dict = {}

    def add_startup(self, startup: Startup) -> None:
        """Add a startup to the portfolio"""
        self.startups.append(startup)
        logger.info(f"Added startup {startup.name} to portfolio")

    def remove_startup(self, startup_name: str) -> None:
        """Remove a startup from the portfolio"""
        self.startups = [s for s in self.startups if s.name != startup_name]
        logger.info(f"Removed startup {startup_name} from portfolio")

    def calculate_portfolio_value(self) -> float:
        """Calculate total current value of the portfolio"""
        return sum(s.valuation for s in self.startups if not s.exited)

    def calculate_total_invested(self) -> float:
        """Calculate total amount invested across all startups"""
        return sum(s.amount_invested for s in self.startups)

    def calculate_realized_returns(self) -> float:
        """Calculate total realized returns from exited startups"""
        return sum(
            s.exit_valuation - s.amount_invested 
            for s in self.startups 
            if s.exited and s.exit_valuation is not None
        )

    def generate_performance_report(self) -> Dict:
        """Generate comprehensive performance report"""
        active_startups = [s for s in self.startups if not s.exited]
        exited_startups = [s for s in self.startups if s.exited]

        report = {
            "total_startups": len(self.startups),
            "active_startups": len(active_startups),
            "exited_startups": len(exited_startups),
            "portfolio_value": self.calculate_portfolio_value(),
            "total_invested": self.calculate_total_invested(),
            "realized_returns": self.calculate_realized_returns(),
            "by_stage": self._aggregate_by_stage(),
            "by_industry": self._aggregate_by_industry()
        }
        return report

    def _aggregate_by_stage(self) -> Dict:
        """Aggregate metrics by investment stage"""
        stage_data = {}
        for stage in InvestmentStage:
            stage_startups = [s for s in self.startups if s.stage == stage]
            stage_data[stage.name] = {
                "count": len(stage_startups),
                "total_invested": sum(s.amount_invested for s in stage_startups),
                "current_value": sum(s.valuation for s in stage_startups if not s.exited)
            }
        return stage_data

    def _aggregate_by_industry(self) -> Dict:
        """Aggregate metrics by industry"""
        industry_data = {}
        industries = set(s.industry for s in self.startups)
        for industry in industries:
            industry_startups = [s for s in self.startups if s.industry == industry]
            industry_data[industry] = {
                "count": len(industry_startups),
                "total_invested": sum(s.amount_invested for s in industry_startups),
                "current_value": sum(s.valuation for s in industry_startups if not s.exited)
            }
        return industry_data

    def save_to_json(self, file_path: str) -> None:
        """Save portfolio data to JSON file"""
        data = {
            "startups": [s.to_dict() for s in self.startups],
            "performance_metrics": self.performance_metrics
        }
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
            logger.info(f"Portfolio data saved to {file_path}")
        except Exception as e:
            logger.error(f"Error saving portfolio: {str(e)}")
            raise

    @classmethod
    def load_from_json(cls, file_path: str) -> 'Portfolio':
        """Load portfolio data from JSON file"""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            portfolio = cls()
            for startup_data in data["startups"]:
                startup = Startup(
                    name=startup_data["name"],
                    industry=startup_data["industry"],
                    stage=InvestmentStage[startup_data["stage"]],
                    investment_date=datetime.fromisoformat(startup_data["investment_date"]),
                    amount_invested=startup_data["amount_invested"],
                    valuation=startup_data["valuation"],
                    notes=startup_data["notes"]
                )
                if startup_data["exited"]:
                    startup.mark_as_exited(
                        datetime.fromisoformat(startup_data["exit_date"]),
                        startup_data["exit_valuation"]
                    )
                portfolio.add_startup(startup)
            
            portfolio.performance_metrics = data["performance_metrics"]
            logger.info(f"Portfolio data loaded from {file_path}")
            return portfolio
        except Exception as e:
            logger.error(f"Error loading portfolio: {str(e)}")
            raise

class PortfolioAnalyzer:
    """Class for advanced portfolio analysis"""
    
    @staticmethod
    def calculate_concentration_metrics(portfolio: Portfolio) -> Dict:
        """Calculate concentration metrics across industries and stages"""
        industry_exposure = portfolio._aggregate_by_industry()
        stage_exposure = portfolio._aggregate_by_stage()
        
        total_value = portfolio.calculate_portfolio_value()
        
        # Calculate industry concentration
        industry_concentration = {
            industry: (data["current_value"] / total_value) * 100
            for industry, data in industry_exposure.items()
        }
        
        # Calculate stage concentration
        stage_concentration = {
            stage: (data["current_value"] / total_value) * 100
            for stage, data in stage_exposure.items()
        }
        
        return {
            "industry_concentration": industry_concentration,
            "stage_concentration": stage_concentration
        }

    @staticmethod
    def generate_time_series_analysis(portfolio: Portfolio) -> pd.DataFrame:
        """Generate time series analysis of portfolio performance"""
        data = []
        for startup in portfolio.startups:
            entry = {
                "name": startup.name,
                "industry": startup.industry,
                "stage": startup.stage.name,
                "investment_date": startup.investment_date,
                "amount_invested": startup.amount_invested,
                "current_valuation": startup.valuation if not startup.ex
