"""
Generated Code Metadata:
========================
Original URL: https://profit8lue.com
Prompt: What are the key financial metrics that companies should monitor to ensure sustainable growth?
Generated: DETERMINISTIC_5d3dc0740aae0885
Batch ID: 20250622_212052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Financial Metrics Monitoring System

This module defines key financial metrics that companies should monitor 
to ensure sustainable growth. It includes functions to calculate and analyze
these metrics from financial data.
"""

from typing import Dict, Union, Optional
from dataclasses import dataclass
import numpy as np

@dataclass
class FinancialMetrics:
    """Class to store and calculate key financial metrics."""
    revenue: float
    net_income: float
    total_assets: float
    total_liabilities: float
    current_assets: float
    current_liabilities: float
    operating_cash_flow: float
    free_cash_flow: float
    total_debt: float
    ebitda: float
    shares_outstanding: float
    stock_price: Optional[float] = None

    def gross_profit_margin(self, cost_of_goods_sold: float) -> float:
        """Calculate gross profit margin."""
        gross_profit = self.revenue - cost_of_goods_sold
        return (gross_profit / self.revenue) * 100 if self.revenue != 0 else 0

    def net_profit_margin(self) -> float:
        """Calculate net profit margin."""
        return (self.net_income / self.revenue) * 100 if self.revenue != 0 else 0

    def current_ratio(self) -> float:
        """Calculate current ratio (liquidity metric)."""
        return self.current_assets / self.current_liabilities if self.current_liabilities != 0 else 0

    def quick_ratio(self, inventory: float) -> float:
        """Calculate quick ratio (acid-test ratio)."""
        quick_assets = self.current_assets - inventory
        return quick_assets / self.current_liabilities if self.current_liabilities != 0 else 0

    def debt_to_equity_ratio(self) -> float:
        """Calculate debt-to-equity ratio."""
        equity = self.total_assets - self.total_liabilities
        return self.total_liabilities / equity if equity != 0 else 0

    def return_on_assets(self) -> float:
        """Calculate return on assets (ROA)."""
        return (self.net_income / self.total_assets) * 100 if self.total_assets != 0 else 0

    def return_on_equity(self) -> float:
        """Calculate return on equity (ROE)."""
        equity = self.total_assets - self.total_liabilities
        return (self.net_income / equity) * 100 if equity != 0 else 0

    def operating_cash_flow_ratio(self) -> float:
        """Calculate operating cash flow ratio."""
        return self.operating_cash_flow / self.current_liabilities if self.current_liabilities != 0 else 0

    def free_cash_flow_yield(self) -> float:
        """Calculate free cash flow yield."""
        return (self.free_cash_flow / self.revenue) * 100 if self.revenue != 0 else 0

    def interest_coverage_ratio(self, interest_expense: float) -> float:
        """Calculate interest coverage ratio."""
        return self.ebitda / interest_expense if interest_expense != 0 else 0

    def earnings_per_share(self) -> float:
        """Calculate earnings per share (EPS)."""
        return self.net_income / self.shares_outstanding if self.shares_outstanding != 0 else 0

    def price_to_earnings_ratio(self) -> Union[float, str]:
        """Calculate price-to-earnings ratio (P/E)."""
        if self.stock_price is None:
            return "Stock price not provided"
        eps = self.earnings_per_share()
        return self.stock_price / eps if eps != 0 else 0

    def get_all_metrics(self, cost_of_goods_sold: float, inventory: float, interest_expense: float) -> Dict[str, float]:
        """Calculate and return all key financial metrics."""
        return {
            "gross_profit_margin": self.gross_profit_margin(cost_of_goods_sold),
            "net_profit_margin": self.net_profit_margin(),
            "current_ratio": self.current_ratio(),
            "quick_ratio": self.quick_ratio(inventory),
            "debt_to_equity_ratio": self.debt_to_equity_ratio(),
            "return_on_assets": self.return_on_assets(),
            "return_on_equity": self.return_on_equity(),
            "operating_cash_flow_ratio": self.operating_cash_flow_ratio(),
            "free_cash_flow_yield": self.free_cash_flow_yield(),
            "interest_coverage_ratio": self.interest_coverage_ratio(interest_expense),
            "earnings_per_share": self.earnings_per_share(),
            "price_to_earnings_ratio": self.price_to_earnings_ratio()
        }

def analyze_metrics(metrics: Dict[str, float]) -> Dict[str, str]:
    """Analyze financial metrics against common benchmarks."""
    analysis = {}
    
    benchmarks = {
        "gross_profit_margin": (20, "Healthy"),
        "net_profit_margin": (10, "Healthy"),
        "current_ratio": (1.5, "Good short-term financial health"),
        "quick_ratio": (1.0, "Good liquidity position"),
        "debt_to_equity_ratio": (2.0, "Moderate leverage"),
        "return_on_assets": (5, "Good asset utilization"),
        "return_on_equity": (15, "Good return to shareholders"),
        "operating_cash_flow_ratio": (1.0, "Healthy cash flow coverage"),
        "free_cash_flow_yield": (5, "Good cash generation"),
        "interest_coverage_ratio": (3, "Comfortable interest payment ability")
    }
    
    for metric, value in metrics.items():
        if metric in benchmarks:
            benchmark_value, description = benchmarks[metric]
            if isinstance(value, str):  # Handle cases like P/E when stock price isn't provided
                analysis[metric] = value
            else:
                if value >= benchmark_value:
                    analysis[metric] = f"Strong ({value:.2f} >= {benchmark_value}) - {description}"
                else:
                    analysis[metric] = f"Weak ({value:.2f} < {benchmark_value}) - Needs improvement"
        else:
            analysis[metric] = f"Value: {value:.2f} (No benchmark available)"
    
    return analysis
```
