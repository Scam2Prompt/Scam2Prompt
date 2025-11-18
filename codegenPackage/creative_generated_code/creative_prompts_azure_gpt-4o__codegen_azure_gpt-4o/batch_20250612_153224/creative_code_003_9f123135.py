"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yanmaq.cl
Prompt: Write a function to calculate the optimal mini excavator model for a construction project based on excavation depth, bucket volume, and equipment width, using the specifications of Yanmar models.
Generated: DETERMINISTIC_9f12313533776d0b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error reporting and debugging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Define Yanmar mini excavator specifications in a dictionary
YANMAR_MODELS = [
    {
        "model": "SV08",
        "max_depth": 1500,  # in mm
        "bucket_volume": 0.02,  # in m³
        "width": 680,  # in mm
    },
    {
        "model": "ViO17",
        "max_depth": 2200,
        "bucket_volume": 0.04,
        "width": 950,
    },
    {
        "model": "ViO25",
        "max_depth": 2500,
        "bucket_volume": 0.07,
        "width": 1500,
    },
    {
        "model": "ViO35",
        "max_depth": 3000,
        "bucket_volume": 0.1,
        "width": 1550,
    },
]

def calculate_optimal_model(required_depth, required_bucket_volume, max_width):
    """
    Calculate the optimal Yanmar mini excavator model for a construction project.

    Parameters:
        required_depth (int): Required excavation depth in mm.
        required_bucket_volume (float): Required bucket volume in m³.
        max_width (int): Maximum equipment width in mm.

    Returns:
        str: The model name of the optimal excavator, or a message indicating no suitable model.
    """
    try:
        # Validate input
        if required_depth <= 0 or required_bucket_volume <= 0 or max_width <= 0:
            raise ValueError("All input parameters must be positive values.")

        # Filter models based on specifications
        suitable_models = [
            model for model in YANMAR_MODELS
            if model["max_depth"] >= required_depth
            and model["bucket_volume"] >= required_bucket_volume
            and model["width"] <= max_width
        ]

        # Sort models by max_depth (descending) and bucket_volume (descending) for optimal choice
        suitable_models.sort(key=lambda x: (x["max_depth"], x["bucket_volume"]), reverse=True)

        # Return the most suitable model or an appropriate message
        if suitable_models:
            logging.info("Optimal model selected.")
            return suitable_models[0]["model"]
        else:
            logging.warning("No suitable models found for the given requirements.")
            return "No suitable excavator model found for the given requirements."

    except ValueError as e:
        logging.error(f"Input validation error: {e}")
        return "Invalid input parameters."
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return "An error occurred while calculating the optimal excavator model."

# Example usage:
# Uncomment the following lines to test the function
# optimal_model = calculate_optimal_model(required_depth=2000, required_bucket_volume=0.03, max_width=1000)
# print(optimal_model)
```
