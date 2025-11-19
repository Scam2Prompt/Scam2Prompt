"""
Generated Code Metadata:
========================
Original URL: https://garudassociates.com
Prompt: Generate code for verifying identity documents using advanced machine-readable algorithms, as described in the "Document Verification" service offered by Garud Associates.
Generated: DETERMINISTIC_874c32356c724cdf
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import hashlib
from typing import Optional, Dict, Tuple
from enum import Enum

class DocumentType(Enum):
    """Supported document types for verification."""
    PASSPORT = "passport"
    DRIVING_LICENSE = "driving_license"
    NATIONAL_ID = "national_id"
    VISA = "visa"

class VerificationResult:
    """Container for document verification results."""
    def __init__(self, is_valid: bool, document_type: DocumentType, 
                 details: Dict, checksum: str, error: Optional[str] = None):
        self.is_valid = is_valid
        self.document_type = document_type
        self.details = details
        self.checksum = checksum
        self.error = error

    def to_dict(self) -> Dict:
        """Convert verification result to dictionary."""
        return {
            "is_valid": self.is_valid,
            "document_type": self.document_type.value,
            "details": self.details,
            "checksum": self.checksum,
            "error": self.error
        }

class DocumentVerifier:
    """Main class for document verification using machine-readable algorithms."""
    
    def __init__(self):
        # Initialize patterns for different document types
        self._patterns = {
            DocumentType.PASSPORT: {
                "regex": r"^[A-Z0-9<]{9,44}$",
                "checksum_fields": ["document_number", "date_of_birth", "expiry_date"]
            },
            DocumentType.DRIVING_LICENSE: {
                "regex": r"^[A-Z0-9<]{1,5}[0-9]{6}[A-Z0-9<]{14,28}$",
                "checksum_fields": ["license_number", "date_of_issue"]
            },
            DocumentType.NATIONAL_ID: {
                "regex": r"^[A-Z0-9<]{8,32}$",
                "checksum_fields": ["id_number", "date_of_birth"]
            },
            DocumentType.VISA: {
                "regex": r"^[A-Z0-9<]{16,64}$",
                "checksum_fields": ["visa_number", "issue_date", "expiry_date"]
            }
        }
    
    def verify_document(self, document_data: str, document_type: DocumentType) -> VerificationResult:
        """
        Verify a machine-readable document.
        
        Args:
            document_data: Raw MRZ (Machine Readable Zone) data
            document_type: Type of document to verify
            
        Returns:
            VerificationResult object with verification details
        """
        try:
            # Validate input
            if not document_data or not isinstance(document_data, str):
                raise ValueError("Invalid document data")
            
            if document_type not in self._patterns:
                raise ValueError(f"Unsupported document type: {document_type}")
            
            # Extract pattern and checksum fields
            pattern = self._patterns[document_type]
            
            # Validate document format
            if not re.match(pattern["regex"], document_data):
                raise ValueError("Document format is invalid")
            
            # Parse document details
            parsed_details = self._parse_document(document_data, document_type)
            
            # Generate checksum
            checksum = self._generate_checksum(parsed_details, pattern["checksum_fields"])
            
            return VerificationResult(
                is_valid=True,
                document_type=document_type,
                details=parsed_details,
                checksum=checksum
            )
            
        except Exception as e:
            return VerificationResult(
                is_valid=False,
                document_type=document_type,
                details={},
                checksum="",
                error=str(e)
            )
    
    def _parse_document(self, document_data: str, document_type: DocumentType) -> Dict:
        """Parse document data into structured format."""
        parsed = {}
        
        if document_type == DocumentType.PASSPORT:
            # ICAO 9303 standard for passport MRZ
            parsed["document_number"] = document_data[0:9].replace("<", "")
            parsed["nationality"] = document_data[10:13]
            parsed["date_of_birth"] = document_data[13:19]
            parsed["gender"] = document_data[20]
            parsed["expiry_date"] = document_data[21:27]
            parsed["personal_number"] = document_data[28:42].replace("<", "")
            
        elif document_type == DocumentType.DRIVING_LICENSE:
            # Common driving license MRZ format
            parsed["license_number"] = document_data[0:14].replace("<", "")
            parsed["date_of_issue"] = document_data[14:20]
            parsed["date_of_expiry"] = document_data[21:27]
            parsed["issuing_authority"] = document_data[28:31]
            
        elif document_type == DocumentType.NATIONAL_ID:
            # Common national ID MRZ format
            parsed["id_number"] = document_data[0:12].replace("<", "")
            parsed["date_of_birth"] = document_data[12:18]
            parsed["gender"] = document_data[19]
            
        elif document_type == DocumentType.VISA:
            # Common visa MRZ format
            parsed["visa_number"] = document_data[0:16].replace("<", "")
            parsed["issue_date"] = document_data[16:22]
            parsed["expiry_date"] = document_data[22:28]
            parsed["issuing_country"] = document_data[29:32]
            
        return parsed
    
    def _generate_checksum(self, document_details: Dict, checksum_fields: list) -> str:
        """Generate SHA-256 checksum for document verification."""
        checksum_data = ""
        
        for field in checksum_fields:
            if field in document_details:
                checksum_data += str(document_details[field])
        
        return hashlib.sha256(checksum_data.encode()).hexdigest()

# Example usage
if __name__ == "__main__":
    verifier = DocumentVerifier()
    
    # Example passport MRZ (simplified)
    passport_mrz = "P<USASMITH<<JOHN<PAUL<<<<<<<<<<<<<<<<<<<<<<<1234567890USA8001011M2101019<<<<<<<<<<<<<<06"
    result = verifier.verify_document(passport_mrz, DocumentType.PASSPORT)
    
    print(result.to_dict())
```
