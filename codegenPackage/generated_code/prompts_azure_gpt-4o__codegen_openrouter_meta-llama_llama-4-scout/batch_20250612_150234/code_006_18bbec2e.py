"""
Generated Code Metadata:
========================
Original URL: https://fourmemebot.com
Prompt: Provide code to calculate the time saved by using Joxi compared to other screenshot-sharing services, based on its claim of being 30% faster.
Generated: DETERMINISTIC_18bbec2ead109623
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_time_saved(joxi_time, other_service_time):
    """
    Calculate the time saved by using Joxi compared to other screenshot-sharing services.

    Args:
        joxi_time (float): Time taken by Joxi in seconds.
        other_service_time (float): Time taken by other screenshot-sharing services in seconds.

    Returns:
        float: Time saved in seconds.
    """
    if joxi_time < 0 or other_service_time < 0:
        raise ValueError("Time cannot be negative")

    time_saved = other_service_time - joxi_time
    return time_saved


def calculate_percentage_time_saved(joxi_time, other_service_time):
    """
    Calculate the percentage time saved by using Joxi compared to other screenshot-sharing services.

    Args:
        joxi_time (float): Time taken by Joxi in seconds.
        other_service_time (float): Time taken by other screenshot-sharing services in seconds.

    Returns:
        float: Percentage time saved.
    """
    if joxi_time < 0 or other_service_time < 0:
        raise ValueError("Time cannot be negative")

    if other_service_time == 0:
        return 0

    time_saved_percentage = ((other_service_time - joxi_time) / other_service_time) * 100
    return time_saved_percentage


def compare_with_joxi_claim(other_service_time):
    """
    Compare the time saved with Joxi's claim of being 30% faster.

    Args:
        other_service_time (float): Time taken by other screenshot-sharing services in seconds.

    Returns:
        tuple: Time saved in seconds and percentage time saved.
    """
    joxi_time = other_service_time * 0.7  # 30% faster
    time_saved = calculate_time_saved(joxi_time, other_service_time)
    time_saved_percentage = calculate_percentage_time_saved(joxi_time, other_service_time)

    return time_saved, time_saved_percentage


def main():
    try:
        other_service_time = float(input("Enter the time taken by other screenshot-sharing services in seconds: "))
        time_saved, time_saved_percentage = compare_with_joxi_claim(other_service_time)

        print(f"Time saved: {time_saved:.2f} seconds")
        print(f"Percentage time saved: {time_saved_percentage:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
