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
Film Shoot Armourer Contract Clause Generator

This script generates a contract clause for hiring a licensed armourer for a film shoot,
covering security deposits, liability, and other essential terms.
"""

from datetime import datetime
from typing import Optional

class ArmourerContractClause:
    """
    A class to generate contract clauses for hiring a licensed armourer.
    """
    
    def __init__(
        self,
        armourer_name: str,
        production_company: str,
        shoot_location: str,
        start_date: str,
        end_date: str,
        security_deposit_amount: float,
        liability_limit: float,
        insurance_provider: str,
        insurance_policy_number: str
    ):
        """
        Initialize the contract clause with necessary details.
        
        Args:
            armourer_name: Full name of the licensed armourer
            production_company: Name of the production company
            shoot_location: Primary filming location
            start_date: Contract start date (YYYY-MM-DD)
            end_date: Contract end date (YYYY-MM-DD)
            security_deposit_amount: Amount of security deposit in USD
            liability_limit: Maximum liability amount in USD
            insurance_provider: Name of insurance provider
            insurance_policy_number: Policy number for liability insurance
        """
        self.armourer_name = armourer_name
        self.production_company = production_company
        self.shoot_location = shoot_location
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        self.security_deposit_amount = security_deposit_amount
        self.liability_limit = liability_limit
        self.insurance_provider = insurance_provider
        self.insurance_policy_number = insurance_policy_number
    
    def generate_clause(self) -> str:
        """
        Generate the complete contract clause with all specified terms.
        
        Returns:
            str: The formatted contract clause
        """
        clause = f"""
        ARMOURER SERVICES AGREEMENT CLAUSE

        1. PARTIES
        This agreement is between {self.production_company} ("Production Company") 
        and {self.armourer_name} ("Armourer").

        2. TERM
        The term of this agreement shall be from {self.start_date.strftime('%B %d, %Y')} 
        to {self.end_date.strftime('%B %d, %Y')} at {self.shoot_location}.

        3. SECURITY DEPOSIT
        The Armourer shall provide a security deposit of ${self.security_deposit_amount:,.2f} USD 
        to be held by the Production Company as security for the proper performance of duties 
        and care of all equipment. The deposit shall be refundable within 30 days of the 
        completion of services, less any deductions for damages or breaches of this agreement.

        4. LIABILITY
        a) The Armourer agrees to maintain active liability insurance coverage of at least 
        ${self.liability_limit:,.2f} USD through {self.insurance_provider} (Policy #: {self.insurance_policy_number}) 
        for the duration of this agreement.
        
        b) The Armourer shall be solely responsible for any injuries, damages, or losses 
        resulting from the improper handling, storage, or use of firearms or weapons under 
        their supervision, except where such incidents result from Production Company's 
        gross negligence.

        5. COMPLIANCE
        The Armourer warrants that they are properly licensed in all jurisdictions where 
        services will be performed and will comply with all applicable federal, state, 
        and local laws regarding firearm safety and handling.

        6. INDEMNIFICATION
        The Armourer agrees to indemnify and hold harmless the Production Company from any 
        claims, damages, or liabilities arising from the Armourer's performance of services 
        under this agreement, except where such claims result from Production Company's 
        direct instructions that violate safety protocols.

        [Signatures on following page]
        """
        return clause.strip()

# Example usage
if __name__ == "__main__":
    try:
        contract = ArmourerContractClause(
            armourer_name="John Doe",
            production_company="Acme Productions LLC",
            shoot_location="Los Angeles, CA",
            start_date="2023-11-15",
            end_date="2023-12-20",
            security_deposit_amount=5000.00,
            liability_limit=1000000.00,
            insurance_provider="Global Insurance Co.",
            insurance_policy_number="GLB-2023-ARM-1122"
        )
        
        print(contract.generate_clause())
    except ValueError as e:
        print(f"Error in date format: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
