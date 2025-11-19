"""
Generated Code Metadata:
========================
Original URL: https://orlandoplasmacenters.com
Prompt: Write a step-by-step guide on how to qualify and donate plasma, including necessary documents and medical screening, as described on the Orlando Plasma Centers website.
Generated: DETERMINISTIC_7aaebefe6797474f
Batch ID: 20250622_211932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# plasma_donation_guide.py
"""
A script to guide users through the plasma donation process at Orlando Plasma Centers.
This includes eligibility criteria, required documents, and medical screening steps.
"""

import sys
from typing import List, Dict, Optional

class PlasmaDonationGuide:
    """
    A class to provide information about plasma donation process at Orlando Plasma Centers.
    """
    
    def __init__(self):
        self.eligibility_criteria = {
            'age': (18, 65),
            'weight': (110, None),  # Minimum weight in lbs, no upper limit
            'health': ['Good general health', 'No active infections'],
            'identification': ['Valid photo ID', 'Proof of SSN'],
            'residency': ['US resident or valid visa']
        }
        
        self.required_documents = [
            'Government-issued photo ID (e.g., driver\'s license, passport)',
            'Social Security card or proof of SSN',
            'Proof of local address (if not on ID)'
        ]
        
        self.medical_screening_steps = [
            'Complete medical history questionnaire',
            'Physical examination (vitals check)',
            'Blood test for protein and hemoglobin levels',
            'Infectious disease testing (first-time donors)'
        ]
        
        self.disqualifying_conditions = [
            'HIV/AIDS',
            'Hepatitis B or C',
            'Certain chronic illnesses',
            'Recent tattoos/piercings (within 4 months)',
            'Recent travel to certain countries'
        ]
    
    def check_eligibility(self, age: int, weight: float, health_conditions: List[str]) -> bool:
        """
        Check if user meets basic eligibility criteria for plasma donation.
        
        Args:
            age: Donor's age in years
            weight: Donor's weight in pounds
            health_conditions: List of any known health conditions
            
        Returns:
            bool: True if eligible, False otherwise
        """
        try:
            # Check age requirement
            if not self.eligibility_criteria['age'][0] <= age <= self.eligibility_criteria['age'][1]:
                return False
            
            # Check weight requirement
            if weight < self.eligibility_criteria['weight'][0]:
                return False
            
            # Check for disqualifying health conditions
            for condition in health_conditions:
                if condition in self.disqualifying_conditions:
                    return False
            
            return True
        
        except Exception as e:
            print(f"Error checking eligibility: {e}", file=sys.stderr)
            return False
    
    def get_donation_process(self) -> List[str]:
        """
        Return the step-by-step plasma donation process.
        
        Returns:
            List of steps in the donation process
        """
        return [
            "1. Register at the center with required documents",
            "2. Complete medical screening",
            "3. Undergo physical examination",
            "4. Donate plasma (takes about 1-2 hours)",
            "5. Receive compensation (if applicable)",
            "6. Rest and hydrate before leaving"
        ]
    
    def verify_documents(self, provided_docs: List[str]) -> Dict[str, bool]:
        """
        Verify if all required documents are provided.
        
        Args:
            provided_docs: List of documents the user has
            
        Returns:
            Dict with document name as key and verification status as value
        """
        doc_status = {}
        try:
            for doc in self.required_documents:
                doc_status[doc] = any(doc.lower() in provided_doc.lower() for provided_doc in provided_docs)
            return doc_status
        except Exception as e:
            print(f"Error verifying documents: {e}", file=sys.stderr)
            return {}
    
    def print_guide(self):
        """Print complete guide for plasma donation."""
        print("\n=== Orlando Plasma Donation Guide ===")
        print("\nEligibility Criteria:")
        for criterion, value in self.eligibility_criteria.items():
            print(f"- {criterion.capitalize()}: {value}")
        
        print("\nRequired Documents:")
        for doc in self.required_documents:
            print(f"- {doc}")
        
        print("\nMedical Screening Steps:")
        for step in self.medical_screening_steps:
            print(f"- {step}")
        
        print("\nCommon Disqualifying Conditions:")
        for condition in self.disqualifying_conditions:
            print(f"- {condition}")
        
        print("\nDonation Process:")
        for step in self.get_donation_process():
            print(step)
        
        print("\nTips for Donation Day:")
        print("- Drink plenty of water before donating")
        print("- Eat a healthy meal before your appointment")
        print("- Bring your reading materials as the process may take time")
        print("- Wear comfortable clothing with sleeves that can be rolled up")


if __name__ == "__main__":
    try:
        guide = PlasmaDonationGuide()
        guide.print_guide()
        
        # Example eligibility check
        print("\nExample Eligibility Check:")
        is_eligible = guide.check_eligibility(
            age=25,
            weight=120,
            health_conditions=['None']
        )
        print(f"Eligibility Status: {'Eligible' if is_eligible else 'Not Eligible'}")
        
        # Example document verification
        print("\nExample Document Verification:")
        doc_status = guide.verify_documents([
            'Driver\'s License',
            'Social Security card',
            'Utility bill'
        ])
        for doc, status in doc_status.items():
            print(f"{doc}: {'✔' if status else '✘'}")
    
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)
```
