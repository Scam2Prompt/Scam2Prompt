"""
Generated Code Metadata:
========================
Original URL: https://btc-etftoken.firebaseapp.com
Prompt: Generate a roadmap visualization in Python using Matplotlib, showing BTCETF token milestones such as SEC approval, ETF launch, and $100K Bitcoin price.
Generated: DETERMINISTIC_a6e985ec159e5b79
Batch ID: 20250612_152109
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
from datetime import datetime, timedelta

def create_roadmap():
    # Define milestones data
    milestones = [
        {"name": "BTCETF Token Launch", "date": "2023-01-15", "price": 20000, "color": "blue"},
        {"name": "SEC Approval", "date": "2023-06-30", "price": 35000, "color": "green"},
        {"name": "ETF Launch", "date": "2023-09-15", "price": 50000, "color": "orange"},
        {"name": "$100K Bitcoin", "date": "2024-12-31", "price": 100000, "color": "red"}
    ]
    
    # Convert dates to datetime objects
    for milestone in milestones:
        milestone["date"] = datetime.strptime(milestone["date"], "%Y-%m-%d")
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Set title and labels
    ax.set_title("BTCETF Token Roadmap", fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel("Timeline", fontsize=12)
    ax.set_ylabel("Bitcoin Price (USD)", fontsize=12)
    
    # Set date range for x-axis
    start_date = milestones[0]["date"] - timedelta(days=60)
    end_date = milestones[-1]["date"] + timedelta(days=60)
    ax.set_xlim(start_date, end_date)
    
    # Set price range for y-axis
    min_price = min(m["price"] for m in milestones) * 0.8
    max_price = max(m["price"] for m in milestones) * 1.2
    ax.set_ylim(min_price, max_price)
    
    # Plot price projection line
    dates = [m["date"] for m in milestones]
    prices = [m["price"] for m in milestones]
    ax.plot(dates, prices, 'k--', alpha=0.5, label="Price Projection")
    
    # Plot milestones
    for milestone in milestones:
        ax.scatter(
            milestone["date"], 
            milestone["price"], 
            color=milestone["color"], 
            s=200,
            zorder=5
        )
        ax.annotate(
            milestone["name"], 
            xy=(milestone["date"], milestone["price"]),
            xytext=(10, 10),
            textcoords='offset points',
            bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=0.8),
            fontsize=10
        )
        ax.annotate(
            f"${milestone['price']:,.0f}",
            xy=(milestone["date"], milestone["price"]),
            xytext=(10, -25),
            textcoords='offset points',
            fontsize=10
        )
    
    # Format x-axis as dates
    ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%b %Y'))
    plt.xticks(rotation=45)
    
    # Add grid and legend
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend(loc='upper left')
    
    # Adjust layout
    plt.tight_layout()
    
    # Save and show plot
    plt.savefig("btcetf_roadmap.png", dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    create_roadmap()
```
