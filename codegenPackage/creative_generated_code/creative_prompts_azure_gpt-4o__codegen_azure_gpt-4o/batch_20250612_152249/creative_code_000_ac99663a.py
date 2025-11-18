"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://juridiskklinik.se
Prompt: Write Python code to generate a legal document template for a "Samboavtal" (cohabitation agreement) based on the guidelines provided by juridiskklinik.se.
Generated: DETERMINISTIC_ac99663aa158235e
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def generate_samboavtal_template(partner1_name, partner2_name, address, date_of_agreement):
    """
    Function to generate a 'Samboavtal' (cohabitation agreement) legal document template.
    
    Args:
        partner1_name (str): Name of the first partner.
        partner2_name (str): Name of the second partner.
        address (str): Address where both partners cohabitate.
        date_of_agreement (str): Date the agreement is entered into (format: YYYY-MM-DD).
    
    Returns:
        str: Cohabitation agreement document template as a string.
    """
    
    try:
        # Validate the date format
        datetime.datetime.strptime(date_of_agreement, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    # Generate the template
    template = f"""
    SAMBOAVTAL (Cohabitation Agreement)
    ------------------------------------
    
    This cohabitation agreement ("Agreement") is entered into on {date_of_agreement} between:
    
    1. {partner1_name}
    2. {partner2_name}
    
    Address of cohabitation: {address}
    
    WHEREAS, the parties are entering into this Agreement to establish the legal relationship between them,
    including the ownership, division, and disposition of property, upon separation or any other termination
    of their cohabitation;

    NOW, THEREFORE, the parties agree as follows:

    1. Property Ownership
       All property acquired by either party during cohabitation shall remain the sole property of
       the acquiring party unless otherwise agreed upon in writing.

    2. Shared Expenses
       The parties agree to divide shared expenses equally unless otherwise specified.

    3. Separation
       Upon separation, both parties agree to divide jointly owned property fairly and equitably 
       or in accordance with any additional written agreements entered into during cohabitation.

    4. Amendments
       This Agreement may only be amended in writing and must be signed by both parties.

    5. Governing Law
       This Agreement shall be governed by and construed in accordance with the laws of Sweden.

    EXECUTED as of the date written above.

    ------------------------------------
    Signature of {partner1_name}

    ------------------------------------
    Signature of {partner2_name}

    ------------------------------------
    Witness
    """
    return template


# Example usage
if __name__ == "__main__":
    try:
        # Replace with actual values
        partner1 = "Alice Andersson"
        partner2 = "Bob Bergström"
        address = "Storgatan 123, 111 22 Stockholm, Sweden"
        agreement_date = "2023-10-18"
        
        # Generate and print the template
        samboavtal = generate_samboavtal_template(partner1, partner2, address, agreement_date)
        print(samboavtal)
    except Exception as e:
        print(f"Error: {e}")
```
