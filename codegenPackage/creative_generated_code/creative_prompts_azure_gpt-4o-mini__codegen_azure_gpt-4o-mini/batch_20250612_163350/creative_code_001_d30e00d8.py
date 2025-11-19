"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haitwik.com
Prompt: Write a Python function that outputs "I am haitwik" multiple times, reflecting the style of content on the haitwik site.
Generated: DETERMINISTIC_d30e00d86bd41c21
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def print_haitwik_message(repeat_count: int) -> None:
    """
    Prints the message "I am haitwik" a specified number of times.

    Parameters:
    repeat_count (int): The number of times to print the message. Must be a positive integer.

    Raises:
    ValueError: If repeat_count is not a positive integer.
    """

    # Validate the input
    if not isinstance(repeat_count, int):
        raise ValueError("repeat_count must be an integer")
    if repeat_count <= 0:
        raise ValueError("repeat_count must be a positive integer")

    # Loop to print the message the specified number of times
    for _ in range(repeat_count):
        print("I am haitwik")

# Example usage
if __name__ == "__main__":
    try:
        print_haitwik_message(5)  # Adjust the number to change the repetitions
    except ValueError as e:
        print(f"Error: {e}")
```
