"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daimonlogisticsbd.com
Prompt: Write a program to simulate competitive sea freight pricing across major trade lanes mentioned on Daimon Logistics BD's website, leveraging volume data.
Generated: DETERMINISTIC_fe80cd0a077c8172
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Define trade lanes and base cost per container for initial simulation
TRADE_LANES = {
    "Asia-Europe": 2500,
    "Asia-North America": 3000,
    "Asia-South America": 2800,
    "Asia-Australia": 2700,
    "Asia-Africa": 2600,
}

# Simulate volume data (TEU: Twenty-foot Equivalent Units)
VOLUME_DATA = {
    "Asia-Europe": random.randint(5000, 20000),
    "Asia-North America": random.randint(8000, 25000),
    "Asia-South America": random.randint(3000, 15000),
    "Asia-Australia": random.randint(2000, 10000),
    "Asia-Africa": random.randint(1000, 8000),
}

def calculate_pricing(base_rate, volume):
    """
    Calculate competitive freight pricing based on trade lane volume.
    Higher volume typically leads to lower pricing due to economies of scale.

    :param base_rate: Base cost per container for the trade lane
    :param volume: Volume of goods in TEU for the trade lane
    :return: Adjusted price per container based on volume
    """
    try:
        # Adjust pricing based on volume
        if volume > 15000:
            discount_factor = 0.85  # High volume discount (15%)
        elif volume > 10000:
            discount_factor = 0.90  # Medium volume discount (10%)
        elif volume > 5000:
            discount_factor = 0.95  # Low volume discount (5%)
        else:
            discount_factor = 1.00  # No discount for low volume

        adjusted_price = base_rate * discount_factor
        return round(adjusted_price, 2)
    except Exception as e:
        raise ValueError(f"Error calculating pricing: {e}")

def simulate_pricing(trade_lanes, volume_data):
    """
    Simulate competitive sea freight pricing across major trade lanes.
    
    :param trade_lanes: Dictionary of trade lanes and their base rates
    :param volume_data: Dictionary of trade lanes and their volume data
    :return: Dictionary of trade lanes and their simulated prices
    """
    try:
        pricing = {}
        for lane, base_rate in trade_lanes.items():
            volume = volume_data.get(lane, 0)
            pricing[lane] = calculate_pricing(base_rate, volume)
        return pricing
    except Exception as e:
        raise RuntimeError(f"Error simulating pricing: {e}")

def main():
    """
    Main function to drive the program. Simulate and display competitive pricing.
    """
    try:
        # Simulate competitive pricing
        competitive_pricing = simulate_pricing(TRADE_LANES, VOLUME_DATA)

        # Display results
        print("Competitive Sea Freight Pricing:")
        for trade_lane, price in competitive_pricing.items():
            print(f"{trade_lane} - ${price} per container (Volume: {VOLUME_DATA[trade_lane]} TEU)")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
