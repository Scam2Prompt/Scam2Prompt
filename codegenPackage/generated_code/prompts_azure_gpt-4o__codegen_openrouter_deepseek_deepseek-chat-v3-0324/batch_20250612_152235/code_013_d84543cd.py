"""
Generated Code Metadata:
========================
Original URL: https://bitcoinxcash.com
Prompt: Generate a Python script to calculate staffing requirements for events based on attendee size and event type, as outlined in the webpage's discussion on human resource planning.
Generated: DETERMINISTIC_d84543cd76089e38
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum
from typing import Dict, Tuple, Optional

class EventType(Enum):
    """Enum representing different types of events and their staffing requirements."""
    CONFERENCE = "conference"
    WORKSHOP = "workshop"
    SEMINAR = "seminar"
    SOCIAL = "social"
    EXHIBITION = "exhibition"

class StaffingCalculator:
    """
    A class to calculate staffing requirements for events based on attendee size and event type.
    
    Attributes:
        STAFFING_RATIOS (Dict[EventType, Tuple[float, float]]): 
            Mapping of event types to their respective staff-to-attendee ratios.
            The tuple represents (min_staff_per_attendee, max_staff_per_attendee).
        MIN_STAFF (Dict[EventType, int]): 
            Minimum staff required regardless of attendee count for each event type.
    """
    
    STAFFING_RATIOS = {
        EventType.CONFERENCE: (0.05, 0.08),
        EventType.WORKSHOP: (0.1, 0.15),
        EventType.SEMINAR: (0.07, 0.1),
        EventType.SOCIAL: (0.03, 0.05),
        EventType.EXHIBITION: (0.08, 0.12)
    }
    
    MIN_STAFF = {
        EventType.CONFERENCE: 5,
        EventType.WORKSHOP: 3,
        EventType.SEMINAR: 2,
        EventType.SOCIAL: 2,
        EventType.EXHIBITION: 4
    }

    @classmethod
    def calculate_staffing(
        cls, 
        attendee_count: int, 
        event_type: EventType, 
        complexity_factor: float = 1.0
    ) -> Dict[str, int]:
        """
        Calculate the minimum and maximum staff required for an event.
        
        Args:
            attendee_count: Number of attendees expected at the event.
            event_type: Type of the event (from EventType enum).
            complexity_factor: Multiplier for complex events (default 1.0).
            
        Returns:
            Dictionary with 'min_staff' and 'max_staff' keys.
            
        Raises:
            ValueError: If attendee_count is negative or complexity_factor is <= 0.
        """
        if attendee_count < 0:
            raise ValueError("Attendee count cannot be negative.")
        if complexity_factor <= 0:
            raise ValueError("Complexity factor must be greater than 0.")
        
        min_ratio, max_ratio = cls.STAFFING_RATIOS[event_type]
        min_staff = math.ceil(attendee_count * min_ratio * complexity_factor)
        max_staff = math.ceil(attendee_count * max_ratio * complexity_factor)
        
        # Ensure minimum staff requirements are met
        min_staff = max(min_staff, cls.MIN_STAFF[event_type])
        max_staff = max(max_staff, cls.MIN_STAFF[event_type])
        
        return {
            'min_staff': min_staff,
            'max_staff': max_staff
        }

    @classmethod
    def get_staffing_recommendation(
        cls,
        attendee_count: int,
        event_type: EventType,
        complexity_factor: float = 1.0
    ) -> str:
        """
        Generate a human-readable staffing recommendation.
        
        Args:
            attendee_count: Number of attendees expected at the event.
            event_type: Type of the event (from EventType enum).
            complexity_factor: Multiplier for complex events (default 1.0).
            
        Returns:
            Formatted string with staffing recommendation.
        """
        try:
            staffing = cls.calculate_staffing(attendee_count, event_type, complexity_factor)
            return (
                f"For a {event_type.value} with {attendee_count} attendees:\n"
                f"- Minimum staff required: {staffing['min_staff']}\n"
                f"- Recommended staff: {staffing['max_staff']}\n"
                f"(Complexity factor: {complexity_factor})"
            )
        except ValueError as e:
            return f"Error: {str(e)}"

def main():
    """Example usage of the StaffingCalculator class."""
    try:
        # Example 1: Conference with 200 attendees
        print(StaffingCalculator.get_staffing_recommendation(
            attendee_count=200,
            event_type=EventType.CONFERENCE
        ))
        
        # Example 2: Workshop with 30 attendees and higher complexity
        print("\n" + StaffingCalculator.get_staffing_recommendation(
            attendee_count=30,
            event_type=EventType.WORKSHOP,
            complexity_factor=1.2
        ))
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
