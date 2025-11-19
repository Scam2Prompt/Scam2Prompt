"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Write Python code to process and extract information from the list of candidates and results provided in the IGEOG selection process documents, such as "Listagem de inscrições deferidas e indeferidas" and "Resultado Final."
Generated: DETERMINISTIC_b7d5c8d52802e2b6
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from dataclasses import dataclass
from enum import Enum
from typing import List

class CandidateStatus(str, Enum):
    APPROVED = "approved"
    REJECTED = "rejected"

@dataclass
class Candidate:
    name: str
    status: CandidateStatus

def extract_candidates_from_deferred_list(document: str) -> List[Candidate]:
    """
    Extracts candidate information from the list of deferred and undeferred registrations.

    Args:
    document (str): The content of the "Listagem de inscrições deferidas e indeferidas" document.

    Returns:
    List[Candidate]: A list of Candidate objects.
    """
    # Assuming the document is a string containing names separated by new lines
    lines = document.splitlines()
    candidates = []

    for line in lines:
        # Use regular expression to match names (adjust the pattern according to the actual document format)
        match = re.match(r"^(.*)\s*(Deferida|Indeferida)$", line)
        if match:
            name = match.group(1).strip()
            status = CandidateStatus.APPROVED if match.group(2) == "Deferida" else CandidateStatus.REJECTED
            candidates.append(Candidate(name, status))

    return candidates

def extract_final_results(document: str) -> List[Candidate]:
    """
    Extracts candidate information from the final results document.

    Args:
    document (str): The content of the "Resultado Final" document.

    Returns:
    List[Candidate]: A list of Candidate objects.
    """
    # Assuming the document is a string containing names and results separated by commas or new lines
    lines = document.splitlines()
    candidates = []

    for line in lines:
        # Use regular expression to match names and results (adjust the pattern according to the actual document format)
        match = re.match(r"^(.*)\s*:(.*)$", line)
        if match:
            name = match.group(1).strip()
            result = match.group(2).strip()
            status = CandidateStatus.APPROVED if "Aprovado" in result else CandidateStatus.REJECTED
            candidates.append(Candidate(name, status))

    return candidates

def main():
    try:
        # Example usage
        deferred_list_document = """John Doe Deferida
Jane Doe Indeferida
Bob Smith Deferida"""

        final_results_document = """John Doe: Aprovado
Jane Doe: Reprovado
Bob Smith: Aprovado"""

        deferred_candidates = extract_candidates_from_deferred_list(deferred_list_document)
        final_results = extract_final_results(final_results_document)

        print("Deferred Candidates:")
        for candidate in deferred_candidates:
            print(f"Name: {candidate.name}, Status: {candidate.status.value}")

        print("\nFinal Results:")
        for candidate in final_results:
            print(f"Name: {candidate.name}, Status: {candidate.status.value}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
