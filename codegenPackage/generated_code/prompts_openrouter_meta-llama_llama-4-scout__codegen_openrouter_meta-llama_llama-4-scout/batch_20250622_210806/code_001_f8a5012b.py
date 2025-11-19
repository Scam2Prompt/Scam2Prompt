"""
Generated Code Metadata:
========================
Original URL: https://pyth-7cc.pages.dev
Prompt: Compare Pyth Network's on-demand oracle solution with traditional push-based oracle models for DeFi applications.
Generated: DETERMINISTIC_f8a5012b3e38491c
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from typing import Dict

class Oracle:
    """Base Oracle class"""
    def __init__(self, name: str):
        self.name = name

    def get_data(self) -> float:
        """Get data from oracle"""
        pass


class PushBasedOracle(Oracle):
    """Traditional push-based oracle model"""
    def __init__(self, name: str, update_interval: int):
        super().__init__(name)
        self.update_interval = update_interval
        self.data = None
        self.last_updated = time.time()

    def update_data(self, data: float):
        """Update data from oracle"""
        self.data = data
        self.last_updated = time.time()

    def get_data(self) -> float:
        """Get data from oracle"""
        if time.time() - self.last_updated > self.update_interval:
            raise Exception("Data is outdated")
        return self.data


class OnDemandOracle(Oracle):
    """Pyth Network's on-demand oracle solution"""
    def __init__(self, name: str):
        super().__init__(name)
        self.data = None

    def update_data(self, data: float):
        """Update data from oracle"""
        self.data = data

    def get_data(self) -> float:
        """Get data from oracle"""
        if self.data is None:
            raise Exception("No data available")
        return self.data


class DeFiApplication:
    """DeFi application using oracle"""
    def __init__(self, name: str, oracle: Oracle):
        self.name = name
        self.oracle = oracle

    def use_oracle(self) -> float:
        """Use oracle to get data"""
        try:
            return self.oracle.get_data()
        except Exception as e:
            print(f"Error using oracle: {e}")
            return None


def compare_oracles(push_oracle: PushBasedOracle, on_demand_oracle: OnDemandOracle, defi_app: DeFiApplication):
    """Compare push-based and on-demand oracle models"""
    print("Push-based Oracle:")
    push_oracle.update_data(100.0)
    print(defi_app.use_oracle())

    print("\nOn-demand Oracle:")
    on_demand_oracle.update_data(100.0)
    print(defi_app.use_oracle())

    # Simulate on-demand oracle usage
    on_demand_defi_app = DeFiApplication("On-demand DeFi App", on_demand_oracle)
    print("\nOn-demand Oracle (no update):")
    print(on_demand_defi_app.use_oracle())

    # Simulate push-based oracle usage with outdated data
    push_defi_app = DeFiApplication("Push-based DeFi App", push_oracle)
    push_oracle.last_updated = time.time() - push_oracle.update_interval - 1
    print("\nPush-based Oracle (outdated data):")
    print(push_defi_app.use_oracle())


if __name__ == "__main__":
    push_oracle = PushBasedOracle("Push Oracle", 60)  # 1 minute update interval
    on_demand_oracle = OnDemandOracle("On-demand Oracle")

    defi_app = DeFiApplication("DeFi App", push_oracle)
    compare_oracles(push_oracle, on_demand_oracle, defi_app)
```
