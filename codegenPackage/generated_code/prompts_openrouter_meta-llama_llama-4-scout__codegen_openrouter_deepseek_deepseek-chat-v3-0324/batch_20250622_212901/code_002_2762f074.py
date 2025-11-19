"""
Generated Code Metadata:
========================
Original URL: https://elitebody.com.br
Prompt: Generate a code snippet to calculate the equivalent time savings of electrostimulation training compared to traditional muscle training, using data from Elite Body's website (e.g., 20 minutes vs. 3 hours).
Generated: DETERMINISTIC_2762f074e0be7e61
Batch ID: 20250622_212901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_time_savings(ems_time: float, traditional_time: float) -> dict:
    """
    Calculate the equivalent time savings of electrostimulation training (EMS) 
    compared to traditional muscle training.
    
    Args:
        ems_time (float): Time spent in EMS training (in minutes).
        traditional_time (float): Time spent in traditional training (in minutes).
    
    Returns:
        dict: Dictionary containing:
            - time_saved: Absolute time saved in minutes
            - time_saved_percentage: Percentage of time saved
            - equivalent_traditional_time: Equivalent traditional training time
            - equivalent_ems_time: Equivalent EMS training time
    
    Raises:
        ValueError: If either time input is zero or negative
    """
    if ems_time <= 0 or traditional_time <= 0:
        raise ValueError("Training times must be positive numbers")
    
    time_saved = traditional_time - ems_time
    time_saved_percentage = (time_saved / traditional_time) * 100
    equivalent_traditional_time = traditional_time
    equivalent_ems_time = ems_time
    
    return {
        "time_saved": time_saved,
        "time_saved_percentage": round(time_saved_percentage, 2),
        "equivalent_traditional_time": equivalent_traditional_time,
        "equivalent_ems_time": equivalent_ems_time
    }

# Example usage
if __name__ == "__main__":
    try:
        ems_time = 20  # minutes
        traditional_time = 180  # minutes (3 hours)
        result = calculate_time_savings(ems_time, traditional_time)
        
        print(f"Time saved: {result['time_saved']} minutes")
        print(f"Percentage saved: {result['time_saved_percentage']}%")
        print(f"20 mins EMS = {result['equivalent_traditional_time']} mins traditional")
        print(f"{result['equivalent_traditional_time']} mins traditional = 20 mins EMS")
    except ValueError as e:
        print(f"Error: {e}")
```
