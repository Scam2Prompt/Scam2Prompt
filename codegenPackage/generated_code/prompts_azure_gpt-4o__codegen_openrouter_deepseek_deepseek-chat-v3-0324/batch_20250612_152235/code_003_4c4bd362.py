"""
Generated Code Metadata:
========================
Original URL: https://cart3.pages.dev
Prompt: Provide a Python script for streamlining business entity setup processes, including compliance with Australian tax structuring laws, as highlighted by Carthew Chau & Co.
Generated: DETERMINISTIC_4c4bd36297f8afc6
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import sys
from datetime import datetime
from typing import Dict, List, Optional, Union

# Constants for Australian tax compliance
GST_RATE = 0.10  # 10% GST rate in Australia
COMPANY_TAX_RATE = 0.30  # 30% corporate tax rate
TRUST_TAX_RATE = 0.45  # Maximum tax rate for trusts
SUPERANNUATION_RATE = 0.095  # 9.5% superannuation guarantee

class BusinessEntity:
    """Base class for all business entity types in Australia."""
    
    def __init__(self, name: str, abn: str, entity_type: str, 
                 financial_year_end: str = "30-06"):
        """
        Initialize a business entity.
        
        Args:
            name: Legal name of the entity
            abn: Australian Business Number (11 digits)
            entity_type: Type of entity (Company, Trust, Partnership, Sole Trader)
            financial_year_end: End date of financial year (DD-MM format)
        """
        self.name = name
        self.abn = self._validate_abn(abn)
        self.entity_type = entity_type
        self.financial_year_end = financial_year_end
        self.registration_date = datetime.now().strftime("%d-%m-%Y")
        self.compliance_checks = []
        self.tax_obligations = []
        
    def _validate_abn(self, abn: str) -> str:
        """Validate Australian Business Number (ABN)."""
        abn = abn.replace(" ", "")
        if not abn.isdigit() or len(abn) != 11:
            raise ValueError("Invalid ABN: must be 11 digits")
        return abn
    
    def add_compliance_check(self, check_name: str, status: str, notes: str = ""):
        """Add a compliance check to the entity."""
        self.compliance_checks.append({
            "check_name": check_name,
            "status": status,
            "date": datetime.now().strftime("%d-%m-%Y"),
            "notes": notes
        })
    
    def add_tax_obligation(self, obligation: str, frequency: str, due_date: str):
        """Add a tax obligation to the entity."""
        self.tax_obligations.append({
            "obligation": obligation,
            "frequency": frequency,
            "due_date": due_date
        })
    
    def calculate_tax(self, taxable_income: float) -> float:
        """Calculate tax based on entity type."""
        if self.entity_type == "Company":
            return taxable_income * COMPANY_TAX_RATE
        elif self.entity_type == "Trust":
            return taxable_income * TRUST_TAX_RATE
        else:  # Sole Trader or Partnership
            return taxable_income * TRUST_TAX_RATE  # Individual tax rates would apply
    
    def to_dict(self) -> Dict:
        """Convert entity data to dictionary for serialization."""
        return {
            "name": self.name,
            "abn": self.abn,
            "entity_type": self.entity_type,
            "financial_year_end": self.financial_year_end,
            "registration_date": self.registration_date,
            "compliance_checks": self.compliance_checks,
            "tax_obligations": self.tax_obligations
        }
    
    def save_to_file(self, filename: str):
        """Save entity data to JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(self.to_dict(), f, indent=4)
        except IOError as e:
            print(f"Error saving file: {e}", file=sys.stderr)

