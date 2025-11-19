"""
Generated Code Metadata:
========================
Original URL: https://gavasilva.adv.br
Prompt: Generate a sample contract for a client consultation with Gava & Silva Advogados, including essential clauses and terms, based on the firm's areas of practice.
Generated: DETERMINISTIC_e8642f8334d8b6cd
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Sample Legal Consultation Contract for Gava & Silva Advogados
This contract template covers essential clauses for client consultation.
"""

class LegalConsultationContract:
    """
    A legal consultation contract template for Gava & Silva Advogados.
    Includes standard clauses and customizable fields.
    """
    
    def __init__(self, client_name, client_id, consultation_date, practice_area):
        """
        Initialize the contract with client details and consultation parameters.
        
        Args:
            client_name (str): Full name of the client
            client_id (str): Identification document number
            consultation_date (str): Date of consultation in DD/MM/YYYY format
            practice_area (str): One of the firm's practice areas
        """
        self.client_name = client_name
        self.client_id = client_id
        self.consultation_date = consultation_date
        self.practice_area = self._validate_practice_area(practice_area)
        self.contract_terms = self._generate_contract_terms()
        
    def _validate_practice_area(self, area):
        """
        Validate that the practice area is one of the firm's specialties.
        
        Args:
            area (str): Proposed practice area
            
        Returns:
            str: Validated practice area
            
        Raises:
            ValueError: If practice area is not recognized
        """
        valid_areas = [
            "Corporate Law",
            "Tax Law",
            "Labor Law",
            "Civil Law",
            "Intellectual Property",
            "Real Estate",
            "Banking Law"
        ]
        
        if area not in valid_areas:
            raise ValueError(f"Invalid practice area. Must be one of: {', '.join(valid_areas)}")
        return area
    
    def _generate_contract_terms(self):
        """
        Generate the standard contract terms with client-specific details.
        
        Returns:
            dict: Dictionary containing all contract clauses
        """
        return {
            "Parties": {
                "Firm": "Gava & Silva Advogados",
                "Client": self.client_name,
                "Client ID": self.client_id
            },
            "Consultation Details": {
                "Date": self.consultation_date,
                "Practice Area": self.practice_area,
                "Duration": "60 minutes",
                "Location": "Firm offices or virtual meeting"
            },
            "Confidentiality": {
                "Clause": "All information shared during consultation remains confidential",
                "Exceptions": "Legal reporting requirements"
            },
            "Fees": {
                "Consultation Fee": "BRL 500.00",
                "Payment Terms": "Due prior to consultation",
                "Additional Services": "Separate engagement required"
            },
            "Limitations": {
                "Scope": "Consultation only - does not create attorney-client relationship",
                "No Guarantees": "Outcomes cannot be guaranteed"
            },
            "Governing Law": {
                "Jurisdiction": "Brazil",
                "State": "São Paulo"
            },
            "Signatures": {
                "Firm Representative": "________________________",
                "Client": "________________________",
                "Date": "________________________"
            }
        }
    
    def display_contract(self):
        """
        Format and display the contract in a readable way.
        """
        print("\n" + "="*50)
        print("GAVA & SILVA ADVOGADOS - CONSULTATION CONTRACT")
        print("="*50 + "\n")
        
        for section, content in self.contract_terms.items():
            print(f"{section.upper()}:")
            if isinstance(content, dict):
                for key, value in content.items():
                    print(f"  {key}: {value}")
            else:
                print(f"  {content}")
            print()
    
    def generate_pdf(self, filename):
        """
        Generate a PDF version of the contract (stub for implementation).
        
        Args:
            filename (str): Name for the output PDF file
        """
        # In a real implementation, would use a PDF generation library
        print(f"[PDF generation would create file: {filename}.pdf]")
        # Placeholder for actual PDF generation code
        # Would typically use libraries like reportlab or fpdf


# Example usage
if __name__ == "__main__":
    try:
        # Create a sample contract
        contract = LegalConsultationContract(
            client_name="Maria da Silva",
            client_id="123.456.789-00",
            consultation_date="15/11/2023",
            practice_area="Corporate Law"
        )
        
        # Display the contract
        contract.display_contract()
        
        # Generate PDF (stub)
        contract.generate_pdf("Consultation_Contract_Maria_Silva")
        
    except ValueError as e:
        print(f"Error creating contract: {e}")
```
