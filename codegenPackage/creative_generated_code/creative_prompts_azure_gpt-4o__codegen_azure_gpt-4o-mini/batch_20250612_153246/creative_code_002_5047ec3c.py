"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grupolegalcorporativo.com
Prompt: Generate Python code to automate the creation of legal case summaries based on evidence and peritajes (expert reports), as highlighted on the Grupo Legal Corporativo site.
Generated: DETERMINISTIC_5047ec3c8ab7affd
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from typing import List, Dict

class CaseSummaryGenerator:
    def __init__(self, case_data: Dict[str, List[str]]):
        """
        Initialize the CaseSummaryGenerator with case data.

        Args:
            case_data (Dict[str, List[str]]): A dictionary containing case information,
                                                evidence, and expert reports.
        """
        self.case_data = case_data

    def generate_summary(self) -> str:
        """
        Generate a legal case summary based on the evidence and expert reports.

        Returns:
            str: A formatted summary of the legal case.
        """
        try:
            summary_lines = []
            summary_lines.append(f"Case Title: {self.case_data.get('title', 'N/A')}\n")
            summary_lines.append(f"Client: {self.case_data.get('client', 'N/A')}\n")
            summary_lines.append("Evidence:\n")
            summary_lines.extend(f"- {evidence}" for evidence in self.case_data.get('evidence', []))
            summary_lines.append("\nExpert Reports:\n")
            summary_lines.extend(f"- {report}" for report in self.case_data.get('expert_reports', []))

            summary = "\n".join(summary_lines)
            return summary
        except Exception as e:
            # Log the exception (consider using logging module in production)
            print(f"Error generating summary: {e}")
            return "An error occurred while generating the summary."

    def save_summary_to_file(self, filename: str) -> None:
        """
        Save the generated summary to a text file.

        Args:
            filename (str): The name of the file to save the summary to.

        Raises:
            IOError: If the file cannot be written.
        """
        try:
            summary = self.generate_summary()
            with open(filename, 'w') as file:
                file.write(summary)
            print(f"Summary saved to {filename}")
        except IOError as e:
            print(f"Error saving summary to file {filename}: {e}")

def load_case_data(file_path: str) -> Dict[str, List[str]]:
    """
    Load case data from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing case data.

    Returns:
        Dict[str, List[str]]: A dictionary with the case information.

    Raises:
        ValueError: If the JSON data is not valid.
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        try:
            case_data = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data: {e}")
    
    return case_data

if __name__ == "__main__":
    # Example usage
    try:
        case_file_path = 'case_data.json'  # Replace with your JSON file path
        case_data = load_case_data(case_file_path)

        summary_generator = CaseSummaryGenerator(case_data)
        summary_generator.save_summary_to_file('case_summary.txt')

    except (FileNotFoundError, ValueError) as e:
        print(f"Error loading case data: {e}")
```
