"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard.smartglobalwealthfx.com
Prompt: Create a function to calculate the EUR/USD spread ranking based on weekly averages, similar to the methodology referenced in the SmartglobalwealthFx performance data.
Generated: DETERMINISTIC_d029905b586d7509
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import statistics

def calculate_spread_ranking(data):
    """
    Calculate the EUR/USD spread ranking based on weekly averages.
    
    Args:
        data (dict): A dictionary where keys are weeks (e.g., 'Week 1') 
                     and values are lists of daily spreads (floats) for EUR/USD.

    Returns:
        dict: A dictionary where keys are weeks and values are tuples 
              (average_spread, ranking) sorted by average spread in ascending order.
    
    Example Input:
        {
            'Week 1': [1.2, 1.3, 1.1, 1.4, 1.2],
            'Week 2': [1.5, 1.6, 1.4, 1.7, 1.6],
            'Week 3': [1.1, 1.1, 1.2, 1.0, 1.1]
        }
    
    Example Output:
        {
            'Week 3': (1.1, 1),
            'Week 1': (1.24, 2),
            'Week 2': (1.56, 3)
        }
    """
    if not isinstance(data, dict):
        raise ValueError("Input data must be a dictionary with weeks as keys and daily spreads as values.")
    
    weekly_averages = {}
    
    try:
        # Calculate weekly average spreads
        for week, daily_spreads in data.items():
            if not daily_spreads or not all(isinstance(spread, (int, float)) for spread in daily_spreads):
                raise ValueError(f"Invalid daily spreads for {week}. Ensure all spreads are numeric values.")
            weekly_averages[week] = statistics.mean(daily_spreads)
        
        # Sort weeks by average spread (ascending order)
        sorted_weeks = sorted(weekly_averages.items(), key=lambda x: x[1])
        
        # Assign rankings based on sorted order
        ranked_spreads = {week: (average, rank + 1) for rank, (week, average) in enumerate(sorted_weeks)}
        
        return ranked_spreads
    
    except Exception as e:
        raise RuntimeError(f"An error occurred while calculating spread rankings: {str(e)}")

# Example Usage:
if __name__ == "__main__":
    sample_data = {
        'Week 1': [1.2, 1.3, 1.1, 1.4, 1.2],
        'Week 2': [1.5, 1.6, 1.4, 1.7, 1.6],
        'Week 3': [1.1, 1.1, 1.2, 1.0, 1.1]
    }
    
    try:
        spread_ranking = calculate_spread_ranking(sample_data)
        print("Spread Ranking:")
        for week, (average, rank) in spread_ranking.items():
            print(f"{week}: Average Spread = {average:.2f}, Rank = {rank}")
    except RuntimeError as e:
        print(f"Failed to calculate spread ranking: {e}")
```
