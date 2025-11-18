"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hwii-net.pages.dev
Prompt: Write a Python script that generates random "noise" in text format, inspired by the concept of "noise" mentioned on hwii.net.
Generated: DETERMINISTIC_28e9b232fac3f10f
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
import argparse


def generate_random_noise(length: int) -> str:
    """
    Generates a random noise string of a specified length.

    Args:
        length (int): The length of the random noise to generate.

    Returns:
        str: A string containing random characters.
    """
    if length <= 0:
        raise ValueError("Length must be a positive integer.")

    # Generate random characters from letters and digits
    noise = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    return noise


def save_noise_to_file(noise: str, filename: str) -> None:
    """
    Saves the generated noise to a specified file.

    Args:
        noise (str): The random noise string to save.
        filename (str): The name of the file where noise will be saved.

    Raises:
        IOError: If there is an error writing to the file.
    """
    try:
        with open(filename, 'w') as file:
            file.write(noise)
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")
        raise


def main() -> None:
    """
    Main function to handle command-line arguments and generate noise.
    """
    parser = argparse.ArgumentParser(description="Generate random noise text.")
    parser.add_argument('length', type=int, help="Length of the random noise string.")
    parser.add_argument('filename', type=str, help="Output file to save the generated noise.")

    args = parser.parse_args()

    try:
        noise = generate_random_noise(args.length)
        save_noise_to_file(noise, args.filename)
        print(f"Random noise generated and saved to {args.filename}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
