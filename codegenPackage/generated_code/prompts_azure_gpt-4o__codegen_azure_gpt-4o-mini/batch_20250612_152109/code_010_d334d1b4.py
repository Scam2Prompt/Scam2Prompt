"""
Generated Code Metadata:
========================
Original URL: https://gadgetexa.com
Prompt: Provide a Python script to calculate the lifespan of laser printers, incorporating the considerations mentioned in Gadgetexa's review.
Generated: DETERMINISTIC_d334d1b497d80624
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class LaserPrinter:
    """
    A class to represent a laser printer and calculate its lifespan based on usage.
    """

    def __init__(self, model: str, purchase_date: str, average_pages_per_month: int, expected_lifespan_years: int):
        """
        Initializes a LaserPrinter instance.

        :param model: The model of the laser printer.
        :param purchase_date: The purchase date in 'YYYY-MM-DD' format.
        :param average_pages_per_month: Average number of pages printed per month.
        :param expected_lifespan_years: Expected lifespan of the printer in years.
        """
        self.model = model
        self.purchase_date = self._parse_date(purchase_date)
        self.average_pages_per_month = average_pages_per_month
        self.expected_lifespan_years = expected_lifespan_years

    @staticmethod
    def _parse_date(date_string: str) -> datetime.date:
        """
        Parses a date string into a datetime.date object.

        :param date_string: The date string in 'YYYY-MM-DD' format.
        :return: A datetime.date object.
        :raises ValueError: If the date string is not in the correct format.
        """
        try:
            return datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_string}. Expected format: YYYY-MM-DD.") from e

    def calculate_lifespan(self) -> str:
        """
        Calculates the expected lifespan of the printer based on the purchase date and expected lifespan.

        :return: A string indicating the expected lifespan of the printer.
        """
        current_date = datetime.date.today()
        lifespan_end_date = self.purchase_date.replace(year=self.purchase_date.year + self.expected_lifespan_years)

        if current_date > lifespan_end_date:
            return f"The printer {self.model} has exceeded its expected lifespan."
        else:
            remaining_years = (lifespan_end_date - current_date).days // 365
            return f"The printer {self.model} is expected to last for {remaining_years} more years."

    def calculate_total_pages(self) -> int:
        """
        Calculates the total number of pages the printer is expected to print over its lifespan.

        :return: Total number of pages expected to be printed.
        """
        return self.average_pages_per_month * 12 * self.expected_lifespan_years

def main():
    """
    Main function to create a LaserPrinter instance and display its lifespan and total pages.
    """
    try:
        # Example printer details
        printer = LaserPrinter(
            model="HP LaserJet Pro M404dn",
            purchase_date="2020-01-15",
            average_pages_per_month=500,
            expected_lifespan_years=5
        )

        # Display lifespan and total pages
        print(printer.calculate_lifespan())
        print(f"Total pages expected to be printed: {printer.calculate_total_pages()}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
