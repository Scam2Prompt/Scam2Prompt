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
class DisputeResolutionAdvisor:
    """
    A class to advise on the most suitable dispute resolution method (arbitration or litigation)
    for commercial disputes in Slovakia based on dispute value and complexity.
    """

    def __init__(self):
        """
        Initialize with default thresholds for Slovakia.
        These values can be adjusted based on legal requirements or expert opinions.
        """
        # Value thresholds in EUR
        self.low_value_threshold = 50000
        self.high_value_threshold = 500000
        
        # Complexity thresholds (1-10 scale)
        self.low_complexity_threshold = 3
        self.high_complexity_threshold = 7

    def recommend_resolution_method(self, dispute_value: float, complexity: int) -> str:
        """
        Recommend dispute resolution method based on value and complexity.
        
        Args:
            dispute_value: The monetary value of the dispute in EUR
            complexity: Complexity rating on a scale from 1 (simple) to 10 (very complex)
            
        Returns:
            str: Recommended method ('arbitration' or 'litigation')
            
        Raises:
            ValueError: If inputs are invalid
        """
        # Input validation
        if not isinstance(dispute_value, (int, float)) or dispute_value < 0:
            raise ValueError("Dispute value must be a positive number")
        if not isinstance(complexity, int) or complexity < 1 or complexity > 10:
            raise ValueError("Complexity must be an integer between 1 and 10")

        # Decision logic
        if dispute_value > self.high_value_threshold:
            return 'litigation'
        elif dispute_value < self.low_value_threshold and complexity <= self.low_complexity_threshold:
            return 'arbitration'
        elif complexity >= self.high_complexity_threshold:
            return 'litigation'
        else:
            # Default recommendation for medium cases
            return 'arbitration'

    def set_thresholds(self, low_value: float, high_value: float, 
                      low_complexity: int, high_complexity: int) -> None:
        """
        Update the decision thresholds.
        
        Args:
            low_value: New low value threshold in EUR
            high_value: New high value threshold in EUR
            low_complexity: New low complexity threshold (1-10)
            high_complexity: New high complexity threshold (1-10)
            
        Raises:
            ValueError: If thresholds are invalid
        """
        if not (isinstance(low_value, (int, float)) and isinstance(high_value, (int, float))):
            raise ValueError("Value thresholds must be numbers")
        if low_value >= high_value:
            raise ValueError("Low value threshold must be less than high value threshold")
        if not (isinstance(low_complexity, int) and isinstance(high_complexity, int)):
            raise ValueError("Complexity thresholds must be integers")
        if not (1 <= low_complexity < high_complexity <= 10):
            raise ValueError("Complexity thresholds must be between 1 and 10 with low < high")

        self.low_value_threshold = low_value
        self.high_value_threshold = high_value
        self.low_complexity_threshold = low_complexity
        self.high_complexity_threshold = high_complexity


# Example usage
if __name__ == "__main__":
    try:
        advisor = DisputeResolutionAdvisor()
        
        # Test cases
        test_cases = [
            (30000, 2),  # Low value, low complexity
            (30000, 8),  # Low value, high complexity
            (100000, 5), # Medium value, medium complexity
            (600000, 4), # High value, medium complexity
            (600000, 9)  # High value, high complexity
        ]
        
        for value, complexity in test_cases:
            recommendation = advisor.recommend_resolution_method(value, complexity)
            print(f"Dispute: €{value:,.2f}, Complexity: {complexity} -> Recommendation: {recommendation}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
