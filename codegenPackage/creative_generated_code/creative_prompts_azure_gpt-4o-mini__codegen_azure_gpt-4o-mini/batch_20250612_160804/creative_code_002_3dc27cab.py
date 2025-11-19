"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethenaapp.pages.dev
Prompt: Explain how to utilize expiring futures or perpetual swaps to create fixed vs floating rate bond exposures in Ethena's product suite.
Generated: DETERMINISTIC_3dc27cabf9e4b456
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for handling futures and swaps
import logging

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EthenaBondExposure:
    """
    A class to represent bond exposure using Ethena's product suite with expiring futures
    or perpetual swaps to create fixed vs floating rate bond exposures.
    """

    def __init__(self, initial_investment: float):
        """
        Initializes the EthenaBondExposure with a given initial investment.
        
        :param initial_investment: The amount of currency to invest in bonds.
        """
        if initial_investment <= 0:
            logging.error("Initial investment must be greater than zero.")
            raise ValueError("Initial investment must be greater than zero.")
        
        self.initial_investment = initial_investment
        self.exposure = 0.0  # Current bond exposure

    def create_fixed_rate_exposure(self, fixed_rate: float, duration: int) -> float:
        """
        Create a fixed rate bond exposure using expiring futures.
        
        :param fixed_rate: The fixed interest rate for the bond.
        :param duration: The duration for which the bond is held, in months.
        :return: The total exposure created.
        """
        try:
            if fixed_rate <= 0:
                raise ValueError("Fixed rate must be greater than zero.")
            if duration <= 0:
                raise ValueError("Duration must be greater than zero.")

            # Calculate the total exposure based on fixed rate and initial investment
            self.exposure = self.initial_investment * (1 + fixed_rate / 100) ** (duration / 12)
            logging.info(f"Fixed rate exposure created: {self.exposure}")
            return self.exposure
        
        except Exception as e:
            logging.error(f"Error creating fixed rate exposure: {e}")
            raise

    def create_floating_rate_exposure(self, base_rate: float, spread: float, duration: int) -> float:
        """
        Create a floating rate bond exposure using perpetual swaps.
        
        :param base_rate: The base interest rate for the bond.
        :param spread: The additional spread over the base rate.
        :param duration: The duration for which the bond is held, in months.
        :return: The total exposure created.
        """
        try:
            if base_rate <= 0 or spread < 0:
                raise ValueError("Base rate must be greater than zero and spread must be non-negative.")
            if duration <= 0:
                raise ValueError("Duration must be greater than zero.")

            # Calculate the total exposure based on floating rate and initial investment
            floating_rate = base_rate + spread
            self.exposure = self.initial_investment * (1 + floating_rate / 100) ** (duration / 12)
            logging.info(f"Floating rate exposure created: {self.exposure}")
            return self.exposure

        except Exception as e:
            logging.error(f"Error creating floating rate exposure: {e}")
            raise

# Example usage of the EthenaBondExposure class
if __name__ == "__main__":
    try:
        # Initialize an EthenaBondExposure instance with an initial investment
        bond_exposure = EthenaBondExposure(initial_investment=10000)

        # Create a fixed rate exposure
        fixed_exposure = bond_exposure.create_fixed_rate_exposure(fixed_rate=5.0, duration=12)

        # Create a floating rate exposure
        floating_exposure = bond_exposure.create_floating_rate_exposure(base_rate=3.0, spread=1.0, duration=12)

    except Exception as e:
        logging.error(f"An error occurred in the main execution: {e}")
```
