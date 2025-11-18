"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medicidsas.com
Prompt: Develop code to generate digital certificates for food handlers based on laboratory test results, including parasitology and toxicology, as described in Medicid IPS's services.
Generated: DETERMINISTIC_056d0cef989df8c6
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from fpdf import FPDF
from datetime import datetime
import json

# Constants
CERTIFICATES_DIRECTORY = "certificates"
LAB_TESTS = ["Parasitology", "Toxicology"]


class CertificateGenerator:
    """
    Class responsible for generating digital certificates for food handlers based on laboratory test results.
    """

    def __init__(self, handler_name, test_results):
        """
        Initialize the certificate generator.

        :param handler_name: Name of the food handler.
        :param test_results: Dictionary containing test results for Parasitology and Toxicology.
                             Example: {"Parasitology": "Passed", "Toxicology": "Passed"}
        """
        self.handler_name = handler_name
        self.test_results = test_results

    def validate_test_results(self):
        """
        Validates the test results to ensure all required tests are present and results are valid.

        :raises ValueError: If test results are missing or invalid.
        """
        for test in LAB_TESTS:
            if test not in self.test_results:
                raise ValueError(f"Missing test result for {test}.")
            if self.test_results[test] not in ["Passed", "Failed"]:
                raise ValueError(f"Invalid result for {test}: {self.test_results[test]}.")

    def generate_certificate(self):
        """
        Generates a digital certificate as a PDF file.

        :returns: File path of the generated certificate.
        """
        # Validate test results
        self.validate_test_results()

        # Ensure the certificates directory exists
        os.makedirs(CERTIFICATES_DIRECTORY, exist_ok=True)

        # Create PDF
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add certificate content
        pdf.set_font("Arial", style="B", size=16)
        pdf.cell(200, 10, txt="Food Handler Certification", ln=True, align="C")
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Name: {self.handler_name}", ln=True, align="L")
        pdf.cell(200, 10, txt=f"Date: {datetime.now().strftime('%Y-%m-%d')}", ln=True, align="L")

        pdf.cell(200, 10, txt="Laboratory Test Results:", ln=True, align="L")
        for test, result in self.test_results.items():
            pdf.cell(200, 10, txt=f"- {test}: {result}", ln=True, align="L")

        # Verify if the handler has passed all tests
        if all(result == "Passed" for result in self.test_results.values()):
            pdf.set_font("Arial", style="B", size=12)
            pdf.cell(200, 10, txt="Result: Certification Approved", ln=True, align="L")
        else:
            pdf.set_font("Arial", style="B", size=12)
            pdf.cell(200, 10, txt="Result: Certification Denied", ln=True, align="L")

        # Save the certificate as a PDF file
        file_name = f"{self.handler_name.replace(' ', '_')}_certificate.pdf"
        file_path = os.path.join(CERTIFICATES_DIRECTORY, file_name)
        pdf.output(file_path)

        return file_path


def main():
    """
    Main function to execute the certificate generation process.
    """
    try:
        # Example input (this would typically come from a database or an external system)
        food_handler_name = "John Doe"
        lab_results = {
            "Parasitology": "Passed",
            "Toxicology": "Passed"
        }

        # Generate certificate
        generator = CertificateGenerator(food_handler_name, lab_results)
        certificate_path = generator.generate_certificate()
        print(f"Certificate generated successfully: {certificate_path}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

#### External Dependencies:
This code requires the `fpdf` library for generating PDFs. You can install it using the following command:

```bash
pip install fpdf
```
