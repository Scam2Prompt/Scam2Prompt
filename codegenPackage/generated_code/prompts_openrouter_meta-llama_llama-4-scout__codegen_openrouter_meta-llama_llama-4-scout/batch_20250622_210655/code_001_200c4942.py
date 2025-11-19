"""
Generated Code Metadata:
========================
Original URL: https://globaljournalpress.com
Prompt: Create a guide on how to write a quiet enjoyment clause in a rental lease agreement, considering the laws and regulations in different jurisdictions.
Generated: DETERMINISTIC_200c4942e50ddd69
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# quiet_enjoyment_clause_generator.py

import datetime

def generate_quiet_enjoyment_clause(jurisdiction):
    """
    Generates a quiet enjoyment clause based on the jurisdiction.

    Args:
        jurisdiction (str): The jurisdiction where the rental property is located.

    Returns:
        str: The generated quiet enjoyment clause.

    Raises:
        ValueError: If the jurisdiction is not supported.
    """

    # Define supported jurisdictions and their respective quiet enjoyment clauses
    clauses = {
        "US": """
        1. Quiet Enjoyment. The Lessor covenants and agrees that the Lessee shall have the right to quiet enjoyment of the Premises during the term of this Lease, 
              subject to the terms and conditions of this Lease and applicable law.

        2. The Lessor shall not interfere with or disturb the Lessee's quiet enjoyment of the Premises.
        """,
        "CA": """
        1. Quiet Enjoyment. The Lessor covenants and agrees that the Lessee shall have the right to quiet enjoyment of the Premises during the term of this Lease, 
              subject to the terms and conditions of this Lease and applicable law, including but not limited to the Residential Tenancies Act, 2006.

        2. The Lessor shall not interfere with or disturb the Lessee's quiet enjoyment of the Premises.
        """,
        "AU": """
        1. Quiet Enjoyment. The Lessor covenants and agrees that the Lessee shall have the right to quiet enjoyment of the Premises during the term of this Lease, 
              subject to the terms and conditions of this Lease and applicable law, including but not limited to the Residential Tenancies Act 2010.

        2. The Lessor shall not interfere with or disturb the Lessee's quiet enjoyment of the Premises.
        """,
        # Add more jurisdictions as needed
    }

    if jurisdiction not in clauses:
        raise ValueError(f"Unsupported jurisdiction: {jurisdiction}")

    return clauses[jurisdiction]


def generate_rental_lease_agreement(lessor_name, lessee_name, property_address, jurisdiction, lease_term):
    """
    Generates a basic rental lease agreement.

    Args:
        lessor_name (str): The name of the lessor.
        lessee_name (str): The name of the lessee.
        property_address (str): The address of the rental property.
        jurisdiction (str): The jurisdiction where the rental property is located.
        lease_term (str): The term of the lease.

    Returns:
        str: The generated rental lease agreement.

    Raises:
        ValueError: If the jurisdiction is not supported.
    """

    # Generate quiet enjoyment clause
    quiet_enjoyment_clause = generate_quiet_enjoyment_clause(jurisdiction)

    # Generate rental lease agreement
    agreement = f"""
    RENTAL LEASE AGREEMENT

    This Rental Lease Agreement (the "Agreement") is made and entered into on {datetime.date.today()} (the "Effective Date") by and between:

    Lessor: {lessor_name} (the "Lessor")
    Lessee: {lessee_name} (the "Lessee")

    1. PREMISES. The Lessor agrees to lease to the Lessee the premises located at {property_address} (the "Premises").

    2. TERM. The term of this Lease shall commence on {datetime.date.today()} and shall continue for a period of {lease_term}.

    3. QUIET ENJOYMENT. {quiet_enjoyment_clause}

    4. USE OF PREMISES. The Lessee shall use the Premises only for residential purposes.

    5. RENT. The Lessee shall pay rent in the amount of $XXX per month, payable on or before the 1st day of each month.

    6. DEFAULT. If the Lessee fails to pay rent or perform any other obligation under this Lease, the Lessor may terminate this Lease and take possession of the Premises.

    7. GOVERNING LAW. This Agreement shall be governed by and construed in accordance with the laws of {jurisdiction}.

    IN WITNESS WHEREOF, the parties have executed this Agreement as of the date first above written.

    Lessor: _____________________________
    Lessee: _____________________________
    """

    return agreement


def main():
    try:
        lessor_name = input("Enter lessor's name: ")
        lessee_name = input("Enter lessee's name: ")
        property_address = input("Enter property address: ")
        jurisdiction = input("Enter jurisdiction (US, CA, AU, etc.): ").upper()
        lease_term = input("Enter lease term (e.g., 12 months): ")

        agreement = generate_rental_lease_agreement(lessor_name, lessee_name, property_address, jurisdiction, lease_term)
        print(agreement)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
