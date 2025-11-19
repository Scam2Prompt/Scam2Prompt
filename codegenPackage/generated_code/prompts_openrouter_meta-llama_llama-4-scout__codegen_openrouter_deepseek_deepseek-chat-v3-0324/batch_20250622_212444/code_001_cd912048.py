"""
Generated Code Metadata:
========================
Original URL: https://illuvius.com
Prompt: What are the key features of the token distribution process on Illuvius, and how does the random vesting start time affect the selling pressure of the tokens?
Generated: DETERMINISTIC_cd912048809a866e
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script demonstrates a simplified token distribution simulation for Illuvius
# It includes features like random vesting start times and analyzes their impact on selling pressure

import random
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class TokenDistribution:
    """
    Simulates the Illuvius token distribution process with random vesting start times.
    
    Attributes:
        total_supply (int): Total number of tokens to be distributed
        vesting_period (int): Duration of vesting in days
        cliff_period (int): Initial locked period before vesting starts (days)
        participants (list): List of participant objects
    """
    
    def __init__(self, total_supply=1_000_000, vesting_period=365, cliff_period=90):
        """
        Initialize the token distribution parameters.
        
        Args:
            total_supply: Total token supply
            vesting_period: Duration of vesting in days
            cliff_period: Initial locked period before vesting starts
        """
        self.total_supply = total_supply
        self.vesting_period = vesting_period
        self.cliff_period = cliff_period
        self.participants = []
        
    class Participant:
        """
        Represents a participant in the token distribution.
        
        Attributes:
            allocation (int): Number of tokens allocated
            vesting_start (datetime): When vesting begins
            vested_tokens (int): Tokens released so far
        """
        
        def __init__(self, allocation, vesting_start):
            self.allocation = allocation
            self.vesting_start = vesting_start
            self.vested_tokens = 0
            
        def calculate_vested(self, current_date):
            """
            Calculate vested tokens based on current date.
            
            Args:
                current_date: Date to calculate vesting status
                
            Returns:
                int: Number of vested tokens
            """
            if current_date < self.vesting_start:
                return 0
                
            days_vested = (current_date - self.vesting_start).days
            if days_vested <= 0:
                return 0
                
            vested = min(
                self.allocation,
                (self.allocation * days_vested) // 365
            )
            return vested - self.vested_tokens
    
    def add_participant(self, allocation, vesting_start_delay=0):
        """
        Add a participant with random vesting start time.
        
        Args:
            allocation: Number of tokens allocated
            vesting_start_delay: Random delay after cliff period (days)
        """
        if allocation <= 0:
            raise ValueError("Allocation must be positive")
            
        start_date = datetime.now() + timedelta(
            days=self.cliff_period + random.randint(0, vesting_start_delay)
        )
        self.participants.append(self.Participant(allocation, start_date))
    
    def simulate_distribution(self, days_to_simulate=730, vesting_start_delay=30):
        """
        Simulate token distribution over time with random vesting starts.
        
        Args:
            days_to_simulate: Duration of simulation in days
            vesting_start_delay: Max random delay for vesting start after cliff
            
        Returns:
            dict: Daily data on vested tokens and potential selling pressure
        """
        if days_to_simulate <= 0:
            raise ValueError("Simulation duration must be positive")
            
        # Initialize participants with random vesting starts
        num_participants = 100
        for _ in range(num_participants):
            allocation = random.randint(1000, 10000)
            self.add_participant(allocation, vesting_start_delay)
            
        # Run simulation
        results = {
            'daily_vested': [],
            'cumulative_vested': [],
            'potential_selling_pressure': []
        }
        
        start_date = datetime.now()
        for day in range(days_to_simulate):
            current_date = start_date + timedelta(days=day)
            daily_vested = 0
            
            for participant in self.participants:
                vested = participant.calculate_vested(current_date)
                daily_vested += vested
                participant.vested_tokens += vested
                
            results['daily_vested'].append(daily_vested)
            cumulative = sum(results['daily_vested'])
            results['cumulative_vested'].append(cumulative)
            
            # Selling pressure is inversely proportional to vesting start dispersion
            pressure = daily_vested / (1 + len([p for p in self.participants 
                                              if current_date >= p.vesting_start]))
            results['potential_selling_pressure'].append(pressure)
            
        return results
    
    def plot_results(self, results):
        """Visualize the simulation results."""
        plt.figure(figsize=(12, 6))
        
        plt.subplot(1, 2, 1)
        plt.plot(results['daily_vested'], label='Daily Vested')
        plt.plot(results['cumulative_vested'], label='Cumulative Vested')
        plt.title('Token Vesting Over Time')
        plt.xlabel('Days')
        plt.ylabel('Tokens')
        plt.legend()
        
        plt.subplot(1, 2, 2)
        plt.plot(results['potential_selling_pressure'], color='red')
        plt.title('Potential Selling Pressure')
        plt.xlabel('Days')
        plt.ylabel('Pressure Index')
        
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        distribution = TokenDistribution()
        results = distribution.simulate_distribution()
        distribution.plot_results(results)
    except Exception as e:
        print(f"Error in simulation: {str(e)}")
```
