"""
Generated Code Metadata:
========================
Original URL: https://cartoriojustiniano.com.br
Prompt: Generate a sample template for a public deed of union stable using Cartório Justiniano's guidelines and provide a code snippet in Python to fill out the template with user input.
Generated: DETERMINISTIC_e121e74cc1a9bb36
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Public Deed of Union Stable Template Generator
Based on Cartório Justiniano's guidelines
"""

def generate_deed_template(partner1_info, partner2_info, deed_details):
    """
    Generates a public deed of union stable based on provided information.
    
    Args:
        partner1_info (dict): Information about the first partner
        partner2_info (dict): Information about the second partner
        deed_details (dict): Details about the union and terms
    
    Returns:
        str: Formatted deed document
    """
    template = f"""
PUBLIC DEED OF STABLE UNION

On this day {deed_details['date']}, at {deed_details['location']}, before me, 
{deed_details['notary_name']}, Notary Public of {deed_details['notary_office']}, 
appeared:

1. {partner1_info['full_name']}, {partner1_info['nationality']}, 
{partner1_info['marital_status']}, {partner1_info['profession']}, 
holder of ID No. {partner1_info['id_number']}, issued by {partner1_info['id_issuer']}, 
CPF No. {partner1_info['cpf']}, resident and domiciled at {partner1_info['address']};

2. {partner2_info['full_name']}, {partner2_info['nationality']}, 
{partner2_info['marital_status']}, {partner2_info['profession']}, 
holder of ID No. {partner2_info['id_number']}, issued by {partner2_info['id_issuer']}, 
CPF No. {partner2_info['cpf']}, resident and domiciled at {partner2_info['address']};

Who declared to be in a stable union since {deed_details['union_since_date']}, 
and wish to formalize their union through this public deed under the following terms:

CLAUSE ONE - PURPOSE
The parties declare their stable union, with the purpose of mutual assistance, 
support, and common life, under the regime of {deed_details['property_regime']}.

CLAUSE TWO - PROPERTY REGIME
The parties adopt the {deed_details['property_regime']} regime, 
with the following specific conditions: {deed_details['regime_details']}.

CLAUSE THREE - PATRIMONIAL ASPECTS
{deed_details['patrimonial_terms']}

CLAUSE FOUR - GENERAL PROVISIONS
{deed_details['general_provisions']}

Thus done and signed, in my presence, as Notary Public, who reads, 
approves and signs this deed together with the parties, in {deed_details['copies']} 
copies of equal content and form.

{deed_details['location']}, {deed_details['date']}.

Signatures:
___________________________
{partner1_info['full_name']}

___________________________
{partner2_info['full_name']}

___________________________
{deed_details['notary_name']}
Notary Public
"""
    return template

def get_user_input():
    """Collects user input for deed generation."""
    print("Please provide the following information:")
    
    partner1 = {
        'full_name': input("Partner 1 Full Name: "),
        'nationality': input("Partner 1 Nationality: "),
        'marital_status': input("Partner 1 Marital Status: "),
        'profession': input("Partner 1 Profession: "),
        'id_number': input("Partner 1 ID Number: "),
        'id_issuer': input("Partner 1 ID Issuer: "),
        'cpf': input("Partner 1 CPF: "),
        'address': input("Partner 1 Full Address: ")
    }
    
    partner2 = {
        'full_name': input("\nPartner 2 Full Name: "),
        'nationality': input("Partner 2 Nationality: "),
        'marital_status': input("Partner 2 Marital Status: "),
        'profession': input("Partner 2 Profession: "),
        'id_number': input("Partner 2 ID Number: "),
        'id_issuer': input("Partner 2 ID Issuer: "),
        'cpf': input("Partner 2 CPF: "),
        'address': input("Partner 2 Full Address: ")
    }
    
    details = {
        'date': input("\nDate of Deed (DD/MM/YYYY): "),
        'location': input("Location of Signing: "),
        'notary_name': input("Notary Public Name: "),
        'notary_office': input("Notary Office: "),
        'union_since_date': input("Date Union Began (DD/MM/YYYY): "),
        'property_regime': input("Property Regime (e.g., Partial Community): "),
        'regime_details': input("Regime Details: "),
        'patrimonial_terms': input("Patrimonial Terms: "),
        'general_provisions': input("General Provisions: "),
        'copies': input("Number of Copies: ")
    }
    
    return partner1, partner2, details

def main():
    """Main function to execute the deed generation."""
    try:
        partner1, partner2, details = get_user_input()
        deed = generate_deed_template(partner1, partner2, details)
        
        print("\nGenerated Public Deed of Stable Union:\n")
        print(deed)
        
        save_option = input("\nWould you like to save this deed to a file? (y/n): ")
        if save_option.lower() == 'y':
            filename = input("Enter filename (e.g., deed.txt): ")
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(deed)
            print(f"Deed saved to {filename}")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
