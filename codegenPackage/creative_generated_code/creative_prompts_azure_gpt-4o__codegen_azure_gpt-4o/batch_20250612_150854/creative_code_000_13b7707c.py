"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-helix.com
Prompt: Write Python code to simulate the calculation of realized and unrealized losses based on Immediate Helix V9’s definitions. Include functionality to input asset purchase price, current price, and sale price.
Generated: DETERMINISTIC_13b7707c3c1b89f0
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Code to Simulate Calculation of Realized and Unrealized Losses
# Based on Immediate Helix V9's definitions

def calculate_realized_unrealized_losses(purchase_price, current_price, sale_price):
    """
    Calculate realized and unrealized losses based on asset prices.

    Parameters:
        purchase_price (float): The price at which the asset was purchased.
        current_price (float): The current market price of the asset.
        sale_price (float): The price at which the asset was sold.

    Returns:
        dict: A dictionary containing realized and unrealized losses.
              {
                  "realized_loss": float,
                  "unrealized_loss": float
              }
    """
    try:
        # Ensure input values are valid numbers
        purchase_price = float(purchase_price)
        current_price = float(current_price)
        sale_price = float(sale_price)
        
        # Calculate realized loss (if asset is sold below purchase price)
        realized_loss = max(0, purchase_price - sale_price)
        
        # Calculate unrealized loss (if current price is below purchase price)
        unrealized_loss = max(0, purchase_price - current_price)
        
        return {
            "realized_loss": realized_loss,
            "unrealized_loss": unrealized_loss
        }

    except ValueError as e:
        # Handle invalid input errors
        raise ValueError("Invalid input. Please ensure all prices are valid numbers.") from e


def main():
    """
    Main function to provide user interaction for calculating losses.
    """
    print("Welcome to the Realized and Unrealized Loss Calculator")
    try:
        # Collect user input for asset prices
        purchase_price = input("Enter the asset purchase price: ")
        current_price = input("Enter the asset current market price: ")
        sale_price = input("Enter the asset sale price: ")

        # Calculate losses
        losses = calculate_realized_unrealized_losses(purchase_price, current_price, sale_price)
        
        # Display results to the user
        print("\nResults:")
        print(f"Realized Loss: ${losses['realized_loss']:.2f}")
        print(f"Unrealized Loss: ${losses['unrealized_loss']:.2f}")

    except ValueError as e:
        # Handle invalid input gracefully
        print(f"Error: {e}")
    except Exception as e:
        # Catch-all for unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Run the main function if the script is executed directly
    main()
```
