"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.eu
Prompt: Write code to calculate the percentage increase in FSC-certified wood purchases year-over-year, as highlighted by PDC Brush's environmental commitment.
Generated: DETERMINISTIC_0819a69b5daf9e5a
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FSCWoodPurchases:
    def __init__(self):
        # Initialize a dictionary to store yearly purchases
        self.purchases = {}

    def add_purchase(self, year: int, amount: float) -> None:
        """
        Adds the amount of FSC-certified wood purchased for the specified year.
        
        :param year: The year of the purchase
        :param amount: The amount of FSC-certified wood purchased (in whatever unit is appropriate)
        """
        if year in self.purchases:
            # If the year already exists, update the amount
            self.purchases[year] += amount
        else:
            # Add a new entry for the year
            self.purchases[year] = amount

    def calculate_percentage_increase(self, year: int) -> float:
        """
        Calculates the percentage increase in FSC-certified wood purchases from the previous year.

        :param year: The year to calculate the increase for
        :return: The percentage increase from the previous year or None if data is insufficient
        """
        if year <= 1:  # Cannot calculate for the first year
            raise ValueError("Year must be greater than 1 to calculate percentage increase.")
        
        previous_year = year - 1
        
        # Retrieve purchase amounts for the specified years
        current_amount = self.purchases.get(year)
        previous_amount = self.purchases.get(previous_year)

        # Check if both years have purchase data
        if current_amount is None or previous_amount is None:
            raise ValueError(f"Purchase data is missing for year {previous_year} or {year}.")

        # Calculate the percentage increase
        try:
            percentage_increase = ((current_amount - previous_amount) / previous_amount) * 100
            return percentage_increase
        except ZeroDivisionError:
            raise ValueError("Previous year's amount cannot be zero when calculating percentage increase.")

# Example usage
if __name__ == "__main__":
    wood_tracker = FSCWoodPurchases()
    
    # Adding purchase data for two consecutive years
    wood_tracker.add_purchase(2021, 1500.0)
    wood_tracker.add_purchase(2022, 1800.0)

    # Calculate the percentage increase for 2022
    try:
        increase = wood_tracker.calculate_percentage_increase(2022)
        print(f"Percentage increase in FSC-certified wood purchases from 2021 to 2022: {increase:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```
