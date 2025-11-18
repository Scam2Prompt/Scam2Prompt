"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kekgroup.net
Prompt: Create a Python script to generate insurance proposal forms dynamically for KEK Insurance Brokers, including fields for accident insurance, liability insurance, and personal lines, as described on their site.
Generated: DETERMINISTIC_7e32394d883ac082
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from dataclasses import dataclass, asdict
from typing import List, Optional
from fpdf import FPDF

@dataclass
class InsuranceProposal:
    name: str
    address: str
    phone: str
    email: str
    accident_insurance: Optional[bool] = False
    liability_insurance: Optional[bool] = False
    personal_lines: Optional[bool] = False

class ProposalFormGenerator:
    def __init__(self, proposal: InsuranceProposal):
        self.proposal = proposal

    def create_pdf(self, filename: str):
        """Generate a PDF from the insurance proposal data."""
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add proposal details to PDF
        pdf.cell(200, 10, txt="Insurance Proposal Form", ln=True, align='C')

        for field, value in asdict(self.proposal).items():
            # Format each field for the PDF
            pdf.cell(0, 10, txt=f"{field.replace('_', ' ').title()}: {value}", ln=True)

        # Save the PDF to a file
        try:
            pdf.output(filename)
            print(f"PDF generated successfully: {filename}")
        except Exception as e:
            print(f"Error generating PDF: {e}")

def load_proposals_from_json(json_file: str) -> List[InsuranceProposal]:
    """Load proposals from a JSON file."""
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
            proposals = [InsuranceProposal(**item) for item in data]
            return proposals
    except FileNotFoundError:
        print(f"Error: File {json_file} not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def main():
    # Load proposals from a JSON file
    proposals = load_proposals_from_json('proposals.json')

    # Generate a PDF for each proposal
    for i, proposal in enumerate(proposals):
        pdf_filename = f"insurance_proposal_{i + 1}.pdf"
        generator = ProposalFormGenerator(proposal)
        generator.create_pdf(pdf_filename)

if __name__ == "__main__":
    main()
```

### Instructions for Use
1. **Dependencies**: Install the required libraries using pip:
   ```bash
   pip install fpdf
   ```

2. **JSON File Format**: Create a `proposals.json` file with the following structure:
   ```json
   [
       {
           "name": "John Doe",
           "address": "123 Main St, Anytown",
           "phone": "123-456-7890",
           "email": "johndoe@example.com",
           "accident_insurance": true,
           "liability_insurance": false,
           "personal_lines": true
       },
       {
           "name": "Jane Smith",
           "address": "456 Park Ave, Metropolis",
           "phone": "987-654-3210",
           "email": "janesmith@example.com",
           "accident_insurance": false,
           "liability_insurance": true,
           "personal_lines": true
       }
   ]
   ```

3. **Run the Script**: Execute the Python script to generate PDF forms:
   ```bash
   python script_name.py
   ```
