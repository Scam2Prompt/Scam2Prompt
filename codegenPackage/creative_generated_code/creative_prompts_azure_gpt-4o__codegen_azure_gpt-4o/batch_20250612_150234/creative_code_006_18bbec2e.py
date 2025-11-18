"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fourmemebot.com
Prompt: Provide code to calculate the time saved by using Joxi compared to other screenshot-sharing services, based on its claim of being 30% faster.
Generated: DETERMINISTIC_18bbec2ead109623
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary module for handling invalid input and calculations
def calculate_time_saved(total_time_spent: float, joxi_efficiency: float = 0.30) -> float:
    """
    Calculate the time saved by using Joxi compared to other services.

    Parameters:
        total_time_spent (float): The total time (in minutes) spent using other services.
        joxi_efficiency (float): The claimed efficiency of Joxi (default is 30% faster, i.e., 0.30).

    Returns:
        float: The time saved (in minutes) by using Joxi.

    Raises:
        ValueError: If total_time_spent is not a positive number.
    """
    # Validate input
    if total_time_spent <= 0:
        raise ValueError("Total time spent must be a positive number.")

    # Calculate time saved
    time_saved = total_time_spent * joxi_efficiency
    return time_saved


# Entry point for the program
if __name__ == "__main__":
    try:
        # Ask the user to input the total time spent on other services
        user_input = input("Enter the total time (in minutes) spent using other screenshot-sharing services: ")
        total_time = float(user_input)  # Convert input to float

        # Calculate the time saved
        time_saved = calculate_time_saved(total_time)

        # Print the result
        print(f"By using Joxi, you can save approximately {time_saved:.2f} minutes.")
    except ValueError as e:
        # Handle invalid input or calculation errors
        print(f"Error: {e}")
```
