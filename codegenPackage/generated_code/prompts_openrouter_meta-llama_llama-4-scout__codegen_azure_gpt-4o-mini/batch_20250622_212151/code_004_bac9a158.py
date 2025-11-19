"""
Generated Code Metadata:
========================
Original URL: https://serveutah.com
Prompt: How do I obtain a Letter of Full Guardianship or Letter of Limited Guardianship in Utah, and what are the necessary steps to complete the guardianship process?
Generated: DETERMINISTIC_bac9a1582bca06bc
Batch ID: 20250622_212151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GuardianshipProcess:
    """
    A class to represent the process of obtaining a Letter of Full or Limited Guardianship in Utah.
    """

    def __init__(self, guardian_name, ward_name, is_full_guardianship):
        """
        Initializes the GuardianshipProcess with the guardian's name, ward's name, and type of guardianship.

        :param guardian_name: str - Name of the guardian
        :param ward_name: str - Name of the ward
        :param is_full_guardianship: bool - True for Full Guardianship, False for Limited Guardianship
        """
        self.guardian_name = guardian_name
        self.ward_name = ward_name
        self.is_full_guardianship = is_full_guardianship

    def gather_documents(self):
        """
        Gathers the necessary documents for the guardianship process.

        :return: list - A list of required documents
        """
        documents = [
            "Petition for Guardianship",
            "Notice of Hearing",
            "Consent of the Ward (if applicable)",
            "Background check results",
            "Financial disclosure statement"
        ]
        if self.is_full_guardianship:
            documents.append("Full Guardianship Plan")
        else:
            documents.append("Limited Guardianship Plan")
        return documents

    def file_petition(self):
        """
        Simulates filing the petition for guardianship with the court.

        :raises Exception: If the filing fails
        """
        try:
            # Simulate filing process
            print(f"Filing petition for {'Full' if self.is_full_guardianship else 'Limited'} Guardianship for {self.ward_name}.")
            # Here you would include actual filing logic
            print("Petition filed successfully.")
        except Exception as e:
            raise Exception(f"Failed to file petition: {e}")

    def attend_hearing(self):
        """
        Simulates attending the court hearing for the guardianship.

        :raises Exception: If the hearing attendance fails
        """
        try:
            # Simulate hearing attendance
            print(f"Attending hearing for guardianship of {self.ward_name}.")
            # Here you would include actual hearing logic
            print("Hearing attended successfully.")
        except Exception as e:
            raise Exception(f"Failed to attend hearing: {e}")

    def obtain_guardianship_letter(self):
        """
        Simulates obtaining the Letter of Guardianship after the court's decision.

        :raises Exception: If obtaining the letter fails
        """
        try:
            # Simulate obtaining the letter
            print(f"Obtaining Letter of {'Full' if self.is_full_guardianship else 'Limited'} Guardianship for {self.ward_name}.")
            # Here you would include actual logic to obtain the letter
            print("Letter obtained successfully.")
        except Exception as e:
            raise Exception(f"Failed to obtain guardianship letter: {e}")

    def complete_guardianship_process(self):
        """
        Completes the entire guardianship process.

        :raises Exception: If any step in the process fails
        """
        try:
            documents = self.gather_documents()
            print("Gathered documents:", documents)
            self.file_petition()
            self.attend_hearing()
            self.obtain_guardianship_letter()
            print("Guardianship process completed successfully.")
        except Exception as e:
            print(f"Error during guardianship process: {e}")


# Example usage
if __name__ == "__main__":
    guardian = GuardianshipProcess("John Doe", "Jane Doe", is_full_guardianship=True)
    guardian.complete_guardianship_process()
```
