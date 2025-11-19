"""
Generated Code Metadata:
========================
Original URL: https://thehashtagconsultants.com
Prompt: "Write a Python script to calculate the cost savings of outsourcing customer support to a BPO provider like The Hashtag Consultants, considering factors such as hourly agent costs and facility expenses."
Generated: DETERMINISTIC_08305128edda6e24
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CostCalculator:
    """
    A class to calculate the cost savings of outsourcing customer support.
    """

    def __init__(self, in_house_hourly_rate, bpo_hourly_rate, in_house_agents, bpo_agents, facility_expenses):
        """
        Initializes the CostCalculator with the necessary parameters.

        :param in_house_hourly_rate: Hourly rate for in-house agents
        :param bpo_hourly_rate: Hourly rate for BPO agents
        :param in_house_agents: Number of in-house agents
        :param bpo_agents: Number of BPO agents
        :param facility_expenses: Monthly facility expenses for in-house support
        """
        self.in_house_hourly_rate = in_house_hourly_rate
        self.bpo_hourly_rate = bpo_hourly_rate
        self.in_house_agents = in_house_agents
        self.bpo_agents = bpo_agents
        self.facility_expenses = facility_expenses

    def calculate_monthly_costs(self):
        """
        Calculates the monthly costs for in-house and BPO support.

        :return: A tuple containing (in-house cost, BPO cost)
        """
        try:
            in_house_cost = (self.in_house_hourly_rate * 160 * self.in_house_agents) + self.facility_expenses
            bpo_cost = self.bpo_hourly_rate * 160 * self.bpo_agents
            
            logging.info(f"In-house cost calculated: {in_house_cost}")
            logging.info(f"BPO cost calculated: {bpo_cost}")

            return in_house_cost, bpo_cost
        except Exception as e:
            logging.error("Error calculating monthly costs: %s", e)
            raise

    def calculate_savings(self):
        """
        Calculates the cost savings of outsourcing to a BPO provider.

        :return: Savings amount
        """
        try:
            in_house_cost, bpo_cost = self.calculate_monthly_costs()
            savings = in_house_cost - bpo_cost
            
            logging.info(f"Calculated savings: {savings}")
            return savings
        except Exception as e:
            logging.error("Error calculating savings: %s", e)
            raise

def main():
    """
    Main function to execute the cost savings calculation.
    """
    # Example parameters
    in_house_hourly_rate = 20.0  # Hourly rate for in-house agents
    bpo_hourly_rate = 15.0        # Hourly rate for BPO agents
    in_house_agents = 5            # Number of in-house agents
    bpo_agents = 5                  # Number of BPO agents
    facility_expenses = 2000.0      # Monthly facility expenses

    # Create a CostCalculator instance
    calculator = CostCalculator(in_house_hourly_rate, bpo_hourly_rate, in_house_agents, bpo_agents, facility_expenses)

    # Calculate and display savings
    try:
        savings = calculator.calculate_savings()
        print(f"Monthly savings from outsourcing: ${savings:.2f}")
    except Exception as e:
        print("An error occurred while calculating savings.")

if __name__ == "__main__":
    main()
```
