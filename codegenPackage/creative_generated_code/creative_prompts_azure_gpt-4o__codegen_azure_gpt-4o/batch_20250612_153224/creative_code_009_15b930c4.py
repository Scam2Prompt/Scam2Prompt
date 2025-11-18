"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yanmaq.cl
Prompt: Provide code to filter Yanmar spare parts (e.g., filters, pistons, alternators) based on compatibility with specific mini excavator models like ViO12, ViO17, ViO25, ViO35, and SV100.
Generated: DETERMINISTIC_15b930c48cc95c86
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import json

# Sample data representing Yanmar spare parts and their compatibility.
# Data format: A list of dictionaries with part information and compatible models.
SPARE_PARTS = [
    {"part_id": 101, "name": "Oil Filter", "compatible_models": ["ViO12", "ViO17", "ViO25"]},
    {"part_id": 102, "name": "Piston", "compatible_models": ["ViO25", "ViO35"]},
    {"part_id": 103, "name": "Air Filter", "compatible_models": ["ViO12", "ViO17"]},
    {"part_id": 104, "name": "Alternator", "compatible_models": ["SV100"]},
    {"part_id": 105, "name": "Hydraulic Pump", "compatible_models": ["ViO35", "SV100"]},
]

def filter_spare_parts_by_model(model: str):
    """
    Filters Yanmar spare parts based on their compatibility with a specific mini excavator model.

    Args:
        model (str): The model of the mini excavator (e.g., 'ViO12').

    Returns:
        list: A list of spare parts compatible with the specified model.
    """
    # Validate input
    if not isinstance(model, str) or not model:
        raise ValueError("Model name must be a non-empty string.")

    # Filter spare parts based on compatibility
    compatible_parts = [part for part in SPARE_PARTS if model in part["compatible_models"]]
    return compatible_parts

def main():
    """
    Main function to demonstrate spare parts filtering.
    """
    try:
        # Example: Filter parts compatible with the model 'ViO17'
        model_name = "ViO17"
        print(f"Filtering spare parts compatible with the model '{model_name}'...")
        compatible_parts = filter_spare_parts_by_model(model_name)

        # Display the filtered parts
        print(json.dumps(compatible_parts, indent=4))

    except ValueError as ve:
        print(f"Error: {ve}")

    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

# Entry point for script execution
if __name__ == "__main__":
    main()
```
