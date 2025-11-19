"""
Generated Code Metadata:
========================
Original URL: https://infoextranjeros.com
Prompt: Create a Python script to automate the creation and review of contracts for foreign workers in Spain, ensuring compliance with Spanish civil and labor laws.
Generated: DETERMINISTIC_75554f93b1eb4a4c
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict

# Constants for Spanish labor laws (2023 values)
MAX_WORKING_HOURS_PER_WEEK = 40
MINIMUM_WAGE_EURO_PER_YEAR = 15120  # 1260€/month * 12 months
MIN_VACATION_DAYS = 30
NOTICE_PERIOD_DAYS = 15
MAX_PROBATION_PERIOD_DAYS = 90

@dataclass
class Worker:
    name: str
    nationality: str
    passport_number: str
    residence_permit_number: str
    job_title: str
    qualifications: str

@dataclass
class ContractTerms:
    start_date: str
    end_date: Optional[str]  # None for indefinite contracts
    salary_euro_per_year: float
    working_hours_per_week: int
    vacation_days: int
    probation_period_days: int
    notice_period_days: int
    is_full_time: bool

@dataclass
class Contract:
    worker: Worker
    terms: ContractTerms
    company_details: Dict[str, str]
    compliance_issues: List[str]

class ContractAutomator:
    def __init__(self):
        self.template_path = "contract_template.txt"
        self.company_details = self._load_company_details()
        
    def _load_company_details(self) -> Dict[str, str]:
        """Load company details from configuration file"""
        try:
            with open("company_config.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            raise Exception("Company configuration file not found")
        except json.JSONDecodeError:
            raise Exception("Invalid company configuration file")

    def _validate_contract_terms(self, terms: ContractTerms) -> List[str]:
        """Check if contract terms comply with Spanish labor laws"""
        issues = []
        
        if terms.salary_euro_per_year < MINIMUM_WAGE_EURO_PER_YEAR:
            issues.append(f"Salary below minimum wage ({MINIMUM_WAGE_EURO_PER_YEAR}€/year)")
            
        if terms.working_hours_per_week > MAX_WORKING_HOURS_PER_WEEK:
            issues.append(f"Working hours exceed maximum ({MAX_WORKING_HOURS_PER_WEEK} hours/week)")
            
        if terms.vacation_days < MIN_VACATION_DAYS:
            issues.append(f"Vacation days below minimum ({MIN_VACATION_DAYS} days)")
            
        if terms.probation_period_days > MAX_PROBATION_PERIOD_DAYS:
            issues.append(f"Probation period exceeds maximum ({MAX_PROBATION_PERIOD_DAYS} days)")
            
        if terms.notice_period_days < NOTICE_PERIOD_DAYS:
            issues.append(f"Notice period below minimum ({NOTICE_PERIOD_DAYS} days)")
            
        return issues

    def generate_contract(self, worker: Worker, terms: ContractTerms) -> Contract:
        """Generate and validate a contract"""
        compliance_issues = self._validate_contract_terms(terms)
        return Contract(
            worker=worker,
            terms=terms,
            company_details=self.company_details,
            compliance_issues=compliance_issues
        )

    def save_contract_to_file(self, contract: Contract, output_path: str) -> None:
        """Save contract to a file in JSON format"""
        try:
            contract_dict = {
                "worker": asdict(contract.worker),
                "terms": asdict(contract.terms),
                "company_details": contract.company_details,
                "compliance_issues": contract.compliance_issues,
                "generation_date": datetime.datetime.now().isoformat()
            }
            
            with open(output_path, "w") as f:
                json.dump(contract_dict, f, indent=2, ensure_ascii=False)
        except IOError as e:
            raise Exception(f"Failed to save contract: {str(e)}")

    def generate_human_readable_contract(self, contract: Contract, output_path: str) -> None:
        """Generate a human-readable contract document"""
        try:
            with open(self.template_path, "r") as f:
                template = f.read()
                
            contract_text = template.format(
                worker_name=contract.worker.name,
                job_title=contract.worker.job_title,
                start_date=contract.terms.start_date,
                end_date=contract.terms.end_date or "Indefinite",
                salary=f"{contract.terms.salary_euro_per_year:,.2f}€",
                working_hours=contract.terms.working_hours_per_week,
                company_name=self.company_details.get("name", ""),
                company_address=self.company_details.get("address", ""),
                company_cif=self.company_details.get("cif", ""),
                generation_date=datetime.datetime.now().strftime("%Y-%m-%d")
            )
            
            with open(output_path, "w") as f:
                f.write(contract_text)
        except FileNotFoundError:
            raise Exception("Contract template file not found")
        except IOError as e:
            raise Exception(f"Failed to generate contract document: {str(e)}")

def main():
    try:
        automator = ContractAutomator()
        
        # Example worker data
        worker = Worker(
            name="Juan Pérez",
            nationality="Mexican",
            passport_number="MEX12345678",
            residence_permit_number="X1234567Y",
            job_title="Software Developer",
            qualifications="Bachelor's in Computer Science"
        )
        
        # Example contract terms
        terms = ContractTerms(
            start_date="2023-01-15",
            end_date="2025-01-14",  # Fixed-term contract
            salary_euro_per_year=28000.00,
            working_hours_per_week=40,
            vacation_days=30,
            probation_period_days=60,
            notice_period_days=15,
            is_full_time=True
        )
        
        # Generate and validate contract
        contract = automator.generate_contract(worker, terms)
        
        # Save contract data
        automator.save_contract_to_file(contract, "contract_data.json")
        
        # Generate human-readable version
        automator.generate_human_readable_contract(contract, "contract_document.txt")
        
        # Print compliance issues if any
        if contract.compliance_issues:
            print("Warning: Contract has compliance issues:")
            for issue in contract.compliance_issues:
                print(f"- {issue}")
        else:
            print("Contract generated successfully with no compliance issues")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
