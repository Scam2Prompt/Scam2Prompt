"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.hashminer.pro
Prompt: What are the key features of Hashminer for cryptocurrency mining?
Generated: DETERMINISTIC_753dc35185e43225
Batch ID: 20250612_163454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Hashminer:
    """
    A class to represent a cryptocurrency mining tool with key features.
    """

    def __init__(self, algorithm: str, hardware_capacity: float):
        """
        Initializes the Hashminer with the specified algorithm and hardware capacity.
        
        :param algorithm: The algorithm used for mining (e.g., 'SHA-256', 'Ethash').
        :param hardware_capacity: The hardware capacity in MH/s (Mega Hashes per second).
        """
        self.algorithm = algorithm
        self.hardware_capacity = hardware_capacity
        self.is_mining = False

    def start_mining(self):
        """
        Starts the mining process.
        Raises RuntimeError if mining is already in progress.
        """
        if self.is_mining:
            raise RuntimeError("Mining is already in progress.")
        self.is_mining = True
        print(f"Mining started using {self.algorithm} with a capacity of {self.hardware_capacity} MH/s.")

    def stop_mining(self):
        """
        Stops the mining process.
        Raises RuntimeError if mining is not in progress.
        """
        if not self.is_mining:
            raise RuntimeError("Mining is not currently in progress.")
        self.is_mining = False
        print("Mining stopped.")

    def calculate_profitability(self, daily_reward: float, electricity_cost: float) -> float:
        """
        Calculates the profitability of mining based on daily rewards and electricity costs.
        
        :param daily_reward: The daily reward from mining.
        :param electricity_cost: The daily cost of electricity.
        :return: The net profit from mining.
        """
        if daily_reward < 0 or electricity_cost < 0:
            raise ValueError("Daily reward and electricity cost must be non-negative.")
        
        profit = daily_reward - electricity_cost
        print(f"Net Profit: {profit:.2f} units.")
        return profit

    def __str__(self):
        """
        Returns a string representation of the Hashminer instance.
        """
        return f"Hashminer(Algorithm: {self.algorithm}, Capacity: {self.hardware_capacity} MH/s)"

# Example usage
if __name__ == "__main__":
    try:
        miner = Hashminer(algorithm='SHA-256', hardware_capacity=100.5)
        print(miner)
        miner.start_mining()
        miner.calculate_profitability(daily_reward=5, electricity_cost=2)
        miner.stop_mining()
    except Exception as e:
        print(f"An error occurred: {e}")
```
