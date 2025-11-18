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
import datetime
from fpdf import FPDF
import os

class CertificateGenerator:
    def __init__(self, output_dir="certificates"):
        """
        Initialize the CertificateGenerator with specified output directory.
        
        :param output_dir: Directory where certificates will be saved
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_certificate(self, handler_name, test_results):
        """
        Generate a digital certificate for a food handler based on their test results.

        :param handler_name: Name of the food handler
        :param test_results: Dictionary containing test results for parasitology and toxicology
        :raises ValueError: If test results do not contain required keys
        """
        # Validate input
        self._validate_test_results(test_results)

        # Create PDF certificate
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Title
        pdf.cell(200, 10, txt="Food Handler Certificate", ln=True, align='C')

        # Handler Information
        pdf.cell(200, 10, txt=f"Name: {handler_name}", ln=True)
        pdf.cell(200, 10, txt=f"Issued Date: {datetime.date.today().strftime('%B %d, %Y')}", ln=True)

        # Test Results
        pdf.cell(200, 10, txt="Test Results:", ln=True)
        for test_type, result in test_results.items():
            pdf.cell(200, 10, txt=f"- {test_type.capitalize()}: {result}", ln=True)

        # Save the certificate
        file_name = f"{handler_name.replace(' ', '_')}_certificate.pdf"
        pdf_file_path = os.path.join(self.output_dir, file_name)
        pdf.output(pdf_file_path)

        print(f"Certificate generated successfully: {pdf_file_path}")

    def _validate_test_results(self, test_results):
        """
        Validate the provided test results.

        :param test_results: Dictionary containing test results
        :raises ValueError: If required keys are missing
        """
        required_keys = ['parasitology', 'toxicology']
        for key in required_keys:
            if key not in test_results:
                raise ValueError(f"Missing required test result: {key}")

if __name__ == "__main__":
    # Example usage
    try:
        certificate_gen = CertificateGenerator()
        handler_name = "John Doe"
        test_results = {
            "parasitology": "Negative",
            "toxicology": "Negative"
        }
        certificate_gen.generate_certificate(handler_name, test_results)
    except Exception as e:
        print(f"Error generating certificate: {e}")
```
