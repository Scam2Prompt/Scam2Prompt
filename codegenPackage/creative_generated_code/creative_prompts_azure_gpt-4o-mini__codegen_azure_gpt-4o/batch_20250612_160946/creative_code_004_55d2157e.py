"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonsaielevation.com
Prompt: Illustrate how to implement a feature that allows users to explore nature quotes, akin to the inspirational messages found on bonsaielevation.com.
Generated: DETERMINISTIC_55d2157e37e4cbb6
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Dictionary of nature-inspired quotes
QUOTES = [
    "In every walk with nature, one receives far more than he seeks. - John Muir",
    "Look deep into nature, and then you will understand everything better. - Albert Einstein",
    "Nature does not hurry, yet everything is accomplished. - Lao Tzu",
    "The earth has music for those who listen. - George Santayana",
    "Adopt the pace of nature: her secret is patience. - Ralph Waldo Emerson",
    "Keep close to Nature's heart... and break clear away, once in awhile, and climb a mountain or spend a week in the woods. Wash your spirit clean. - John Muir",
    "The clearest way into the Universe is through a forest wilderness. - John Muir",
    "Heaven is under our feet as well as over our heads. - Henry David Thoreau",
    "To sit in the shade on a fine day and look upon verdure is the most perfect refreshment. - Jane Austen",
    "Nature always wears the colors of the spirit. - Ralph Waldo Emerson"
]

def fetch_random_quote():
    """
    Fetch a random nature quote from the predefined list.

    Returns:
        str: A randomly selected nature quote.
    """
    try:
        # Randomly select a quote from the list
        return random.choice(QUOTES)
    except Exception as e:
        # Handle unexpected errors gracefully
        return f"An error occurred while fetching the quote: {str(e)}"

def main():
    """
    Main function to illustrate the nature quotes feature.
    """
    print("Welcome to Nature Quotes Explorer!")
    print("Fetching an inspirational quote for you...\n")
    
    # Fetch and display a random quote
    quote = fetch_random_quote()
    print(f"Inspirational Quote: {quote}")

if __name__ == "__main__":
    # Entry point for the program
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
