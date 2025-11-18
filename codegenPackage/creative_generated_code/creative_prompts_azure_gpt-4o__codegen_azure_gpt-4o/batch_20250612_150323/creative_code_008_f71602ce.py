"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.gr
Prompt: Generate a Python function to calculate maintenance schedules for a fleet of RIBs based on usage frequency and maritime safety standards, as described by OpenSea's services.
Generated: DETERMINISTIC_f71602ce3dab33ec
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

def calculate_maintenance_schedule(rib_usage_data, safety_standard_days=365, usage_threshold_hours=500):
    """
    Calculate maintenance schedules for a fleet of RIBs (Rigid Inflatable Boats).

    Parameters:
        rib_usage_data (list of dict): A list of dictionaries where each dictionary represents a RIB and contains:
            - 'id' (str): The unique identifier of the RIB.
            - 'last_maintenance_date' (str): The last maintenance date in 'YYYY-MM-DD' format.
            - 'hours_used_since_last_maintenance' (int): The number of operating hours since the last maintenance.
        safety_standard_days (int): The maximum number of days allowed between maintenance as per maritime safety standards.
        usage_threshold_hours (int): The maximum operating hours allowed between maintenance.

    Returns:
        list of dict: A list of dictionaries where each dictionary represents a RIB's maintenance schedule, including:
            - 'id' (str): The unique identifier of the RIB.
            - 'next_maintenance_date' (str): The next maintenance date in 'YYYY-MM-DD' format.
            - 'requires_immediate_maintenance' (bool): Whether the RIB requires immediate maintenance.
    """
    maintenance_schedules = []

    for rib in rib_usage_data:
        try:
            # Parse the last maintenance date
            last_maintenance_date = datetime.strptime(rib['last_maintenance_date'], '%Y-%m-%d')
            
            # Calculate the next maintenance date based on safety standards
            next_maintenance_date_by_time = last_maintenance_date + timedelta(days=safety_standard_days)
            
            # Calculate days remaining until the next maintenance date
            days_since_last_maintenance = (datetime.now() - last_maintenance_date).days
            requires_maintenance_by_time = days_since_last_maintenance >= safety_standard_days

            # Check if maintenance is required based on usage
            requires_maintenance_by_usage = rib['hours_used_since_last_maintenance'] >= usage_threshold_hours
            
            # Determine if maintenance is immediately required
            requires_immediate_maintenance = requires_maintenance_by_time or requires_maintenance_by_usage
            
            # Determine the earliest of the two maintenance requirements
            if requires_immediate_maintenance:
                next_maintenance_date = datetime.now()
            else:
                next_maintenance_date = min(
                    next_maintenance_date_by_time,
                    last_maintenance_date + timedelta(
                        days=(usage_threshold_hours / rib['hours_used_since_last_maintenance']) * days_since_last_maintenance
                    )
                )
            
            # Format the next maintenance date as a string
            next_maintenance_date_str = next_maintenance_date.strftime('%Y-%m-%d')
            
            # Add the maintenance schedule for this RIB
            maintenance_schedules.append({
                'id': rib['id'],
                'next_maintenance_date': next_maintenance_date_str,
                'requires_immediate_maintenance': requires_immediate_maintenance
            })
        except (KeyError, ValueError, TypeError) as e:
            # Handle errors gracefully and log them
            print(f"Error processing RIB with ID {rib.get('id', 'UNKNOWN')}: {e}")
            continue

    return maintenance_schedules

# Example usage:
rib_data = [
    {
        'id': 'RIB001',
        'last_maintenance_date': '2022-10-01',
        'hours_used_since_last_maintenance': 600
    },
    {
        'id': 'RIB002',
        'last_maintenance_date': '2023-01-15',
        'hours_used_since_last_maintenance': 200
    }
]

# Calculate the maintenance schedules
schedules = calculate_maintenance_schedule(rib_data)
for schedule in schedules:
    print(schedule)
```
