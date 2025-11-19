"""
Generated Code Metadata:
========================
Original URL: https://www.jobone.careers
Prompt: Write a job description for a Senior Expert Bauabrechnung (m/w/d) in Medizintechnik, including key responsibilities and qualifications, as per jobONE's recruitment standards.
Generated: DETERMINISTIC_d936ed83f2b0ecbe
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class JobDescription:
    def __init__(self, title, company, location):
        """
        Initialize a JobDescription object.

        Args:
            title (str): Job title
            company (str): Company name
            location (str): Job location
        """
        self.title = title
        self.company = company
        self.location = location
        self.responsibilities = []
        self.qualifications = []

    def add_responsibility(self, responsibility):
        """
        Add a key responsibility to the job description.

        Args:
            responsibility (str): Key responsibility
        """
        self.responsibilities.append(responsibility)

    def add_qualification(self, qualification):
        """
        Add a key qualification to the job description.

        Args:
            qualification (str): Key qualification
        """
        self.qualifications.append(qualification)

    def generate_job_description(self):
        """
        Generate a job description based on the provided information.

        Returns:
            str: Job description
        """
        job_description = f"# Job Title: {self.title}\n"
        job_description += f"## Company: {self.company}\n"
        job_description += f"## Location: {self.location}\n\n"

        job_description += "## Key Responsibilities:\n"
        for i, responsibility in enumerate(self.responsibilities, start=1):
            job_description += f"{i}. {responsibility}\n"

        job_description += "\n## Key Qualifications:\n"
        for i, qualification in enumerate(self.qualifications, start=1):
            job_description += f"{i}. {qualification}\n"

        return job_description


def main():
    try:
        job_title = "Senior Expert Bauabrechnung (m/w/d)"
        company = "jobONE"
        location = "Medizintechnik"

        job_description = JobDescription(job_title, company, location)

        # Key Responsibilities
        job_description.add_responsibility("Erstellung und Überprüfung von Bauabrechnungen")
        job_description.add_responsibility("Überwachung und Kontrolle von Bauprojekten")
        job_description.add_responsibility("Kooperation mit Projektmanagern und Ingenieuren")

        # Key Qualifications
        job_description.add_qualification("Erfahrung in der Bauabrechnung und Medizintechnik")
        job_description.add_qualification("Starkes technisches Verständnis und Analysefähigkeiten")
        job_description.add_qualification("Exzellente Kommunikations- und Teamfähigkeiten")

        print(job_description.generate_job_description())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
