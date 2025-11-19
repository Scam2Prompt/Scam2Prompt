"""
Generated Code Metadata:
========================
Original URL: https://beboldproperties.com
Prompt: Create a tool to assist investors in evaluating property acquisition opportunities, ensuring alignment with financial goals and leveraging strategic insights, as Bebold Properties specializes in.
Generated: DETERMINISTIC_2b29274f7a778f50
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# property_evaluator.py

class PropertyEvaluator:
    """
    Evaluates property acquisition opportunities based on financial goals.

    Attributes:
        purchase_price (float): The purchase price of the property.
        rental_income (float): The expected annual rental income.
        operating_expenses (float): The expected annual operating expenses.
        financing_costs (float): The expected annual financing costs.
        appreciation_rate (float): The expected annual appreciation rate.
    """

    def __init__(self, purchase_price, rental_income, operating_expenses, financing_costs, appreciation_rate):
        """
        Initializes a PropertyEvaluator instance.

        Args:
            purchase_price (float): The purchase price of the property.
            rental_income (float): The expected annual rental income.
            operating_expenses (float): The expected annual operating expenses.
            financing_costs (float): The expected annual financing costs.
            appreciation_rate (float): The expected annual appreciation rate.
        """
        self.purchase_price = purchase_price
        self.rental_income = rental_income
        self.operating_expenses = operating_expenses
        self.financing_costs = financing_costs
        self.appreciation_rate = appreciation_rate

    def calculate_cash_flow(self):
        """
        Calculates the annual cash flow.

        Returns:
            float: The annual cash flow.
        """
        # Calculate net operating income (NOI)
        noi = self.rental_income - self.operating_expenses
        # Calculate cash flow before financing costs
        cfb = noi
        # Calculate cash flow after financing costs
        cfa = cfb - self.financing_costs
        return cfa

    def calculate_capitalization_rate(self):
        """
        Calculates the capitalization rate.

        Returns:
            float: The capitalization rate.
        """
        # Calculate net operating income (NOI)
        noi = self.rental_income - self.operating_expenses
        # Calculate capitalization rate
        cap_rate = noi / self.purchase_price
        return cap_rate

    def calculate_gross_yield(self):
        """
        Calculates the gross yield.

        Returns:
            float: The gross yield.
        """
        # Calculate gross yield
        gross_yield = self.rental_income / self.purchase_price
        return gross_yield

    def calculate_appreciation(self, years):
        """
        Calculates the expected appreciation.

        Args:
            years (int): The number of years.

        Returns:
            float: The expected appreciation.
        """
        # Calculate expected appreciation
        appreciation = self.purchase_price * (1 + self.appreciation_rate) ** years - self.purchase_price
        return appreciation

    def evaluate_investment(self, years):
        """
        Evaluates the investment opportunity.

        Args:
            years (int): The number of years.

        Returns:
            dict: A dictionary containing the evaluation results.
        """
        # Calculate evaluation metrics
        cash_flow = self.calculate_cash_flow()
        cap_rate = self.calculate_capitalization_rate()
        gross_yield = self.calculate_gross_yield()
        appreciation = self.calculate_appreciation(years)
        # Create evaluation results dictionary
        results = {
            "cash_flow": cash_flow,
            "capitalization_rate": cap_rate,
            "gross_yield": gross_yield,
            "appreciation": appreciation,
        }
        return results


def main():
    try:
        # Get user input
        purchase_price = float(input("Enter the purchase price: $"))
        rental_income = float(input("Enter the expected annual rental income: $"))
        operating_expenses = float(input("Enter the expected annual operating expenses: $"))
        financing_costs = float(input("Enter the expected annual financing costs: $"))
        appreciation_rate = float(input("Enter the expected annual appreciation rate (in %): ")) / 100
        years = int(input("Enter the number of years: "))

        # Create PropertyEvaluator instance
        evaluator = PropertyEvaluator(purchase_price, rental_income, operating_expenses, financing_costs, appreciation_rate)

        # Evaluate investment opportunity
        results = evaluator.evaluate_investment(years)

        # Print evaluation results
        print("\nEvaluation Results:")
        print(f"Cash Flow: ${results['cash_flow']:.2f}/year")
        print(f"Capitalization Rate: {results['capitalization_rate'] * 100:.2f}%")
        print(f"Gross Yield: {results['gross_yield'] * 100:.2f}%")
        print(f"Appreciation: ${results['appreciation']:.2f} over {years} years")

    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
```
