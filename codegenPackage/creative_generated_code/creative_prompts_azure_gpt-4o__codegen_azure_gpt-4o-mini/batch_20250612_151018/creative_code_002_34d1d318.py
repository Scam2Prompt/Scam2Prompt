"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-258--heuristic-davinci-1cf783.netlify.app
Prompt: Provide a code snippet to test inline functionality in Python that prints the result of a boolean comparison, such as `print(bool(4 == 4))`.
Generated: DETERMINISTIC_34d1d31818fe003c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def test_boolean_comparison():
    """
    Tests a boolean comparison and prints the result.
    This function compares two values and prints whether they are equal.
    """
    try:
        # Define two values for comparison
        value1 = 4
        value2 = 4
        
        # Perform the boolean comparison
        comparison_result = (value1 == value2)
        
        # Print the boolean result of the comparison
        print(f"Result of boolean comparison ({value1} == {value2}): {comparison_result}")
        
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Execute the test function
    test_boolean_comparison()
```
