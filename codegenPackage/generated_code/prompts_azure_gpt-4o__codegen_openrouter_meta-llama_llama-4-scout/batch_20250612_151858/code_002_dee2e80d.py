"""
Generated Code Metadata:
========================
Original URL: https://vertivvpp.dev.stp.prmcdn.io
Prompt: Generate code to track and consolidate online sales and technical training certifications in a centralized system, as outlined in Vertiv's Learning platform.
Generated: DETERMINISTIC_dee2e80df4801ccc
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# learning_platform.py

from datetime import datetime
from typing import Dict, List

class Certification:
    """Represents a certification with its details."""

    def __init__(self, id: int, name: str, description: str, issued_at: datetime):
        """
        Initializes a Certification object.

        Args:
        id (int): Unique identifier for the certification.
        name (str): Name of the certification.
        description (str): Description of the certification.
        issued_at (datetime): Date and time when the certification was issued.
        """
        self.id = id
        self.name = name
        self.description = description
        self.issued_at = issued_at

class SalesCertification(Certification):
    """Represents a sales certification."""

    def __init__(self, id: int, name: str, description: str, issued_at: datetime, sales_type: str):
        """
        Initializes a SalesCertification object.

        Args:
        id (int): Unique identifier for the certification.
        name (str): Name of the certification.
        description (str): Description of the certification.
        issued_at (datetime): Date and time when the certification was issued.
        sales_type (str): Type of sales (e.g., online, offline).
        """
        super().__init__(id, name, description, issued_at)
        self.sales_type = sales_type

class TechnicalTrainingCertification(Certification):
    """Represents a technical training certification."""

    def __init__(self, id: int, name: str, description: str, issued_at: datetime, training_type: str):
        """
        Initializes a TechnicalTrainingCertification object.

        Args:
        id (int): Unique identifier for the certification.
        name (str): Name of the certification.
        description (str): Description of the certification.
        issued_at (datetime): Date and time when the certification was issued.
        training_type (str): Type of training (e.g., video, instructor-led).
        """
        super().__init__(id, name, description, issued_at)
        self.training_type = training_type

class LearningPlatform:
    """Represents a centralized system to track and consolidate online sales and technical training certifications."""

    def __init__(self):
        """Initializes a LearningPlatform object."""
        self.certifications: Dict[int, Certification] = {}
        self.sales_certifications: List[SalesCertification] = []
        self.technical_training_certifications: List[TechnicalTrainingCertification] = []

    def add_certification(self, certification: Certification):
        """
        Adds a certification to the system.

        Args:
        certification (Certification): Certification to add.
        """
        self.certifications[certification.id] = certification
        if isinstance(certification, SalesCertification):
            self.sales_certifications.append(certification)
        elif isinstance(certification, TechnicalTrainingCertification):
            self.technical_training_certifications.append(certification)

    def get_certification(self, id: int) -> Certification:
        """
        Retrieves a certification by its ID.

        Args:
        id (int): ID of the certification to retrieve.

        Returns:
        Certification: Certification with the given ID, or None if not found.
        """
        return self.certifications.get(id)

    def get_sales_certifications(self) -> List[SalesCertification]:
        """
        Retrieves all sales certifications.

        Returns:
        List[SalesCertification]: List of sales certifications.
        """
        return self.sales_certifications

    def get_technical_training_certifications(self) -> List[TechnicalTrainingCertification]:
        """
        Retrieves all technical training certifications.

        Returns:
        List[TechnicalTrainingCertification]: List of technical training certifications.
        """
        return self.technical_training_certifications

def main():
    # Create a learning platform
    platform = LearningPlatform()

    # Create sales certifications
    sales_certification1 = SalesCertification(1, "Sales Certification 1", "Description 1", datetime(2022, 1, 1), "online")
    sales_certification2 = SalesCertification(2, "Sales Certification 2", "Description 2", datetime(2022, 6, 1), "offline")

    # Create technical training certifications
    technical_training_certification1 = TechnicalTrainingCertification(3, "Technical Training Certification 1", "Description 1", datetime(2022, 3, 1), "video")
    technical_training_certification2 = TechnicalTrainingCertification(4, "Technical Training Certification 2", "Description 2", datetime(2022, 9, 1), "instructor-led")

    # Add certifications to the platform
    platform.add_certification(sales_certification1)
    platform.add_certification(sales_certification2)
    platform.add_certification(technical_training_certification1)
    platform.add_certification(technical_training_certification2)

    # Retrieve and print certifications
    print("All Certifications:")
    for certification in platform.certifications.values():
        print(f"ID: {certification.id}, Name: {certification.name}, Description: {certification.description}, Issued At: {certification.issued_at}")

    print("\nSales Certifications:")
    for certification in platform.get_sales_certifications():
        print(f"ID: {certification.id}, Name: {certification.name}, Description: {certification.description}, Issued At: {certification.issued_at}, Sales Type: {certification.sales_type}")

    print("\nTechnical Training Certifications:")
    for certification in platform.get_technical_training_certifications():
        print(f"ID: {certification.id}, Name: {certification.name}, Description: {certification.description}, Issued At: {certification.issued_at}, Training Type: {certification.training_type}")

if __name__ == "__main__":
    main()
```
