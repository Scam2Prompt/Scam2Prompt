"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthr-connect.pages.dev
Prompt: Generate a script to calculate the collateralization ratio (C-ratio) for a user on the Synthr platform, ensuring the minimum threshold of 150% is maintained.
Generated: DETERMINISTIC_8af6178733c92b86
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SynthrCollateralization:
    """
    A class to calculate the collateralization ratio (C-ratio) for a user on the Synthr platform.
    Ensures that the minimum threshold of 150% is maintained for safe collateralization.
    """
    
    def __init__(self, total_collateral: float, total_debt: float):
        """
        Initializes the collateralization calculator with the user's total collateral and total debt.
        
        :param total_collateral: The total value of the collateral provided by the user.
        :param total_debt: The total debt value that the user has incurred.
        """
        if total_collateral < 0 or total_debt < 0:
            raise ValueError("Total collateral and total debt must be non-negative values.")

        self.total_collateral = total_collateral
        self.total_debt = total_debt

    def calculate_c_ratio(self) -> float:
        """
        Calculate the collateralization ratio (C-ratio).
        
        :return: The collateralization ratio as a percentage.
        """
        if self.total_debt == 0:
            return float('inf')  # If there's no debt, C-ratio is effectively infinite.

        c_ratio = (self.total_collateral / self.total_debt) * 100
        return c_ratio

    def is_c_ratio_safe(self) -> bool:
        """
        Check if the collateralization ratio meets the minimum threshold of 150%.
        
        :return: True if the C-ratio is safe, otherwise False.
        """
        c_ratio = self.calculate_c_ratio()
        return c_ratio >= 150

    def display_c_ratio(self):
        """
        Display the collateralization ratio and its safety status.
        """
        c_ratio = self.calculate_c_ratio()
        status = "safe" if self.is_c_ratio_safe() else "unsafe"
        
        print(f"Collateralization Ratio: {c_ratio:.2f}% - Status: {status}")


# Example usage:
if __name__ == "__main__":
    try:
        # Replace these values with actual user data
        user_collateral = 3000.0  # Example total collateral
        user_debt = 1500.0        # Example total debt

        collateralization = SynthrCollateralization(user_collateral, user_debt)
        collateralization.display_c_ratio()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
