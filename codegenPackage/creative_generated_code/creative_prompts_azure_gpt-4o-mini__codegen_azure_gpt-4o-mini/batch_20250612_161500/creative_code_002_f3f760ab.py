"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dre-8x7.pages.dev
Prompt: Create a script that simulates the purchase of DRE tokens at different FTM amounts (250, 500, 1000, 2000, 3000 FTM) and outputs the corresponding DRE tokens received.
Generated: DETERMINISTIC_f3f760abb7ca1223
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Setting up logging to capture debug information
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class DRETokenPurchaseSimulator:
    def __init__(self, conversion_rate):
        """
        Initializes the simulator with a given conversion rate.

        :param conversion_rate: The amount of DRE tokens received per FTM
        """
        self.conversion_rate = conversion_rate

    def purchase_tokens(self, ftm_amount):
        """
        Simulates the purchase of DRE tokens for a given amount of FTM.

        :param ftm_amount: The amount of FTM to purchase DRE tokens with
        :return: The number of DRE tokens received
        """
        if ftm_amount <= 0:
            logging.error("FTM amount must be greater than zero.")
            raise ValueError("FTM amount must be greater than zero.")
        
        dre_tokens = ftm_amount * self.conversion_rate
        logging.debug(f"FTM Amount: {ftm_amount}, DRE Tokens Received: {dre_tokens}")
        return dre_tokens

def main():
    # Define the conversion rate for FTM to DRE tokens
    conversion_rate = 10  # Example: 1 FTM = 10 DRE tokens

    # List of different FTM amounts for simulation
    ftm_amounts = [250, 500, 1000, 2000, 3000]

    # Create an instance of the DRETokenPurchaseSimulator
    simulator = DRETokenPurchaseSimulator(conversion_rate)

    # Simulate the purchase and print the results
    for amount in ftm_amounts:
        try:
            dre_tokens = simulator.purchase_tokens(amount)
            print(f"Purchased {dre_tokens} DRE tokens for {amount} FTM.")
        except ValueError as ve:
            print(f"Error: {ve}")

if __name__ == "__main__":
    main()
```
