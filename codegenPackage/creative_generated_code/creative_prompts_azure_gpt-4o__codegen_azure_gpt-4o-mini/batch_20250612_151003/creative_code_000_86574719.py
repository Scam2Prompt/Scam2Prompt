"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddysoluniversity.com
Prompt: Write a Python script to calculate the total cost of purchasing three used books and getting the fourth one free, based on Sakura Books' "Buy 3, Get 1 Free" offer. Include functionality to input book prices and apply the discount.
Generated: DETERMINISTIC_86574719b7800831
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_cost(book_prices):
    """
    Calculate the total cost for purchasing books under the 
    "Buy 3, Get 1 Free" offer.
    
    Args:
        book_prices (list): A list of book prices (float) for the purchased books.
    
    Returns:
        float: The total cost after applying the offer.
    
    Raises:
        ValueError: If there are fewer than 3 prices in the input list.
    """
    
    # Check if there are at least 3 book prices
    if len(book_prices) < 3:
        raise ValueError("At least 3 book prices are required to apply the offer.")
    
    # Sort prices in descending order to get the most expensive book free
    book_prices.sort(reverse=True)

    # Calculate total cost:
    # Sum the prices of the three most expensive books
    total_cost = sum(book_prices[:3])
    
    return total_cost


def main():
    """
    Main function to handle user input and display the total cost.
    """
    try:
        # Get input from user
        input_prices = input("Enter the prices of the books separated by commas: ")
        
        # Convert input string to a list of floats
        book_prices = [float(price.strip()) for price in input_prices.split(',')]
        
        # Calculate total cost
        total_cost = calculate_total_cost(book_prices)
        
        # Display the total cost
        print(f"The total cost after applying the 'Buy 3, Get 1 Free' offer is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
