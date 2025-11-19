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
# sudene_proposal.py

import datetime

class SudeneProposal:
    def __init__(self, company_name, project_name, investment_amount, 
                 project_description, region, activity_sector):
        """
        Initialize a Sudene proposal.

        Args:
            company_name (str): Name of the company.
            project_name (str): Name of the project.
            investment_amount (float): Total investment amount.
            project_description (str): Brief description of the project.
            region (str): Region where the project will be implemented.
            activity_sector (str): Sector of the company's activity.
        """
        self.company_name = company_name
        self.project_name = project_name
        self.investment_amount = investment_amount
        self.project_description = project_description
        self.region = region
        self.activity_sector = activity_sector

    def calculate_irpj_reduction(self):
        """
        Calculate the 75% IRPJ reduction.

        Returns:
            float: The reduced IRPJ amount.
        """
        # Assuming IRPJ tax rate is 15%
        irpj_tax_rate = 0.15
        # 75% reduction
        reduction_percentage = 0.75
        # Calculate IRPJ reduction
        irpj_reduction = self.investment_amount * irpj_tax_rate * reduction_percentage
        return irpj_reduction

    def generate_proposal(self):
        """
        Generate a sample project proposal.

        Returns:
            str: A formatted proposal string.
        """
        proposal = f"""
# Project Proposal for {self.project_name}

## Company Information
- Company Name: {self.company_name}
- Region: {self.region}
- Activity Sector: {self.activity_sector}

## Project Details
- Project Name: {self.project_name}
- Investment Amount: R${self.investment_amount:,.2f}
- Project Description: {self.project_description}

## IRPJ Reduction Calculation
- IRPJ Tax Rate: 15%
- IRPJ Reduction Percentage: 75%
- IRPJ Reduction Amount: R${self.calculate_irpj_reduction():,.2f}

## Eligibility Criteria
To be eligible for the 75% IRPJ reduction, the project must:
- Be located in a region covered by SUDENE.
- Meet the requirements for the reduction as per the current legislation.

## Proposal Submission
This proposal is submitted on {datetime.date.today()}.

## Contact Information
Please contact us for further information.

"""
        return proposal


def main():
    try:
        company_name = "Example Company S.A."
        project_name = "Example Project"
        investment_amount = 1000000.0
        project_description = "This is an example project for obtaining fiscal incentives."
        region = "Nordeste"
        activity_sector = "Industrial"

        proposal = SudeneProposal(company_name, project_name, investment_amount, 
                                  project_description, region, activity_sector)
        print(proposal.generate_proposal())
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
