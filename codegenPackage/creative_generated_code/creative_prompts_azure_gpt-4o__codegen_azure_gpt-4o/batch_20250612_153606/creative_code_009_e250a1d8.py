"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bipzy-frontend-master-5ot8k5vwq-bipzy1.vercel.app
Prompt: Write a function to calculate and display the percentage commission earned by Bipzy from presale allocations, ensuring competitive valuations for projects.
Generated: DETERMINISTIC_e250a1d806f8a0cc
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Function to calculate and display the percentage commission earned by Bipzy
def calculate_commission(total_presale, allocation, commission_rate):
    """
    Calculate and display Bipzy's commission earned from presale allocations.

    Parameters:
    total_presale (float): The total presale amount in USD.
    allocation (float): Bipzy's allocated share from the total presale amount.
    commission_rate (float): Commission rate as a percentage (e.g., 10 for 10%).

    Returns:
    float: The commission earned by Bipzy in USD.
    """
    try:
        # Validate inputs
        if total_presale <= 0 or allocation <= 0 or commission_rate < 0:
            raise ValueError("Invalid input values. Ensure positive presale and allocation amounts and non-negative commission rate.")

        if allocation > total_presale:
            raise ValueError("Allocation cannot exceed total presale amount.")

        # Calculate commission
        commission_earned = (allocation * commission_rate) / 100

        # Display commission details
        print(f"Total Presale Amount: ${total_presale:,.2f}")
        print(f"Bipzy's Allocation: ${allocation:,.2f}")
        print(f"Commission Rate: {commission_rate}%")
        print(f"Commission Earned: ${commission_earned:,.2f}")

        return commission_earned

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Sample data
    total_presale_amount = 500000  # Example: $500,000
    allocation_amount = 50000     # Example: $50,000 allocated to Bipzy
    commission_rate_percent = 10  # Example: 10% commission

    # Calculate commission
    calculate_commission(total_presale_amount, allocation_amount, commission_rate_percent)
```
