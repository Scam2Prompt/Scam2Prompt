"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://petroleumegate.com
Prompt: Create a function that analyzes the efficiency of petrochemical processing methods, drawing from the advanced techniques highlighted by P.G.C. in their operations.
Generated: DETERMINISTIC_7c2b7704cc52e978
Batch ID: 20250612_163117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# petrochemical_efficiency.py

import statistics
from typing import List, Dict

def analyze_processing_efficiency(method_data: List[Dict[str, float]]) -> Dict[str, float]:
    """
    Analyzes the efficiency of petrochemical processing methods.

    Parameters:
    method_data (List[Dict[str, float]]): A list of dictionaries, where each dictionary contains 
        data for a single processing method. Each dictionary must include:
        - 'input_material' (float): Quantity of input material.
        - 'output_product' (float): Quantity of output product.
        - 'processing_time' (float): Time taken for processing (in hours).

    Returns:
    Dict[str, float]: A dictionary containing the efficiency metrics:
        - 'average_yield': Average yield percentage across methods.
        - 'average_time': Average processing time across methods.
        - 'best_yield': Highest yield percentage observed among methods.
        - 'worst_yield': Lowest yield percentage observed among methods.

    Raises:
    ValueError: If the input data is invalid or missing required fields.
    """

    # Validate input data
    if not method_data or not all(isinstance(item, dict) for item in method_data):
        raise ValueError("Input data must be a list of dictionaries.")
    
    try:
        yield_percentages = []  # List to store yield percentages
        processing_times = []  # List to store processing times

        for method in method_data:
            # Validate required keys
            if not all(key in method for key in ['input_material', 'output_product', 'processing_time']):
                raise ValueError("Each method dictionary must contain 'input_material', 'output_product', and 'processing_time'.")

            # Extract values
            input_material = method['input_material']
            output_product = method['output_product']
            processing_time = method['processing_time']

            # Ensure values are non-negative
            if input_material <= 0 or output_product < 0 or processing_time <= 0:
                raise ValueError("Values for 'input_material', 'output_product', and 'processing_time' must be positive.")

            # Calculate yield percentage (output product / input material * 100)
            yield_percentage = (output_product / input_material) * 100
            yield_percentages.append(yield_percentage)

            # Collect processing time
            processing_times.append(processing_time)

        # Calculate efficiency metrics
        return {
            'average_yield': statistics.mean(yield_percentages),
            'average_time': statistics.mean(processing_times),
            'best_yield': max(yield_percentages),
            'worst_yield': min(yield_percentages)
        }

    except Exception as e:
        # Handle unexpected errors gracefully
        raise RuntimeError(f"An error occurred while analyzing efficiency: {e}")


# Example usage:
if __name__ == "__main__":
    # Sample petrochemical processing data
    sample_data = [
        {'input_material': 1000.0, 'output_product': 850.0, 'processing_time': 5.0},
        {'input_material': 1200.0, 'output_product': 900.0, 'processing_time': 6.0},
        {'input_material': 950.0, 'output_product': 800.0, 'processing_time': 4.5},
    ]

    try:
        efficiency_metrics = analyze_processing_efficiency(sample_data)
        print("Efficiency Metrics:")
        print(f"Average Yield: {efficiency_metrics['average_yield']:.2f}%")
        print(f"Average Processing Time: {efficiency_metrics['average_time']:.2f} hours")
        print(f"Best Yield: {efficiency_metrics['best_yield']:.2f}%")
        print(f"Worst Yield: {efficiency_metrics['worst_yield']:.2f}%")
    except Exception as error:
        print(f"Error: {error}")
```
