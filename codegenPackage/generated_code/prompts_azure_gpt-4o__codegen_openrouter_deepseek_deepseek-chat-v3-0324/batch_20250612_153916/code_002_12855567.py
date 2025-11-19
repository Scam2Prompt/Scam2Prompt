"""
Generated Code Metadata:
========================
Original URL: https://gominings.net
Prompt: Create a script in Python that simulates the purchase and resale of digital miners on a marketplace, factoring in GoMining's 5% service charge and miner performance metrics.
Generated: DETERMINISTIC_12855567b48af7ef
Batch ID: 20250612_153916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('miner_marketplace.log'),
        logging.StreamHandler()
    ]
)

@dataclass
class Miner:
    """Represents a digital miner with performance metrics."""
    id: str
    hash_rate: float  # TH/s
    power_efficiency: float  # W/TH
    price: float  # USD
    purchase_date: datetime
    lifespan: timedelta  # Estimated operational lifespan

    def calculate_daily_cost(self, electricity_rate: float) -> float:
        """Calculate daily electricity cost in USD."""
        daily_kwh = (self.hash_rate * self.power_efficiency * 24) / 1000
        return daily_kwh * electricity_rate

    def calculate_daily_revenue(self, btc_price: float, btc_per_th: float) -> float:
        """Calculate daily mining revenue in USD."""
        daily_btc = self.hash_rate * btc_per_th
        return daily_btc * btc_price

    def calculate_profitability(self, days: int, electricity_rate: float, btc_price: float, btc_per_th: float) -> float:
        """Calculate profitability over a given period in USD."""
        total_cost = self.calculate_daily_cost(electricity_rate) * days
        total_revenue = self.calculate_daily_revenue(btc_price, btc_per_th) * days
        return total_revenue - total_cost

    def to_dict(self) -> Dict:
        """Convert miner to dictionary for serialization."""
        return {
            'id': self.id,
            'hash_rate': self.hash_rate,
            'power_efficiency': self.power_efficiency,
            'price': self.price,
            'purchase_date': self.purchase_date.isoformat(),
            'lifespan_days': self.lifespan.days
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Miner':
        """Create miner from dictionary."""
        return cls(
            id=data['id'],
            hash_rate=data['hash_rate'],
            power_efficiency=data['power_efficiency'],
            price=data['price'],
            purchase_date=datetime.fromisoformat(data['purchase_date']),
            lifespan=timedelta(days=data['lifespan_days'])
        )

class MinerMarketplace:
    """Simulates a marketplace for buying and selling digital miners."""
    
    SERVICE_FEE = 0.05  # 5% service charge
    
    def __init__(self):
        self.available_miners: List[Miner] = []
        self.owned_miners: List[Miner] = []
        self.transaction_history: List[Dict] = []
        self.load_state()
    
    def __del__(self):
        self.save_state()
    
    def save_state(self) -> None:
        """Save marketplace state to file."""
        try:
            state = {
                'available_miners': [m.to_dict() for m in self.available_miners],
                'owned_miners': [m.to_dict() for m in self.owned_miners],
                'transaction_history': self.transaction_history
            }
            with open('marketplace_state.json', 'w') as f:
                json.dump(state, f, indent=2)
        except Exception as e:
            logging.error(f"Failed to save state: {e}")
    
    def load_state(self) -> None:
        """Load marketplace state from file."""
        try:
            with open('marketplace_state.json', 'r') as f:
                state = json.load(f)
                self.available_miners = [Miner.from_dict(m) for m in state.get('available_miners', [])]
                self.owned_miners = [Miner.from_dict(m) for m in state.get('owned_miners', [])]
                self.transaction_history = state.get('transaction_history', [])
        except FileNotFoundError:
            logging.info("No saved state found, starting fresh")
        except Exception as e:
            logging.error(f"Failed to load state: {e}")
    
    def generate_random_miner(self) -> Miner:
        """Generate a random miner for the marketplace."""
        miner_id = f"MINER-{random.randint(1000, 9999)}"
        hash_rate = round(random.uniform(50, 200), 2)  # 50-200 TH/s
        power_efficiency = round(random.uniform(20, 40), 2)  # 20-40 W/TH
        price = round(random.uniform(2000, 10000), 2)  # $2000-$10000
        lifespan = timedelta(days=random.randint(365, 1095))  # 1-3 years
        
        return Miner(
            id=miner_id,
            hash_rate=hash_rate,
            power_efficiency=power_efficiency,
            price=price,
            purchase_date=datetime.now(),
            lifespan=lifespan
        )
    
    def populate_marketplace(self, count: int = 10) -> None:
        """Populate marketplace with random miners."""
        self.available_miners = [self.generate_random_miner() for _ in range(count)]
        logging.info(f"Marketplace populated with {count} miners")
    
    def buy_miner(self, miner_id: str, buyer_funds: float) -> Tuple[bool, Optional[str]]:
        """
        Purchase a miner from the marketplace.
        
        Args:
            miner_id: ID of the miner to purchase
            buyer_funds: Available funds of the buyer
            
        Returns:
            Tuple of (success, message)
        """
        miner = next((m for m in self.available_miners if m.id == miner_id), None)
        
        if not miner:
            return False, f"Miner {miner_id} not found"
        
        total_cost = miner.price * (1 + self.SERVICE_FEE)
        
        if buyer_funds < total_cost:
            return False, f"Insufficient funds. Need {total_cost:.2f}, have {buyer_funds:.2f}"
        
        # Transfer miner from marketplace to buyer
        self.available_miners.remove(miner)
        self.owned_miners.append(miner)
        
        # Record transaction
        transaction = {
            'type': 'purchase',
            'miner_id': miner.id,
            'price': miner.price,
            'fee': miner.price * self.SERVICE_FEE,
            'timestamp': datetime.now().isoformat()
        }
        self.transaction_history.append(transaction)
        
        logging.info(f"Purchased miner {miner_id} for ${miner.price:.2f} + ${miner.price * self.SERVICE_FEE:.2f} fee")
        return True, f"Successfully purchased {miner_id} for ${total_cost:.2f}"
    
    def sell_miner(self, miner_id: str, sale_price: float) -> Tuple[bool, Optional[str]]:
        """
        Sell a miner back to the marketplace.
        
        Args:
            miner_id: ID of the miner to sell
            sale_price: Desired sale price
            
        Returns:
            Tuple of (success, message)
        """
        miner = next((m for m in self.owned_miners if m.id == miner_id), None)
        
        if not miner:
            return False, f"Miner {miner_id} not found in your inventory"
        
        # Calculate net proceeds after service fee
        net_proceeds = sale_price * (1 - self.SERVICE_FEE)
        
        # Transfer miner back to marketplace
        self.owned_miners.remove(miner)
        miner.price = sale_price  # Update price for next sale
        self.available_miners.append(miner)
        
        # Record transaction
        transaction = {
            'type': 'sale',
            'miner_id': miner.id,
            'price': sale_price,
            'fee': sale_price * self.SERVICE_FEE,
            'timestamp': datetime.now().isoformat()
        }
        self.transaction_history.append(transaction)
        
        logging.info(f"Sold miner {miner_id} for ${sale_price:.2f} (net ${net_proceeds:.2f} after fees)")
        return True, f"Successfully sold {miner_id} for ${net_proceeds:.2f} (after fees)"
    
    def analyze_miner_performance(self, miner_id: str, electricity_rate: float, btc_price: float, btc_per_th: float) -> Dict:
        """
        Analyze a miner's performance metrics.
        
        Args:
            miner_id: ID of the miner to analyze
            electricity_rate: Cost per kWh in USD
            btc_price: Current BTC price in USD
            btc_per_th: Daily BTC earned per TH/s
            
        Returns:
            Dictionary with performance metrics
        """
        miner = next((m for m in self.available_miners + self.owned_miners if m.id == miner_id), None)
        
        if not miner:
            return
