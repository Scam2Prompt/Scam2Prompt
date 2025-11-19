"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Generate a sample contract clause for hiring a licensed armourer for a film shoot, ensuring it covers security deposits and liability.
Generated: DETERMINISTIC_3ab1ec862b2a595f
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Contract Clause Generator for Hiring a Licensed Armourer
This script generates a sample contract clause for hiring a licensed armourer for a film shoot.
The clause includes provisions for security deposits and liability.
"""

def generate_armourer_contract_clause(armourer_name, film_name, security_deposit_amount, liability_limit):
    """
    Generates a contract clause for hiring a licensed armourer.

    Parameters:
        armourer_name (str): Name of the licensed armourer.
        film_name (str): Name of the film project.
        security_deposit_amount (float): Security deposit amount in USD.
        liability_limit (float): Liability limit in USD.

    Returns:
        str: A formatted contract clause.
    """
    try:
        # Validate inputs
        if not armourer_name or not isinstance(armourer_name, str):
            raise ValueError("Invalid armourer name. It must be a non-empty string.")
        if not film_name or not isinstance(film_name, str):
            raise ValueError("Invalid film name. It must be a non-empty string.")
        if security_deposit_amount <= 0:
            raise ValueError("Security deposit amount must be greater than zero.")
        if liability_limit <= 0:
            raise ValueError("Liability limit must be greater than zero.")

        # Generate contract clause
        clause = f"""
        CONTRACT CLAUSE: LICENSED ARMOURER SERVICES

        This agreement is made between the production company of "{film_name}" (hereinafter referred to as "The Company")
        and {armourer_name} (hereinafter referred to as "The Armourer").

        1. Security Deposit:
           The Armourer shall provide a security deposit of ${security_deposit_amount:,.2f} to The Company prior to the commencement of services.
           This deposit will be held to cover any damages, losses, or breaches of contract caused by The Armourer during the film shoot.
           The deposit will be refunded in full upon successful completion of services, provided no damages or breaches occur.

        2. Liability:
           The Armourer shall be liable for any damages, injuries, or losses caused by negligence or improper handling of equipment during the film shoot.
           The liability of The Armourer shall be limited to ${liability_limit:,.2f}.
           The Company agrees to indemnify The Armourer for any claims arising from circumstances outside The Armourer's control.

        3. Licensing and Compliance:
           The Armourer guarantees that they hold all necessary licenses and certifications required to perform their duties.
           The Armourer agrees to comply with all local, state, and federal laws governing the use of firearms and weaponry on set.

        4. Termination:
           Either party may terminate this agreement with written notice, provided all outstanding obligations are settled.

        Signed and agreed upon by both parties on the date of execution.

        """
        return clause.strip()

    except ValueError as e:
        # Handle input validation errors
        return f"Error: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Sample inputs
    armourer_name = "John Doe"
    film_name = "Action Movie 2023"
    security_deposit_amount = 5000.00
    liability_limit = 100000.00

    # Generate and print the contract clause
    contract_clause = generate_armourer_contract_clause(
        armourer_name, film_name, security_deposit_amount, liability_limit
    )
    print(contract_clause)
```
