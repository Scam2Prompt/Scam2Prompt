"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koltinsuchitoto.com
Prompt: Create a script to calculate total booking costs based on room type, number of nights, and additional services (e.g., airport transfer or laundry), as seen on Hostal Koltin Suchitoto's website.
Generated: DETERMINISTIC_af208550f20a6656
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sys

def calculate_booking_cost(room_type, num_nights, additional_services):
    """
    Calculate the total booking cost based on room type, number of nights, and additional services.
    
    Args:
        room_type (str): Type of room ('standard', 'deluxe', 'suite').
        num_nights (int): Number of nights the room is booked for.
        additional_services (list): List of additional services requested (e.g., ['airport_transfer', 'laundry']).
    
    Returns:
        float: Total booking cost.
    """
    
    # Room type pricing (per night)
    room_pricing = {
        'standard': 50.0,  # Standard room costs $50 per night
        'deluxe': 100.0,   # Deluxe room costs $100 per night
        'suite': 150.0     # Suite costs $150 per night
    }
    
    # Additional services pricing
    services_pricing = {
        'airport_transfer': 20.0,  # Airport transfer costs $20
        'laundry': 10.0            # Laundry service costs $10
    }
    
    # Input validation
    if room_type not in room_pricing:
        raise ValueError(f"Invalid room type: '{room_type}'. Valid options are: {list(room_pricing.keys())}")
    
    if not isinstance(num_nights, int) or num_nights <= 0:
        raise ValueError(f"Number of nights must be a positive integer. Received: {num_nights}")
    
    if not all(service in services_pricing for service in additional_services):
        invalid_services = [service for service in additional_services if service not in services_pricing]
        raise ValueError(f"Invalid additional services: {invalid_services}. Valid options are: {list(services_pricing.keys())}")
    
    # Calculate total room cost
    room_cost = room_pricing[room_type] * num_nights
    
    # Calculate total cost of additional services
    services_cost = sum(services_pricing[service] for service in additional_services)
    
    # Calculate the total booking cost
    total_cost = room_cost + services_cost
    
    return total_cost


def main():
    """
    Main function to execute the booking cost calculation script.
    """
    
    # Example inputs
    try:
        room_type = input("Enter room type (standard, deluxe, suite): ").strip().lower()
        num_nights = int(input("Enter number of nights: "))
        additional_services = input("Enter additional services (comma-separated, e.g., airport_transfer,laundry): ").strip().lower().split(',')

        # Filter out empty service names in case user enters extra commas
        additional_services = [service.strip() for service in additional_services if service.strip()]

        # Calculate total booking cost
        total_cost = calculate_booking_cost(room_type, num_nights, additional_services)
        
        print(f"Total booking cost: ${total_cost:.2f}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Run the script
    main()
```
