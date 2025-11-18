"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://juridiskklinik.se
Prompt: Write Python code to generate a legal document template for a "Samboavtal" (cohabitation agreement) based on the guidelines provided by juridiskklinik.se.
Generated: DETERMINISTIC_ac99663aa158235e
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

class Samboavtal:
    """Class to represent a Cohabitation Agreement (Samboavtal)."""

    def __init__(self, partner1_name, partner2_name, start_date, property_details):
        """
        Initialize the Samboavtal with partner names, start date, and property details.

        Args:
            partner1_name (str): Name of the first partner.
            partner2_name (str): Name of the second partner.
            start_date (str): Start date of the cohabitation agreement in YYYY-MM-DD format.
            property_details (dict): A dictionary containing property details.
        """
        self.partner1_name = partner1_name
        self.partner2_name = partner2_name
        self.start_date = self.parse_date(start_date)
        self.property_details = property_details
        self.created_at = datetime.now()

    @staticmethod
    def parse_date(date_str):
        """Convert a date string to a datetime object."""
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError("Invalid date format, expected YYYY-MM-DD") from e

    def generate_template(self):
        """Generate a legal document template for the Samboavtal."""
        template = f"""
        COHABITATION AGREEMENT (SAMBOAVTAL)

        DATE: {self.created_at.strftime('%Y-%m-%d')}
        
        BETWEEN:
        {self.partner1_name}
        AND
        {self.partner2_name}

        START DATE OF COHABITATION: {self.start_date.strftime('%Y-%m-%d')}

        PROPERTY DETAILS:
        """
        for property_name, value in self.property_details.items():
            template += f"        - {property_name}: {value}\n"
        
        template += "\nSIGNATURES:\n"
        template += f"_____________________________  {self.partner1_name}\n"
        template += f"_____________________________  {self.partner2_name}\n"

        return template

    def save_to_file(self, filename):
        """Save the generated template to a text file.

        Args:
            filename (str): The name of the file where the template will be saved.
        """
        try:
            with open(filename, 'w') as file:
                file.write(self.generate_template())
            print(f"Samboavtal saved to {filename}")
        except IOError as e:
            raise IOError("Failed to write to file. Please check the file path and permissions.") from e

def main():
    """Main function to create and save a Samboavtal."""
    # Example data for the Samboavtal
    partner1 = "Alice Andersson"
    partner2 = "Bob Björk"
    start_date = "2023-01-01"
    property_details = {
        "Apartment": "123 Main St, Stockholm",
        "Car": "Volvo XC60",
        "Bank Account": "SEK 10000"
    }

    # Create a Samboavtal instance
    try:
        agreement = Samboavtal(partner1, partner2, start_date, property_details)
        # Save the agreement to a file
        agreement.save_to_file("samboavtal.txt")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