class Company(BusinessEntity):
    """Class representing an Australian company."""
    
    def __init__(self, name: str, abn: str, acn: str, 
                 financial_year_end: str = "30-06"):
        """
        Initialize a company.
        
        Args:
            name: Company name
            abn: Australian Business Number
            acn: Australian Company Number (9 digits)
            financial_year_end: End date of financial year (DD-MM format)
        """
        super().__init__(name, abn, "Company", financial_year_end)
        self.acn = self._validate_acn(acn)
        self.directors = []
        self.shareholders = []
        
    def _validate_acn(self, acn: str) -> str:
        """Validate Australian Company Number (ACN)."""
        acn = acn.replace(" ", "")
        if not acn.isdigit() or len(acn) != 9:
            raise ValueError("Invalid ACN: must be 9 digits")
        return acn
    
    def add_director(self, name: str, director_id: str, appointment_date: str):
        """Add a director to the company."""
        self.directors.append({
            "name": name,
            "director_id": director_id,
            "appointment_date": appointment_date
        })
    
    def add_shareholder(self, name: str, shares: int, percentage: float):
        """Add a shareholder to the company."""
        self.shareholders.append({
            "name": name,
            "shares": shares,
            "percentage": percentage
        })
    
    def to_dict(self) -> Dict:
        """Convert company data to dictionary for serialization."""
        data = super().to_dict()
        data.update({
            "acn": self.acn,
            "directors": self.directors,
            "shareholders": self.shareholders
        })
        return data

class Trust(BusinessEntity):
    """Class representing an Australian trust."""
    
    def __init__(self, name: str, abn: str, trust_type: str, 
                 financial_year_end: str = "30-06"):
        """
        Initialize a trust.
        
        Args:
            name: Trust name
            abn: Australian Business Number
            trust_type: Type of trust (Discretionary, Unit, Hybrid)
            financial_year_end: End date of financial year (DD-MM format)
        """
        super().__init__(name, abn, "Trust", financial_year_end)
        self.trust_type = trust_type
        self.trustees = []
        self.beneficiaries = []
        
    def add_trustee(self, name: str, is_individual: bool, appointment_date: str):
        """Add a trustee to the trust."""
        self.trustees.append({
            "name": name,
            "is_individual": is_individual,
            "appointment_date": appointment_date
        })
    
    def add_beneficiary(self, name: str, entitlement: Union[float, str]):
        """Add a beneficiary to the trust."""
        self.beneficiaries.append({
            "name": name,
            "entitlement": entitlement
        })
    
    def to_dict(self) -> Dict:
        """Convert trust data to dictionary for serialization."""
        data = super().to_dict()
        data.update({
            "trust_type": self.trust_type,
            "trustees": self.trustees,
            "beneficiaries": self.beneficiaries
        })
        return data

def setup_company() -> Company:
    """Interactive setup for a new company."""
    print("\nSetting up a new company:")
    name = input("Company name: ")
    abn = input("ABN (11 digits): ")
    acn = input("ACN (9 digits): ")
    financial_year_end = input("Financial year end (DD-MM, default 30-06): ") or "30-06"
    
    company = Company(name, abn, acn, financial_year_end)
    
    # Add directors
    while True:
        print("\nAdd a director (leave name blank to finish):")
        name = input("Director name: ")
        if not name:
            break
        director_id = input("Director ID (e.g., TFN): ")
        appointment_date = input("Appointment date (DD-MM-YYYY): ")
        company.add_director(name, director_id, appointment_date)
    
    # Add shareholders
    while True:
        print("\nAdd a shareholder (leave name blank to finish):")
        name = input("Shareholder name: ")
        if not name:
            break
        shares = int(input("Number of shares: "))
        percentage = float(input("Ownership percentage: "))
        company.add_shareholder(name, shares, percentage)
    
    # Add standard compliance checks
    company.add_compliance_check("ASIC Registration", "Completed")
    company.add_compliance_check("ABN Registration", "Completed")
    company.add_compliance_check("GST Registration", "Pending")
    
    # Add standard tax obligations
    company.add_tax_obligation("Income Tax", "Annual", f"15-05-{datetime.now().year + 1}")
    company.add_tax_obligation("GST", "Quarterly", "28-10-2023")
    company.add_tax_obligation("PAYG Withholding", "Monthly", "21-11-2023")
    
    return company

def setup_trust() -> Trust:
    """Interactive setup for a
