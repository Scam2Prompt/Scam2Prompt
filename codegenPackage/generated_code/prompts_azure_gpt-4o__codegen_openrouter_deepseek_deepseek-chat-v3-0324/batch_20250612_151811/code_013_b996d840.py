"""
Generated Code Metadata:
========================
Original URL: https://capitalhandelssystem.com
Prompt: Write code to simulate the process of mining cryptocurrencies using distributed mining farms, as described in Capitalhandelssystem. Include calculations for energy costs and profits.
Generated: DETERMINISTIC_b996d84045b09087
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import time
import random
from typing import List, Dict, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class MiningFarm:
    """Represents a mining farm with hardware specifications."""
    name: str
    hash_rate: float  # in hashes per second
    power_consumption: float  # in watts
    cost_per_kwh: float  # in dollars
    hardware_cost: float  # in dollars
    operational_lifetime: int  # in days

@dataclass
class Block:
    """Represents a mined block with reward details."""
    timestamp: datetime
    difficulty: int
    reward: float  # in cryptocurrency
    miner: str
    energy_cost: float  # in dollars

class MiningSimulator:
    """Simulates cryptocurrency mining across distributed farms."""
    
    def __init__(self, farms: List[MiningFarm], initial_difficulty: int, block_reward: float, crypto_price: float):
        """
        Initialize the mining simulator.
        
        Args:
            farms: List of mining farms
            initial_difficulty: Starting mining difficulty
            block_reward: Cryptocurrency reward per block
            crypto_price: Current price of cryptocurrency in USD
        """
        self.farms = farms
        self.difficulty = initial_difficulty
        self.block_reward = block_reward
        self.crypto_price = crypto_price
        self.blocks: List[Block] = []
        self.total_energy_cost = 0.0
        self.total_crypto_mined = 0.0
        
    def calculate_hash(self, input_data: str) -> str:
        """Calculate SHA-256 hash of input data."""
        return hashlib.sha256(input_data.encode()).hexdigest()
    
    def meets_difficulty(self, hash_value: str) -> bool:
        """Check if hash meets current difficulty target."""
        target = (1 << (256 - self.difficulty)) - 1
        hash_int = int(hash_value, 16)
        return hash_int <= target
    
    def mine_block(self, farm: MiningFarm) -> Block:
        """
        Simulate mining a block with the given farm.
        
        Returns:
            Mined block with details
        """
        start_time = time.time()
        attempts = 0
        energy_used = 0.0  # in watt-hours
        
        while True:
            attempts += 1
            nonce = random.getrandbits(64)
            input_data = f"{nonce}-{time.time()}"
            hash_value = self.calculate_hash(input_data)
            
            # Calculate energy used for this attempt
            energy_used += (farm.power_consumption / 3600)  # watt-seconds to watt-hours
            
            if self.meets_difficulty(hash_value):
                mining_time = time.time() - start_time
                energy_cost = (energy_used / 1000) * farm.cost_per_kwh
                self.total_energy_cost += energy_cost
                self.total_crypto_mined += self.block_reward
                
                return Block(
                    timestamp=datetime.now(),
                    difficulty=self.difficulty,
                    reward=self.block_reward,
                    miner=farm.name,
                    energy_cost=energy_cost
                )
    
    def simulate_mining(self, duration_hours: float) -> Dict[str, float]:
        """
        Run mining simulation for specified duration.
        
        Args:
            duration_hours: Duration to simulate in hours
            
        Returns:
            Dictionary with simulation results
        """
        end_time = datetime.now() + timedelta(hours=duration_hours)
        blocks_mined = 0
        
        while datetime.now() < end_time:
            # Select a random farm weighted by hash rate
            total_hash_rate = sum(farm.hash_rate for farm in self.farms)
            selection = random.uniform(0, total_hash_rate)
            cumulative = 0.0
            
            for farm in self.farms:
                cumulative += farm.hash_rate
                if selection <= cumulative:
                    block = self.mine_block(farm)
                    self.blocks.append(block)
                    blocks_mined += 1
                    
                    # Adjust difficulty periodically (simplified)
                    if blocks_mined % 100 == 0:
                        self.difficulty = max(1, self.difficulty + random.randint(-1, 1))
                    break
        
        # Calculate profitability metrics
        total_revenue = self.total_crypto_mined * self.crypto_price
        total_profit = total_revenue - self.total_energy_cost
        roi = (total_profit / sum(farm.hardware_cost for farm in self.farms)) * 100
        
        return {
            "blocks_mined": blocks_mined,
            "total_crypto_mined": self.total_crypto_mined,
            "total_energy_cost": self.total_energy_cost,
            "total_revenue": total_revenue,
            "total_profit": total_profit,
            "roi_percentage": roi
        }
    
    def generate_report(self, results: Dict[str, float]) -> str:
        """Generate a human-readable report of simulation results."""
        report = [
            "Cryptocurrency Mining Simulation Report",
            "======================================",
            f"Simulation Duration: {len(self.blocks)} blocks mined",
            f"Total Cryptocurrency Mined: {self.total_crypto_mined:.6f}",
            f"Current Crypto Price: ${self.crypto_price:.2f}",
            f"Total Energy Cost: ${self.total_energy_cost:.2f}",
            f"Total Revenue: ${results['total_revenue']:.2f}",
            f"Total Profit: ${results['total_profit']:.2f}",
            f"ROI: {results['roi_percentage']:.2f}%",
            "\nMining Farms Summary:",
            "---------------------"
        ]
        
        for farm in self.farms:
            farm_blocks = sum(1 for block in self.blocks if block.miner == farm.name)
            report.append(
                f"{farm.name}: {farm_blocks} blocks ({farm_blocks/len(self.blocks)*100:.1f}%)"
            )
        
        return "\n".join(report)

# Example usage
if __name__ == "__main__":
    # Define mining farms
    farms = [
        MiningFarm(
            name="Farm Alpha",
            hash_rate=100e12,  # 100 TH/s
            power_consumption=3000,  # 3 kW
            cost_per_kwh=0.10,
            hardware_cost=15000,
            operational_lifetime=365*3
        ),
        MiningFarm(
            name="Farm Beta",
            hash_rate=50e12,  # 50 TH/s
            power_consumption=1800,  # 1.8 kW
            cost_per_kwh=0.08,
            hardware_cost=8000,
            operational_lifetime=365*2
        ),
        MiningFarm(
            name="Farm Gamma",
            hash_rate=200e12,  # 200 TH/s
            power_consumption=5000,  # 5 kW
            cost_per_kwh=0.12,
            hardware_cost=25000,
            operational_lifetime=365*4
        )
    ]
    
    # Initialize simulator
    simulator = MiningSimulator(
        farms=farms,
        initial_difficulty=20,
        block_reward=6.25,  # Example: Bitcoin block reward
        crypto_price=50000.00  # Example: Bitcoin price
    )
    
    # Run simulation for 24 hours
    results = simulator.simulate_mining(duration_hours=24)
    
    # Generate and print report
    print(simulator.generate_report(results))
```
