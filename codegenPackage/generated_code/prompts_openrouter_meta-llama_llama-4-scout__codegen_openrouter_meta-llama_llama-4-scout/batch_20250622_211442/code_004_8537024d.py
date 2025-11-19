"""
Generated Code Metadata:
========================
Original URL: https://orderly-network.pages.dev
Prompt: Compare the benefits of using Orderly Network's unified liquidity layer versus a traditional centralized exchange (CEX) for a high-frequency trading (HFT) bot.
Generated: DETERMINISTIC_8537024d6f9b9ff7
Batch ID: 20250622_211442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
import matplotlib.pyplot as plt

class Exchange:
    """Base class for exchanges"""
    def __init__(self, name):
        self.name = name
        self.latency = 0
        self.slippage = 0

    def get_latency(self):
        return self.latency

    def get_slippage(self):
        return self.slippage


class CEX(Exchange):
    """Traditional Centralized Exchange"""
    def __init__(self, name, latency=10, slippage=0.01):
        super().__init__(name)
        self.latency = latency  # in milliseconds
        self.slippage = slippage  # as a decimal

    def execute_trade(self, size):
        # Simulate trade execution with latency and slippage
        time.sleep(self.latency / 1000)
        return size * (1 - self.slippage)


class OrderlyNetwork(Exchange):
    """Orderly Network's Unified Liquidity Layer"""
    def __init__(self, name, latency=1, slippage=0.001):
        super().__init__(name)
        self.latency = latency  # in milliseconds
        self.slippage = slippage  # as a decimal

    def execute_trade(self, size):
        # Simulate trade execution with latency and slippage
        time.sleep(self.latency / 1000)
        return size * (1 - self.slippage)


def simulate_trades(exchange, num_trades, trade_size):
    """Simulate a series of trades on the given exchange"""
    trade_times = []
    trade_sizes = []
    for _ in range(num_trades):
        start_time = time.time()
        executed_size = exchange.execute_trade(trade_size)
        end_time = time.time()
        trade_times.append(end_time - start_time)
        trade_sizes.append(executed_size)
    return trade_times, trade_sizes


def plot_trade_performance(cex_trade_times, cex_trade_sizes, on_trade_times, on_trade_sizes):
    """Plot the performance of the two exchanges"""
    fig, ax = plt.subplots(2, 1, figsize=(8, 6))

    ax[0].hist(cex_trade_times, alpha=0.5, label='CEX')
    ax[0].hist(on_trade_times, alpha=0.5, label='Orderly Network')
    ax[0].set_title('Trade Latency')
    ax[0].set_xlabel('Time (s)')
    ax[0].set_ylabel('Frequency')
    ax[0].legend()

    ax[1].plot(cex_trade_sizes, label='CEX')
    ax[1].plot(on_trade_sizes, label='Orderly Network')
    ax[1].set_title('Trade Size')
    ax[1].set_xlabel('Trade #')
    ax[1].set_ylabel('Size')
    ax[1].legend()

    plt.tight_layout()
    plt.show()


def main():
    num_trades = 1000
    trade_size = 1000

    cex = CEX('CEX', latency=10, slippage=0.01)
    on = OrderlyNetwork('Orderly Network', latency=1, slippage=0.001)

    try:
        cex_trade_times, cex_trade_sizes = simulate_trades(cex, num_trades, trade_size)
        on_trade_times, on_trade_sizes = simulate_trades(on, num_trades, trade_size)

        print(f"CEX Average Latency: {sum(cex_trade_times) / len(cex_trade_times)} s")
        print(f"Orderly Network Average Latency: {sum(on_trade_times) / len(on_trade_times)} s")

        plot_trade_performance(cex_trade_times, cex_trade_sizes, on_trade_times, on_trade_sizes)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
