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
# Python script to calculate the total cost of purchasing books under Sakura Books' "Buy 3, Get 1 Free" offer.

def calculate_total_cost(book_prices):
    """
    Calculate the total cost for Sakura Books' "Buy 3, Get 1 Free" offer.
    
    Parameters:
        book_prices (list): A list of prices for the books being purchased.
        
    Returns:
        float: The total cost after applying the discount.
    """
    # Validate input
    if not isinstance(book_prices, list) or not all(isinstance(price, (int, float)) for price in book_prices):
        raise ValueError("book_prices must be a list of numeric values.")
    
    if len(book_prices) < 4:
        raise ValueError("At least 4 books are required for the 'Buy 3, Get 1 Free' offer.")
    
    # Sort prices in descending order
    book_prices.sort(reverse=True)
    
    # Apply the "Buy 3, Get 1 Free" offer
    total_cost = sum(book_prices) - book_prices[3]  # Subtract the cost of the cheapest book (4th in sorted order)
    
    return total_cost


def main():
    """
    Main function to input book prices and calculate total cost.
    """
    try:
        # Prompt the user to input book prices
        print("Enter the prices of at least 4 books (separated by spaces):")
        user_input = input().strip()
        
        # Convert input to a list of floats
        book_prices = [float(price) for price in user_input.split()]
        
        if len(book_prices) < 4:
            print("Error: You need to enter at least 4 book prices.")
            return
        
        # Calculate the total cost
        total_cost = calculate_total_cost(book_prices)
        
        # Display the total cost
        print(f"Total cost after 'Buy 3, Get 1 Free' offer: ${total_cost:.2f}")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Run the main function
    main()
```
