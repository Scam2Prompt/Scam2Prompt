"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safargenie.com
Prompt: Generate a detailed itinerary for a Chardham Yatra package that includes helicopter travel options and highlights key spiritual sites.
Generated: DETERMINISTIC_fedb5628d70ec7ca
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class ChardhamYatraPackage:
    def __init__(self, start_date, end_date, helicopter_option):
        """
        Initialize the Chardham Yatra package details.

        Args:
            start_date (str): Start date of the yatra in 'YYYY-MM-DD' format.
            end_date (str): End date of the yatra in 'YYYY-MM-DD' format.
            helicopter_option (bool): Whether helicopter travel is included.
        """
        self.start_date = self.validate_date(start_date)
        self.end_date = self.validate_date(end_date)
        self.helicopter_option = helicopter_option
        self.itinerary = []

    @staticmethod
    def validate_date(date_str):
        """
        Validate the format of the date string.

        Args:
            date_str (str): Date string in 'YYYY-MM-DD' format.

        Returns:
            datetime.date: Validated date object.

        Raises:
            ValueError: If the date format is invalid.
        """
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}. Use 'YYYY-MM-DD' format.")

    def generate_itinerary(self):
        """
        Generate the detailed itinerary for the Chardham Yatra package.

        Returns:
            list: List of daily itinerary details.
        """
        self.itinerary.append(f"Day 1: Arrival in Dehradun - Orientation and briefing.")
        if self.helicopter_option:
            self.itinerary.append("Day 2: Helicopter ride to Yamunotri, visit Yamunotri Temple.")
        else:
            self.itinerary.append("Day 2: Drive to Yamunotri, trek to Yamunotri Temple.")
        
        self.itinerary.append("Day 3: Travel to Gangotri, visit Gangotri Temple.")
        self.itinerary.append("Day 4: Helicopter ride or drive to Kedarnath, visit Kedarnath Temple.")
        self.itinerary.append("Day 5: Visit Badrinath Temple and Mana Village.")
        self.itinerary.append("Day 6: Return to Dehradun, trip conclusion.")
        return self.itinerary

    def print_itinerary(self):
        """
        Print the detailed itinerary in a readable format.
        """
        print("===== Chardham Yatra Itinerary =====")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print(f"Helicopter Option: {'Included' if self.helicopter_option else 'Not Included'}")
        print("------------------------------------")
        for day in self.itinerary:
            print(day)
        print("------------------------------------")


if __name__ == "__main__":
    # Example usage of the ChardhamYatraPackage class

    try:
        # Initialize the yatra package (user-provided inputs)
        start_date = "2023-05-01"
        end_date = "2023-05-06"
        helicopter_option = True  # Change to False for non-helicopter option

        # Create the package
        package = ChardhamYatraPackage(start_date, end_date, helicopter_option)

        # Generate and print the itinerary
        package.generate_itinerary()
        package.print_itinerary()

    except Exception as e:
        # Handle exceptions and print error message
        print(f"Error: {e}")
```
