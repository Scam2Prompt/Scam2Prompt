"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eagle-tex.cn
Prompt: Create a Python script to analyze fabric weights (e.g., 180g, 240g, 320g) and recommend the most suitable options for T-shirt production using Shaoxing Eagles Textile Co., Ltd.'s product data.
Generated: DETERMINISTIC_258bcf26ffca9316
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def recommend_fabric_for_tshirts(fabric_weights, tolerance=20):
    """
    Analyzes fabric weights and recommends the most suitable options for T-shirt production.

    Parameters:
        fabric_weights (list): A list of available fabric weights in grams (e.g., [180, 240, 320]).
        tolerance (int): Acceptable weight deviation for T-shirt fabric selection (default is 20 grams).

    Returns:
        list: Recommended fabric weights for T-shirt production.
    """
    # Define an ideal range for T-shirt fabric weight (commonly used: 180g - 240g with slight tolerance)
    ideal_min_weight = 180 - tolerance
    ideal_max_weight = 240 + tolerance

    # Filter fabric weights within the ideal range
    recommended_weights = [
        weight for weight in fabric_weights
        if ideal_min_weight <= weight <= ideal_max_weight
    ]
    
    return recommended_weights


def main():
    """
    Main function to demonstrate fabric weight analysis and recommendation.
    """
    # Example data from Shaoxing Eagles Textile Co., Ltd.
    # Replace with actual data if available, e.g., fetched via an API or loaded from a database.
    fabric_data = {
        "Fabric Name": ["Cotton Jersey", "Polyester Spandex", "Heavy Cotton", "Linen Mix"],
        "Fabric Weight (g)": [180, 240, 320, 150]
    }

    # Create a DataFrame for better data handling
    df = pd.DataFrame(fabric_data)

    try:
        # Extract fabric weights
        fabric_weights = df["Fabric Weight (g)"].tolist()

        # Analyze and recommend suitable fabric weights for T-shirts
        recommendations = recommend_fabric_for_tshirts(fabric_weights)

        # Display recommendations
        print("Recommended fabric weights for T-shirt production:")
        for weight in recommendations:
            fabric_name = df.loc[df["Fabric Weight (g)"] == weight, "Fabric Name"].values[0]
            print(f"- {fabric_name} ({weight}g)")

    except KeyError as e:
        print(f"Error: Missing expected column in fabric data - {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
