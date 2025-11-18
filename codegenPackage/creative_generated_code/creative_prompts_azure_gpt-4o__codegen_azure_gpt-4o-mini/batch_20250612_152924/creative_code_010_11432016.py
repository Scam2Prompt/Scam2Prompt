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
class HimalayanSaltProduct:
    """
    Represents a Himalayan salt product with attributes for quality, packaging, and compliance.
    """

    def __init__(self, quality_score: float, packaging_cost: float, compliance_score: float):
        """
        Initialize the HimalayanSaltProduct instance.

        :param quality_score: A score representing the quality of the product (0 to 100).
        :param packaging_cost: The cost of packaging in dollars.
        :param compliance_score: A score for compliance with global standards (0 to 100).
        """
        self.quality_score = quality_score
        self.packaging_cost = packaging_cost
        self.compliance_score = compliance_score

    def calculate_cost_benefit_ratio(self) -> float:
        """
        Calculate the cost-benefit ratio for the Himalayan salt product.

        :return: The cost-benefit ratio as a float.
        :raises ValueError: If any scores are outside the range of 0 to 100, or if packaging_cost is negative.
        """

        # Validate input values
        if not (0 <= self.quality_score <= 100):
            raise ValueError("Quality score must be between 0 and 100.")
        if not (0 <= self.compliance_score <= 100):
            raise ValueError("Compliance score must be between 0 and 100.")
        if self.packaging_cost < 0:
            raise ValueError("Packaging cost must not be negative.")

        # Calculate the benefit as a weighted sum of quality and compliance
        benefit = (self.quality_score + self.compliance_score) / 2

        # Cost is just the packaging cost
        cost = self.packaging_cost

        # Calculate the cost-benefit ratio
        if cost == 0:
            raise ValueError("Packaging cost cannot be zero for cost-benefit calculation.")

        cost_benefit_ratio = benefit / cost
        return cost_benefit_ratio


def main():
    """
    Main function to create a Himalayan salt product and calculate its cost-benefit ratio.
    """
    try:
        # Example values for quality, packaging cost, and compliance
        quality_score = 85.0
        packaging_cost = 10.0
        compliance_score = 90.0

        # Create a Himalayan salt product instance
        salt_product = HimalayanSaltProduct(quality_score, packaging_cost, compliance_score)

        # Calculate and print the cost-benefit ratio
        ratio = salt_product.calculate_cost_benefit_ratio()
        print(f"The cost-benefit ratio of importing the Himalayan salt product is: {ratio:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
