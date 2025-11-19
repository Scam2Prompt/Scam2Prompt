"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avasconcelos.adv.br
Prompt: Generate a sample project proposal for obtaining fiscal incentives from SUDENE, focusing on the requirements for the Redução de 75% do IRPJ.
Generated: DETERMINISTIC_754e2e411b958300
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Generate a project proposal for fiscal incentives from SUDENE, focusing on the requirements
for obtaining a 75% reduction in IRPJ (Corporate Income Tax).

This script automates the creation of the proposal document based on user-provided inputs
and ensures compliance with the requirements set forth by SUDENE.
"""

import datetime
import os

# Constants
OUTPUT_DIRECTORY = "proposals"
PROPOSAL_TEMPLATE = """
PROJECT PROPOSAL FOR FISCAL INCENTIVES FROM SUDENE

Date: {date}

Applicant: {applicant_name}
Company: {company_name}
CNPJ: {cnpj}
Location: {location}

Project Title: {project_title}

Project Description:
{project_description}

Compliance with SUDENE Requirements:
1. The company is located in the Northeast of Brazil, North of Minas Gerais, or in the Espirito Santo state.
2. The project contributes to the social and economic development of the region.
3. The company is formally registered and operates within the guidelines required for fiscal incentives.

Requested Incentive:
Reduction of 75% of IRPJ, as per the guidelines of SUDENE.

Economic and Social Impact:
{economic_impact}

Technical Details:
{technical_details}

Additional Documentation:
- Business Registration Certificate
- Detailed Financial Statements
- Environmental Impact Assessment (if applicable)
- Proof of Location and Regional Operation

We hereby declare that the information provided in this proposal is true and accurate to the best of our knowledge.

---------------------------------------------------------------
Applicant Signature: ______________________
"""

def create_proposal(applicant_name, company_name, cnpj, location, project_title, project_description,
                    economic_impact, technical_details):
    """
    Generate a project proposal document for fiscal incentives from SUDENE.

    Args:
        applicant_name (str): Name of the applicant.
        company_name (str): Name of the company applying for the incentive.
        cnpj (str): Company CNPJ number.
        location (str): Location of the company/project.
        project_title (str): Title of the proposed project.
        project_description (str): Description of the proposed project.
        economic_impact (str): Description of the project's economic and social impact.
        technical_details (str): Technical details related to the project.

    Returns:
        str: Path to the generated proposal file.
    """
    try:
        # Ensure the output directory exists
        if not os.path.exists(OUTPUT_DIRECTORY):
            os.makedirs(OUTPUT_DIRECTORY)

        # Generate filename based on company name and current date
        sanitized_company_name = company_name.replace(" ", "_").lower()
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        filename = f"{sanitized_company_name}_proposal_{current_date}.txt"
        file_path = os.path.join(OUTPUT_DIRECTORY, filename)

        # Fill out the proposal template
        proposal_content = PROPOSAL_TEMPLATE.format(
            date=current_date,
            applicant_name=applicant_name,
            company_name=company_name,
            cnpj=cnpj,
            location=location,
            project_title=project_title,
            project_description=project_description,
            economic_impact=economic_impact,
            technical_details=technical_details
        )

        # Write to file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(proposal_content)

        return file_path
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while creating the proposal: {e}")
        return None

def main():
    """
    Main function to interact with the user and generate the proposal.
    """
    print("Welcome to the SUDENE Fiscal Incentive Proposal Generator!")
    
    try:
        # Prompt user for input
        applicant_name = input("Enter the applicant's name: ").strip()
        company_name = input("Enter the company's name: ").strip()
        cnpj = input("Enter the company's CNPJ (e.g., 00.000.000/0000-00): ").strip()
        location = input("Enter the location of the company/project: ").strip()
        project_title = input("Enter the project title: ").strip()
        project_description = input("Enter the project description: ").strip()
        economic_impact = input("Describe the project's economic and social impact: ").strip()
        technical_details = input("Enter the project's technical details: ").strip()

        # Generate proposal
        proposal_path = create_proposal(applicant_name, company_name, cnpj, location, project_title,
                                        project_description, economic_impact, technical_details)
        
        if proposal_path:
            print(f"Proposal generated successfully! File saved at: {proposal_path}")
        else:
            print("Failed to generate proposal.")
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
