"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: Develop an algorithm to estimate the risk reduction in fatalities when fire sprinklers are installed, using the 80% decrease statistic mentioned by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_1828a63754208300
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def estimate_risk_reduction(original_fatalities, sprinkler_effectiveness=0.8):
    """
    Estimates the reduction in fatalities after installing fire sprinklers.
    
    Args:
        original_fatalities (float): The number of fatalities before sprinkler installation.
        sprinkler_effectiveness (float, optional): The effectiveness of sprinklers in reducing 
                                                  fatalities (default is 0.8 for 80% reduction).
    
    Returns:
        float: The estimated number of fatalities after sprinkler installation.
    
    Raises:
        ValueError: If input values are negative or effectiveness is not between 0 and 1.
    """
    # Validate input parameters
    if original_fatalities < 0:
        raise ValueError("Original fatalities cannot be negative.")
    if not 0 <= sprinkler_effectiveness <= 1:
        raise ValueError("Sprinkler effectiveness must be between 0 and 1.")
    
    # Calculate reduced fatalities
    reduced_fatalities = original_fatalities * (1 - sprinkler_effectiveness)
    return reduced_fatalities


def calculate_risk_reduction(original_fatalities, sprinkler_effectiveness=0.8):
    """
    Calculates the absolute and percentage reduction in fatalities.
    
    Args:
        original_fatalities (float): The number of fatalities before sprinkler installation.
        sprinkler_effectiveness (float, optional): The effectiveness of sprinklers in reducing 
                                                  fatalities (default is 0.8 for 80% reduction).
    
    Returns:
        dict: A dictionary containing:
            - 'original_fatalities': Input value
            - 'reduced_fatalities': Estimated fatalities after sprinklers
            - 'absolute_reduction': Absolute number of lives saved
            - 'percentage_reduction': Percentage reduction (effectiveness)
    
    Raises:
        ValueError: If input values are negative or effectiveness is not between 0 and 1.
    """
    reduced_fatalities = estimate_risk_reduction(original_fatalities, sprinkler_effectiveness)
    
    return {
        'original_fatalities': original_fatalities,
        'reduced_fatalities': reduced_fatalities,
        'absolute_reduction': original_fatalities - reduced_fatalities,
        'percentage_reduction': sprinkler_effectiveness * 100
    }


# Example usage
if __name__ == "__main__":
    try:
        original = 100  # Example: 100 fatalities before sprinklers
        result = calculate_risk_reduction(original)
        
        print(f"Original fatalities: {result['original_fatalities']}")
        print(f"Reduced fatalities: {result['reduced_fatalities']:.1f}")
        print(f"Lives saved: {result['absolute_reduction']:.1f}")
        print(f"Risk reduction: {result['percentage_reduction']:.1f}%")
        
    except ValueError as e:
        print(f"Error: {e}")
```
