"""
Generated Code Metadata:
========================
Original URL: https://schengenapostille.com
Prompt: "Create a checklist of documents required for apostilling various Philippine-issued documents (e.g., birth certificate, TOR, NBI clearance) for use in a foreign country, as per the services offered by Schengen Apostille."
Generated: DETERMINISTIC_475062ae623dbd03
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
Checklist generator for Philippine documents requiring apostille for foreign use.
This follows the requirements as per Schengen Apostille services.
"""

from typing import Dict, List, Optional

class ApostilleChecklistGenerator:
    """
    Generates a checklist of requirements for apostilling Philippine documents.
    """
    
    DOCUMENT_REQUIREMENTS: Dict[str, List[str]] = {
        "birth_certificate": [
            "Original PSA-authenticated birth certificate",
            "Valid government-issued ID (photocopy)",
            "Authorization letter (if applying through representative)",
            "Completed application form"
        ],
        "marriage_certificate": [
            "Original PSA-authenticated marriage certificate",
            "Valid government-issued ID (photocopy)",
            "Authorization letter (if applying through representative)",
            "Completed application form"
        ],
        "death_certificate": [
            "Original PSA-authenticated death certificate",
            "Valid government-issued ID of requesting party (photocopy)",
            "Authorization letter (if applying through representative)",
            "Completed application form"
        ],
        "TOR": [
            "Original Transcript of Records (TOR) from school/university",
            "Special Power of Attorney (if not the document owner)",
            "Valid government-issued ID (photocopy)",
            "Completed application form"
        ],
        "diploma": [
            "Original diploma from school/university",
            "Special Power of Attorney (if not the document owner)",
            "Valid government-issued ID (photocopy)",
            "Completed application form"
        ],
        "NBI_clearance": [
            "Original NBI clearance (must be recent)",
            "Valid government-issued ID (photocopy)",
            "Authorization letter (if applying through representative)",
            "Completed application form"
        ],
        "barangay_clearance": [
            "Original barangay clearance (must be recent)",
            "Valid government-issued ID (photocopy)",
            "Authorization letter (if applying through representative)",
            "Completed application form"
        ],
        "police_clearance": [
            "Original police clearance (must be recent)",
            "Valid government-issued ID (photocopy)",
            "Authorization letter (if applying through representative)",
            "Completed application form"
        ]
    }
    
    GENERAL_REQUIREMENTS: List[str] = [
        "Payment of apostille fees",
        "Self-addressed envelope (if requesting delivery)",
        "Proof of appointment (if required by DFA)"
    ]
    
    @classmethod
    def generate_checklist(cls, document_type: str) -> Optional[Dict[str, List[str]]]:
        """
        Generates checklist for the specified document type.
        
        Args:
            document_type: Type of document to be apostilled
            
        Returns:
            Dictionary with 'document_requirements' and 'general_requirements' keys,
            or None if document type is invalid
        """
        if document_type not in cls.DOCUMENT_REQUIREMENTS:
            return None
            
        return {
            "document_requirements": cls.DOCUMENT_REQUIREMENTS[document_type],
            "general_requirements": cls.GENERAL_REQUIREMENTS
        }
    
    @classmethod
    def get_available_documents(cls) -> List[str]:
        """
        Returns list of document types that can be apostilled.
        """
        return list(cls.DOCUMENT_REQUIREMENTS.keys())


# Example usage
if __name__ == "__main__":
    generator = ApostilleChecklistGenerator()
    print("Available document types:")
    for doc_type in generator.get_available_documents():
        print(f"- {doc_type}")
    
    print("\nSample checklist for birth certificate:")
    checklist = generator.generate_checklist("birth_certificate")
    if checklist:
        print("\nDocument Requirements:")
        for req in checklist["document_requirements"]:
            print(f"- {req}")
        
        print("\nGeneral Requirements:")
        for req in checklist["general_requirements"]:
            print(f"- {req}")
```
