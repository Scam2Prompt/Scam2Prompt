"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigen-labs-287829331544c3a3caa5f5b77a00.webflow.io
Prompt: Develop a simulation model in Python to demonstrate the infinite horizon game concept described by Eigen Labs, using EigenLayer as the core protocol.
Generated: DETERMINISTIC_fd7f763fa0b37ee1
Batch ID: 20250612_154157
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class EigenLayer:
    def __init__(self, initial_stake: float, reward_rate: float, decay_rate: float):
        """
        Initialize the EigenLayer with the given parameters.
        
        :param initial_stake: Initial amount of stake in the system.
        :param reward_rate: Rate at which rewards are generated.
        :param decay_rate: Rate at which the stake decays over time.
        """
        self.stake = initial_stake
        self.reward_rate = reward_rate
        self.decay_rate = decay_rate
        self.total_rewards = 0.0

    def simulate_time_step(self, time: float):
        """
        Simulate a time step in the EigenLayer, updating stake and rewards.
        
        :param time: The time increment for this simulation step.
        """
        # Calculate rewards based on current stake
        rewards = self.stake * self.reward_rate * time
        self.total_rewards += rewards
        
        # Update the stake by applying decay
        self.stake -= self.stake * self.decay_rate * time
        
        # Ensure stake does not go below zero
        self.stake = max(self.stake, 0)

    def get_stake(self) -> float:
        """
        Get the current stake in the EigenLayer.
        
        :return: Current stake value.
        """
        return self.stake

    def get_total_rewards(self) -> float:
        """
        Get the total rewards accumulated in the EigenLayer.
        
        :return: Total rewards value.
        """
        return self.total_rewards

def run_simulation(initial_stake: float, reward_rate: float, decay_rate: float, total_time: float, time_step: float):
    """
    Run the simulation for the EigenLayer over a specified total time.
    
    :param initial_stake: Initial amount of stake.
    :param reward_rate: Rate of reward generation.
    :param decay_rate: Rate of decay for the stake.
    :param total_time: Total time for the simulation.
    :param time_step: Time increment per simulation step.
    :return: Lists of time points, stake values, and total rewards.
    """
    eigen_layer = EigenLayer(initial_stake, reward_rate, decay_rate)
    
    time_points = []
    stake_values = []
    rewards_values = []

    current_time = 0.0
    
    while current_time <= total_time:
        # Simulate a time step
        eigen_layer.simulate_time_step(time_step)
        
        # Record the results
        time_points.append(current_time)
        stake_values.append(eigen_layer.get_stake())
        rewards_values.append(eigen_layer.get_total_rewards())

        # Increment time
        current_time += time_step

    return time_points, stake_values, rewards_values

def plot_results(time_points, stake_values, rewards_values):
    """
    Plot the results of the simulation.
    
    :param time_points: List of time points for the simulation.
    :param stake_values: List of stake values over time.
    :param rewards_values: List of total rewards over time.
    """
    plt.figure(figsize=(14, 7))
    
    # Plot stake values
    plt.subplot(2, 1, 1)
    plt.plot(time_points, stake_values, label='Stake Value', color='blue')
    plt.title("Stake Value Over Time")
    plt.xlabel("Time")
    plt.ylabel("Stake Value")
    plt.grid()
    plt.legend()

    # Plot rewards values
    plt.subplot(2, 1, 2)
    plt.plot(time_points, rewards_values, label='Total Rewards', color='green')
    plt.title("Total Rewards Over Time")
    plt.xlabel("Time")
    plt.ylabel("Total Rewards")
    plt.grid()
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    try:
        # Define simulation parameters
        INITIAL_STAKE = 1000.0
        REWARD_RATE = 0.05  # 5% reward per time unit
        DECAY_RATE = 0.02    # 2% decay per time unit
        TOTAL_TIME = 100.0   # Total time to run the simulation
        TIME_STEP = 1.0      # Time increment for each step

        # Run the simulation
        time_points, stake_values, rewards_values = run_simulation(
            INITIAL_STAKE, REWARD_RATE, DECAY_RATE, TOTAL_TIME, TIME_STEP
        )

        # Plot the results
        plot_results(time_points, stake_values, rewards_values)
    
    except Exception as e:
        print(f"An error occurred during simulation: {e}")
```
