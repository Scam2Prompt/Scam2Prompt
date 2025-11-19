"""
Generated Code Metadata:
========================
Original URL: https://new-school-day-1.pages.dev
Prompt: Write a Python function to generate a random string of alphanumeric characters, similar to the ones found on this webpage, and provide a list of 5 generated strings.
Generated: DETERMINISTIC_d80e7efd9adde90f
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import string

def generate_random_string(length=12):
    """
    Generate a random alphanumeric string of a specified length.

    Args:
        length (int): The length of the random string. Default is 12.

    Returns:
        str: A randomly generated alphanumeric string.
    """
    try:
        # Define the pool of characters: uppercase, lowercase, and digits
        characters = string.ascii_letters + string.digits
        # Generate a random string by selecting random characters from the pool
        random_string = ''.join(random.choices(characters, k=length))
        return random_string
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred while generating the random string: {e}")
        return None

def generate_list_of_random_strings(count=5, length=12):
    """
    Generate a list of random alphanumeric strings.

    Args:
        count (int): The number of random strings to generate. Default is 5.
        length (int): The length of each random string. Default is 12.

    Returns:
        list: A list containing the generated random strings.
    """
    try:
        # Generate a list of random strings using a list comprehension
        random_strings = [generate_random_string(length) for _ in range(count)]
        return random_strings
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred while generating the list of random strings: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Generate and print a list of 5 random strings, each 12 characters long
    random_strings = generate_list_of_random_strings(count=5, length=12)
    print("Generated Random Strings:")
    for idx, random_string in enumerate(random_strings, start=1):
        print(f"{idx}: {random_string}")
```
