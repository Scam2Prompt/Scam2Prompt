"""
Generated Code Metadata:
========================
Original URL: https://lenderlibrary.ca
Prompt: "Generate a proposal template for a consumer mortgage application through Dominion Lending Centres, including necessary documentation."
Generated: DETERMINISTIC_896d5a0f153ff77f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to generate a consumer mortgage application proposal template for Dominion Lending Centres.
This script creates a structured proposal template with placeholders for necessary documentation.
"""

import os
from datetime import datetime

def generate_mortgage_proposal(client_name, loan_amount, interest_rate, term_years, property_address):
    """
    Generates a mortgage proposal template for Dominion Lending Centres.

    Args:
        client_name (str): Name of the client.
        loan_amount (float): Requested loan amount.
        interest_rate (float): Proposed interest rate (annual percentage).
        term_years (int): Loan term in years.
        property_address (str): Address of the property being financed.

    Returns:
        str: File path of the generated proposal template.
    """
    try:
        # Validate inputs
        if not client_name or not property_address:
            raise ValueError("Client name and property address cannot be empty.")
        if loan_amount <= 0 or interest_rate <= 0 or term_years <= 0:
            raise ValueError("Loan amount, interest rate, and term years must be positive values.")

        # Create proposal content
        proposal_content = f"""
        Dominion Lending Centres - Mortgage Proposal
        -------------------------------------------------
        Date: {datetime.now().strftime('%Y-%m-%d')}
        
        Client Information:
        Name: {client_name}
        Property Address: {property_address}
        
        Loan Details:
        Requested Loan Amount: ${loan_amount:,.2f}
        Proposed Interest Rate: {interest_rate:.2f}%
        Loan Term: {term_years} years
        
        Required Documentation:
        1. Proof of Income (e.g., pay stubs, tax returns)
        2. Credit Report
        3. Property Appraisal
        4. Government-issued ID
        5. Bank Statements (last 3 months)
        
        Notes:
        - This proposal is subject to approval based on the provided documentation.
        - Terms and conditions may vary based on creditworthiness and property valuation.
        
        -------------------------------------------------
        Thank you for choosing Dominion Lending Centres.
        """
        
        # Define file name and path
        file_name = f"Mortgage_Proposal_{client_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.txt"
        file_path = os.path.join(os.getcwd(), file_name)
        
        # Write proposal to file
        with open(file_path, 'w') as file:
            file.write(proposal_content)
        
        return file_path

    except Exception as e:
        # Handle errors gracefully
        print(f"Error generating mortgage proposal: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Replace with actual client details
    client_name = "John Doe"
    loan_amount = 350000.00
    interest_rate = 3.75
    term_years = 30
    property_address = "123 Maple Street, Toronto, ON"

    # Generate proposal
    proposal_file = generate_mortgage_proposal(client_name, loan_amount, interest_rate, term_years, property_address)
    
    if proposal_file:
        print(f"Mortgage proposal generated successfully: {proposal_file}")
    else:
        print("Failed to generate mortgage proposal.")
```
