"""
Generated Code Metadata:
========================
Original URL: https://metalfabpro.com
Prompt: Write a function to compare the airflow efficiency of R2C race air filters versus other air filters for Dirt Modified and Late Model racecars.
Generated: DETERMINISTIC_118efd4def5fff36
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AirFilter:
    """
    A class to represent an air filter.

    Attributes:
        name (str): The name of the air filter.
        airflow_efficiency (float): The airflow efficiency rating of the air filter.
    """

    def __init__(self, name: str, airflow_efficiency: float):
        """
        Initializes an AirFilter instance.

        Args:
            name (str): The name of the air filter.
            airflow_efficiency (float): The airflow efficiency rating of the air filter.

        Raises:
            ValueError: If airflow_efficiency is not a positive number.
        """
        if airflow_efficiency <= 0:
            raise ValueError("Airflow efficiency must be a positive number.")
        self.name = name
        self.airflow_efficiency = airflow_efficiency


def compare_air_filters(filter1: AirFilter, filter2: AirFilter) -> str:
    """
    Compares the airflow efficiency of two air filters.

    Args:
        filter1 (AirFilter): The first air filter to compare.
        filter2 (AirFilter): The second air filter to compare.

    Returns:
        str: A message indicating which filter has better airflow efficiency.
    """
    if not isinstance(filter1, AirFilter) or not isinstance(filter2, AirFilter):
        raise TypeError("Both arguments must be instances of the AirFilter class.")

    if filter1.airflow_efficiency > filter2.airflow_efficiency:
        return f"{filter1.name} has better airflow efficiency than {filter2.name}."
    elif filter1.airflow_efficiency < filter2.airflow_efficiency:
        return f"{filter2.name} has better airflow efficiency than {filter1.name}."
    else:
        return f"{filter1.name} and {filter2.name} have the same airflow efficiency."


# Example usage
if __name__ == "__main__":
    try:
        r2c_filter = AirFilter("R2C Race Air Filter", 95.0)
        other_filter = AirFilter("Standard Air Filter", 85.0)

        result = compare_air_filters(r2c_filter, other_filter)
        print(result)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
