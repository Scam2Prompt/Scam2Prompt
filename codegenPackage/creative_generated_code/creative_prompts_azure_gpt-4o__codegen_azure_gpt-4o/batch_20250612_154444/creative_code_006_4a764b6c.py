"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beboldproperties.com
Prompt: Write code to generate a detailed property investment report, incorporating metrics for income stream generation and capital growth, as Bebold Properties advocates.
Generated: DETERMINISTIC_4a764b6c93a1bd29
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt

class PropertyInvestmentReport:
    """
    Class to generate a property investment report incorporating metrics for
    income stream generation and capital growth.
    """

    def __init__(self, property_name, purchase_price, rental_income, expenses, growth_rate, years):
        """
        Initialize the property investment details.

        :param property_name: Name of the property
        :param purchase_price: Purchase price of the property
        :param rental_income: Monthly rental income
        :param expenses: Monthly expenses (e.g., maintenance, taxes)
        :param growth_rate: Annual capital growth rate (percentage)
        :param years: Investment time frame in years
        """
        self.property_name = property_name
        self.purchase_price = purchase_price
        self.rental_income = rental_income
        self.expenses = expenses
        self.growth_rate = growth_rate / 100
        self.years = years
        self.report_data = None

    def generate_report(self):
        """
        Generate the investment report with yearly metrics.
        """
        # Initialize data storage
        years = list(range(1, self.years + 1))
        net_income = []
        property_value = []
        roi = []

        current_value = self.purchase_price

        for year in years:
            # Calculate yearly metrics
            annual_rental_income = self.rental_income * 12
            annual_expenses = self.expenses * 12
            annual_net_income = annual_rental_income - annual_expenses
            net_income.append(annual_net_income)

            current_value += current_value * self.growth_rate
            property_value.append(current_value)

            # Calculate return on investment (ROI)
            roi.append((annual_net_income / self.purchase_price) * 100)

        # Store report data in a DataFrame for easy analysis and visualization
        self.report_data = pd.DataFrame({
            'Year': years,
            'Net Income ($)': net_income,
            'Property Value ($)': property_value,
            'ROI (%)': roi
        })

    def save_report(self, filename):
        """
        Save the generated report to a CSV file.

        :param filename: Name of the file to save the report
        """
        if self.report_data is None:
            raise ValueError("Report has not been generated. Call generate_report() first.")
        
        try:
            self.report_data.to_csv(filename, index=False)
            print(f"Report successfully saved to {filename}")
        except Exception as e:
            print(f"Error saving report: {e}")

    def plot_report(self):
        """
        Plot metrics from the report for visualization.
        """
        if self.report_data is None:
            raise ValueError("Report has not been generated. Call generate_report() first.")

        try:
            # Create subplots for metrics
            fig, axes = plt.subplots(3, 1, figsize=(8, 12))
            fig.suptitle(f'Investment Report for {self.property_name}', fontsize=16)

            # Plot net income
            axes[0].plot(self.report_data['Year'], self.report_data['Net Income ($)'], marker='o', label='Net Income ($)')
            axes[0].set_title('Annual Net Income')
            axes[0].set_xlabel('Year')
            axes[0].set_ylabel('Net Income ($)')
            axes[0].legend()
            axes[0].grid()

            # Plot property value
            axes[1].plot(self.report_data['Year'], self.report_data['Property Value ($)'], marker='o', label='Property Value ($)', color='green')
            axes[1].set_title('Property Value Over Time')
            axes[1].set_xlabel('Year')
            axes[1].set_ylabel('Property Value ($)')
            axes[1].legend()
            axes[1].grid()

            # Plot ROI
            axes[2].plot(self.report_data['Year'], self.report_data['ROI (%)'], marker='o', label='ROI (%)', color='orange')
            axes[2].set_title('Return on Investment (ROI)')
            axes[2].set_xlabel('Year')
            axes[2].set_ylabel('ROI (%)')
            axes[2].legend()
            axes[2].grid()

            plt.tight_layout(rect=[0, 0, 1, 0.96])
            plt.show()
        except Exception as e:
            print(f"Error plotting report: {e}")

# Example Usage
if __name__ == "__main__":
    # Initialize a sample property investment
    report = PropertyInvestmentReport(
        property_name="Oceanview Apartment",
        purchase_price=500000,
        rental_income=2500,
        expenses=500,
        growth_rate=5,
        years=10
    )

    report.generate_report()
    report.save_report("property_investment_report.csv")
    report.plot_report()
```
