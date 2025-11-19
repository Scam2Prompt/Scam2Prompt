"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://2857qualifications.blogspot.com
Prompt: Are there specific coding tasks or examples that align with the qualifications discussed on the 2857qualifications blog?
Generated: DETERMINISTIC_a49e3c8d5409a7bf
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates a variety of coding practices that align with general software development qualifications 
such as clean code principles, proper error handling, and best practices. This sample code calculates the factorial 
of a number, reads and writes JSON data, and handles common errors gracefully.
"""

import json


def factorial(n):
    """
    Calculate the factorial of a given number.

    Args:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of the number.

    Raises:
        ValueError: If the input is a negative number.
    """
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def read_json_file(file_path):
    """
    Read a JSON file and return its contents.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: The contents of the JSON file.

    Raises:
        FileNotFoundError: If the file is not found.
        json.JSONDecodeError: If the file contents cannot be parsed as JSON.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {file_path}") from e
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON data in file: {file_path}") from e


def write_json_file(file_path, data):
    """
    Write data to a JSON file.

    Args:
        file_path (str): Path to the JSON file.
        data (dict): The data to write to the file.

    Raises:
        IOError: If there is an error writing to the file.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        raise IOError(f"Error writing to file: {file_path}") from e


def main():
    """
    Main function to demonstrate the functionality of the script.
    """
    try:
        # Example: Calculate factorial
        number = 5
        print(f"Factorial of {number}: {factorial(number)}")

        # Example: Read and write JSON data
        json_file_path = "example.json"
        data = {"name": "John Doe", "age": 30, "skills": ["Python", "JavaScript", "SQL"]}
        
        # Write example data to a JSON file
        write_json_file(json_file_path, data)
        print(f"Data written to {json_file_path}")

        # Read the same JSON file
        read_data = read_json_file(json_file_path)
        print(f"Data read from {json_file_path}: {read_data}")
    
    except Exception as e:
        # Catch all unexpected errors
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
