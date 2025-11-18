"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftimus.com
Prompt: Write a program to calculate the cost-benefit ratio of importing Himalayan salt products, factoring in quality, packaging, and compliance with global standards as described by Craftimus Industries.
Generated: DETERMINISTIC_1143201656fc30f5
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to calculate the cost-benefit ratio of importing Himalayan salt products.
Factors:
1. Quality: Scored on a scale from 1 to 10.
2. Packaging: Scored on a scale from 1 to 10.
3. Compliance with global standards: Scored as a percentage [0-100%].
Craftimus Industries-specific weights:
- Quality: 50%
- Packaging: 30%
- Compliance: 20%
"""

# Required libraries
import sys


def calculate_cost_benefit_ratio(cost, quality_score, packaging_score, compliance_percentage):
    """
    Calculates the cost-benefit ratio of importing Himalayan salt products.

    Parameters:
    - cost (float): The cost of importing the product.
    - quality_score (int): Score for product quality (1-10).
    - packaging_score (int): Score for packaging quality (1-10).
    - compliance_percentage (float): Compliance with global standards (0-100%).

    Returns:
    - float: Cost-benefit ratio. Higher ratio indicates better value.
    """
    try:
        # Validate inputs
        if not (1 <= quality_score <= 10):
            raise ValueError("Quality score must be between 1 and 10.")
        if not (1 <= packaging_score <= 10):
            raise ValueError("Packaging score must be between 1 and 10.")
        if not (0 <= compliance_percentage <= 100):
            raise ValueError("Compliance percentage must be between 0 and 100.")
        if cost <= 0:
            raise ValueError("Cost must be greater than 0.")

        # Weights defined by Craftimus Industries
        QUALITY_WEIGHT = 0.5
        PACKAGING_WEIGHT = 0.3
        COMPLIANCE_WEIGHT = 0.2

        # Calculate weighted scores
        weighted_quality = quality_score * QUALITY_WEIGHT
        weighted_packaging = packaging_score * PACKAGING_WEIGHT
        weighted_compliance = compliance_percentage / 100 * COMPLIANCE_WEIGHT

        # Calculate total benefit score
        total_benefit_score = weighted_quality + weighted_packaging + weighted_compliance

        # Calculate cost-benefit ratio
        cost_benefit_ratio = total_benefit_score / cost

        return cost_benefit_ratio

    except ValueError as ve:
        print(f"Input Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected Error: {e}")
        sys.exit(1)


def main():
    """
    Main function to prompt user input and calculate the cost-benefit ratio.
    """
    try:
        print("Craftimus Industries Himalayan Salt Cost-Benefit Calculator")
        # Get user inputs
        cost = float(input("Enter the cost of importing the product (in USD): "))
        quality_score = int(input("Enter the quality score of the product (1-10): "))
        packaging_score = int(input("Enter the packaging score (1-10): "))
        compliance_percentage = float(input("Enter the compliance percentage with global standards (0-100): "))

        # Calculate cost-benefit ratio
        result = calculate_cost_benefit_ratio(cost, quality_score, packaging_score, compliance_percentage)

        # Display results
        print(f"The calculated cost-benefit ratio is: {result:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values where required.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
