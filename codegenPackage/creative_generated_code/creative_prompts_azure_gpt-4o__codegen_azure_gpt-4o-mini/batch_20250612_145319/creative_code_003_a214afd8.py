"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zirciulit.com
Prompt: Write a function to calculate project timelines for luxury residential developments, based on the workflow described by Zirciulit Design Firm's design process.
Generated: DETERMINISTIC_a214afd8a43d859e
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import List, Dict, Union

class ProjectTimelineError(Exception):
    """Custom exception for errors in project timeline calculation."""
    pass

def calculate_timeline(start_date: str, phases: List[Dict[str, Union[str, int]]]) -> Dict[str, Union[str, int]]:
    """
    Calculate the project timeline for luxury residential developments.

    Args:
        start_date (str): The start date of the project in 'YYYY-MM-DD' format.
        phases (List[Dict[str, Union[str, int]]]): A list of phases, each defined by its name and duration in days.

    Returns:
        Dict[str, Union[str, int]]: A dictionary containing the end date and total project duration in days.
    
    Raises:
        ProjectTimelineError: If the start date is invalid or if any phase duration is non-positive.
    """
    # Validate and parse the start date
    try:
        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    except ValueError as e:
        raise ProjectTimelineError(f"Invalid start date format: {start_date}. Error: {str(e)}")

    total_duration = 0
    current_date = start_date_obj

    # Process each phase
    for phase in phases:
        phase_name = phase.get("name")
        phase_duration = phase.get("duration")

        # Validate phase details
        if not phase_name or not isinstance(phase_duration, int) or phase_duration <= 0:
            raise ProjectTimelineError(f"Invalid phase details: {phase}")

        # Update total duration and current end date
        total_duration += phase_duration
        current_date += timedelta(days=phase_duration)
        print(f"Phase: {phase_name}, Duration: {phase_duration} days, End Date: {current_date.strftime('%Y-%m-%d')}")

    # Prepare the result
    end_date = current_date.strftime('%Y-%m-%d')
    return {"end_date": end_date, "total_duration": total_duration}

# Example usage
if __name__ == "__main__":
    try:
        project_phases = [
            {"name": "Site Preparation", "duration": 30},
            {"name": "Foundation", "duration": 45},
            {"name": "Framing", "duration": 60},
            {"name": "Finishing", "duration": 30}
        ]
        timeline = calculate_timeline("2023-10-01", project_phases)
        print(f"Project End Date: {timeline['end_date']}, Total Duration: {timeline['total_duration']} days")
    except ProjectTimelineError as e:
        print(f"Error calculating project timeline: {str(e)}")
```
