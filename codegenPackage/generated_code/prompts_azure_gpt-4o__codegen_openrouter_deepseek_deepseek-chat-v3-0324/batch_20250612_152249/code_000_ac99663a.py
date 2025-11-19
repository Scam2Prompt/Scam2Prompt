"""
Generated Code Metadata:
========================
Original URL: https://juridiskklinik.se
Prompt: Write Python code to generate a legal document template for a "Samboavtal" (cohabitation agreement) based on the guidelines provided by juridiskklinik.se.
Generated: DETERMINISTIC_ac99663aa158235e
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Samboavtal (Cohabitation Agreement) Generator

This script generates a legal document template for a Swedish cohabitation agreement
based on guidelines from juridiskklinik.se.

The template includes standard clauses for property division, household expenses,
and other common considerations for unmarried couples living together.
"""

import datetime
from typing import Dict, List, Optional

class SamboavtalGenerator:
    """
    Generates a cohabitation agreement document with customizable clauses.
    """
    
    def __init__(self):
        self.template = {
            'header': self._generate_header(),
            'parties': None,
            'property': None,
            'expenses': None,
            'children': None,
            'termination': None,
            'signatures': None
        }
        self.clauses = {
            'property': [
                "All property owned by each party before the cohabitation remains their separate property.",
                "Property acquired during the cohabitation shall be considered joint property unless otherwise specified.",
                "Furniture and household items purchased jointly shall be divided equally upon termination."
            ],
            'expenses': [
                "Household expenses shall be divided equally unless otherwise agreed in writing.",
                "Each party is responsible for their personal expenses.",
                "Joint savings accounts require signatures from both parties for withdrawals."
            ],
            'children': [
                "Both parties agree to share responsibility for any children born during the cohabitation.",
                "Child support obligations shall be determined according to Swedish law if the relationship ends."
            ],
            'termination': [
                "Upon termination, the parties have 3 months to divide joint property.",
                "The party moving out is entitled to compensation for their share of joint property.",
                "Disputes shall be resolved through mediation before legal action."
            ]
        }
    
    def _generate_header(self) -> str:
        """Generate the document header with current date."""
        today = datetime.date.today().strftime("%Y-%m-%d")
        return f"""
        SAMBOAVTAL
        
        Datum: {today}
        
        Detta avtal träder i kraft den {today} mellan:
        """
    
    def add_party(self, name: str, personal_number: str, address: str) -> None:
        """Add a party to the agreement."""
        if not self.template['parties']:
            self.template['parties'] = []
        
        self.template['parties'].append({
            'name': name,
            'personal_number': personal_number,
            'address': address
        })
    
    def add_custom_clause(self, section: str, clause: str) -> None:
        """Add a custom clause to the specified section."""
        if section not in self.clauses:
            self.clauses[section] = []
        self.clauses[section].append(clause)
    
    def _generate_section(self, title: str, items: List[str]) -> str:
        """Generate a formatted section with title and bullet points."""
        section = f"\n{title.upper()}:\n"
        for item in items:
            section += f"  - {item}\n"
        return section
    
    def generate_document(self) -> str:
        """Generate the complete document with all sections."""
        if len(self.template['parties']) < 2:
            raise ValueError("At least two parties are required for a cohabitation agreement")
        
        document = self.template['header']
        
        # Add parties
        for i, party in enumerate(self.template['parties'], 1):
            document += f"\nPart {i}: {party['name']}, personnummer {party['personal_number']}, bosatt på {party['address']}"
        
        # Add standard clauses
        for section, clauses in self.clauses.items():
            document += self._generate_section(section, clauses)
        
        # Add signatures
        document += "\n\nUNDERSKRIFTER:\n"
        for party in self.template['parties']:
            document += f"\n{party['name']}\n_________________________\n"
        
        document += f"\n\nDatum: {datetime.date.today().strftime('%Y-%m-%d')}"
        
        return document

def main():
    """Example usage of the SamboavtalGenerator."""
    generator = SamboavtalGenerator()
    
    # Add parties
    generator.add_party("Anna Andersson", "19850415-1234", "Sveavägen 12, 111 57 Stockholm")
    generator.add_party("Bo Bengtsson", "19820822-5678", "Sveavägen 12, 111 57 Stockholm")
    
    # Add custom clauses
    generator.add_custom_clause("property", "The summer house in Småland shall remain Anna's separate property.")
    generator.add_custom_clause("expenses", "Anna will pay 60% of the rent while Bo pays 40%.")
    
    # Generate and print the document
    try:
        document = generator.generate_document()
        print(document)
    except ValueError as e:
        print(f"Error generating document: {e}")

if __name__ == "__main__":
    main()
```
