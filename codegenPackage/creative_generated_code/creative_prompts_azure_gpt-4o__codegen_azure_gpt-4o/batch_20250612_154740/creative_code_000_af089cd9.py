"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Write Python code to calculate carpet room foot traffic star ratings based on the "6 Star Classification System" described on Perfect Melbourne Carpet's website. Include logic for light, medium, heavy, and extra heavy traffic flow.
Generated: DETERMINISTIC_af089cd938d31022
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script calculates carpet room foot traffic star ratings based on the "6 Star Classification System"
and categorizes the traffic as light, medium, heavy, or extra heavy flow.
"""

def calculate_traffic_rating(traffic_count):
    """
    Determines the star rating and traffic flow category based on the number of foot traffic events.

    Parameters:
        traffic_count (int): The number of foot traffic events per day.

    Returns:
        tuple: A tuple containing the star rating (int) and traffic flow category (str).
    """
    try:
        # Validate input type
        if not isinstance(traffic_count, int) or traffic_count < 0:
            raise ValueError("Traffic count must be a non-negative integer.")

        # Determine star rating and traffic flow category
        if traffic_count < 50:
            return (1, "Light traffic flow")
        elif 50 <= traffic_count < 100:
            return (2, "Medium traffic flow")
        elif 100 <= traffic_count < 200:
            return (3, "Heavy traffic flow")
        elif 200 <= traffic_count < 400:
            return (4, "Extra heavy traffic flow")
        elif 400 <= traffic_count < 600:
            return (5, "Extra heavy traffic flow")
        else:
            return (6, "Extra heavy traffic flow")
    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")
        return None


def get_user_input():
    """
    Prompts the user to enter the daily foot traffic count and validates the input.

    Returns:
        int: The validated foot traffic count entered by the user.
    """
    while True:
        try:
            user_input = input("Enter daily foot traffic count (non-negative integer): ")
            traffic_count = int(user_input)
            if traffic_count < 0:
                raise ValueError("Traffic count cannot be negative.")
            return traffic_count
        except ValueError:
            print("Invalid input. Please enter a valid non-negative integer.")


def main():
    """
    Main function to calculate and display the carpet star rating and traffic flow category.
    """
    print("Welcome to the Carpet Traffic Rating Calculator!")
    
    # Get user input
    traffic_count = get_user_input()
    
    # Calculate rating and category
    result = calculate_traffic_rating(traffic_count)
    if result:
        star_rating, traffic_category = result
        print(f"Carpet Star Rating: {star_rating} Star(s)")
        print(f"Traffic Flow Category: {traffic_category}")


if __name__ == "__main__":
    # Execute the program
    main()
```
