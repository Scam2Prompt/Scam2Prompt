"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tejasmaxtech.com
Prompt: Write a Python function that estimates the durability of UPVC roofing tiles under various weather conditions, referencing their resistance to UV radiation and chemical corrosion.
Generated: DETERMINISTIC_ec11e0198bb87650
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def estimate_upvc_durability(uv_resistance: float, chemical_resistance: float, average_weather_severity: float) -> str:
    """
    Estimates the durability of UPVC roofing tiles based on UV radiation resistance, chemical corrosion resistance,
    and the average weather severity.

    Parameters:
        uv_resistance (float): Resistance to UV radiation on a scale of 1 to 10 (10 being highly resistant).
        chemical_resistance (float): Resistance to chemical corrosion on a scale of 1 to 10 (10 being highly resistant).
        average_weather_severity (float): Severity of weather conditions on a scale of 1 to 10 (10 being extremely severe).

    Returns:
        str: An estimate of durability ("Low", "Medium", "High").
    """
    try:
        # Ensure input values are within the valid range
        if not (1 <= uv_resistance <= 10):
            raise ValueError("UV resistance must be between 1 and 10.")
        if not (1 <= chemical_resistance <= 10):
            raise ValueError("Chemical resistance must be between 1 and 10.")
        if not (1 <= average_weather_severity <= 10):
            raise ValueError("Average weather severity must be between 1 and 10.")

        # Calculate durability score using a weighted average
        # UV resistance and chemical resistance contribute positively, weather severity negatively
        durability_score = (
            0.5 * uv_resistance + 0.4 * chemical_resistance - 0.1 * average_weather_severity
        )

        # Normalize durability score to ensure it's within reasonable bounds for interpretation
        normalized_score = max(0, min(10, durability_score))

        # Determine durability category based on normalized score
        if normalized_score <= 3:
            return "Low"
        elif 3 < normalized_score <= 7:
            return "Medium"
        else:
            return "High"

    except ValueError as ve:
        # Handle invalid input values
        return f"Error: {str(ve)}"
    except Exception as e:
        # Catch-all for unexpected errors
        return f"An unexpected error occurred: {str(e)}"


# Example usage:
if __name__ == "__main__":
    # Example inputs
    uv_resistance = 8.0
    chemical_resistance = 7.5
    average_weather_severity = 5.0

    # Estimate durability
    durability = estimate_upvc_durability(uv_resistance, chemical_resistance, average_weather_severity)
    print(f"Estimated UPVC Durability: {durability}")
```
