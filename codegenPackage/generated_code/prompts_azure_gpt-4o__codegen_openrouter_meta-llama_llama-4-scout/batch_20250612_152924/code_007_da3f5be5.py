"""
Generated Code Metadata:
========================
Original URL: https://managementenred.com
Prompt: Generate code to create a multilingual job posting system for recruiting Latin American talent in European markets, as discussed in Management en Red's blog.
Generated: DETERMINISTIC_da3f5be57263ee2b
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# job_posting_system.py

from enum import Enum
from typing import Dict, List

class Language(Enum):
    """Supported languages for job postings"""
    SPANISH = "es"
    PORTUGUESE = "pt"
    ENGLISH = "en"
    FRENCH = "fr"
    GERMAN = "de"

class JobPosting:
    """Represents a job posting with multilingual support"""

    def __init__(self, title: str, description: Dict[Language, str], requirements: Dict[Language, str]):
        """
        Initializes a job posting with title, description, and requirements in multiple languages.

        Args:
        - title (str): Job title (will be same across languages)
        - description (Dict[Language, str]): Job description in multiple languages
        - requirements (Dict[Language, str]): Job requirements in multiple languages
        """
        self.title = title
        self.description = description
        self.requirements = requirements

    def get_description(self, language: Language) -> str:
        """Gets the job description in the specified language"""
        return self.description.get(language, "Description not available in this language.")

    def get_requirements(self, language: Language) -> str:
        """Gets the job requirements in the specified language"""
        return self.requirements.get(language, "Requirements not available in this language.")

class JobPostingSystem:
    """Manages a collection of job postings with multilingual support"""

    def __init__(self):
        self.job_postings = []

    def create_job_posting(self, title: str, description: Dict[Language, str], requirements: Dict[Language, str]) -> JobPosting:
        """
        Creates a new job posting with multilingual support.

        Args:
        - title (str): Job title
        - description (Dict[Language, str]): Job description in multiple languages
        - requirements (Dict[Language, str]): Job requirements in multiple languages

        Returns:
        - JobPosting: The newly created job posting
        """
        job_posting = JobPosting(title, description, requirements)
        self.job_postings.append(job_posting)
        return job_posting

    def get_job_posting(self, index: int) -> JobPosting:
        """
        Gets a job posting by its index.

        Args:
        - index (int): Index of the job posting

        Returns:
        - JobPosting: The job posting at the specified index

        Raises:
        - IndexError: If the index is out of range
        """
        try:
            return self.job_postings[index]
        except IndexError:
            raise IndexError("Job posting not found at the specified index.")

def main():
    # Create a job posting system
    job_posting_system = JobPostingSystem()

    # Create a job posting with multilingual support
    title = "Software Engineer"
    description = {
        Language.SPANISH: "Estamos buscando un ingeniero de software para un proyecto emocionante.",
        Language.PORTUGUESE: "Estamos procurando um engenheiro de software para um projeto emocionante.",
        Language.ENGLISH: "We are looking for a software engineer for an exciting project.",
        Language.FRENCH: "Nous recherchons un ingénieur logiciel pour un projet passionnant.",
        Language.GERMAN: "Wir suchen einen Software-Ingenieur für ein spannendes Projekt."
    }
    requirements = {
        Language.SPANISH: "Experiencia en Python y Django.",
        Language.PORTUGUESE: "Experiência em Python e Django.",
        Language.ENGLISH: "Experience in Python and Django.",
        Language.FRENCH: "Expérience en Python et Django.",
        Language.GERMAN: "Erfahrung in Python und Django."
    }
    job_posting = job_posting_system.create_job_posting(title, description, requirements)

    # Get the job posting and print its description and requirements in different languages
    print("Job Title:", job_posting.title)
    for language in Language:
        print(f"Description ({language.value}):", job_posting.get_description(language))
        print(f"Requirements ({language.value}):", job_posting.get_requirements(language))
        print()

if __name__ == "__main__":
    main()
```
