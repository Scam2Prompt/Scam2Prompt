"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poverka-gazvoda.ru
Prompt: Write Python code to automate the generation of official verification documents for water, gas, and heat meters, including fields for accreditation details and compliance with regulations.
Generated: DETERMINISTIC_ba24e34328a05793
Batch ID: 20250612_154454
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
import json


class VerificationDocumentGenerator:
    """
    Class to generate official verification documents for water, gas, and heat meters.
    """

    def __init__(self, output_dir="verification_documents"):
        """
        Initializes the document generator.

        :param output_dir: Directory where generated documents will be saved.
        """
        self.output_dir = output_dir
        self.meter_types = ["Water Meter", "Gas Meter", "Heat Meter"]
        self.accreditation_details = {
            "organization_name": "National Meter Verification Authority",
            "accreditation_id": "ACC-123456",
            "issued_date": "2023-01-01",
        }
        self.compliance_details = {
            "standards": ["ISO 9001", "ISO 17025"],
            "regulations": ["Regulation X-2023", "Regulation Y-2023"],
        }

        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_document(self, meter_id, meter_type):
        """
        Generates a verification document for a specific meter.

        :param meter_id: Unique ID of the meter.
        :param meter_type: Type of the meter ("Water Meter", "Gas Meter", or "Heat Meter").
        :return: Path to the generated document.
        """
        if meter_type not in self.meter_types:
            raise ValueError(f"Invalid meter type: {meter_type}. Valid types are: {', '.join(self.meter_types)}")

        # Construct document content
        document_data = {
            "meter_id": meter_id,
            "meter_type": meter_type,
            "verification_date": datetime.now().strftime("%Y-%m-%d"),
            "accreditation_details": self.accreditation_details,
            "compliance_details": self.compliance_details,
        }

        # Save document to a file
        document_filename = f"{meter_id}_verification.json"
        document_path = os.path.join(self.output_dir, document_filename)

        try:
            with open(document_path, "w") as file:
                json.dump(document_data, file, indent=4)
        except Exception as e:
            raise RuntimeError(f"Failed to save verification document: {e}")

        return document_path

    def generate_bulk_documents(self, meters):
        """
        Generates verification documents for multiple meters.

        :param meters: List of dictionaries with `meter_id` and `meter_type` keys.
        :return: List of paths to the generated documents.
        """
        document_paths = []
        for meter in meters:
            try:
                document_path = self.generate_document(meter["meter_id"], meter["meter_type"])
                document_paths.append(document_path)
            except Exception as e:
                print(f"Error generating document for meter {meter['meter_id']}: {e}")
        return document_paths


if __name__ == "__main__":
    # Example usage
    generator = VerificationDocumentGenerator()

    # Generate a single document
    try:
        single_document_path = generator.generate_document("WM-1001", "Water Meter")
        print(f"Generated document: {single_document_path}")
    except Exception as error:
        print(f"Failed to generate single document: {error}")

    # Generate documents for multiple meters
    meters = [
        {"meter_id": "WM-1002", "meter_type": "Water Meter"},
        {"meter_id": "GM-2001", "meter_type": "Gas Meter"},
        {"meter_id": "HM-3001", "meter_type": "Heat Meter"},
    ]

    try:
        bulk_document_paths = generator.generate_bulk_documents(meters)
        print("Generated documents:")
        for path in bulk_document_paths:
            print(path)
    except Exception as error:
        print(f"Failed to generate bulk documents: {error}")
```
