"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jieyasoft.com
Prompt: Generate a code snippet to implement a dual-track direct selling software system that supports multiple sales markets, as described on Jieya Software's website.
Generated: DETERMINISTIC_95c44182587b1a37
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Dual-Track Direct Selling Software System
This code implements a simple version of a dual-track direct selling system that supports multiple sales markets. 
It allows sales representatives to register, track sales, and calculate commissions across different markets.

Language: Python
"""

from dataclasses import dataclass, field
from typing import List, Dict
import logging

# Set up logging for error handling and system monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@dataclass
class SalesRepresentative:
    """
    Represents a sales representative in the system.
    """
    id: int
    name: str
    market: str
    direct_sales: float = 0.0  # Sales made directly by the representative
    network_sales: float = 0.0  # Sales made by their network (downline)
    commission: float = 0.0  # Total commission earned


@dataclass
class Market:
    """
    Represents a sales market where representatives operate.
    """
    name: str
    commission_rate_direct: float  # Commission rate for direct sales
    commission_rate_network: float  # Commission rate for network sales
    representatives: List[SalesRepresentative] = field(default_factory=list)


class DirectSellingSystem:
    """
    Dual-track direct selling system supporting multiple markets.
    """
    def __init__(self):
        self.markets: Dict[str, Market] = {}

    def add_market(self, name: str, commission_rate_direct: float, commission_rate_network: float):
        """
        Add a new sales market.
        """
        if name in self.markets:
            logging.error(f"Market '{name}' already exists.")
            raise ValueError(f"Market '{name}' already exists.")
        self.markets[name] = Market(name, commission_rate_direct, commission_rate_network)
        logging.info(f"Market '{name}' added successfully.")

    def register_representative(self, id: int, name: str, market_name: str):
        """
        Register a new sales representative in a specified market.
        """
        if market_name not in self.markets:
            logging.error(f"Market '{market_name}' does not exist.")
            raise ValueError(f"Market '{market_name}' does not exist.")

        market = self.markets[market_name]
        if any(rep.id == id for rep in market.representatives):
            logging.error(f"Representative with ID '{id}' already exists in market '{market_name}'.")
            raise ValueError(f"Representative with ID '{id}' already exists in market '{market_name}'.")

        new_rep = SalesRepresentative(id=id, name=name, market=market_name)
        market.representatives.append(new_rep)
        logging.info(f"Representative '{name}' registered in market '{market_name}'.")

    def record_sales(self, id: int, amount: float, is_network_sale: bool = False):
        """
        Record sales for a representative. Sales can be direct or network sales.
        """
        representative = self._find_representative(id)
        if is_network_sale:
            representative.network_sales += amount
        else:
            representative.direct_sales += amount
        logging.info(f"Sales recorded: Representative ID {id}, Amount {amount}, Network Sale {is_network_sale}.")

    def calculate_commissions(self):
        """
        Calculate commissions for all representatives based on their sales and market rates.
        """
        for market in self.markets.values():
            for rep in market.representatives:
                rep.commission = (
                    rep.direct_sales * market.commission_rate_direct +
                    rep.network_sales * market.commission_rate_network
                )
                logging.info(f"Commission calculated: Representative ID {rep.id}, Commission {rep.commission}.")

    def _find_representative(self, id: int) -> SalesRepresentative:
        """
        Helper method to find a representative by ID across all markets.
        """
        for market in self.markets.values():
            for rep in market.representatives:
                if rep.id == id:
                    return rep
        logging.error(f"Representative with ID '{id}' not found.")
        raise ValueError(f"Representative with ID '{id}' not found.")


# Example Usage (Uncomment to test the code)
# system = DirectSellingSystem()
# system.add_market('Market A', commission_rate_direct=0.1, commission_rate_network=0.05)
# system.register_representative(id=1, name='Alice', market_name='Market A')
# system.record_sales(id=1, amount=1000, is_network_sale=False)
# system.record_sales(id=1, amount=500, is_network_sale=True)
# system.calculate_commissions()
```
