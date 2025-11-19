"""
Generated Code Metadata:
========================
Original URL: https://bonsaielevation.com
Prompt: Illustrate how to implement a feature that allows users to explore nature quotes, akin to the inspirational messages found on bonsaielevation.com.
Generated: DETERMINISTIC_55d2157e37e4cbb6
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

# Define a collection of nature quotes
NATURE_QUOTES = [
    "Look deep into nature, and then you will understand everything better. - Albert Einstein",
    "In every walk with nature, one receives far more than he seeks. - John Muir",
    "The earth has music for those who listen. - William Shakespeare",
    "Nature does not hurry, yet everything is accomplished. - Lao Tzu",
    "Adopt the pace of nature: her secret is patience. - Ralph Waldo Emerson",
    "The mountains are calling and I must go. - John Muir",
    "To sit in the shade on a fine day and look upon verdure is the most perfect refreshment. - Jane Austen",
    "Keep close to Nature's heart... and break clear away, once in awhile, and climb a mountain or spend a week in the woods. Wash your spirit clean. - John Muir",
    "Nature always wears the colors of the spirit. - Ralph Waldo Emerson",
    "The clearest way into the Universe is through a forest wilderness. - John Muir"
]

def get_random_quote():
    """
    Fetch a random nature quote from the predefined list.

    Returns:
        str: A randomly selected nature quote.
    """
    try:
        # Randomly select a quote from the list
        return random.choice(NATURE_QUOTES)
    except IndexError:
        # Handle the case where the list is empty
        return "No quotes available at the moment. Please try again later."

def main():
    """
    Main function to interact with the user and display nature quotes.
    """
    print("Welcome to the Nature Quotes Explorer!")
    print("Type 'next' to see a new quote or 'exit' to quit.")

    while True:
        user_input = input("Enter your choice: ").strip().lower()

        if user_input == 'next':
            # Display a random nature quote
            print("\n" + get_random_quote() + "\n")
        elif user_input == 'exit':
            # Exit the program
            print("Thank you for exploring nature quotes. Goodbye!")
            break
        else:
            # Handle invalid input
            print("Invalid input. Please type 'next' or 'exit'.")

if __name__ == "__main__":
    # Entry point of the program
    main()
```
