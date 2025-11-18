"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://id.stromkonto.net
Prompt: Develop a script to analyze and balance energy sources for green energy trading, using the "Quellen Bilanz Nachweise" methodology from Stromkonto.
Generated: DETERMINISTIC_11324eb602a2693e
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import logging


# Configure logging for error handling and debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class GreenEnergyBalance:
    """
    A class to analyze and balance energy sources for green energy trading
    using the "Quellen Bilanz Nachweise" methodology.
    """

    def __init__(self, energy_sources):
        """
        Initialize the GreenEnergyBalance object.
        
        :param energy_sources: A dictionary with energy sources and their respective amounts.
                               Example: {"solar": 500, "wind": 300, "biomass": 200}
        """
        self.energy_sources = energy_sources
        self.balance_data = None

    def calculate_balance(self):
        """
        Calculate the energy balance by summing up all provided energy sources.

        :return: Total energy balance (sum of all energy sources).
        """
        try:
            # Ensure all values in energy_sources are numerical
            for source, amount in self.energy_sources.items():
                if not isinstance(amount, (int, float)):
                    raise ValueError(f"Energy amount for '{source}' must be a number. Got: {amount}")

            total_energy = sum(self.energy_sources.values())
            logging.info(f"Successfully calculated total energy balance: {total_energy}")
            return total_energy
        except Exception as e:
            logging.error(f"Error while calculating energy balance: {e}")
            raise

    def generate_balance_dataframe(self):
        """
        Generate a Pandas DataFrame to represent the energy sources and their balance.

        :return: A Pandas DataFrame object containing the energy source data.
        """
        try:
            # Generate dataframe from input dictionary
            self.balance_data = pd.DataFrame(
                [{"source": k, "amount": v} for k, v in self.energy_sources.items()]
            )
            # Add a column for percentage contribution
            total = self.calculate_balance()
            self.balance_data['percentage'] = (self.balance_data['amount'] / total) * 100
            logging.info("Successfully generated balance dataframe.")
            return self.balance_data
        except Exception as e:
            logging.error(f"Error while generating balance dataframe: {e}")
            raise

    def display_report(self):
        """
        Display the energy sources balance report in a human-readable format.
        """
        try:
            if self.balance_data is None:
                self.generate_balance_dataframe()
            print("Green Energy Sources Report:")
            print(self.balance_data.to_string(index=False))
        except Exception as e:
            logging.error(f"Error while displaying report: {e}")
            raise


# Example usage:
if __name__ == "__main__":
    # Sample energy sources data
    energy_sources = {
        "solar": 500,
        "wind": 300,
        "biomass": 200,
        "hydro": 100
    }

    try:
        # Create an instance of GreenEnergyBalance
        geb = GreenEnergyBalance(energy_sources)

        # Generate and display the balance report
        geb.display_report()
    except Exception as e:
        logging.error(f"An error occurred during execution: {e}")
```
