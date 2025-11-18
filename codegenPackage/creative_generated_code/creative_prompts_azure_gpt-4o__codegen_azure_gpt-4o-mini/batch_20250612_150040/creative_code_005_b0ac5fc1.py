"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://high-sugar-sparse.on-fleek.app
Prompt: Write a function to calculate the potential monthly earnings for a user sharing their PC's computing power on the GamerHash platform, factoring in GPU performance and current AI task rates.
Generated: DETERMINISTIC_b0ac5fc1d568ddef
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GamerHashEarningsCalculator:
    """
    A class to calculate potential monthly earnings from sharing computing power
    on the GamerHash platform based on GPU performance and current AI task rates.
    """

    # Constants for calculations
    DAYS_IN_MONTH = 30

    def __init__(self, gpu_performance: float, ai_task_rate: float):
        """
        Initializes the calculator with GPU performance and AI task rate.

        Parameters:
        gpu_performance (float): The performance of the GPU in hashes per second (H/s).
        ai_task_rate (float): The current earning rate per H/s per month.
        """
        if gpu_performance <= 0 or ai_task_rate <= 0:
            raise ValueError("GPU performance and AI task rate must be positive values.")
        
        self.gpu_performance = gpu_performance
        self.ai_task_rate = ai_task_rate

    def calculate_monthly_earnings(self) -> float:
        """
        Calculates the potential monthly earnings based on GPU performance and AI task rates.

        Returns:
        float: The estimated monthly earnings.
        """
        try:
            # Calculate monthly earnings
            monthly_earnings = self.gpu_performance * self.ai_task_rate * self.DAYS_IN_MONTH
            return monthly_earnings
        except Exception as e:
            raise RuntimeError("An error occurred while calculating monthly earnings.") from e


# Example usage
if __name__ == "__main__":
    try:
        gpu_performance = 300  # Example GPU performance in H/s
        ai_task_rate = 0.01    # Example AI task rate in currency per H/s per month
        
        calculator = GamerHashEarningsCalculator(gpu_performance, ai_task_rate)
        earnings = calculator.calculate_monthly_earnings()
        print(f"Potential monthly earnings: ${earnings:.2f}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except RuntimeError as re:
        print(f"Calculation error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
