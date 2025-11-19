"""
Generated Code Metadata:
========================
Original URL: https://inceptiontrades.net
Prompt: Write a script to simulate multi-assets management, incorporating features like market analysis and project management as described by Inception Trades.
Generated: DETERMINISTIC_5679acb469d05571
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple


class Asset:
    """Represents a financial asset with market data and performance metrics."""

    def __init__(self, name: str, asset_type: str, initial_price: float):
        """
        Initialize an Asset instance.

        Args:
            name: Name of the asset.
            asset_type: Type of the asset (e.g., 'Stock', 'Bond', 'Crypto').
            initial_price: Initial price of the asset.
        """
        self.name = name
        self.type = asset_type
        self.current_price = initial_price
        self.historical_prices = [initial_price]
        self.performance_metrics = {
            "volatility": 0.0,
            "return": 0.0,
            "liquidity": random.uniform(0.1, 1.0),
        }
        self.last_updated = datetime.now()

    def update_price(self, new_price: float) -> None:
        """
        Update the asset's current price and record historical data.

        Args:
            new_price: New price to set for the asset.
        """
        if new_price <= 0:
            raise ValueError("Price must be positive.")
        self.historical_prices.append(new_price)
        self.current_price = new_price
        self._update_performance_metrics()
        self.last_updated = datetime.now()

    def _update_performance_metrics(self) -> None:
        """Calculate and update performance metrics based on historical prices."""
        if len(self.historical_prices) < 2:
            return

        returns = []
        for i in range(1, len(self.historical_prices)):
            prev_price = self.historical_prices[i - 1]
            current_price = self.historical_prices[i]
            returns.append((current_price - prev_price) / prev_price)

        avg_return = sum(returns) / len(returns) if returns else 0.0
        variance = sum((r - avg_return) ** 2 for r in returns) / len(returns) if returns else 0.0
        volatility = variance ** 0.5

        self.performance_metrics["return"] = avg_return
        self.performance_metrics["volatility"] = volatility

    def get_summary(self) -> Dict:
        """
        Get a summary of the asset's current state.

        Returns:
            Dictionary containing asset details and metrics.
        """
        return {
            "name": self.name,
            "type": self.type,
            "current_price": self.current_price,
            "performance_metrics": self.performance_metrics,
            "last_updated": self.last_updated.isoformat(),
        }


class Portfolio:
    """Manages a collection of assets and provides portfolio-level analysis."""

    def __init__(self, name: str):
        """
        Initialize a Portfolio instance.

        Args:
            name: Name of the portfolio.
        """
        self.name = name
        self.assets: Dict[str, Asset] = {}
        self.projects: List[Dict] = []

    def add_asset(self, asset: Asset) -> None:
        """
        Add an asset to the portfolio.

        Args:
            asset: Asset instance to add.
        """
        if asset.name in self.assets:
            raise ValueError(f"Asset '{asset.name}' already exists in the portfolio.")
        self.assets[asset.name] = asset

    def remove_asset(self, asset_name: str) -> None:
        """
        Remove an asset from the portfolio.

        Args:
            asset_name: Name of the asset to remove.
        """
        if asset_name not in self.assets:
            raise ValueError(f"Asset '{asset_name}' not found in the portfolio.")
        del self.assets[asset_name]

    def update_asset_prices(self, price_updates: Dict[str, float]) -> None:
        """
        Update prices for multiple assets in the portfolio.

        Args:
            price_updates: Dictionary mapping asset names to new prices.
        """
        for asset_name, new_price in price_updates.items():
            if asset_name not in self.assets:
                raise ValueError(f"Asset '{asset_name}' not found in the portfolio.")
            self.assets[asset_name].update_price(new_price)

    def get_portfolio_value(self) -> float:
        """
        Calculate the total value of the portfolio.

        Returns:
            Sum of all asset current prices.
        """
        return sum(asset.current_price for asset in self.assets.values())

    def get_portfolio_performance(self) -> Dict:
        """
        Calculate portfolio-level performance metrics.

        Returns:
            Dictionary containing portfolio performance metrics.
        """
        total_value = self.get_portfolio_value()
        if not self.assets:
            return {
                "total_value": 0.0,
                "avg_return": 0.0,
                "avg_volatility": 0.0,
                "diversification": 0.0,
            }

        weighted_returns = []
        weighted_volatilities = []
        for asset in self.assets.values():
            weight = asset.current_price / total_value
            weighted_returns.append(weight * asset.performance_metrics["return"])
            weighted_volatilities.append(weight * asset.performance_metrics["volatility"])

        asset_types = {asset.type for asset in self.assets.values()}
        diversification = len(asset_types) / len(self.assets) if self.assets else 0.0

        return {
            "total_value": total_value,
            "avg_return": sum(weighted_returns),
            "avg_volatility": sum(weighted_volatilities),
            "diversification": diversification,
        }

    def add_project(self, name: str, description: str, deadline: str) -> None:
        """
        Add a project to the portfolio's project management system.

        Args:
            name: Name of the project.
            description: Description of the project.
            deadline: Deadline in ISO format (YYYY-MM-DD).
        """
        try:
            deadline_date = datetime.strptime(deadline, "%Y-%m-%d").date()
        except ValueError as e:
            raise ValueError("Invalid deadline format. Use YYYY-MM-DD.") from e

        self.projects.append({
            "name": name,
            "description": description,
            "deadline": deadline,
            "status": "Pending",
            "created_at": datetime.now().isoformat(),
        })

    def update_project_status(self, project_name: str, status: str) -> None:
        """
        Update the status of a project.

        Args:
            project_name: Name of the project to update.
            status: New status ('Pending', 'In Progress', 'Completed', 'Cancelled').
        """
        valid_statuses = {"Pending", "In Progress", "Completed", "Cancelled"}
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")

        for project in self.projects:
            if project["name"] == project_name:
                project["status"] = status
                project["last_updated"] = datetime.now().isoformat()
                return

        raise ValueError(f"Project '{project_name}' not found.")

    def get_upcoming_projects(self, days_ahead: int = 7) -> List[Dict]:
        """
        Get projects with deadlines within the specified number of days.

        Args:
            days_ahead: Number of days to look ahead for deadlines.

        Returns:
            List of projects with upcoming deadlines.
        """
        today = datetime.now().date()
        cutoff_date = today + timedelta(days=days_ahead)
        upcoming = []

        for project in self.projects:
            try:
                deadline = datetime.strptime(project["deadline"], "%Y-%m-%d").date()
                if today <= deadline <= cutoff_date:
                    upcoming.append(project)
            except ValueError:
                continue

        return upcoming

    def generate_report(self) -> Dict:
        """
        Generate a comprehensive report of the portfolio.

        Returns:
            Dictionary containing portfolio summary, assets, and projects.
        """
        return {
            "portfolio_name": self.name,
            "portfolio_summary": self.get_portfolio_performance(),
            "assets": [asset.get_summary() for asset in self.assets.values()],
            "projects": self.projects,
            "report_generated": datetime.now().isoformat(),
        }


class MarketSimulator:
    """Simulates market conditions and generates price updates for assets."""

    def __init__(self, volatility_factor: float = 0.05):
        """
        Initialize the MarketSimulator.

        Args:
            volatility_factor: Controls how much prices can change (0-1).
        """
        self.volatility_factor = volatility_factor
        self.market_conditions = {
            "trend": random.choice(["bull", "bear", "neutral"]),
            "volatility": random.uniform(0.1, 0.3),
        }

    def update_market_conditions(self) -> None:
        """Randomly update the simulated market conditions."""
        self.market_conditions = {
            "trend": random.choice(["bull", "bear", "neutral"]),
            "volatility": random.uniform(0.1, 0.3),
