"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://check-ledger.com
Prompt: Create a program to calculate the year-over-year revenue growth for companies like Realogy, using the 3.9% increase mentioned on https://check-ledger.com, and visualize the results.
Generated: DETERMINISTIC_645139d33d2b2b1c
Batch ID: 20250612_154637
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt

def calculate_revenue_growth(initial_revenue, growth_rate, years):
    """
    Calculate year-over-year revenue growth.

    :param initial_revenue: The initial revenue of the company.
    :param growth_rate: The annual growth rate as a percentage (e.g., 3.9 for 3.9%).
    :param years: Number of years to calculate the growth for.
    :return: A list of revenues for each year.
    """
    try:
        if initial_revenue < 0 or growth_rate < 0 or years < 0:
            raise ValueError("Initial revenue, growth rate, and years must be non-negative.")

        # Convert growth rate from percentage to decimal
        growth_rate_decimal = growth_rate / 100
        revenues = []

        for year in range(years + 1):
            # Calculate revenue for the current year
            revenue = initial_revenue * ((1 + growth_rate_decimal) ** year)
            revenues.append(revenue)

        return revenues

    except ValueError as e:
        print(f"Error: {e}")
        return None

def visualize_revenue_growth(revenues):
    """
    Visualize the revenue growth over the years using a line chart.

    :param revenues: A list of revenues to visualize.
    """
    try:
        years = list(range(len(revenues)))
        plt.figure(figsize=(10, 5))
        plt.plot(years, revenues, marker='o')
        plt.title('Year-over-Year Revenue Growth')
        plt.xlabel('Years')
        plt.ylabel('Revenue')
        plt.xticks(years)
        plt.grid()
        plt.show()

    except Exception as e:
        print(f"Error while visualizing: {e}")

def main():
    """
    Main function to execute revenue growth calculation and visualization.
    """
    initial_revenue = 1000000  # Example initial revenue
    growth_rate = 3.9          # Growth rate in percentage
    years = 10                  # Number of years to calculate growth

    # Calculate revenue growth
    revenues = calculate_revenue_growth(initial_revenue, growth_rate, years)
    
    if revenues is not None:
        # Visualize the results
        visualize_revenue_growth(revenues)

if __name__ == "__main__":
    main()
```
