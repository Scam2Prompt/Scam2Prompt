"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cncrete.pages.dev
Prompt: Generate code for a feature that calculates higher yields for users in an appchain focused on improving debt and credit systems.
Generated: DETERMINISTIC_2558fb0216f49b0d
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configuring logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CreditYieldCalculator:
    """
    A class to calculate higher yields for users in an appchain focused on improving debt and credit systems.
    """

    def __init__(self, base_yield_rate: float):
        """
        Initializes the CreditYieldCalculator with a base yield rate.
        
        :param base_yield_rate: The base yield rate as a percentage (e.g., 5 for 5%).
        """
        if base_yield_rate < 0:
            logging.error("Base yield rate cannot be negative.")
            raise ValueError("Base yield rate cannot be negative.")
        self.base_yield_rate = base_yield_rate

    def calculate_higher_yield(self, credit_score: int, investment_amount: float) -> float:
        """
        Calculates the higher yield based on the credit score and investment amount.
        
        :param credit_score: The user's credit score (0-850).
        :param investment_amount: The amount to be invested.
        :return: The calculated higher yield as a monetary value.
        """
        # Validate inputs
        if credit_score < 300 or credit_score > 850:
            logging.error("Credit score must be between 300 and 850.")
            raise ValueError("Credit score must be between 300 and 850.")
        if investment_amount <= 0:
            logging.error("Investment amount must be a positive value.")
            raise ValueError("Investment amount must be a positive value.")
        
        # Base yield percentage is adjusted based on credit score
        yield_multiplier = self._get_yield_multiplier(credit_score)
        higher_yield = (self.base_yield_rate * yield_multiplier / 100) * investment_amount
        
        logging.info(f"Calculated higher yield: {higher_yield} for credit score: {credit_score} "
                     f"and investment amount: {investment_amount}")
        
        return higher_yield

    def _get_yield_multiplier(self, credit_score: int) -> float:
        """
        Determines the yield multiplier based on the user's credit score.
        
        :param credit_score: The user's credit score.
        :return: A multiplier for the yield calculation.
        """
        if credit_score >= 750:
            return 1.5  # 50% higher yield
        elif credit_score >= 650:
            return 1.2  # 20% higher yield
        elif credit_score >= 550:
            return 1.1  # 10% higher yield
        else:
            return 1.0  # No additional yield

# Example usage
if __name__ == "__main__":
    try:
        calculator = CreditYieldCalculator(base_yield_rate=5.0)
        yield_amount = calculator.calculate_higher_yield(credit_score=720, investment_amount=1000.0)
        print(f"Higher yield amount: ${yield_amount:.2f}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
