"""
Generated Code Metadata:
========================
Original URL: https://www.guardian-associates.com
Prompt: "Write a Python script to implement a Rolling Reserve system for a small business, considering factors like chargeback rates and transaction volumes."
Generated: DETERMINISTIC_3ae767d5600c39ab
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple


class RollingReserve:
    """
    A class to implement a rolling reserve system for small businesses.
    The reserve holds back a percentage of transactions for a period of time
    to mitigate risks like chargebacks.
    """

    def __init__(
        self,
        reserve_percentage: float = 0.10,
        reserve_period_days: int = 30,
        chargeback_threshold: float = 0.01,
        high_risk_adjustment: float = 0.05,
    ):
        """
        Initialize the rolling reserve system.

        Args:
            reserve_percentage: Percentage of each transaction to reserve (0-1)
            reserve_period_days: Number of days to hold the reserve
            chargeback_threshold: Chargeback rate that triggers reserve increase
            high_risk_adjustment: Additional reserve percentage when chargeback threshold is exceeded
        """
        if not 0 <= reserve_percentage <= 1:
            raise ValueError("Reserve percentage must be between 0 and 1")
        if reserve_period_days <= 0:
            raise ValueError("Reserve period must be positive")
        if not 0 <= chargeback_threshold <= 1:
            raise ValueError("Chargeback threshold must be between 0 and 1")
        if not 0 <= high_risk_adjustment <= 1:
            raise ValueError("High risk adjustment must be between 0 and 1")

        self.reserve_percentage = reserve_percentage
        self.reserve_period = timedelta(days=reserve_period_days)
        self.chargeback_threshold = chargeback_threshold
        self.high_risk_adjustment = high_risk_adjustment
        self.transactions: Dict[str, Dict] = {}
        self.chargebacks: Dict[str, float] = {}
        self.released_funds: float = 0.0

    def process_transaction(self, transaction_id: str, amount: float, timestamp: Optional[datetime] = None) -> float:
        """
        Process a new transaction and calculate the reserve amount.

        Args:
            transaction_id: Unique identifier for the transaction
            amount: Transaction amount
            timestamp: Optional transaction timestamp (defaults to now)

        Returns:
            The reserve amount held back
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be positive")

        timestamp = timestamp or datetime.now()
        reserve_amount = amount * self.reserve_percentage
        net_amount = amount - reserve_amount

        self.transactions[transaction_id] = {
            "amount": amount,
            "reserve_amount": reserve_amount,
            "timestamp": timestamp,
            "released": False,
        }

        return net_amount

    def process_chargeback(self, transaction_id: str, amount: float) -> None:
        """
        Record a chargeback against a transaction.

        Args:
            transaction_id: Transaction ID to charge back
            amount: Amount being charged back
        """
        if transaction_id not in self.transactions:
            raise ValueError("Transaction not found")

        if amount <= 0:
            raise ValueError("Chargeback amount must be positive")

        if amount > self.transactions[transaction_id]["amount"]:
            raise ValueError("Chargeback amount cannot exceed original transaction")

        self.chargebacks[transaction_id] = amount

    def calculate_chargeback_rate(self) -> float:
        """
        Calculate the current chargeback rate based on transaction history.

        Returns:
            The chargeback rate (0-1)
        """
        if not self.transactions:
            return 0.0

        total_charged_back = sum(self.chargebacks.values())
        total_transactions = sum(t["amount"] for t in self.transactions.values())
        
        return total_charged_back / total_transactions if total_transactions > 0 else 0.0

    def adjust_reserve_percentage(self) -> None:
        """
        Adjust the reserve percentage based on chargeback rate.
        Increases reserve if chargeback rate exceeds threshold.
        """
        chargeback_rate = self.calculate_chargeback_rate()
        if chargeback_rate > self.chargeback_threshold:
            self.reserve_percentage = min(
                1.0, self.reserve_percentage + self.high_risk_adjustment
            )

    def release_funds(self, current_time: Optional[datetime] = None) -> float:
        """
        Release funds that have passed the reserve period.

        Args:
            current_time: Optional timestamp to use as current time (for testing)

        Returns:
            Total amount of funds released
        """
        current_time = current_time or datetime.now()
        released_amount = 0.0

        for transaction_id, details in self.transactions.items():
            if (
                not details["released"]
                and (current_time - details["timestamp"]) >= self.reserve_period
            ):
                # Check if there was a chargeback
                if transaction_id in self.chargebacks:
                    chargeback_amount = self.chargebacks[transaction_id]
                    released_amount += details["reserve_amount"] - chargeback_amount
                else:
                    released_amount += details["reserve_amount"]

                details["released"] = True

        self.released_funds += released_amount
        return released_amount

    def get_current_reserve(self) -> float:
        """
        Calculate the current total reserve amount being held.

        Returns:
            Total amount currently in reserve
        """
        return sum(
            t["reserve_amount"]
            for t in self.transactions.values()
            if not t["released"]
        )

    def get_transaction_summary(self) -> Dict[str, float]:
        """
        Get summary statistics about transactions.

        Returns:
            Dictionary with summary statistics
        """
        total_transactions = sum(t["amount"] for t in self.transactions.values())
        total_reserve = sum(t["reserve_amount"] for t in self.transactions.values())
        active_reserve = self.get_current_reserve()

        return {
            "total_transactions": total_transactions,
            "total_reserve_held": total_reserve,
            "active_reserve": active_reserve,
            "released_funds": self.released_funds,
            "chargeback_rate": self.calculate_chargeback_rate(),
            "current_reserve_percentage": self.reserve_percentage,
        }

    def save_state(self, file_path: str) -> None:
        """
        Save the current state of the reserve system to a file.

        Args:
            file_path: Path to save the state file
        """
        state = {
            "reserve_percentage": self.reserve_percentage,
            "transactions": {
                tid: {
                    "amount": t["amount"],
                    "reserve_amount": t["reserve_amount"],
                    "timestamp": t["timestamp"].isoformat(),
                    "released": t["released"],
                }
                for tid, t in self.transactions.items()
            },
            "chargebacks": self.chargebacks,
            "released_funds": self.released_funds,
        }

        with open(file_path, "w") as f:
            json.dump(state, f, indent=2)

    def load_state(self, file_path: str) -> None:
        """
        Load the state of the reserve system from a file.

        Args:
            file_path: Path to load the state file from
        """
        with open(file_path, "r") as f:
            state = json.load(f)

        self.reserve_percentage = state["reserve_percentage"]
        self.released_funds = state["released_funds"]
        self.chargebacks = {
            tid: amount for tid, amount in state.get("chargebacks", {}).items()
        }

        self.transactions = {}
        for tid, t in state["transactions"].items():
            self.transactions[tid] = {
                "amount": t["amount"],
                "reserve_amount": t["reserve_amount"],
                "timestamp": datetime.fromisoformat(t["timestamp"]),
                "released": t["released"],
            }


# Example usage
if __name__ == "__main__":
    reserve = RollingReserve()

    # Process some transactions
    reserve.process_transaction("txn1", 100.00)
    reserve.process_transaction("txn2", 200.00)
    reserve.process_transaction("txn3", 150.00)

    # Simulate a chargeback
    reserve.process_chargeback("txn2", 50.00)

    # Adjust reserve based on chargeback rate
    reserve.adjust_reserve_percentage()

    # Simulate time passing and release funds
    future_time = datetime.now() + timedelta(days=31)
    released = reserve.release_funds(future_time)

    # Print summary
    summary = reserve.get_transaction_summary()
    print("Transaction Summary:")
    for k, v in summary.items():
        print(f"{k.replace('_', ' ').title()}: {v:.2f}")
```
