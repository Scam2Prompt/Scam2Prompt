"""
Generated Code Metadata:
========================
Original URL: https://bafybeicbffa3pntrrd6o7gbifdctk2ingttjnunx3qdqyzr27guaqcdgbi.ipfs.dweb.link
Prompt: Create a program to calculate monthly costs for renting AI nodes from NodeAI, based on GPU types and pricing provided (e.g., $0.85/hr for A100).
Generated: DETERMINISTIC_69b08ae00d57ce41
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class NodeAI:
    """
    A class to represent a NodeAI rental service for calculating monthly costs
    based on GPU types and their respective hourly rates.
    """

    def __init__(self):
        # Dictionary to hold GPU types and their hourly rates
        self.gpu_rates = {
            'A100': 0.85,
            'V100': 0.75,
            'T4': 0.50,
            'P100': 0.60
        }

    def calculate_monthly_cost(self, gpu_type: str, hours_per_day: float) -> float:
        """
        Calculate the monthly cost of renting a specified GPU type.

        Parameters:
        gpu_type (str): The type of GPU to rent.
        hours_per_day (float): The number of hours the GPU will be used per day.

        Returns:
        float: The total monthly cost for renting the GPU.

        Raises:
        ValueError: If the GPU type is not recognized or if hours_per_day is negative.
        """
        # Validate GPU type
        if gpu_type not in self.gpu_rates:
            raise ValueError(f"Unrecognized GPU type: {gpu_type}. Available types: {', '.join(self.gpu_rates.keys())}")

        # Validate hours per day
        if hours_per_day < 0:
            raise ValueError("Hours per day cannot be negative.")

        # Calculate the monthly cost
        hourly_rate = self.gpu_rates[gpu_type]
        monthly_cost = hourly_rate * hours_per_day * 30  # Assuming 30 days in a month
        return monthly_cost

def main():
    """
    Main function to execute the NodeAI rental cost calculation.
    """
    node_ai = NodeAI()

    try:
        # Example usage
        gpu_type = 'A100'  # Specify the GPU type
        hours_per_day = 10  # Specify the number of hours per day

        # Calculate the monthly cost
        cost = node_ai.calculate_monthly_cost(gpu_type, hours_per_day)
        print(f"The monthly cost for renting {gpu_type} for {hours_per_day} hours per day is: ${cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
