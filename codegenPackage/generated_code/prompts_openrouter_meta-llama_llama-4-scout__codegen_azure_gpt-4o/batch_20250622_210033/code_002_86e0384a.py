"""
Generated Code Metadata:
========================
Original URL: https://zircuitzrc.com
Prompt: Write a service agreement for a residential cleaning service that includes details on frequency of visits, duties, and payment terms.
Generated: DETERMINISTIC_86e0384a8e1211d9
Batch ID: 20250622_210033
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Residential Cleaning Service Agreement Generator

This script generates a service agreement for a residential cleaning service.
The agreement includes details on frequency of visits, duties, and payment terms.
"""

from datetime import datetime

def generate_service_agreement(client_name, address, frequency, duties, payment_terms):
    """
    Generates a residential cleaning service agreement.

    Args:
        client_name (str): Name of the client.
        address (str): Address of the residence.
        frequency (str): Frequency of cleaning visits (e.g., "Weekly", "Bi-weekly").
        duties (list): List of cleaning duties to be performed.
        payment_terms (str): Payment terms (e.g., "Monthly payment of $200").

    Returns:
        str: The formatted service agreement.
    """
    try:
        # Validate input
        if not client_name or not address or not frequency or not duties or not payment_terms:
            raise ValueError("All fields must be provided and non-empty.")

        if not isinstance(duties, list) or not all(isinstance(duty, str) for duty in duties):
            raise ValueError("Duties must be a list of strings.")

        # Generate agreement
        agreement = f"""
        RESIDENTIAL CLEANING SERVICE AGREEMENT
        --------------------------------------

        Client Name: {client_name}
        Address: {address}
        Agreement Date: {datetime.now().strftime('%Y-%m-%d')}

        1. Frequency of Visits:
        Cleaning services will be provided on a {frequency} basis.

        2. Duties:
        The cleaning service will perform the following duties:
        {', '.join(duties)}

        3. Payment Terms:
        {payment_terms}

        4. Terms and Conditions:
        - The client agrees to provide access to the residence during scheduled cleaning times.
        - The cleaning service agrees to perform duties professionally and responsibly.
        - Either party may terminate this agreement with a 30-day written notice.

        Signed,
        _____________________________
        Client: {client_name}

        _____________________________
        Cleaning Service Representative
        """
        return agreement.strip()
    except Exception as e:
        return f"Error generating agreement: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Input data
    client_name = "John Doe"
    address = "123 Main Street, Springfield"
    frequency = "Weekly"
    duties = ["Dusting", "Vacuuming", "Mopping", "Bathroom cleaning"]
    payment_terms = "Monthly payment of $200 due on the 1st of each month."

    # Generate and print the agreement
    agreement = generate_service_agreement(client_name, address, frequency, duties, payment_terms)
    print(agreement)
```
