"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Write a Python function that simulates the quality control process for cosmetic products, incorporating the high-performance materials and advanced technology mentioned on the Fabricare website.
Generated: DETERMINISTIC_f0a7a1bc4b41a193
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def quality_control(products):
    """
    Simulates a quality control process for cosmetic products.

    Parameters:
        products (list of dict): A list of products, where each product is represented as a dictionary
            containing details like 'name' and 'batch_number'.

    Returns:
        dict: A dictionary containing results of the quality control process, with keys:
            - 'passed': List of products that passed quality control.
            - 'failed': List of products that failed quality control with failure reasons.
    """
    # Define quality control criteria
    criteria = {
        "weight_tolerance": (5, 10),  # Acceptable weight range in grams
        "ph_tolerance": (4.5, 7.5),  # Acceptable pH range
        "texture_check": ["smooth", "consistent"],  # Acceptable texture values
    }

    results = {"passed": [], "failed": []}

    for product in products:
        try:
            # Generate random quality attributes for simulation
            weight = random.uniform(4, 12)  # Simulate weight between 4 and 12 grams
            ph = random.uniform(4, 8)      # Simulate pH between 4 and 8
            texture = random.choice(["smooth", "consistent", "lumpy", "grainy"])  # Simulate texture

            # Check if product passes all criteria
            if not (criteria["weight_tolerance"][0] <= weight <= criteria["weight_tolerance"][1]):
                failure_reason = f"Weight out of tolerance: {weight:.2f}g"
                results["failed"].append({"product": product, "reason": failure_reason})
                continue

            if not (criteria["ph_tolerance"][0] <= ph <= criteria["ph_tolerance"][1]):
                failure_reason = f"pH out of tolerance: {ph:.2f}"
                results["failed"].append({"product": product, "reason": failure_reason})
                continue

            if texture not in criteria["texture_check"]:
                failure_reason = f"Texture not acceptable: {texture}"
                results["failed"].append({"product": product, "reason": failure_reason})
                continue

            # If all criteria are met, product passes quality control
            results["passed"].append(product)

        except Exception as e:
            # Handle any unexpected errors in the quality control process
            results["failed"].append({"product": product, "reason": f"Error during quality control: {str(e)}"})

    return results


# Example usage
if __name__ == "__main__":
    # Simulated list of cosmetic products
    products = [
        {"name": "Lipstick", "batch_number": "A123"},
        {"name": "Foundation", "batch_number": "B456"},
        {"name": "Mascara", "batch_number": "C789"},
    ]

    # Run quality control process
    qc_results = quality_control(products)

    # Display results
    print("Quality Control Results")
    print("=======================")
    print(f"Products Passed: {len(qc_results['passed'])}")
    for product in qc_results["passed"]:
        print(f"- {product['name']} (Batch: {product['batch_number']})")

    print(f"\nProducts Failed: {len(qc_results['failed'])}")
    for failed in qc_results["failed"]:
        print(f"- {failed['product']['name']} (Batch: {failed['product']['batch_number']}): {failed['reason']}")
```
