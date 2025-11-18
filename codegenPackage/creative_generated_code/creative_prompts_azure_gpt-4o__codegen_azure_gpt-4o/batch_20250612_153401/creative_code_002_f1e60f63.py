"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sol-ido-lake.vercel.app
Prompt: Create a function to calculate the ROI (Return on Investment) for a completed IDO on the Memes Pad SOL IDO platform.
Generated: DETERMINISTIC_f1e60f63662d43db
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
def calculate_roi(initial_investment: float, final_value: float) -> float:
    """
    Calculate the Return on Investment (ROI) for a completed IDO.

    Parameters:
    initial_investment (float): The amount of money initially invested in the IDO.
    final_value (float): The total value of the investment at the end of the IDO.

    Returns:
    float: The ROI percentage as a decimal (e.g., 0.75 for a 75% ROI).

    Raises:
    ValueError: If initial_investment is zero or negative.
    """
    # Validate inputs
    if initial_investment <= 0:
        raise ValueError("Initial investment must be greater than zero.")
    
    # Calculate ROI
    roi = (final_value - initial_investment) / initial_investment
    
    return roi


# Example usage:
if __name__ == "__main__":
    try:
        # Example scenario
        initial = 1000.0  # Initial investment in USD
        final = 1750.0    # Final value after IDO
        result = calculate_roi(initial_investment=initial, final_value=final)
        
        print(f"ROI: {result:.2%}")  # Convert decimal ROI to percentage for display
    except ValueError as e:
        print(f"Error: {e}")
```
