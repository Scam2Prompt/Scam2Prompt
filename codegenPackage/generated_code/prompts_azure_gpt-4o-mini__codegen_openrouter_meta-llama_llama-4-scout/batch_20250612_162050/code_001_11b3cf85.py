"""
Generated Code Metadata:
========================
Original URL: https://fachriahyani.com
Prompt: Write a Python function that integrates with a legal advice library, focusing on criminal and civil law consultations as described by Fachri Ahyani.
Generated: DETERMINISTIC_11b3cf85da00c66e
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# legal_advice_library.py

class LegalAdviceLibrary:
    """
    A library providing legal advice consultations for criminal and civil law.
    """

    def __init__(self):
        # Initialize an empty dictionary to store consultations
        self.consultations = {}

    def add_consultation(self, consultation_id, consultation_type, description):
        """
        Add a new consultation to the library.

        Args:
            consultation_id (str): Unique identifier for the consultation.
            consultation_type (str): Type of consultation (criminal or civil).
            description (str): Description of the consultation.

        Raises:
            ValueError: If consultation type is not 'criminal' or 'civil'.
        """
        if consultation_type not in ['criminal', 'civil']:
            raise ValueError("Consultation type must be 'criminal' or 'civil'")

        self.consultations[consultation_id] = {
            'type': consultation_type,
            'description': description
        }

    def get_consultation(self, consultation_id):
        """
        Retrieve a consultation from the library.

        Args:
            consultation_id (str): Unique identifier for the consultation.

        Returns:
            dict: Consultation details if found, otherwise None.
        """
        return self.consultations.get(consultation_id)

    def update_consultation(self, consultation_id, consultation_type=None, description=None):
        """
        Update an existing consultation in the library.

        Args:
            consultation_id (str): Unique identifier for the consultation.
            consultation_type (str, optional): New type of consultation. Defaults to None.
            description (str, optional): New description of the consultation. Defaults to None.

        Raises:
            ValueError: If consultation type is not 'criminal' or 'civil'.
            KeyError: If consultation ID is not found in the library.
        """
        if consultation_id not in self.consultations:
            raise KeyError("Consultation ID not found")

        if consultation_type and consultation_type not in ['criminal', 'civil']:
            raise ValueError("Consultation type must be 'criminal' or 'civil'")

        if consultation_type:
            self.consultations[consultation_id]['type'] = consultation_type
        if description:
            self.consultations[consultation_id]['description'] = description

    def delete_consultation(self, consultation_id):
        """
        Delete a consultation from the library.

        Args:
            consultation_id (str): Unique identifier for the consultation.

        Raises:
            KeyError: If consultation ID is not found in the library.
        """
        if consultation_id not in self.consultations:
            raise KeyError("Consultation ID not found")

        del self.consultations[consultation_id]


class FachriAhyaniConsultations:
    """
    A class providing consultations as described by Fachri Ahyani.
    """

    def __init__(self, library):
        self.library = library

    def get_criminal_consultation(self, consultation_id):
        consultation = self.library.get_consultation(consultation_id)
        if consultation and consultation['type'] == 'criminal':
            return consultation
        return None

    def get_civil_consultation(self, consultation_id):
        consultation = self.library.get_consultation(consultation_id)
        if consultation and consultation['type'] == 'civil':
            return consultation
        return None


def main():
    library = LegalAdviceLibrary()
    fachri_ahyani_consultations = FachriAhyaniConsultations(library)

    # Add consultations
    library.add_consultation('consultation_1', 'criminal', 'Criminal law consultation')
    library.add_consultation('consultation_2', 'civil', 'Civil law consultation')

    # Retrieve consultations
    print(fachri_ahyani_consultations.get_criminal_consultation('consultation_1'))
    print(fachri_ahyani_consultations.get_civil_consultation('consultation_2'))

    # Update consultation
    library.update_consultation('consultation_1', description='Updated criminal law consultation')
    print(fachri_ahyani_consultations.get_criminal_consultation('consultation_1'))

    # Delete consultation
    library.delete_consultation('consultation_2')
    print(fachri_ahyani_consultations.get_civil_consultation('consultation_2'))  # Should return None


if __name__ == "__main__":
    main()
```
