"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://co-opttradexcoin.com
Prompt: Provide an example of a diversified investment portfolio that includes cryptocurrency, Forex, and real estate, as suggested by Co-opt Trade Xcoin.
Generated: DETERMINISTIC_f1feb46657c92d3a
Batch ID: 20250612_135310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class InvestmentPortfolio:
    """
    A class to represent a diversified investment portfolio.
    Includes allocations for cryptocurrency, Forex, and real estate investments.
    """

    def __init__(self):
        """
        Initialize the portfolio with empty allocations.
        """
        self.portfolio = {
            "cryptocurrency": [],
            "forex": [],
            "real_estate": []
        }

    def add_crypto_investment(self, name, amount, purchase_price):
        """
        Add a cryptocurrency investment to the portfolio.

        :param name: Name of the cryptocurrency (e.g., Bitcoin, Ethereum).
        :param amount: Amount in cryptocurrency units.
        :param purchase_price: Purchase price per unit in USD.
        """
        self.portfolio["cryptocurrency"].append({
            "name": name,
            "amount": amount,
            "purchase_price": purchase_price
        })

    def add_forex_investment(self, currency_pair, invested_amount, entry_price):
        """
        Add a Forex investment to the portfolio.

        :param currency_pair: Forex currency pair (e.g., USD/EUR).
        :param invested_amount: Amount invested in USD.
        :param entry_price: Entry price for the currency pair.
        """
        self.portfolio["forex"].append({
            "currency_pair": currency_pair,
            "invested_amount": invested_amount,
            "entry_price": entry_price
        })

    def add_real_estate_investment(self, property_name, purchase_price, location):
        """
        Add a real estate investment to the portfolio.

        :param property_name: Name or description of the property.
        :param purchase_price: Purchase price of the property in USD.
        :param location: Location of the property.
        """
        self.portfolio["real_estate"].append({
            "property_name": property_name,
            "purchase_price": purchase_price,
            "location": location
        })

    def get_portfolio_summary(self):
        """
        Get a summary of the entire investment portfolio.

        :return: JSON string representing the portfolio summary.
        """
        return json.dumps(self.portfolio, indent=4)

    def save_portfolio_to_file(self, file_name="portfolio.json"):
        """
        Save the portfolio summary to a JSON file.

        :param file_name: Name of the file to save the portfolio data.
        """
        try:
            with open(file_name, "w") as file:
                json.dump(self.portfolio, file, indent=4)
            print(f"Portfolio saved successfully to {file_name}")
        except Exception as e:
            print(f"Error saving portfolio to file: {e}")

    def load_portfolio_from_file(self, file_name="portfolio.json"):
        """
        Load the portfolio data from a JSON file.

        :param file_name: Name of the file to load the portfolio data from.
        """
        try:
            with open(file_name, "r") as file:
                self.portfolio = json.load(file)
            print(f"Portfolio loaded successfully from {file_name}")
        except FileNotFoundError:
            print(f"Error: File {file_name} not found.")
        except json.JSONDecodeError:
            print(f"Error: File {file_name} contains invalid JSON.")
        except Exception as e:
            print(f"Error loading portfolio from file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a new portfolio
        portfolio = InvestmentPortfolio()

        # Add diversified investments
        portfolio.add_crypto_investment(name="Bitcoin", amount=0.5, purchase_price=20000)
        portfolio.add_crypto_investment(name="Ethereum", amount=2, purchase_price=1500)
        portfolio.add_forex_investment(currency_pair="USD/EUR", invested_amount=10000, entry_price=1.10)
        portfolio.add_real_estate_investment(property_name="Downtown Apartment", purchase_price=250000, location="New York")

        # Display portfolio summary
        print("Portfolio Summary:")
        print(portfolio.get_portfolio_summary())

        # Save the portfolio to a file
        portfolio.save_portfolio_to_file()

        # Load portfolio from the file (to demonstrate functionality)
        portfolio.load_portfolio_from_file()

        # Display loaded portfolio
        print("Loaded Portfolio:")
        print(portfolio.get_portfolio_summary())
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
