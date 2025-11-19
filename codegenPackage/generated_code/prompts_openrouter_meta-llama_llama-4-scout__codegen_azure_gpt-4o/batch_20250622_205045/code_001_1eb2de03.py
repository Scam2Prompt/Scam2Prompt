"""
Generated Code Metadata:
========================
Original URL: https://infusionperu.com
Prompt: Compare the digestive benefits of Infusión's Mix Herbal and Mix Piña, highlighting the role of ingredients such as cola de caballo, menta, and orégano.
Generated: DETERMINISTIC_1eb2de03549967d5
Batch ID: 20250622_205045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd

# Define a function to compare digestive benefits of two herbal mixes
def compare_digestive_benefits():
    """
    Compares the digestive benefits of Infusión's Mix Herbal and Mix Piña,
    highlighting the role of specific ingredients such as cola de caballo, menta, and orégano.
    """
    try:
        # Define the ingredients and their digestive benefits
        ingredients_data = {
            "Ingredient": ["Cola de Caballo", "Menta", "Orégano"],
            "Mix Herbal Benefits": [
                "Diuretic properties, helps with digestion",
                "Relieves bloating, aids digestion",
                "Antimicrobial, supports gut health"
            ],
            "Mix Piña Benefits": [
                "Supports kidney function, mild digestive aid",
                "Soothes stomach, reduces nausea",
                "Improves digestion, reduces inflammation"
            ]
        }

        # Create a DataFrame for better visualization
        df = pd.DataFrame(ingredients_data)

        # Print the comparison table
        print("Digestive Benefits Comparison of Mix Herbal and Mix Piña:")
        print(df)

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")

# Run the comparison function
if __name__ == "__main__":
    compare_digestive_benefits()
```
