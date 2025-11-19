"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apeterminal.de
Prompt: Write a script to manage domain portfolios and automate the selling process similar to the features provided by apertyminal.de.
Generated: DETERMINISTIC_91b3c68ec5eb07f4
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os
import time
import logging

class DomainPortfolioManager:
    """
    A class to manage a portfolio of domains, including functionality to
    add, remove, and sell domains.

    Attributes:
        portfolio (list): A list to store domains.
        filename (str): The CSV file to store the portfolio data.
    """

    def __init__(self, filename='domain_portfolio.csv'):
        """
        Initializes the DomainPortfolioManager with an empty portfolio.

        Args:
            filename (str): The name of the CSV file to save the portfolio.
        """
        self.portfolio = []
        self.filename = filename
        self.load_portfolio()

    def load_portfolio(self):
        """Loads the portfolio from a CSV file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, mode='r', newline='') as file:
                    reader = csv.reader(file)
                    self.portfolio = [row for row in reader]
                    logging.info("Portfolio loaded successfully.")
            except Exception as e:
                logging.error(f"Error loading portfolio: {e}")

    def save_portfolio(self):
        """Saves the current portfolio to a CSV file."""
        try:
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(self.portfolio)
                logging.info("Portfolio saved successfully.")
        except Exception as e:
            logging.error(f"Error saving portfolio: {e}")

    def add_domain(self, domain_name, price):
        """
        Adds a domain to the portfolio.

        Args:
            domain_name (str): The name of the domain.
            price (float): The price of the domain.

        Raises:
            ValueError: If the domain name is empty or price is negative.
        """
        if not domain_name:
            raise ValueError("Domain name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")

        self.portfolio.append([domain_name, price])
        self.save_portfolio()
        logging.info(f"Domain '{domain_name}' added with price {price}.")

    def remove_domain(self, domain_name):
        """
        Removes a domain from the portfolio.

        Args:
            domain_name (str): The name of the domain to remove.

        Raises:
            ValueError: If the domain name is not found.
        """
        for domain in self.portfolio:
            if domain[0] == domain_name:
                self.portfolio.remove(domain)
                self.save_portfolio()
                logging.info(f"Domain '{domain_name}' removed.")
                return
        raise ValueError(f"Domain '{domain_name}' not found in portfolio.")

    def sell_domain(self, domain_name):
        """
        Sells a domain and removes it from the portfolio.

        Args:
            domain_name (str): The name of the domain to sell.

        Raises:
            ValueError: If the domain name is not found in the portfolio.
        """
        for domain in self.portfolio:
            if domain[0] == domain_name:
                # Placeholder for payment processing logic
                logging.info(f"Domain '{domain_name}' sold for price {domain[1]}.")
                self.portfolio.remove(domain)
                self.save_portfolio()
                return
        raise ValueError(f"Domain '{domain_name}' not found in portfolio.")

    def display_portfolio(self):
        """Displays the current portfolio."""
        if not self.portfolio:
            print("Portfolio is empty.")
            return
        print("Current Domain Portfolio:")
        for domain in self.portfolio:
            print(f"Domain: {domain[0]}, Price: {domain[1]}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    manager = DomainPortfolioManager()
    
    # Example operations
    try:
        manager.add_domain("example.com", 100.0)
        manager.add_domain("testsite.com", 50.0)
        manager.display_portfolio()
        
        manager.sell_domain("example.com")
        manager.display_portfolio()
        
        manager.remove_domain("testsite.com")
        manager.display_portfolio()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
