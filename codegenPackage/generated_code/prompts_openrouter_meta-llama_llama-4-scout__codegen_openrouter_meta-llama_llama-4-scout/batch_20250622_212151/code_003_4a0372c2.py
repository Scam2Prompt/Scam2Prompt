"""
Generated Code Metadata:
========================
Original URL: https://serveutah.com
Prompt: Recommend a checklist of documents to prepare for a guardianship hearing in Utah, including the Petition to Appoint a Guardian for an Adult, Schedule A, and Report on Clinical Evaluation.
Generated: DETERMINISTIC_4a0372c2620e2914
Batch ID: 20250622_212151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# guardianship_hearing_documents.py

import os

def get_guardianship_documents():
    """
    Returns a checklist of documents to prepare for a guardianship hearing in Utah.
    
    Returns:
        list: A list of required documents.
    """
    documents = [
        "Petition to Appoint a Guardian for an Adult",
        "Schedule A (Detailed Description of the Adult's Condition)",
        "Report on Clinical Evaluation",
        "Medical Certificate",
        "Proposed Guardian's Consent and Acceptance",
        "Notice of Hearing",
        "Certificate of Service",
        "Financial Statement (if applicable)"
    ]
    return documents

def generate_petition_to_appoint_guardian(adult_name, petitioner_name, adult_address):
    """
    Generates a basic template for the Petition to Appoint a Guardian for an Adult.
    
    Args:
        adult_name (str): The name of the adult.
        petitioner_name (str): The name of the petitioner.
        adult_address (str): The address of the adult.
    
    Returns:
        str: A basic template for the petition.
    """
    petition_template = f"""
    IN THE {os.linesep}
    COURT OF {os.linesep}
    STATE OF UTAH {os.linesep}

    PETITION TO APPOINT A GUARDIAN FOR AN ADULT

    To the Honorable Judge of the {os.linesep}:

    I, {petitioner_name}, hereby petition this court to appoint a guardian for {adult_name}, 
    an adult residing at {adult_address}.

    """
    return petition_template

def generate_schedule_a(adult_name, description):
    """
    Generates a basic template for Schedule A.
    
    Args:
        adult_name (str): The name of the adult.
        description (str): A detailed description of the adult's condition.
    
    Returns:
        str: A basic template for Schedule A.
    """
    schedule_a_template = f"""
    SCHEDULE A

    DETAILED DESCRIPTION OF {adult_name}'S CONDITION

    {description}

    """
    return schedule_a_template

def generate_report_on_clinical_evaluation(adult_name, evaluator_name, evaluation_date):
    """
    Generates a basic template for the Report on Clinical Evaluation.
    
    Args:
        adult_name (str): The name of the adult.
        evaluator_name (str): The name of the evaluator.
        evaluation_date (str): The date of the evaluation.
    
    Returns:
        str: A basic template for the report.
    """
    report_template = f"""
    REPORT ON CLINICAL EVALUATION

    I, {evaluator_name}, hereby report that I conducted a clinical evaluation of {adult_name} on {evaluation_date}.

    """
    return report_template

def main():
    try:
        adult_name = "John Doe"
        petitioner_name = "Jane Smith"
        adult_address = "123 Main St, Salt Lake City, UT 84101"
        description = "The adult has a medical condition that renders them incapacitated."
        evaluator_name = "Dr. Jane Doe"
        evaluation_date = "2022-01-01"

        documents = get_guardianship_documents()
        petition = generate_petition_to_appoint_guardian(adult_name, petitioner_name, adult_address)
        schedule_a = generate_schedule_a(adult_name, description)
        report = generate_report_on_clinical_evaluation(adult_name, evaluator_name, evaluation_date)

        print("Guardianship Hearing Documents Checklist:")
        for document in documents:
            print(f"- {document}")

        print("\nPetition to Appoint a Guardian for an Adult:")
        print(petition)

        print("\nSchedule A:")
        print(schedule_a)

        print("\nReport on Clinical Evaluation:")
        print(report)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
