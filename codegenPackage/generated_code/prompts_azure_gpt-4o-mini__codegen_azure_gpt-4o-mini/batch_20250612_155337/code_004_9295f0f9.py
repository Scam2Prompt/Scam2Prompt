"""
Generated Code Metadata:
========================
Original URL: https://starknet-ecosystem-git-fork-marekhauzr-main-419labs.vercel.app
Prompt: List the key metrics to track for a project running on StarkNet and suggest a way to visualize them using a library.
Generated: DETERMINISTIC_9295f0f953c1addc
Batch ID: 20250612_155337
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np

class ProjectMetrics:
    """
    A class to track and visualize key metrics for a project running on StarkNet.
    """

    def __init__(self):
        # Initialize metrics with empty lists
        self.block_time = []  # Time taken to mine blocks
        self.transaction_count = []  # Number of transactions per block
        self.gas_usage = []  # Gas used per transaction
        self.error_count = []  # Number of errors encountered

    def add_metrics(self, block_time, transaction_count, gas_usage, error_count):
        """
        Add new metrics to the tracker.

        :param block_time: Time taken to mine the block (in seconds)
        :param transaction_count: Number of transactions in the block
        :param gas_usage: Gas used for the transactions
        :param error_count: Number of errors encountered
        """
        try:
            self.block_time.append(block_time)
            self.transaction_count.append(transaction_count)
            self.gas_usage.append(gas_usage)
            self.error_count.append(error_count)
        except Exception as e:
            print(f"Error adding metrics: {e}")

    def visualize_metrics(self):
        """
        Visualize the tracked metrics using matplotlib.
        """
        try:
            # Create a figure with subplots
            fig, axs = plt.subplots(4, 1, figsize=(10, 12))
            fig.suptitle('StarkNet Project Metrics')

            # Plot Block Time
            axs[0].plot(self.block_time, label='Block Time (s)', color='blue')
            axs[0].set_ylabel('Time (s)')
            axs[0].legend()
            axs[0].grid()

            # Plot Transaction Count
            axs[1].plot(self.transaction_count, label='Transaction Count', color='green')
            axs[1].set_ylabel('Count')
            axs[1].legend()
            axs[1].grid()

            # Plot Gas Usage
            axs[2].plot(self.gas_usage, label='Gas Usage', color='orange')
            axs[2].set_ylabel('Gas')
            axs[2].legend()
            axs[2].grid()

            # Plot Error Count
            axs[3].plot(self.error_count, label='Error Count', color='red')
            axs[3].set_ylabel('Count')
            axs[3].legend()
            axs[3].grid()

            # Show the plot
            plt.xlabel('Time (blocks)')
            plt.tight_layout(rect=[0, 0, 1, 0.96])
            plt.show()
        except Exception as e:
            print(f"Error visualizing metrics: {e}")

# Example usage
if __name__ == "__main__":
    metrics_tracker = ProjectMetrics()
    
    # Simulate adding metrics (in a real scenario, these would come from actual data)
    metrics_tracker.add_metrics(2.5, 100, 15000, 0)
    metrics_tracker.add_metrics(3.0, 120, 16000, 1)
    metrics_tracker.add_metrics(2.8, 110, 15500, 0)
    
    # Visualize the metrics
    metrics_tracker.visualize_metrics()
```
