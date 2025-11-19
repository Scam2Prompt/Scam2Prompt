"""
Generated Code Metadata:
========================
Original URL: https://pyth-test.vercel.app
Prompt: Discuss the role of Pyth Network's token ($Pyth) in the ecosystem and how it incentivizes data providers to contribute to the network.
Generated: DETERMINISTIC_36c0eb03c0b892f5
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script demonstrates a simplified model of how Pyth Network's token ($PYTH) incentivizes data providers
# It includes staking, reward distribution, and slashing mechanisms

import random
from typing import List, Dict
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class DataProvider:
    """Represents a data provider in the Pyth Network ecosystem."""
    address: str
    staked_amount: float
    reputation_score: float
    last_update_time: datetime
    is_active: bool = True

@dataclass
class DataFeed:
    """Represents a data feed in the Pyth Network."""
    feed_id: str
    value: float
    timestamp: datetime
    provider_address: str

class PythNetwork:
    """Simulates the Pyth Network ecosystem with token incentives."""
    
    def __init__(self):
        self.data_providers: Dict[str, DataProvider] = {}
        self.data_feeds: Dict[str, List[DataFeed]] = {}
        self.total_staked = 0.0
        self.reward_pool = 1000000.0  # Initial reward pool
        self.slash_percentage = 0.05  # 5% slashing for bad data
        
    def add_data_provider(self, address: str, initial_stake: float) -> None:
        """Register a new data provider with an initial stake."""
        if address in self.data_providers:
            raise ValueError("Provider already exists")
            
        provider = DataProvider(
            address=address,
            staked_amount=initial_stake,
            reputation_score=1.0,
            last_update_time=datetime.now(),
            is_active=True
        )
        self.data_providers[address] = provider
        self.total_staked += initial_stake
        
    def submit_data_feed(self, provider_address: str, feed_id: str, value: float) -> None:
        """Submit new data to a feed from a provider."""
        if provider_address not in self.data_providers:
            raise ValueError("Provider not registered")
            
        provider = self.data_providers[provider_address]
        if not provider.is_active:
            raise ValueError("Provider is inactive")
            
        timestamp = datetime.now()
        feed = DataFeed(
            feed_id=feed_id,
            value=value,
            timestamp=timestamp,
            provider_address=provider_address
        )
        
        if feed_id not in self.data_feeds:
            self.data_feeds[feed_id] = []
            
        self.data_feeds[feed_id].append(feed)
        provider.last_update_time = timestamp
        
    def calculate_rewards(self, period_days: int = 7) -> Dict[str, float]:
        """Calculate rewards for active providers based on their stake and reputation."""
        end_time = datetime.now()
        start_time = end_time - timedelta(days=period_days)
        
        active_providers = [
            p for p in self.data_providers.values() 
            if p.is_active and p.last_update_time >= start_time
        ]
        
        if not active_providers:
            return {}
            
        total_weight = sum(
            p.staked_amount * p.reputation_score 
            for p in active_providers
        )
        
        if total_weight <= 0:
            return {}
            
        rewards = {}
        for provider in active_providers:
            weight = (provider.staked_amount * provider.reputation_score) / total_weight
            reward = weight * self.reward_pool
            rewards[provider.address] = reward
            
        return rewards
    
    def distribute_rewards(self, rewards: Dict[str, float]) -> None:
        """Distribute calculated rewards to providers."""
        for address, amount in rewards.items():
            self.data_providers[address].staked_amount += amount
            
    def verify_data_quality(self, feed_id: str) -> None:
        """Verify data quality and slash providers for bad data."""
        if feed_id not in self.data_feeds:
            return
            
        feeds = self.data_feeds[feed_id]
        if len(feeds) < 2:
            return
            
        # Simple verification: compare with median value
        values = [f.value for f in feeds]
        median = sorted(values)[len(values) // 2]
        threshold = median * 0.05  # 5% deviation threshold
        
        for feed in feeds:
            deviation = abs(feed.value - median) / median
            if deviation > threshold:
                provider = self.data_providers[feed.provider_address]
                slash_amount = provider.staked_amount * self.slash_percentage
                provider.staked_amount -= slash_amount
                provider.reputation_score *= 0.9  # Reduce reputation
                self.total_staked -= slash_amount
                
    def simulate_network_activity(self, num_providers: int, num_feeds: int, days: int) -> None:
        """Simulate network activity over time for demonstration purposes."""
        # Add providers
        for i in range(num_providers):
            self.add_data_provider(f"provider_{i}", random.uniform(1000, 10000))
            
        # Simulate daily activity
        for day in range(days):
            # Providers submit data
            for feed_id in range(num_feeds):
                for provider in self.data_providers.values():
                    if random.random() > 0.1:  # 90% chance of submitting data
                        value = random.uniform(100, 200)
                        self.submit_data_feed(provider.address, f"feed_{feed_id}", value)
                        
            # Verify data quality
            for feed_id in range(num_feeds):
                self.verify_data_quality(f"feed_{feed_id}")
                
            # Weekly reward distribution
            if day % 7 == 0:
                rewards = self.calculate_rewards()
                self.distribute_rewards(rewards)
                
# Example usage
if __name__ == "__main__":
    network = PythNetwork()
    
    # Simulate 10 providers, 5 feeds over 30 days
    network.simulate_network_activity(10, 5, 30)
    
    # Display final provider stakes
    for address, provider in network.data_providers.items():
        print(f"Provider {address}: {provider.staked_amount:.2f} PYTH")
```
