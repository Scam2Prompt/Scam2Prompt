"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staylodu.io
Prompt: Create a program to analyze the sustainability of Loud's reward distribution system by simulating trading volume and fee splits over time.
Generated: DETERMINISTIC_f24497937e98c25e
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RewardDistributionSystem:
    """
    A class to simulate and analyze the sustainability of a reward distribution system.
    """

    def __init__(self, trading_volume, fee_rate, reward_split_ratio, time_periods):
        """
        Initialize the system parameters.
        
        :param trading_volume: Initial trading volume (in units).
        :param fee_rate: Percentage of trading volume dedicated to fees (e.g., 0.02 for 2%).
        :param reward_split_ratio: The ratio of fees distributed as rewards (e.g., 0.7 means 70% of fees go to rewards).
        :param time_periods: Number of time periods to simulate.
        """
        self.trading_volume = trading_volume
        self.fee_rate = fee_rate
        self.reward_split_ratio = reward_split_ratio
        self.time_periods = time_periods
        self.results = []

    def simulate(self):
        """
        Simulate trading volume, fee collection, and reward distribution over the configured time periods.
        
        Each time period introduces random fluctuations in trading volume.
        """
        try:
            logging.info("Starting simulation of reward distribution system...")
            for period in range(1, self.time_periods + 1):
                # Simulate trading volume fluctuation (±10%)
                fluctuation = random.uniform(-0.1, 0.1)
                self.trading_volume += self.trading_volume * fluctuation
                
                # Calculate fees
                fees_collected = self.trading_volume * self.fee_rate
                rewards_distributed = fees_collected * self.reward_split_ratio
                fees_retained = fees_collected - rewards_distributed
                
                # Store results
                self.results.append({
                    'Period': period,
                    'Trading Volume': round(self.trading_volume, 2),
                    'Fees Collected': round(fees_collected, 2),
                    'Rewards Distributed': round(rewards_distributed, 2),
                    'Fees Retained': round(fees_retained, 2)
                })
                
                logging.info(f"Period {period}: Volume = {self.trading_volume:.2f}, "
                             f"Fees = {fees_collected:.2f}, Rewards = {rewards_distributed:.2f}, "
                             f"Retained = {fees_retained:.2f}")
        except Exception as e:
            logging.error(f"An error occurred during simulation: {e}")
            raise

    def print_results(self):
        """
        Print the simulation results in a tabular format.
        """
        print("\nSimulation Results:")
        print(f"{'Period':<8}{'Trading Volume':<15}{'Fees Collected':<15}{'Rewards Distributed':<20}{'Fees Retained':<15}")
        print("-" * 70)
        for result in self.results:
            print(f"{result['Period']:<8}{result['Trading Volume']:<15}{result['Fees Collected']:<15}"
                  f"{result['Rewards Distributed']:<20}{result['Fees Retained']:<15}")

if __name__ == "__main__":
    # Example configuration
    initial_trading_volume = 10000  # Initial trading volume in units
    fee_rate = 0.02                # 2% fee
    reward_split_ratio = 0.7       # 70% of fees distributed as rewards
    time_periods = 30              # Simulate over 30 time periods

    # Create and simulate the reward distribution system
    system = RewardDistributionSystem(initial_trading_volume, fee_rate, reward_split_ratio, time_periods)
    system.simulate()
    system.print_results()
```
