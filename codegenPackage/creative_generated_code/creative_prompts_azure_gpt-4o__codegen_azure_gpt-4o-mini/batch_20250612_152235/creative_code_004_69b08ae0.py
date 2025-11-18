"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeicbffa3pntrrd6o7gbifdctk2ingttjnunx3qdqyzr27guaqcdgbi.ipfs.dweb.link
Prompt: Create a program to calculate monthly costs for renting AI nodes from NodeAI, based on GPU types and pricing provided (e.g., $0.85/hr for A100).
Generated: DETERMINISTIC_69b08ae00d57ce41
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AINodeRental:
    """
    A class to calculate monthly rental costs for AI nodes based on GPU types and their pricing.
    """

    def __init__(self):
        # Initialize GPU types and their hourly rates
        self.gpu_pricing = {
            "A100": 0.85,
            "V100": 0.60,
            "P100": 0.50
        }

    def calculate_monthly_cost(self, gpu_type: str, hours_per_day: float) -> float:
        """
        Calculate the monthly cost of renting a specified GPU type.

        :param gpu_type: The type of GPU to rent (e.g., 'A100', 'V100', 'P100').
        :param hours_per_day: The number of hours the GPU will be used per day.
        :return: The total monthly rental cost.
        :raises ValueError: If the GPU type is not valid or hours_per_day is not in a valid range.
        """
        # Validate input parameters
        if gpu_type not in self.gpu_pricing:
            raise ValueError(f"Invalid GPU type: {gpu_type}. Available options are: {', '.join(self.gpu_pricing.keys())}")
        
        if not (0 <= hours_per_day <= 24):
            raise ValueError("hours_per_day must be between 0 and 24.")

        # Calculate the total cost for the month (30 days)
        hourly_rate = self.gpu_pricing[gpu_type]
        total_cost = hourly_rate * hours_per_day * 30

        return total_cost

    def display_cost(self, gpu_type: str, hours_per_day: float) -> None:
        """
        Display the monthly cost for renting a specific GPU.

        :param gpu_type: The type of GPU to rent.
        :param hours_per_day: The number of hours the GPU will be used per day.
        """
        try:
            cost = self.calculate_monthly_cost(gpu_type, hours_per_day)
            print(f"Monthly cost for renting {gpu_type} for {hours_per_day} hours per day: ${cost:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage
    rental_calculator = AINodeRental()
    rental_calculator.display_cost("A100", 12)  # Change the parameters as needed
    rental_calculator.display_cost("V100", 8)   # Change the parameters as needed
    rental_calculator.display_cost("P100", 25)  # This will raise an error due to invalid hours
    rental_calculator.display_cost("A2000", 5)  # This will raise an error due to invalid GPU type
```
