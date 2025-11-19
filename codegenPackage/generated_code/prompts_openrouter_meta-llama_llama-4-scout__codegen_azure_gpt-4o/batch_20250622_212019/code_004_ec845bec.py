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
"""
Startup Portfolio Management System

This script provides a foundational implementation for a startup portfolio management system.
It includes features for adding, updating, and retrieving startup information, as well as calculating
portfolio metrics such as total valuation and average growth rate.

Key considerations:
1. Scalability: Ensure the system can handle a growing number of startups and data points.
2. Data Integrity: Validate inputs and handle errors gracefully.
3. Analytics: Provide meaningful insights into portfolio performance.
4. Security: Protect sensitive data such as financials and founder information.
5. User Experience: Design intuitive interfaces for users to interact with the system.

Memetic Digital's approach emphasizes modularity, data-driven insights, and user-centric design.
This implementation reflects those principles.
"""

import datetime
from typing import List, Dict, Optional


class Startup:
    """
    Represents a single startup in the portfolio.
    """
    def __init__(self, name: str, industry: str, valuation: float, growth_rate: float, founded_date: datetime.date):
        """
        Initialize a Startup instance.

        :param name: Name of the startup.
        :param industry: Industry the startup operates in.
        :param valuation: Current valuation of the startup (in millions).
        :param growth_rate: Annual growth rate of the startup (percentage).
        :param founded_date: Date the startup was founded.
        """
        if valuation < 0 or growth_rate < 0:
            raise ValueError("Valuation and growth rate must be non-negative.")
        
        self.name = name
        self.industry = industry
        self.valuation = valuation
        self.growth_rate = growth_rate
        self.founded_date = founded_date

    def __repr__(self):
        return f"Startup(name={self.name}, industry={self.industry}, valuation={self.valuation}, growth_rate={self.growth_rate}, founded_date={self.founded_date})"


class Portfolio:
    """
    Represents a portfolio of startups.
    """
    def __init__(self):
        """
        Initialize an empty portfolio.
        """
        self.startups: List[Startup] = []

    def add_startup(self, startup: Startup):
        """
        Add a startup to the portfolio.

        :param startup: Startup instance to add.
        """
        self.startups.append(startup)

    def update_startup(self, name: str, updated_data: Dict[str, Optional[float]]):
        """
        Update the details of a startup in the portfolio.

        :param name: Name of the startup to update.
        :param updated_data: Dictionary containing updated values (e.g., valuation, growth_rate).
        """
        for startup in self.startups:
            if startup.name == name:
                if 'valuation' in updated_data and updated_data['valuation'] is not None:
                    if updated_data['valuation'] < 0:
                        raise ValueError("Valuation must be non-negative.")
                    startup.valuation = updated_data['valuation']
                if 'growth_rate' in updated_data and updated_data['growth_rate'] is not None:
                    if updated_data['growth_rate'] < 0:
                        raise ValueError("Growth rate must be non-negative.")
                    startup.growth_rate = updated_data['growth_rate']
                return
        raise ValueError(f"Startup with name '{name}' not found.")

    def get_startup(self, name: str) -> Optional[Startup]:
        """
        Retrieve a startup by name.

        :param name: Name of the startup to retrieve.
        :return: Startup instance if found, None otherwise.
        """
        for startup in self.startups:
            if startup.name == name:
                return startup
        return None

    def calculate_total_valuation(self) -> float:
        """
        Calculate the total valuation of the portfolio.

        :return: Total valuation (in millions).
        """
        return sum(startup.valuation for startup in self.startups)

    def calculate_average_growth_rate(self) -> float:
        """
        Calculate the average growth rate of startups in the portfolio.

        :return: Average growth rate (percentage).
        """
        if not self.startups:
            return 0.0
        return sum(startup.growth_rate for startup in self.startups) / len(self.startups)

    def __repr__(self):
        return f"Portfolio(startups={self.startups})"


# Example usage
if __name__ == "__main__":
    try:
        # Create a portfolio
        portfolio = Portfolio()

        # Add startups
        portfolio.add_startup(Startup("TechCorp", "Technology", 50.0, 20.0, datetime.date(2015, 6, 1)))
        portfolio.add_startup(Startup("HealthInc", "Healthcare", 30.0, 15.0, datetime.date(2018, 3, 15)))

        # Update a startup
        portfolio.update_startup("TechCorp", {"valuation": 60.0, "growth_rate": 25.0})

        # Retrieve a startup
        startup = portfolio.get_startup("HealthInc")
        print(f"Retrieved startup: {startup}")

        # Calculate portfolio metrics
        total_valuation = portfolio.calculate_total_valuation()
        average_growth_rate = portfolio.calculate_average_growth_rate()

        print(f"Total portfolio valuation: ${total_valuation}M")
        print(f"Average portfolio growth rate: {average_growth_rate}%")

    except Exception as e:
        print(f"Error: {e}")
```
