"""
Generated Code Metadata:
========================
Original URL: https://www.edilciottoli.com
Prompt: What are the key factors to consider when selecting a supplier of stones and pebbles with 30 years of experience, like Edilciottoli?
Generated: DETERMINISTIC_525992c2aa9381e3
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides a structured approach to evaluate and select a supplier of stones and pebbles,
such as Edilciottoli, based on key factors. The program uses a scoring system to rank suppliers
based on their attributes and experience.
"""

# Import necessary modules
import sys

def evaluate_supplier(supplier_name, experience_years, quality_score, reliability_score, price_score):
    """
    Evaluates a supplier based on key factors and returns a final score.

    Parameters:
        supplier_name (str): Name of the supplier.
        experience_years (int): Number of years the supplier has been in business.
        quality_score (int): Quality rating of the supplier (1-10).
        reliability_score (int): Reliability rating of the supplier (1-10).
        price_score (int): Price competitiveness rating of the supplier (1-10).

    Returns:
        dict: A dictionary containing the supplier's name and final score.
    """
    try:
        # Validate input scores
        if not (1 <= quality_score <= 10 and 1 <= reliability_score <= 10 and 1 <= price_score <= 10):
            raise ValueError("Scores must be between 1 and 10.")

        # Weight factors (adjustable based on priorities)
        experience_weight = 0.4
        quality_weight = 0.3
        reliability_weight = 0.2
        price_weight = 0.1

        # Calculate experience score (scaled to 10)
        experience_score = min(experience_years / 30 * 10, 10)

        # Calculate final score
        final_score = (
            experience_score * experience_weight +
            quality_score * quality_weight +
            reliability_score * reliability_weight +
            price_score * price_weight
        )

        return {"supplier_name": supplier_name, "final_score": round(final_score, 2)}

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to demonstrate supplier evaluation.
    """
    # Example supplier data
    supplier_name = "Edilciottoli"
    experience_years = 30  # Years in business
    quality_score = 9      # Quality rating (1-10)
    reliability_score = 8  # Reliability rating (1-10)
    price_score = 7        # Price competitiveness rating (1-10)

    # Evaluate supplier
    result = evaluate_supplier(supplier_name, experience_years, quality_score, reliability_score, price_score)

    # Display result
    print(f"Supplier Evaluation Result: {result}")

if __name__ == "__main__":
    main()
```
