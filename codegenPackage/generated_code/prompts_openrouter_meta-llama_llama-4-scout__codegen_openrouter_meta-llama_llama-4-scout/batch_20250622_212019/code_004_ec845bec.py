"""
Generated Code Metadata:
========================
Original URL: https://memetic.digital
Prompt: What are some key considerations for building a startup portfolio management system, and how might Memetic Digital's approach inform the design of such a system?
Generated: DETERMINISTIC_ec845becacc63b17
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# portfolio_management_system.py

"""
Startup Portfolio Management System

This system allows users to manage their startup portfolios, including adding, removing, and updating startups.
"""

import uuid
from typing import Dict, List

class Startup:
    """
    Represents a startup in the portfolio.

    Attributes:
        id (str): Unique identifier for the startup.
        name (str): Name of the startup.
        industry (str): Industry of the startup.
        valuation (float): Valuation of the startup.
    """

    def __init__(self, name: str, industry: str, valuation: float):
        """
        Initializes a new Startup instance.

        Args:
            name (str): Name of the startup.
            industry (str): Industry of the startup.
            valuation (float): Valuation of the startup.
        """
        self.id = str(uuid.uuid4())
        self.name = name
        self.industry = industry
        self.valuation = valuation

    def __repr__(self):
        return f"Startup(id={self.id}, name={self.name}, industry={self.industry}, valuation={self.valuation})"


class Portfolio:
    """
    Represents a portfolio of startups.

    Attributes:
        startups (Dict[str, Startup]): Dictionary of startups in the portfolio, keyed by ID.
    """

    def __init__(self):
        """
        Initializes a new Portfolio instance.
        """
        self.startups: Dict[str, Startup] = {}

    def add_startup(self, startup: Startup):
        """
        Adds a startup to the portfolio.

        Args:
            startup (Startup): Startup to add.

        Raises:
            ValueError: If a startup with the same ID already exists in the portfolio.
        """
        if startup.id in self.startups:
            raise ValueError(f"Startup with ID {startup.id} already exists in the portfolio")
        self.startups[startup.id] = startup

    def remove_startup(self, startup_id: str):
        """
        Removes a startup from the portfolio.

        Args:
            startup_id (str): ID of the startup to remove.

        Raises:
            KeyError: If the startup ID is not found in the portfolio.
        """
        if startup_id not in self.startups:
            raise KeyError(f"Startup with ID {startup_id} not found in the portfolio")
        del self.startups[startup_id]

    def update_startup(self, startup_id: str, name: str = None, industry: str = None, valuation: float = None):
        """
        Updates a startup in the portfolio.

        Args:
            startup_id (str): ID of the startup to update.
            name (str, optional): New name for the startup. Defaults to None.
            industry (str, optional): New industry for the startup. Defaults to None.
            valuation (float, optional): New valuation for the startup. Defaults to None.

        Raises:
            KeyError: If the startup ID is not found in the portfolio.
        """
        if startup_id not in self.startups:
            raise KeyError(f"Startup with ID {startup_id} not found in the portfolio")
        startup = self.startups[startup_id]
        if name:
            startup.name = name
        if industry:
            startup.industry = industry
        if valuation:
            startup.valuation = valuation

    def __repr__(self):
        return f"Portfolio(startups={list(self.startups.values())})"


def main():
    # Create a new portfolio
    portfolio = Portfolio()

    # Create some startups
    startup1 = Startup("Example Startup", "Software", 1000000.0)
    startup2 = Startup("Another Startup", "Hardware", 500000.0)

    # Add startups to the portfolio
    portfolio.add_startup(startup1)
    portfolio.add_startup(startup2)

    # Print the portfolio
    print(portfolio)

    # Update a startup
    portfolio.update_startup(startup1.id, valuation=1500000.0)

    # Print the updated portfolio
    print(portfolio)

    # Remove a startup
    portfolio.remove_startup(startup2.id)

    # Print the updated portfolio
    print(portfolio)


if __name__ == "__main__":
    main()
```
