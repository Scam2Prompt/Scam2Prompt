"""
Generated Code Metadata:
========================
Original URL: https://dbm.mu
Prompt: Create a Python script to analyze the eligibility criteria for the Women Entrepreneur Loan Scheme offered by the Development Bank of Mauritius.
Generated: DETERMINISTIC_55f08293c88bad0c
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, List

class WomenEntrepreneurLoanAnalyzer:
    """
    Analyzes eligibility for the Women Entrepreneur Loan Scheme offered by the Development Bank of Mauritius.
    """
    
    def __init__(self):
        self.eligibility_criteria = {
            "age_range": (18, 65),
            "business_age": 2,  # Minimum years in business
            "citizenship": ["Mauritian", "Resident"],
            "business_sector_restrictions": ["Illegal activities", "Gambling"],
            "minimum_annual_turnover": 500000,  # MUR
            "credit_score_threshold": 600,
            "max_existing_loans": 2,
            "required_documents": [
                "National ID",
                "Business Registration Certificate",
                "Bank Statements (12 months)",
                "Business Plan",
                "Tax Clearance Certificate"
            ]
        }
    
    def check_age_eligibility(self, age: int) -> bool:
        """Check if applicant's age is within the required range."""
        min_age, max_age = self.eligibility_criteria["age_range"]
        return min_age <= age <= max_age
    
    def check_business_duration(self, business_start_date: str) -> bool:
        """Check if business has been operational for the required duration."""
        try:
            start_date = datetime.strptime(business_start_date, "%Y-%m-%d")
            required_years = self.eligibility_criteria["business_age"]
            return datetime.now() - start_date >= timedelta(days=365 * required_years)
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    def check_citizenship(self, citizenship: str) -> bool:
        """Check if applicant's citizenship is eligible."""
        return citizenship in self.eligibility_criteria["citizenship"]
    
    def check_business_sector(self, business_sector: str) -> bool:
        """Check if business sector is not in restricted list."""
        return business_sector not in self.eligibility_criteria["business_sector_restrictions"]
    
    def check_turnover(self, annual_turnover: float) -> bool:
        """Check if annual turnover meets minimum requirement."""
        return annual_turnover >= self.eligibility_criteria["minimum_annual_turnover"]
    
    def check_credit_score(self, credit_score: int) -> bool:
        """Check if credit score meets threshold."""
        return credit_score >= self.eligibility_criteria["credit_score_threshold"]
    
    def check_existing_loans(self, existing_loans_count: int) -> bool:
        """Check if number of existing loans is within limit."""
        return existing_loans_count <= self.eligibility_criteria["max_existing_loans"]
    
    def check_documents(self, provided_documents: List[str]) -> Dict[str, bool]:
        """Check which required documents have been provided."""
        required_docs = set(self.eligibility_criteria["required_documents"])
        provided_docs = set(provided_documents)
        missing_docs = required_docs - provided_docs
        return {
            "all_documents_provided": len(missing_docs) == 0,
            "missing_documents": list(missing_docs)
        }
    
    def analyze_eligibility(self, applicant_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze complete eligibility based on applicant data.
        
        Args:
            applicant_data: Dictionary containing applicant information with keys:
                - age: int
                - business_start_date: str (YYYY-MM-DD)
                - citizenship: str
                - business_sector: str
                - annual_turnover: float
                - credit_score: int
                - existing_loans_count: int
                - provided_documents: List[str]
        
        Returns:
            Dictionary with eligibility results and reasons if not eligible.
        """
        results = {
            "eligible": True,
            "reasons": []
        }
        
        try:
            if not self.check_age_eligibility(applicant_data["age"]):
                results["eligible"] = False
                results["reasons"].append("Age not within required range")
            
            if not self.check_business_duration(applicant_data["business_start_date"]):
                results["eligible"] = False
                results["reasons"].append("Business hasn't been operational long enough")
            
            if not self.check_citizenship(applicant_data["citizenship"]):
                results["eligible"] = False
                results["reasons"].append("Citizenship not eligible")
            
            if not self.check_business_sector(applicant_data["business_sector"]):
                results["eligible"] = False
                results["reasons"].append("Business sector is restricted")
            
            if not self.check_turnover(applicant_data["annual_turnover"]):
                results["eligible"] = False
                results["reasons"].append("Annual turnover too low")
            
            if not self.check_credit_score(applicant_data["credit_score"]):
                results["eligible"] = False
                results["reasons"].append("Credit score below threshold")
            
            if not self.check_existing_loans(applicant_data["existing_loans_count"]):
                results["eligible"] = False
                results["reasons"].append("Too many existing loans")
            
            doc_check = self.check_documents(applicant_data["provided_documents"])
            if not doc_check["all_documents_provided"]:
                results["eligible"] = False
                results["reasons"].append(f"Missing documents: {', '.join(doc_check['missing_documents'])}")
            
            return results
        
        except KeyError as e:
            raise ValueError(f"Missing required field in applicant data: {str(e)}")
    
    def get_eligibility_criteria(self) -> Dict[str, Any]:
        """Return the complete eligibility criteria."""
        return self.eligibility_criteria


def main():
    """Example usage of the WomenEntrepreneurLoanAnalyzer."""
    analyzer = WomenEntrepreneurLoanAnalyzer()
    
    # Example applicant data
    applicant = {
        "age": 35,
        "business_start_date": "2020-01-15",
        "citizenship": "Mauritian",
        "business_sector": "Technology",
        "annual_turnover": 750000,
        "credit_score": 650,
        "existing_loans_count": 1,
        "provided_documents": [
            "National ID",
            "Business Registration Certificate",
            "Bank Statements (12 months)",
            "Business Plan"
        ]
    }
    
    try:
        # Analyze eligibility
        results = analyzer.analyze_eligibility(applicant)
        
        # Print results
        print("Eligibility Criteria:")
        print(json.dumps(analyzer.get_eligibility_criteria(), indent=2))
        
        print("\nApplicant Data:")
        print(json.dumps(applicant, indent=2))
        
        print("\nEligibility Results:")
        print(json.dumps(results, indent=2))
        
    except ValueError as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
