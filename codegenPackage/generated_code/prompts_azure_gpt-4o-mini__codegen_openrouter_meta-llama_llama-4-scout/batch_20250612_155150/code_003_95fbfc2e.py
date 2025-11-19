"""
Generated Code Metadata:
========================
Original URL: https://fuelinjectorservices.com.au
Prompt: Generate a Python script that calculates the performance improvement after cleaning fuel injectors based on contamination levels.
Generated: DETERMINISTIC_95fbfc2e513f1f06
Batch ID: 20250612_155150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Fuel Injector Performance Improvement Calculator

Calculates the performance improvement after cleaning fuel injectors based on contamination levels.
"""

def calculate_performance_improvement(contamination_level_before, contamination_level_after):
    """
    Calculate the performance improvement after cleaning fuel injectors.

    Args:
        contamination_level_before (float): Contamination level before cleaning (in %).
        contamination_level_after (float): Contamination level after cleaning (in %).

    Returns:
        float: Performance improvement (in %).

    Raises:
        ValueError: If contamination levels are not within the valid range (0-100).
    """
    if not (0 <= contamination_level_before <= 100) or not (0 <= contamination_level_after <= 100):
        raise ValueError("Contamination levels must be between 0 and 100")

    if contamination_level_before < contamination_level_after:
        raise ValueError("Contamination level after cleaning cannot be higher than before")

    performance_improvement = ((contamination_level_before - contamination_level_after) / contamination_level_before) * 100
    return performance_improvement


def main():
    try:
        contamination_level_before = float(input("Enter contamination level before cleaning (in %): "))
        contamination_level_after = float(input("Enter contamination level after cleaning (in %): "))

        performance_improvement = calculate_performance_improvement(contamination_level_before, contamination_level_after)

        print(f"Performance improvement: {performance_improvement:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
