"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afms.in
Prompt: Write code to calculate the cost of multiple cleaning services (e.g., deep cleaning, pest control) based on the service categories provided by Ashvi Facility Management.
Generated: DETERMINISTIC_7191bfb4cec1e492
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Cleaning Service Cost Calculator for Ashvi Facility Management

# Using Python 3. Code is clean, production-ready, and well-documented.

# Define cleaning service rates (cost per service in USD)
SERVICE_RATES = {
    "deep_cleaning": 150,  # Cost for deep cleaning
    "standard_cleaning": 100,  # Cost for standard cleaning
    "pest_control": 200,  # Cost for pest control
    "carpet_cleaning": 80,  # Cost for carpet cleaning
    "window_cleaning": 50  # Cost for window cleaning
}

def calculate_total_cost(service_counts):
    """
    Calculate the total cost of cleaning services.

    Args:
        service_counts (dict): A dictionary where keys are service names and values are the count of services requested.

    Returns:
        float: Total cost of the requested services.

    Raises:
        ValueError: If an invalid service name is provided.
    """
    total_cost = 0.0

    for service, count in service_counts.items():
        if service not in SERVICE_RATES:
            raise ValueError(f"Invalid service name provided: {service}")
        if count < 0:
            raise ValueError(f"Service count cannot be negative: {service} -> {count}")
        
        # Calculate cost for the current service
        total_cost += SERVICE_RATES[service] * count

    return total_cost

def main():
    """
    Main function to demonstrate usage of the cleaning service cost calculator.
    """
    try:
        # Example input: Dictionary containing service names and counts
        service_counts = {
            "deep_cleaning": 2,
            "pest_control": 1,
            "window_cleaning": 3
        }

        # Calculate total cost
        total = calculate_total_cost(service_counts)
        print(f"Total cost for requested services: ${total:.2f}")
    except ValueError as ve:
        # Handle errors gracefully and print error message
        print(f"Error: {ve}")
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")

# Entry point for script execution
if __name__ == "__main__":
    main()
```
