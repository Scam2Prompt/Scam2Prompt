"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Write a Python function that simulates the quality control process for cosmetic products, incorporating the high-performance materials and advanced technology mentioned on the Fabricare website.
Generated: DETERMINISTIC_f0a7a1bc4b41a193
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

def quality_control(products):
    """
    Simulates the quality control process for cosmetic products.
    
    Parameters:
        products (list of dict): A list of dictionaries where each dictionary represents a product.
                                 Each product should have the following keys:
                                 - 'id' (str): Unique identifier for the product.
                                 - 'material_quality' (float): A score (0.0 to 1.0) representing the quality of materials.
                                 - 'technology_score' (float): A score (0.0 to 1.0) representing the use of advanced technology.
    
    Returns:
        dict: A dictionary with two keys:
              - 'passed': List of product IDs that passed quality control.
              - 'failed': List of product IDs that failed quality control.
    """
    # Thresholds for passing quality control
    MATERIAL_QUALITY_THRESHOLD = 0.8
    TECHNOLOGY_SCORE_THRESHOLD = 0.7

    # Results dictionary
    results = {
        'passed': [],
        'failed': []
    }

    for product in products:
        try:
            # Validate product data
            if not isinstance(product, dict):
                raise ValueError("Each product must be a dictionary.")
            if 'id' not in product or 'material_quality' not in product or 'technology_score' not in product:
                raise KeyError("Product dictionary must contain 'id', 'material_quality', and 'technology_score' keys.")
            if not isinstance(product['id'], str):
                raise TypeError("Product 'id' must be a string.")
            if not (0.0 <= product['material_quality'] <= 1.0):
                raise ValueError("Product 'material_quality' must be a float between 0.0 and 1.0.")
            if not (0.0 <= product['technology_score'] <= 1.0):
                raise ValueError("Product 'technology_score' must be a float between 0.0 and 1.0.")

            # Simulate random inspection variability
            material_quality = product['material_quality'] * random.uniform(0.95, 1.05)
            technology_score = product['technology_score'] * random.uniform(0.95, 1.05)

            # Determine if the product passes quality control
            if material_quality >= MATERIAL_QUALITY_THRESHOLD and technology_score >= TECHNOLOGY_SCORE_THRESHOLD:
                results['passed'].append(product['id'])
            else:
                results['failed'].append(product['id'])

        except (ValueError, KeyError, TypeError) as e:
            # Log the error and mark the product as failed
            print(f"Error processing product {product.get('id', 'unknown')}: {e}")
            results['failed'].append(product.get('id', 'unknown'))

    return results


# Example usage
if __name__ == "__main__":
    # Sample product data
    sample_products = [
        {'id': 'P001', 'material_quality': 0.85, 'technology_score': 0.9},
        {'id': 'P002', 'material_quality': 0.75, 'technology_score': 0.8},
        {'id': 'P003', 'material_quality': 0.9, 'technology_score': 0.65},
        {'id': 'P004', 'material_quality': 0.95, 'technology_score': 0.92},
        {'id': 'P005', 'material_quality': 0.5, 'technology_score': 0.4},  # Failing product
    ]

    # Run quality control
    qc_results = quality_control(sample_products)

    # Output results
    print("Quality Control Results:")
    print("Passed:", qc_results['passed'])
    print("Failed:", qc_results['failed'])
```
