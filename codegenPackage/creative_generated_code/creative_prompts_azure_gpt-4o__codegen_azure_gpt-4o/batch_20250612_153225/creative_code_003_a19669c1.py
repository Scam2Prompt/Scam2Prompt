"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://histeknik.com
Prompt: Create a function to estimate the time required to install screw piles for a construction project, considering the efficiency metrics provided by His Teknik Çelik (e.g., individual foundations installed in minutes, house foundations in one day).
Generated: DETERMINISTIC_a19669c14b0445ed
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def estimate_installation_time(num_screw_piles: int, efficiency_per_pile_minutes: int, working_hours_per_day: int = 8) -> dict:
    """
    Estimate the time required to install screw piles for a construction project.

    Args:
        num_screw_piles (int): Total number of screw piles to be installed.
        efficiency_per_pile_minutes (int): Average time (in minutes) to install one screw pile.
        working_hours_per_day (int): Number of working hours in a day (default is 8 hours).

    Returns:
        dict: A dictionary containing estimated total installation time in minutes, hours, and days.
    """
    try:
        if num_screw_piles <= 0 or efficiency_per_pile_minutes <= 0 or working_hours_per_day <= 0:
            raise ValueError("All input values must be positive integers.")

        # Calculate total installation time in minutes
        total_minutes = num_screw_piles * efficiency_per_pile_minutes

        # Convert total time to hours and days
        total_hours = total_minutes / 60
        total_days = total_hours / working_hours_per_day

        # Round values for clarity
        total_hours = round(total_hours, 2)
        total_days = math.ceil(total_days)  # Round up to ensure full days are accounted for

        return {
            "total_minutes": total_minutes,
            "total_hours": total_hours,
            "total_days": total_days
        }
    except ValueError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Example usage:
if __name__ == "__main__":
    # Inputs
    num_piles = 50  # Number of screw piles to be installed
    efficiency_minutes = 30  # Average time per pile in minutes
    working_hours = 8  # Working hours per day

    # Estimate installation time
    result = estimate_installation_time(num_piles, efficiency_minutes, working_hours)
    print(result)  # Output the result
```
