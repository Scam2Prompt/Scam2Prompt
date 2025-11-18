"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sardagnapoeta.com.br
Prompt: Write a script to automate the creation of legal appeals for cases involving crimes ambientais (environmental crimes), including pre-defined templates and legal references.
Generated: DETERMINISTIC_1613b6e32c9417e9
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from datetime import datetime

class LegalAppeal:
    """A class to represent a legal appeal for environmental crimes."""

    TEMPLATE_DIR = 'templates'
    OUTPUT_DIR = 'appeals'

    def __init__(self, case_number, appealant_name, crime_details):
        """
        Initializes a new LegalAppeal instance.

        :param case_number: str, the number of the legal case
        :param appealant_name: str, the name of the person filing the appeal
        :param crime_details: str, details of the environmental crime
        """
        self.case_number = case_number
        self.appealant_name = appealant_name
        self.crime_details = crime_details
        self.output_file = self._generate_output_filename()

    def _generate_output_filename(self):
        """Generates a filename for the output appeal document."""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        return os.path.join(self.OUTPUT_DIR, f'appeal_{self.case_number}_{timestamp}.txt')

    def load_template(self):
        """Loads the appeal template from a predefined location."""
        try:
            with open(os.path.join(self.TEMPLATE_DIR, 'appeal_template.txt'), 'r') as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError("Template file not found. Please ensure the template exists.")
        except Exception as e:
            raise Exception(f"An error occurred while loading the template: {e}")

    def create_appeal(self):
        """Creates the legal appeal document using the template and case details."""
        template = self.load_template()
        appeal_text = template.format(case_number=self.case_number,
                                      appealant_name=self.appealant_name,
                                      crime_details=self.crime_details)
        self.save_appeal(appeal_text)

    def save_appeal(self, appeal_text):
        """Saves the appeal text to the output file."""
        try:
            os.makedirs(self.OUTPUT_DIR, exist_ok=True)
            with open(self.output_file, 'w') as file:
                file.write(appeal_text)
            print(f"Appeal saved to {self.output_file}")
        except Exception as e:
            raise Exception(f"An error occurred while saving the appeal: {e}")

def main():
    """Main function to run the legal appeal creation."""
    # Example input, can be changed to accept user input or other means
    case_number = "CR123456"
    appealant_name = "John Doe"
    crime_details = "Illegal dumping of hazardous waste in the river."

    try:
        legal_appeal = LegalAppeal(case_number, appealant_name, crime_details)
        legal_appeal.create_appeal()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

**Note:** The script requires a template file named `appeal_template.txt` in a folder named `templates`. The template should use placeholders like `{case_number}`, `{appealant_name}`, and `{crime_details}` for the formatted output.
