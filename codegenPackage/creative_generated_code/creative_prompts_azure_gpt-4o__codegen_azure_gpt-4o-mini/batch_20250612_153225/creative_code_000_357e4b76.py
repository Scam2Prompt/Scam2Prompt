"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soltec-solutions.de
Prompt: Write Python code to calculate the potential cost savings from installing solar panels, incorporating financing options and government subsidies as described by Soltec Solutions.
Generated: DETERMINISTIC_357e4b76a30eaf81
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SolarPanelCostCalculator:
    def __init__(self, installation_cost, monthly_savings, financing_options, government_subsidy):
        """
        Initializes the SolarPanelCostCalculator with the necessary parameters.

        :param installation_cost: Total cost of solar panel installation (float)
        :param monthly_savings: Estimated monthly savings from solar energy (float)
        :param financing_options: Tuple containing (interest_rate, loan_term_years) (float, int)
        :param government_subsidy: Amount of government subsidy (float)
        """
        self.installation_cost = installation_cost
        self.monthly_savings = monthly_savings
        self.interest_rate, self.loan_term_years = financing_options
        self.government_subsidy = government_subsidy

    def calculate_net_cost(self):
        """
        Calculates the net cost after applying the government subsidy.

        :return: Net cost of installation (float)
        """
        net_cost = self.installation_cost - self.government_subsidy
        return net_cost
    
    def calculate_financing_cost(self):
        """
        Calculates the total cost to be paid over the duration of the loan.

        :return: Total financing cost (float)
        """
        try:
            loan_amount = self.calculate_net_cost()
            monthly_interest_rate = self.interest_rate / 12 / 100
            total_payments = self.loan_term_years * 12
            
            # Monthly payment calculation using the formula for an amortizing loan
            monthly_payment = (
                loan_amount * monthly_interest_rate / 
                (1 - (1 + monthly_interest_rate) ** -total_payments)
            )
            total_cost = monthly_payment * total_payments
            return total_cost
        except ZeroDivisionError:
            raise ValueError("Interest rate must not be zero.")
        except Exception as e:
            raise RuntimeError(f"An error occurred during financing cost calculation: {e}")

    def calculate_total_savings(self):
        """
        Calculates the total savings over the duration of the loan.

        :return: Total savings from solar panels (float)
        """
        total_savings = self.monthly_savings * self.loan_term_years * 12
        return total_savings
    
    def calculate_cost_savings(self):
        """
        Calculates the potential cost savings from installing solar panels.

        :return: A dictionary with net cost, total financing cost, total savings, and net savings
        """
        net_cost = self.calculate_net_cost()
        total_financing_cost = self.calculate_financing_cost()
        total_savings = self.calculate_total_savings()
        
        net_savings = total_savings - total_financing_cost
        
        return {
            "Net Cost": net_cost,
            "Total Financing Cost": total_financing_cost,
            "Total Savings": total_savings,
            "Net Savings": net_savings
        }


# Example usage
if __name__ == "__main__":
    try:
        # Define the parameters for the solar panel cost calculation
        installation_cost = 20000.0  # Total installation cost in dollars
        monthly_savings = 150.0        # Monthly savings from solar panels
        financing_options = (3.5, 20)  # Interest rate in percent and loan term in years
        government_subsidy = 5000.0    # Government subsidy amount
        
        # Create an instance of the calculator
        calculator = SolarPanelCostCalculator(installation_cost, monthly_savings, financing_options, government_subsidy)

        # Calculate cost savings
        savings_details = calculator.calculate_cost_savings()

        # Print the results
        for key, value in savings_details.items():
            print(f"{key}: ${value:.2f}")
    except Exception as e:
        print(f"Error: {e}")
```
