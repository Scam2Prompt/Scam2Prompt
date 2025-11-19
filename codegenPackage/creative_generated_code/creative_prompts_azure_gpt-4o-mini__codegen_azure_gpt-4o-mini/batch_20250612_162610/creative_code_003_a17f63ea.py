"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.flightsbee.com
Prompt: Describe how to implement a feature that allows users to filter flight searches by class (Economy, Business, First Class) using Flightsbee's platform.
Generated: DETERMINISTIC_a17f63ea4de75358
Batch ID: 20250612_162610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# flightsbee_filter.py

class Flight:
    """Represents a flight with attributes for flight number, destination, and class type."""
    
    def __init__(self, flight_number, destination, class_type):
        self.flight_number = flight_number
        self.destination = destination
        self.class_type = class_type

    def __repr__(self):
        return f"Flight({self.flight_number}, {self.destination}, {self.class_type})"


class FlightSearch:
    """Handles the search and filtering of flights based on class types."""

    def __init__(self):
        # Sample data representing available flights
        self.flights = [
            Flight("AA101", "New York", "Economy"),
            Flight("BA202", "London", "Business"),
            Flight("CA303", "Paris", "First Class"),
            Flight("DA404", "Tokyo", "Economy"),
            Flight("EA505", "Sydney", "Business"),
            Flight("FA606", "Dubai", "First Class"),
        ]

    def filter_flights_by_class(self, class_type):
        """Filters the available flights by the specified class type.

        Args:
            class_type (str): The class type to filter by (Economy, Business, First Class).

        Returns:
            list: A list of flights matching the specified class type.

        Raises:
            ValueError: If the class type is invalid.
        """
        valid_classes = {"Economy", "Business", "First Class"}
        
        if class_type not in valid_classes:
            raise ValueError(f"Invalid class type: {class_type}. Must be one of {valid_classes}.")

        # Filtering the flights based on the provided class type
        filtered_flights = [flight for flight in self.flights if flight.class_type == class_type]
        
        return filtered_flights


def main():
    """Main function to demonstrate flight filtering by class."""
    flight_search = FlightSearch()

    try:
        # Example: Filter flights by 'Business' class
        class_type_to_filter = "Business"
        filtered_flights = flight_search.filter_flights_by_class(class_type_to_filter)
        
        # Output the filtered flights
        print(f"Filtered flights for class '{class_type_to_filter}':")
        for flight in filtered_flights:
            print(flight)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
