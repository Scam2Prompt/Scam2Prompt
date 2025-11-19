"""
Generated Code Metadata:
========================
Original URL: https://immediatecode.app
Prompt: "Design a risk management system for investment portfolios, incorporating features such as stop-loss orders and position sizing, and provide an example code in a programming language of choice."
Generated: DETERMINISTIC_4c40719b29f89ce3
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# risk_management_system.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RiskLevel(Enum):
    """Risk levels for investment portfolios"""
    CONSERVATIVE = 1
    MODERATE = 2
    AGGRESSIVE = 3

@dataclass
class Asset:
    """Represents an asset in the portfolio"""
    symbol: str
    current_price: float
    quantity: int

class RiskManagementSystem:
    """Manages risk for investment portfolios"""

    def __init__(self, risk_level: RiskLevel, stop_loss_percentage: float, position_size: float):
        """
        Initializes the risk management system

        Args:
        - risk_level (RiskLevel): The risk level for the portfolio
        - stop_loss_percentage (float): The percentage for stop-loss orders
        - position_size (float): The size of each position
        """
        self.risk_level = risk_level
        self.stop_loss_percentage = stop_loss_percentage
        self.position_size = position_size
        self.portfolio: Dict[str, Asset] = {}

    def add_asset(self, asset: Asset):
        """Adds an asset to the portfolio"""
        self.portfolio[asset.symbol] = asset

    def remove_asset(self, symbol: str):
        """Removes an asset from the portfolio"""
        if symbol in self.portfolio:
            del self.portfolio[symbol]
        else:
            logger.warning(f"Asset {symbol} not found in portfolio")

    def calculate_stop_loss(self, asset: Asset) -> float:
        """
        Calculates the stop-loss price for an asset

        Args:
        - asset (Asset): The asset to calculate the stop-loss price for

        Returns:
        - float: The stop-loss price
        """
        return asset.current_price * (1 - self.stop_loss_percentage / 100)

    def calculate_position_size(self, asset: Asset) -> float:
        """
        Calculates the position size for an asset

        Args:
        - asset (Asset): The asset to calculate the position size for

        Returns:
        - float: The position size
        """
        return self.position_size

    def manage_risk(self):
        """Manages risk for all assets in the portfolio"""
        for asset in self.portfolio.values():
            stop_loss_price = self.calculate_stop_loss(asset)
            position_size = self.calculate_position_size(asset)
            logger.info(f"Asset {asset.symbol}: Stop-loss price = {stop_loss_price:.2f}, Position size = {position_size:.2f}")

def main():
    # Create a risk management system
    risk_management_system = RiskManagementSystem(
        risk_level=RiskLevel.MODERATE,
        stop_loss_percentage=10.0,
        position_size=1000.0
    )

    # Create assets
    assets: List[Asset] = [
        Asset("AAPL", 150.0, 10),
        Asset("GOOGL", 2500.0, 5),
        Asset("MSFT", 200.0, 20)
    ]

    # Add assets to the portfolio
    for asset in assets:
        risk_management_system.add_asset(asset)

    # Manage risk
    risk_management_system.manage_risk()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"Error: {e}")
```

```python
# requirements.txt
risk-management-system
```

```python
# Dockerfile
FROM python:3.9-slim

# Set working directory to /app
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run command
CMD ["python", "risk_management_system.py"]
```
