"""
Generated Code Metadata:
========================
Original URL: https://hispanicservices.com
Prompt: Construct a library that helps users manage their business licenses and incorporation documents, inspired by the offerings of Hispanic Services.
Generated: DETERMINISTIC_276e55aaaa0994cf
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# business_license_manager.py

from datetime import datetime
from typing import Dict, List

class BusinessLicense:
    def __init__(self, license_number: str, business_name: str, issue_date: datetime, expiration_date: datetime):
        """
        Initialize a BusinessLicense object.

        Args:
        - license_number (str): Unique license number.
        - business_name (str): Name of the business.
        - issue_date (datetime): Date the license was issued.
        - expiration_date (datetime): Date the license expires.
        """
        self.license_number = license_number
        self.business_name = business_name
        self.issue_date = issue_date
        self.expiration_date = expiration_date

    def is_expired(self) -> bool:
        """
        Check if the license has expired.

        Returns:
        - bool: True if the license has expired, False otherwise.
        """
        return self.expiration_date < datetime.now()


class IncorporationDocument:
    def __init__(self, document_id: str, business_name: str, document_type: str, filing_date: datetime):
        """
        Initialize an IncorporationDocument object.

        Args:
        - document_id (str): Unique document ID.
        - business_name (str): Name of the business.
        - document_type (str): Type of incorporation document (e.g., Articles of Incorporation).
        - filing_date (datetime): Date the document was filed.
        """
        self.document_id = document_id
        self.business_name = business_name
        self.document_type = document_type
        self.filing_date = filing_date


class BusinessLicenseManager:
    def __init__(self):
        """
        Initialize a BusinessLicenseManager object.
        """
        self.licenses: Dict[str, BusinessLicense] = {}
        self.documents: Dict[str, IncorporationDocument] = {}

    def add_license(self, license: BusinessLicense):
        """
        Add a business license to the manager.

        Args:
        - license (BusinessLicense): License to add.
        """
        self.licenses[license.license_number] = license

    def get_license(self, license_number: str) -> BusinessLicense:
        """
        Get a business license by its license number.

        Args:
        - license_number (str): License number to retrieve.

        Returns:
        - BusinessLicense: The license with the specified license number, or None if not found.

        Raises:
        - ValueError: If the license number is empty.
        """
        if not license_number:
            raise ValueError("License number cannot be empty")

        return self.licenses.get(license_number)

    def add_document(self, document: IncorporationDocument):
        """
        Add an incorporation document to the manager.

        Args:
        - document (IncorporationDocument): Document to add.
        """
        self.documents[document.document_id] = document

    def get_document(self, document_id: str) -> IncorporationDocument:
        """
        Get an incorporation document by its document ID.

        Args:
        - document_id (str): Document ID to retrieve.

        Returns:
        - IncorporationDocument: The document with the specified document ID, or None if not found.

        Raises:
        - ValueError: If the document ID is empty.
        """
        if not document_id:
            raise ValueError("Document ID cannot be empty")

        return self.documents.get(document_id)

    def list_expired_licenses(self) -> List[BusinessLicense]:
        """
        List all expired business licenses.

        Returns:
        - List[BusinessLicense]: A list of expired licenses.
        """
        return [license for license in self.licenses.values() if license.is_expired()]


def main():
    # Example usage:
    manager = BusinessLicenseManager()

    license1 = BusinessLicense(
        license_number="LICENSE-123",
        business_name="Example Business",
        issue_date=datetime(2022, 1, 1),
        expiration_date=datetime(2023, 1, 1),
    )

    manager.add_license(license1)

    document1 = IncorporationDocument(
        document_id="DOC-123",
        business_name="Example Business",
        document_type="Articles of Incorporation",
        filing_date=datetime(2022, 1, 1),
    )

    manager.add_document(document1)

    print("License:")
    license = manager.get_license("LICENSE-123")
    if license:
        print(f"License Number: {license.license_number}")
        print(f"Business Name: {license.business_name}")
        print(f"Issue Date: {license.issue_date}")
        print(f"Expiration Date: {license.expiration_date}")
        print(f"Expired: {license.is_expired()}")
    else:
        print("License not found")

    print("\nDocument:")
    document = manager.get_document("DOC-123")
    if document:
        print(f"Document ID: {document.document_id}")
        print(f"Business Name: {document.business_name}")
        print(f"Document Type: {document.document_type}")
        print(f"Filing Date: {document.filing_date}")
    else:
        print("Document not found")

    print("\nExpired Licenses:")
    expired_licenses = manager.list_expired_licenses()
    for license in expired_licenses:
        print(f"License Number: {license.license_number}")
        print(f"Business Name: {license.business_name}")
        print(f"Expiration Date: {license.expiration_date}")


if __name__ == "__main__":
    main()
```
