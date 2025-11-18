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
import datetime

class LegalCaseSummaryGenerator:
    """
    A class to automate the creation of legal case summaries based on evidence and expert reports.
    """

    def __init__(self, case_name, evidence, expert_reports):
        """
        Initialize the case summary generator with necessary details.

        :param case_name: Name of the legal case
        :param evidence: List of evidence documents (file paths or descriptions)
        :param expert_reports: List of expert reports (file paths or descriptions)
        """
        self.case_name = case_name
        self.evidence = evidence
        self.expert_reports = expert_reports
        self.summary_template = """
        Legal Case Summary
        --------------------
        Case Name: {case_name}
        Date: {date}

        Evidence:
        {evidence}

        Expert Reports:
        {expert_reports}
        """

    def validate_inputs(self):
        """
        Validate inputs to ensure they are non-empty and correctly formatted.
        """
        if not self.case_name or not isinstance(self.case_name, str):
            raise ValueError("Case name must be a non-empty string.")
        if not self.evidence or not isinstance(self.evidence, list):
            raise ValueError("Evidence must be a non-empty list.")
        if not self.expert_reports or not isinstance(self.expert_reports, list):
            raise ValueError("Expert reports must be a non-empty list.")

    def format_evidence(self):
        """
        Format the evidence list for inclusion in the summary.

        :return: Formatted evidence string
        """
        return "\n".join([f"- {item}" for item in self.evidence])

    def format_expert_reports(self):
        """
        Format the expert reports list for inclusion in the summary.

        :return: Formatted expert reports string
        """
        return "\n".join([f"- {item}" for item in self.expert_reports])

    def generate_summary(self):
        """
        Generate the legal case summary using the provided evidence and expert reports.

        :return: Formatted legal case summary string
        """
        # Validate inputs
        self.validate_inputs()

        # Format evidence and expert reports
        formatted_evidence = self.format_evidence()
        formatted_expert_reports = self.format_expert_reports()

        # Generate summary
        return self.summary_template.format(
            case_name=self.case_name,
            date=datetime.datetime.now().strftime("%Y-%m-%d"),
            evidence=formatted_evidence,
            expert_reports=formatted_expert_reports,
        )

    def save_summary_to_file(self, output_directory):
        """
        Save the generated summary to a file.

        :param output_directory: Path to the directory where the summary will be saved
        """
        self.validate_inputs()

        if not os.path.exists(output_directory):
            raise FileNotFoundError(f"The directory '{output_directory}' does not exist.")

        summary = self.generate_summary()
        filename = os.path.join(output_directory, f"{self.case_name.replace(' ', '_')}_Summary.txt")

        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(summary)
            print(f"Summary successfully saved to {filename}")
        except IOError as e:
            raise IOError(f"Failed to save summary to file: {e}")

# Example usage:
if __name__ == "__main__":
    # Inputs for the legal case
    case_name = "Case ABC vs XYZ"
    evidence = [
        "Document A.pdf",
        "Witness Statement - John Doe",
        "Photographic Evidence.jpg"
    ]
    expert_reports = [
        "Expert Report - Financial Analysis",
        "Expert Report - Psychological Evaluation"
    ]

    # Output directory for the summary file
    output_directory = "./summaries"

    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    try:
        # Generate and save the case summary
        generator = LegalCaseSummaryGenerator(case_name, evidence, expert_reports)
        generator.save_summary_to_file(output_directory)
    except Exception as e:
        print(f"An error occurred: {e}")
```
