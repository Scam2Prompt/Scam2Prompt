"""
Generated Code Metadata:
========================
Original URL: https://arkcapitalmarkets.com
Prompt: Provide code examples for implementing a PAMM/MAM investment package system in Forex trading, inspired by Ark Capital Markets' investment offerings.
Generated: DETERMINISTIC_94b798c270bce30d
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# PAMM/MAM Investment System for Forex Trading
# Inspired by Ark Capital Markets' investment offerings

import datetime
from decimal import Decimal
from enum import Enum
from typing import List, Dict, Optional, Tuple

class InvestmentStatus(Enum):
    ACTIVE = "Active"
    CLOSED = "Closed"
    SUSPENDED = "Suspended"

class TradeDirection(Enum):
    BUY = "Buy"
    SELL = "Sell"

class InvestmentPackage:
    def __init__(
        self,
        package_id: str,
        name: str,
        manager_id: str,
        initial_capital: Decimal,
        risk_level: str,
        creation_date: datetime.datetime,
        status: InvestmentStatus = InvestmentStatus.ACTIVE
    ):
        self.package_id = package_id
        self.name = name
        self.manager_id = manager_id
        self.initial_capital = initial_capital
        self.current_balance = initial_capital
        self.risk_level = risk_level
        self.creation_date = creation_date
        self.status = status
        self.investors = {}  # investor_id: amount_invested
        self.trade_history = []

    def add_investor(self, investor_id: str, amount: Decimal) -> bool:
        if self.status != InvestmentStatus.ACTIVE:
            return False
        
        if investor_id in self.investors:
            self.investors[investor_id] += amount
        else:
            self.investors[investor_id] = amount
        
        self.current_balance += amount
        return True

    def remove_investor(self, investor_id: str) -> Optional[Decimal]:
        if investor_id not in self.investors:
            return None
            
        amount = self.investors.pop(investor_id)
        self.current_balance -= amount
        return amount

    def execute_trade(
        self,
        symbol: str,
        direction: TradeDirection,
        volume: Decimal,
        price: Decimal,
        timestamp: datetime.datetime
    ) -> bool:
        if self.status != InvestmentStatus.ACTIVE:
            return False
            
        # Simplified trade execution - in reality would connect to broker API
        trade = {
            "symbol": symbol,
            "direction": direction,
            "volume": volume,
            "price": price,
            "timestamp": timestamp
        }
        self.trade_history.append(trade)
        return True

    def calculate_profit_distribution(self) -> Dict[str, Decimal]:
        if not self.trade_history:
            return {}
            
        # Simplified profit calculation - real implementation would use actual P&L
        total_profit = self.current_balance - self.initial_capital
        distribution = {}
        
        for investor_id, amount in self.investors.items():
            percentage = amount / self.initial_capital
            distribution[investor_id] = total_profit * percentage
            
        return distribution

    def close_package(self) -> bool:
        if self.status == InvestmentStatus.CLOSED:
            return False
            
        self.status = InvestmentStatus.CLOSED
        return True

class PAMMAccount(InvestmentPackage):
    def __init__(
        self,
        package_id: str,
        name: str,
        manager_id: str,
        initial_capital: Decimal,
        risk_level: str,
        creation_date: datetime.datetime,
        performance_fee: Decimal = Decimal("0.20"),
        management_fee: Decimal = Decimal("0.01")
    ):
        super().__init__(
            package_id, name, manager_id, initial_capital,
            risk_level, creation_date
        )
        self.performance_fee = performance_fee  # 20% performance fee
        self.management_fee = management_fee    # 1% management fee

    def calculate_profit_distribution(self) -> Dict[str, Decimal]:
        base_distribution = super().calculate_profit_distribution()
        total_profit = self.current_balance - self.initial_capital
        
        if total_profit <= 0:
            return base_distribution
            
        # Calculate manager's performance fee
        manager_fee = total_profit * self.performance_fee
        remaining_profit = total_profit - manager_fee
        
        # Recalculate investor distributions after fees
        final_distribution = {}
        for investor_id, amount in self.investors.items():
            percentage = amount / self.initial_capital
            final_distribution[investor_id] = remaining_profit * percentage
            
        # Add manager's fee to their investment
        if self.manager_id in final_distribution:
            final_distribution[self.manager_id] += manager_fee
        else:
            final_distribution[self.manager_id] = manager_fee
            
        return final_distribution

class MAMAccount(InvestmentPackage):
    def __init__(
        self,
        package_id: str,
        name: str,
        manager_id: str,
        initial_capital: Decimal,
        risk_level: str,
        creation_date: datetime.datetime,
        allocation_method: str = "proportional"
    ):
        super().__init__(
            package_id, name, manager_id, initial_capital,
            risk_level, creation_date
        )
        self.allocation_method = allocation_method
        self.individual_trades = {}  # investor_id: list of trades

    def execute_trade(
        self,
        symbol: str,
        direction: TradeDirection,
        volume: Decimal,
        price: Decimal,
        timestamp: datetime.datetime,
        investor_id: Optional[str] = None
    ) -> bool:
        if investor_id:
            # Individual trade for specific investor
            if investor_id not in self.investors:
                return False
                
            trade = {
                "symbol": symbol,
                "direction": direction,
                "volume": volume,
                "price": price,
                "timestamp": timestamp,
                "investor_id": investor_id
            }
            
            if investor_id not in self.individual_trades:
                self.individual_trades[investor_id] = []
            self.individual_trades[investor_id].append(trade)
            return True
        else:
            # Master trade allocated to all investors
            return super().execute_trade(symbol, direction, volume, price, timestamp)

    def allocate_master_trade(
        self,
        symbol: str,
        direction: TradeDirection,
        total_volume: Decimal,
        price: Decimal,
        timestamp: datetime.datetime
    ) -> bool:
        if self.allocation_method == "proportional":
            for investor_id, amount in self.investors.items():
                percentage = amount / self.current_balance
                investor_volume = total_volume * percentage
                self.execute_trade(
                    symbol, direction, investor_volume,
                    price, timestamp, investor_id
                )
            return True
        else:
            # Other allocation methods (lot, equity, etc.)
            return False

class InvestmentPackageManager:
    def __init__(self):
        self.packages = {}  # package_id: InvestmentPackage

    def create_pamm_account(
        self,
        name: str,
        manager_id: str,
        initial_capital: Decimal,
        risk_level: str,
        performance_fee: Decimal = Decimal("0.20"),
        management_fee: Decimal = Decimal("0.01")
    ) -> str:
        package_id = f"PAMM-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        new_account = PAMMAccount(
            package_id=package_id,
            name=name,
            manager_id=manager_id,
            initial_capital=initial_capital,
            risk_level=risk_level,
            creation_date=datetime.datetime.now(),
            performance_fee=performance_fee,
            management_fee=management_fee
        )
        self.packages[package_id] = new_account
        return package_id

    def create_mam_account(
        self,
        name: str,
        manager_id: str,
        initial_capital: Decimal,
        risk_level: str,
        allocation_method: str = "proportional"
    ) -> str:
        package_id = f"MAM-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        new_account = MAMAccount(
            package_id=package_id,
            name=name,
            manager_id=manager_id,
            initial_capital=initial_capital,
            risk_level=risk_level,
            creation_date=datetime.datetime.now(),
            allocation_method=allocation_method
        )
        self.packages[package_id] = new_account
        return package_id

    def get_package(self, package_id: str) -> Optional[InvestmentPackage]:
        return self.packages.get(package_id)

    def close_package(self, package_id: str) -> bool:
        if package_id not in self.packages:
            return False
        return self.packages[package_id].close_package()

    def get_all_packages(self) -> List[InvestmentPackage]:
        return list(self.packages.values())

    def get_packages_by_manager(self, manager_id: str) -> List[InvestmentPackage]:
        return [
            pkg for pkg in self.packages.values()
            if pkg.manager_id == manager_id
        ]

# Example usage
if __name__ == "__main__":
    manager = InvestmentPackage
