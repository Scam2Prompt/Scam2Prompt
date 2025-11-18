"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pansos4dvisi.pro
Prompt: Write Python code to simulate a lottery number generator for "TOTO WUHAN" based on the results format provided on PANSOS4D.
Generated: DETERMINISTIC_0241c0d8ea48081c
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def generate_toto_wuhan_numbers(draw_count=1):
    """
    Simulate a "TOTO WUHAN" lottery number generator.
    Each ticket contains 6 unique numbers from 1 to 49.
    
    Parameters:
        draw_count (int): The number of draws to generate.

    Returns:
        list of lists: A list containing the generated lottery numbers for each draw.
    """
    # Validate input
    if not isinstance(draw_count, int) or draw_count <= 0:
        raise ValueError("draw_count must be a positive integer.")

    results = []
    for _ in range(draw_count):
        # Generate a set of 6 unique random numbers from 1 to 49
        draw = sorted(random.sample(range(1, 50), 6))  # `sorted` ensures ascending order
        results.append(draw)
    
    return results

def main():
    """
    Main function to execute the lottery generator.
    """
    print("Welcome to the TOTO WUHAN Lottery Number Generator!")
    
    try:
        # Prompt user for the number of draws
        draw_count = int(input("Enter the number of lottery draws you want: "))
        # Generate lottery numbers
        lottery_results = generate_toto_wuhan_numbers(draw_count)
        
        # Display results
        print("\nHere are your lottery numbers:")
        for index, draw in enumerate(lottery_results, start=1):
            print(f"Draw {index}: {', '.join(map(str, draw))}")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

if __name__ == "__main__":
    main()
```
