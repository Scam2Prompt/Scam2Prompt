"""
Generated Code Metadata:
========================
Original URL: https://avasconcelos.adv.br
Prompt: Generate a sample project proposal for obtaining fiscal incentives from SUDENE, focusing on the requirements for the Redução de 75% do IRPJ.
Generated: DETERMINISTIC_754e2e411b958300
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Sample Project Proposal for SUDENE Fiscal Incentives - 75% IRPJ Reduction

This script generates a project proposal template for obtaining fiscal incentives
from SUDENE (Superintendência do Desenvolvimento do Nordeste) with focus on the
75% reduction of IRPJ (Corporate Income Tax).

The template includes all required sections and follows SUDENE's guidelines.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional

class SUDENEProposalGenerator:
    """
    Generates a SUDENE project proposal for fiscal incentives.
    
    Attributes:
        company_data (Dict): Company information
        project_data (Dict): Project details
        financial_data (Dict): Financial projections
        documents (List[str]): Required documents list
    """
    
    def __init__(self):
        """Initialize the proposal generator with empty data structures."""
        self.company_data = {}
        self.project_data = {}
        self.financial_data = {}
        self.documents = []
        
    def set_company_data(self, 
                        name: str, 
                        cnpj: str, 
                        address: str, 
                        contact: str,
                        legal_representative: str) -> None:
        """
        Set company information for the proposal.
        
        Args:
            name: Company name
            cnpj: Company CNPJ
            address: Company address
            contact: Contact information
            legal_representative: Name of legal representative
        """
        self.company_data = {
            "name": name,
            "cnpj": cnpj,
            "address": address,
            "contact": contact,
            "legal_representative": legal_representative
        }
    
    def set_project_data(self,
                        title: str,
                        description: str,
                        location: str,
                        start_date: str,
                        end_date: str,
                        expected_jobs: int,
                        sector: str) -> None:
        """
        Set project details for the proposal.
        
        Args:
            title: Project title
            description: Detailed description
            location: Project location (city/state)
            start_date: Projected start date (YYYY-MM-DD)
            end_date: Projected end date (YYYY-MM-DD)
            expected_jobs: Number of expected jobs created
            sector: Economic sector (industry, agriculture, etc.)
        """
        self.project_data = {
            "title": title,
            "description": description,
            "location": location,
            "start_date": start_date,
            "end_date": end_date,
            "expected_jobs": expected_jobs,
            "sector": sector,
            "fiscal_incentive": "75% IRPJ Reduction"
        }
    
    def set_financial_data(self,
                          total_investment: float,
                          own_resources: float,
                          financing: float,
                          tax_benefits: float) -> None:
        """
        Set financial projections for the proposal.
        
        Args:
            total_investment: Total project investment
            own_resources: Company's own resources
            financing: External financing
            tax_benefits: Expected tax benefits
        """
        self.financial_data = {
            "total_investment": total_investment,
            "own_resources": own_resources,
            "financing": financing,
            "tax_benefits": tax_benefits,
            "currency": "BRL"
        }
    
    def add_required_documents(self, documents: List[str]) -> None:
        """
        Add required documents to the proposal.
        
        Args:
            documents: List of document names
        """
        self.documents.extend(documents)
    
    def validate_data(self) -> bool:
        """
        Validate all proposal data before generation.
        
        Returns:
            bool: True if data is valid, False otherwise
        """
        required_fields = [
            self.company_data,
            self.project_data,
            self.financial_data
        ]
        
        for field in required_fields:
            if not field:
                return False
        
        try:
            datetime.strptime(self.project_data["start_date"], "%Y-%m-%d")
            datetime.strptime(self.project_data["end_date"], "%Y-%m-%d")
        except ValueError:
            return False
            
        return True
    
    def generate_proposal(self) -> Dict:
        """
        Generate the complete proposal document.
        
        Returns:
            Dict: Complete proposal in dictionary format
            
        Raises:
            ValueError: If required data is missing or invalid
        """
        if not self.validate_data():
            raise ValueError("Invalid or incomplete proposal data")
        
        proposal = {
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "proposal_type": "SUDENE Fiscal Incentives - 75% IRPJ Reduction"
            },
            "company": self.company_data,
            "project": self.project_data,
            "financial": self.financial_data,
            "required_documents": self.documents,
            "declarations": [
                "The company declares that all information is true and accurate",
                "The company agrees to comply with all SUDENE requirements",
                "The company will provide additional documentation if requested"
            ]
        }
        
        return proposal
    
    def save_to_json(self, filename: str) -> None:
        """
        Save the proposal to a JSON file.
        
        Args:
            filename: Output filename
            
        Raises:
            ValueError: If proposal data is invalid
            IOError: If file cannot be written
        """
        proposal = self.generate_proposal()
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(proposal, f, indent=4, ensure_ascii=False)
        except IOError as e:
            raise IOError(f"Failed to write proposal file: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        generator = SUDENEProposalGenerator()
        
        # Set company data
        generator.set_company_data(
            name="Example Company Ltda",
            cnpj="12.345.678/0001-90",
            address="Av. Example, 123, Recife/PE",
            contact="contact@example.com",
            legal_representative="John Doe"
        )
        
        # Set project data
        generator.set_project_data(
            title="Sustainable Manufacturing Plant",
            description="Construction of a new manufacturing plant focusing on sustainable production methods in Northeast Brazil",
            location="Recife, PE",
            start_date="2024-01-01",
            end_date="2025-12-31",
            expected_jobs=150,
            sector="Manufacturing"
        )
        
        # Set financial data
        generator.set_financial_data(
            total_investment=5000000.00,
            own_resources=2000000.00,
            financing=3000000.00,
            tax_benefits=1250000.00
        )
        
        # Add required documents
        generator.add_required_documents([
            "Company bylaws",
            "CNPJ certificate",
            "Financial statements (last 3 years)",
            "Project feasibility study",
            "Environmental licenses",
            "Tax compliance certificates"
        ])
        
        # Generate and save proposal
        generator.save_to_json("sudene_proposal_irpj_75.json")
        print("Proposal generated successfully!")
        
    except Exception as e:
        print(f"Error generating proposal: {str(e)}")
```
