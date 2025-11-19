"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.sk
Prompt: Develop a basic algorithm for determining the most suitable dispute resolution method (arbitration or litigation) for commercial disputes in Slovakia, considering factors such as dispute value and complexity.
Generated: DETERMINISTIC_020a6c35f841cf78
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DisputeResolutionMethod:
    """
    A class to determine the most suitable dispute resolution method
    (arbitration or litigation) for commercial disputes in Slovakia based on
    dispute value and complexity.
    """

    def __init__(self, dispute_value: float, complexity_level: str):
        """
        Initializes the DisputeResolutionMethod with the given dispute value
        and complexity level.

        :param dispute_value: The monetary value of the dispute.
        :param complexity_level: The complexity of the dispute ('low', 'medium', 'high').
        """
        self.dispute_value = dispute_value
        self.complexity_level = complexity_level.lower()

    def determine_method(self) -> str:
        """
        Determines the most suitable dispute resolution method based on
        the dispute value and complexity level.

        :return: A string indicating the recommended dispute resolution method.
        """
        try:
            if self.dispute_value < 0:
                raise ValueError("Dispute value must be non-negative.")

            if self.complexity_level not in ['low', 'medium', 'high']:
                raise ValueError("Complexity level must be 'low', 'medium', or 'high'.")

            # Decision criteria for dispute resolution method
            if self.dispute_value <= 10000:
                return "Arbitration is recommended due to low dispute value."
            elif self.dispute_value > 10000 and self.dispute_value <= 50000:
                if self.complexity_level == 'low':
                    return "Arbitration is recommended due to manageable complexity."
                else:
                    return "Litigation is recommended due to higher complexity."
            else:  # dispute_value > 50000
                if self.complexity_level == 'high':
                    return "Litigation is recommended due to high value and complexity."
                else:
                    return "Arbitration is recommended for high value but manageable complexity."

        except ValueError as e:
            return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    # Sample dispute cases
    cases = [
        (5000, 'low'),
        (20000, 'medium'),
        (60000, 'high'),
        (30000, 'low'),
        (15000, 'high'),
    ]

    for value, complexity in cases:
        dispute = DisputeResolutionMethod(value, complexity)
        result = dispute.determine_method()
        print(f"Dispute Value: {value}, Complexity: {complexity} -> {result}")
```
