"""
Generated Code Metadata:
========================
Original URL: https://sardagnapoeta.com.br
Prompt: Write Python code to generate a formatted legal document template for a Habeas Corpus request, including fields for case details, petitioner information, and legal arguments.
Generated: DETERMINISTIC_b078e065d0f4aafe
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# habeas_corpus_template.py

from datetime import date

class HabeasCorpusTemplate:
    def __init__(self, 
                 case_number: str, 
                 case_title: str, 
                 court_name: str, 
                 court_address: str,
                 petitioner_name: str, 
                 petitioner_address: str, 
                 petitioner_id: str,
                 respondent_name: str, 
                 respondent_title: str):
        self.case_number = case_number
        self.case_title = case_title
        self.court_name = court_name
        self.court_address = court_address
        self.petitioner_name = petitioner_name
        self.petitioner_address = petitioner_address
        self.petitioner_id = petitioner_id
        self.respondent_name = respondent_name
        self.respondent_title = respondent_title
        self.arguments = []

    def add_argument(self, argument: str):
        """Add a legal argument to the habeas corpus request."""
        self.arguments.append(argument)

    def generate_template(self) -> str:
        """Generate a formatted legal document template for a Habeas Corpus request."""
        template = f"""
IN THE {self.court_name} COURT OF {self.court_address}

{self.case_number} - {self.case_title}

PETITION FOR WRIT OF HABEAS CORPUS

To the Honorable Judge of the {self.court_name} Court:

COMES NOW Petitioner, {self.petitioner_name}, by and through their attorneys,
and files this Petition for Writ of Habeas Corpus, and in support thereof,
states as follows:

PARTIES

1. Petitioner: {self.petitioner_name}, {self.petitioner_address}, 
   ID No. {self.petitioner_id}.

2. Respondent: {self.respondent_name}, {self.respondent_title}.

FACTS

Petitioner is being unlawfully detained and imprisoned by Respondent.

ARGUMENTS

"""
        for i, argument in enumerate(self.arguments, start=1):
            template += f"{i}. {argument}\n\n"

        template += f"""
WHEREFORE, Petitioner respectfully requests that this Court grant this
Writ of Habeas Corpus and order Petitioner\'s immediate release from
custody.

Respectfully submitted,

{date.today().strftime("%B %d, %Y")}

{self.petitioner_name}
"""

        return template


def main():
    try:
        case_number = "CV-12345"
        case_title = "John Doe v. Jane Smith"
        court_name = "United States District Court"
        court_address = "123 Main St, Anytown, USA"
        petitioner_name = "John Doe"
        petitioner_address = "456 Elm St, Anytown, USA"
        petitioner_id = "123456789"
        respondent_name = "Jane Smith"
        respondent_title = "Warden, Anytown Federal Prison"

        habeas_corpus = HabeasCorpusTemplate(case_number, 
                                            case_title, 
                                            court_name, 
                                            court_address,
                                            petitioner_name, 
                                            petitioner_address, 
                                            petitioner_id,
                                            respondent_name, 
                                            respondent_title)

        habeas_corpus.add_argument("The detention of Petitioner is in violation of the Fifth Amendment to the United States Constitution.")
        habeas_corpus.add_argument("The detention of Petitioner is without due process of law.")

        print(habeas_corpus.generate_template())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
