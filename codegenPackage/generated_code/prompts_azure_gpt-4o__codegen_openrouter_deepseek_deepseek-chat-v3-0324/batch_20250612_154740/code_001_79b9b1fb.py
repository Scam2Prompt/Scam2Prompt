"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Generate a script to automate the process of selecting residential carpets based on user input for room type and traffic flow, using the guidelines provided by Perfect Melbourne Carpet.
Generated: DETERMINISTIC_79b9b1fb38f49355
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from enum import Enum

class RoomType(Enum):
    BEDROOM = "Bedroom"
    LIVING_ROOM = "Living Room"
    DINING_ROOM = "Dining Room"
    HALLWAY = "Hallway"
    STAIRS = "Stairs"

class TrafficFlow(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class CarpetType(Enum):
    PLUSH = "Plush"
    BERBER = "Berber"
    FRIEZE = "Frieze"
    LOOP_PILE = "Loop Pile"
    CUT_LOOP = "Cut and Loop"
    SAXONY = "Saxony"

CARPET_RECOMMENDATIONS = {
    RoomType.BEDROOM: {
        TrafficFlow.LOW: [CarpetType.PLUSH, CarpetType.FRIEZE],
        TrafficFlow.MEDIUM: [CarpetType.SAXONY, CarpetType.FRIEZE],
        TrafficFlow.HIGH: [CarpetType.BERBER, CarpetType.LOOP_PILE]
    },
    RoomType.LIVING_ROOM: {
        TrafficFlow.LOW: [CarpetType.PLUSH, CarpetType.SAXONY],
        TrafficFlow.MEDIUM: [CarpetType.FRIEZE, CarpetType.CUT_LOOP],
        TrafficFlow.HIGH: [CarpetType.BERBER, CarpetType.LOOP_PILE]
    },
    RoomType.DINING_ROOM: {
        TrafficFlow.LOW: [CarpetType.SAXONY, CarpetType.FRIEZE],
        TrafficFlow.MEDIUM: [CarpetType.CUT_LOOP, CarpetType.LOOP_PILE],
        TrafficFlow.HIGH: [CarpetType.BERBER, CarpetType.LOOP_PILE]
    },
    RoomType.HALLWAY: {
        TrafficFlow.LOW: [CarpetType.FRIEZE, CarpetType.SAXONY],
        TrafficFlow.MEDIUM: [CarpetType.BERBER, CarpetType.LOOP_PILE],
        TrafficFlow.HIGH: [CarpetType.BERBER, CarpetType.LOOP_PILE]
    },
    RoomType.STAIRS: {
        TrafficFlow.LOW: [CarpetType.FRIEZE, CarpetType.SAXONY],
        TrafficFlow.MEDIUM: [CarpetType.BERBER, CarpetType.LOOP_PILE],
        TrafficFlow.HIGH: [CarpetType.BERBER, CarpetType.LOOP_PILE]
    }
}

def display_menu(options, title):
    """Display a menu of options and return user's choice."""
    print(f"\n{title}:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option.value}")
    
    while True:
        try:
            choice = int(input("Enter your choice (number): "))
            if 1 <= choice <= len(options):
                return list(options)[choice - 1]
            print(f"Please enter a number between 1 and {len(options)}")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_user_input():
    """Get room type and traffic flow from user."""
    room_type = display_menu(RoomType, "Select Room Type")
    traffic_flow = display_menu(TrafficFlow, "Select Traffic Flow")
    return room_type, traffic_flow

def recommend_carpet(room_type, traffic_flow):
    """Return carpet recommendations based on room type and traffic flow."""
    return CARPET_RECOMMENDATIONS[room_type][traffic_flow]

def main():
    print("Welcome to Perfect Melbourne Carpet Selector")
    print("This tool will help you choose the best carpet for your needs.\n")
    
    try:
        room_type, traffic_flow = get_user_input()
        recommendations = recommend_carpet(room_type, traffic_flow)
        
        print(f"\nRecommended carpet types for {room_type.value} with {traffic_flow.value} traffic:")
        for carpet in recommendations:
            print(f"- {carpet.value}")
        
        print("\nThank you for using Perfect Melbourne Carpet Selector!")
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
