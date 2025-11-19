"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Write Python code to calculate carpet room foot traffic star ratings based on the "6 Star Classification System" described on Perfect Melbourne Carpet's website. Include logic for light, medium, heavy, and extra heavy traffic flow.
Generated: DETERMINISTIC_af089cd938d31022
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class TrafficFlow(Enum):
    """ Enum representing traffic flow levels """
    LIGHT = 1
    MEDIUM = 2
    HEAVY = 3
    EXTRA_HEAVY = 4

class CarpetStarRating(Enum):
    """ Enum representing carpet star ratings """
    ONE_STAR = 1
    TWO_STAR = 2
    THREE_STAR = 3
    FOUR_STAR = 4
    FIVE_STAR = 5
    SIX_STAR = 6

def calculate_carpet_star_rating(traffic_flow: TrafficFlow) -> CarpetStarRating:
    """
    Calculate carpet star rating based on traffic flow.

    The 6 Star Classification System is as follows:
    - Light traffic: 4-6 star
    - Medium traffic: 3-5 star
    - Heavy traffic: 2-4 star
    - Extra Heavy traffic: 1-3 star

    Args:
        traffic_flow (TrafficFlow): The traffic flow level.

    Returns:
        CarpetStarRating: The calculated carpet star rating.
    """
    traffic_flow_star_ratings: Dict[TrafficFlow, range] = {
        TrafficFlow.LIGHT: range(4, 7),
        TrafficFlow.MEDIUM: range(3, 6),
        TrafficFlow.HEAVY: range(2, 5),
        TrafficFlow.EXTRA_HEAVY: range(1, 4)
    }

    star_rating_range = traffic_flow_star_ratings.get(traffic_flow)
    if star_rating_range is None:
        raise ValueError("Invalid traffic flow level")

    # For simplicity, we will return the highest star rating for each traffic flow level
    return CarpetStarRating(star_rating_range.stop - 1)

def main():
    try:
        traffic_flows = [
            TrafficFlow.LIGHT,
            TrafficFlow.MEDIUM,
            TrafficFlow.HEAVY,
            TrafficFlow.EXTRA_HEAVY
        ]

        for traffic_flow in traffic_flows:
            star_rating = calculate_carpet_star_rating(traffic_flow)
            print(f"Traffic Flow: {traffic_flow.name}, Star Rating: {star_rating.name}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
