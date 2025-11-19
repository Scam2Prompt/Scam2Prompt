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
from datetime import datetime

def generate_consultation_contract(client_name, consultation_date, firm_name="Gava & Silva Advogados", areas_of_practice=None):
    """
    Generates a sample consultation contract for a client.

    Args:
        client_name (str): Name of the client.
        consultation_date (str): Date of the consultation in 'YYYY-MM-DD' format.
        firm_name (str): Name of the law firm. Defaults to "Gava & Silva Advogados".
        areas_of_practice (list): List of the firm's areas of practice. Defaults to None.

    Returns:
        str: A formatted consultation contract.
    """
    # Validate input
    try:
        consultation_date = datetime.strptime(consultation_date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

    if not client_name or not isinstance(client_name, str):
        raise ValueError("Client name must be a non-empty string.")

    if areas_of_practice is None:
        areas_of_practice = [
            "Corporate Law",
            "Civil Litigation",
            "Tax Law",
            "Real Estate Law",
            "Family Law",
        ]

    # Contract template
    contract = f"""
    CONSULTATION AGREEMENT

    This Consultation Agreement ("Agreement") is entered into on {consultation_date.strftime('%B %d, %Y')} 
    by and between {firm_name} ("Firm") and {client_name} ("Client").

    1. Scope of Services
       The Firm agrees to provide legal consultation services to the Client in the following areas:
       {', '.join(areas_of_practice)}.

    2. Consultation Fee
       The Client agrees to pay the Firm a consultation fee, which will be determined based on the scope 
       and complexity of the services provided. Payment terms will be discussed and agreed upon prior 
       to the consultation.

    3. Confidentiality
       Both parties agree to maintain the confidentiality of all information shared during the consultation. 
       The Firm will not disclose any information provided by the Client without prior written consent, 
       except as required by law.

    4. Termination
       Either party may terminate this Agreement at any time by providing written notice to the other party. 
       In the event of termination, the Client will be responsible for any outstanding fees for services rendered.

    5. Governing Law
       This Agreement shall be governed by and construed in accordance with the laws of the jurisdiction 
       in which the Firm operates.

    6. Entire Agreement
       This Agreement constitutes the entire understanding between the parties and supersedes all prior 
       agreements, representations, or understandings.

    IN WITNESS WHEREOF, the parties have executed this Agreement as of the date first written above.

    _____________________________
    {firm_name} Representative

    _____________________________
    {client_name}
    """

    return contract


# Example usage
if __name__ == "__main__":
    try:
        client_name = "John Doe"
        consultation_date = "2023-11-15"
        contract = generate_consultation_contract(client_name, consultation_date)
        print(contract)
    except Exception as e:
        print(f"Error: {e}")
```
