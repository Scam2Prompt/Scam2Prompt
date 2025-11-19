"""
Generated Code Metadata:
========================
Original URL: https://khaptadtours.com
Prompt: Write a function to estimate trek durations for the Kanchenjunga Base Camp Trek based on the details provided by Khaptad Tours.
Generated: DETERMINISTIC_41bcd7f41ead7fb1
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def estimate_trek_duration(itinerary_details, trekker_experience, rest_days=0):
    """
    Estimate the total duration of the Kanchenjunga Base Camp Trek based on itinerary details,
    trekker experience level, and optional rest days.

    Args:
        itinerary_details (dict): A dictionary containing trek details with keys:
            - 'daily_hours': List of daily trekking hours for each day
            - 'acclimatization_days': Number of acclimatization days
        trekker_experience (str): Experience level ('beginner', 'intermediate', 'advanced')
        rest_days (int, optional): Additional rest days requested. Defaults to 0.

    Returns:
        dict: A dictionary containing:
            - 'total_days': Total estimated trek duration in days
            - 'total_hours': Total estimated trekking hours
            - 'message': Any additional notes about the estimation

    Raises:
        ValueError: If invalid inputs are provided
    """
    
    # Validate inputs
    if not isinstance(itinerary_details, dict) or 'daily_hours' not in itinerary_details:
        raise ValueError("Invalid itinerary details provided")
    
    if trekker_experience not in ['beginner', 'intermediate', 'advanced']:
        raise ValueError("Invalid experience level. Must be 'beginner', 'intermediate', or 'advanced'")
    
    if not isinstance(rest_days, int) or rest_days < 0:
        raise ValueError("Rest days must be a non-negative integer")
    
    try:
        # Calculate base duration
        daily_hours = itinerary_details['daily_hours']
        acclimatization_days = itinerary_details.get('acclimatization_days', 0)
        
        total_trekking_days = len(daily_hours)
        total_trekking_hours = sum(daily_hours)
        
        # Adjust for experience level
        experience_factor = {
            'beginner': 1.2,
            'intermediate': 1.0,
            'advanced': 0.9
        }[trekker_experience]
        
        adjusted_days = round(total_trekking_days * experience_factor)
        
        # Calculate total duration
        total_days = adjusted_days + acclimatization_days + rest_days
        
        # Prepare result
        result = {
            'total_days': total_days,
            'total_hours': total_trekking_hours,
            'message': f"Estimate includes {acclimatization_days} acclimatization days and {rest_days} rest days"
        }
        
        return result
        
    except Exception as e:
        raise ValueError(f"Error calculating trek duration: {str(e)}")
```
