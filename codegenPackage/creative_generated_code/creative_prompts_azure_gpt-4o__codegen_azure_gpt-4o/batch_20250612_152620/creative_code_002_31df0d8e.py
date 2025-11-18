"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sala-events.co.il
Prompt: Develop a Python script to calculate the cost of hosting an event at DCITY Events based on parameters such as the number of guests, type of event, and selected services (e.g., catering, decorations, technology).
Generated: DETERMINISTIC_31df0d8e68c512cb
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_event_cost(guest_count, event_type, services):
    """
    Calculate the cost of hosting an event based on guest count, type of event, and selected services.

    Args:
        guest_count (int): Number of guests attending the event.
        event_type (str): Type of event ('conference', 'wedding', 'party', etc.).
        services (dict): Selected services with their boolean values (e.g., {'catering': True, 'decorations': False}).

    Returns:
        float: Total cost of the event.

    Raises:
        ValueError: If guest_count is negative or unsupported values for event_type/services are provided.
    """
    # Base costs for different event types
    base_costs = {
        'conference': 500.0,
        'wedding': 1000.0,
        'party': 750.0
    }

    # Service costs per guest
    service_costs = {
        'catering': 50.0,        # Catering cost per guest
        'decorations': 20.0,     # Decoration cost per guest
        'technology': 30.0       # Technology cost per guest (e.g., projectors, sound systems)
    }

    # Validate guest_count
    if guest_count < 0:
        raise ValueError("Guest count cannot be negative.")

    # Validate event_type
    if event_type not in base_costs:
        raise ValueError(f"Unsupported event type: {event_type}. Supported types are: {list(base_costs.keys())}.")

    # Validate services
    for service in services:
        if service not in service_costs:
            raise ValueError(f"Unsupported service: {service}. Supported services are: {list(service_costs.keys())}.")

    # Calculate base cost based on event type
    total_cost = base_costs[event_type]

    # Add service costs
    for service, is_selected in services.items():
        if is_selected:
            total_cost += service_costs[service] * guest_count

    return total_cost


if __name__ == "__main__":
    try:
        # Example usage
        guest_count = 100  # Number of guests
        event_type = 'wedding'  # Type of event
        selected_services = {
            'catering': True,
            'decorations': True,
            'technology': False
        }

        # Calculate the cost
        total_cost = calculate_event_cost(guest_count, event_type, selected_services)
        print(f"The total cost for hosting the event is: ${total_cost:.2f}")

    except ValueError as e:
        # Handle invalid input gracefully
        print(f"Error: {e}")
        sys.exit(1)
```
