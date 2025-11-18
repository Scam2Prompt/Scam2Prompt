"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://test.coin-bubbles.com
Prompt: Write code to create an interactive bubble chart for visualizing cryptocurrency market data, similar to the visualizations described on Coin Bubbles.
Generated: DETERMINISTIC_4d576383442d8dff
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Sample cryptocurrency market data (replace with actual data for production use)
crypto_data = [
    {"name": "Bitcoin", "symbol": "BTC", "market_cap": 800_000_000_000, "price": 20000},
    {"name": "Ethereum", "symbol": "ETH", "market_cap": 400_000_000_000, "price": 1500},
    {"name": "Cardano", "symbol": "ADA", "market_cap": 15_000_000_000, "price": 0.40},
    {"name": "Dogecoin", "symbol": "DOGE", "market_cap": 10_000_000_000, "price": 0.08},
    {"name": "Polkadot", "symbol": "DOT", "market_cap": 8_000_000_000, "price": 6},
]

# Function to simulate dynamic data changes (replace with real-time API updates for production)
def update_crypto_data(crypto_data):
    for crypto in crypto_data:
        # Simulate price fluctuations
        crypto["price"] = round(crypto["price"] * (1 + random.uniform(-0.05, 0.05)), 2)
        # Simulate market cap changes based on price fluctuation
        crypto["market_cap"] = int(crypto["market_cap"] * (1 + random.uniform(-0.05, 0.05)))

# Initialize the figure
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title("Cryptocurrency Market Bubble Chart", fontsize=16)
ax.set_xlabel("Price (USD)", fontsize=12)
ax.set_ylabel("Market Cap (USD)", fontsize=12)
ax.set_xscale("log")  # Log scale for better spread visualization
ax.set_yscale("log")

# Function to update the bubble chart dynamically
def update(frame):
    ax.clear()  # Clear the previous frame
    ax.set_title("Cryptocurrency Market Bubble Chart", fontsize=16)
    ax.set_xlabel("Price (USD)", fontsize=12)
    ax.set_ylabel("Market Cap (USD)", fontsize=12)
    ax.set_xscale("log")
    ax.set_yscale("log")

    update_crypto_data(crypto_data)  # Simulate data changes

    # Extract data for plotting
    prices = [crypto["price"] for crypto in crypto_data]
    market_caps = [crypto["market_cap"] for crypto in crypto_data]
    sizes = [crypto["market_cap"] / 10_000_000 for crypto in crypto_data]  # Scale bubble sizes
    names = [crypto["symbol"] for crypto in crypto_data]

    # Create bubble chart
    scatter = ax.scatter(prices, market_caps, s=sizes, alpha=0.6, edgecolors="w", linewidth=2)

    # Annotate bubbles with cryptocurrency symbols
    for i, name in enumerate(names):
        ax.annotate(name, (prices[i], market_caps[i]), fontsize=10, ha="center", va="center")

# Define the animation
ani = animation.FuncAnimation(fig, update, interval=1000)  # Update every second

# Display the chart
plt.show()
```
