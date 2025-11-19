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
import pandas as pd
import os

class CandidateProcessor:
    """
    A class to process candidate information from selection documents.
    """

    def __init__(self, approved_file: str, results_file: str):
        """
        Initializes the CandidateProcessor with file paths for approved candidates and results.

        :param approved_file: Path to the file containing approved candidates.
        :param results_file: Path to the file containing final results.
        """
        self.approved_file = approved_file
        self.results_file = results_file
        self.approved_candidates = pd.DataFrame()
        self.final_results = pd.DataFrame()

    def load_data(self):
        """
        Loads data from the provided files into DataFrames.
        """
        try:
            self.approved_candidates = pd.read_csv(self.approved_file)
            self.final_results = pd.read_csv(self.results_file)
            print("Data loaded successfully.")
        except FileNotFoundError as e:
            print(f"Error: {e}. Please check the file paths.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: One of the files is empty.")
            raise
        except pd.errors.ParserError:
            print("Error: Could not parse the data. Please check the file format.")
            raise

    def extract_approved_candidates(self):
        """
        Extracts and returns a list of approved candidates.
        
        :return: List of approved candidates.
        """
        try:
            approved_list = self.approved_candidates['Candidate Name'].tolist()
            return approved_list
        except KeyError:
            print("Error: 'Candidate Name' column not found in approved candidates data.")
            raise

    def extract_final_results(self):
        """
        Extracts and returns a DataFrame of final results.
        
        :return: DataFrame containing final results.
        """
        try:
            return self.final_results[['Candidate Name', 'Result']]
        except KeyError as e:
            print(f"Error: Column {e} not found in final results data.")
            raise

    def process_candidates(self):
        """
        Main method to process candidates and print results.
        """
        self.load_data()
        approved_candidates = self.extract_approved_candidates()
        final_results = self.extract_final_results()

        print("Approved Candidates:")
        print(approved_candidates)
        print("\nFinal Results:")
        print(final_results)

if __name__ == "__main__":
    # Define file paths (update these paths as necessary)
    approved_candidates_file = os.path.join("data", "approved_candidates.csv")
    final_results_file = os.path.join("data", "final_results.csv")

    # Create an instance of CandidateProcessor
    processor = CandidateProcessor(approved_candidates_file, final_results_file)

    # Process the candidates
    processor.process_candidates()
```

Make sure to replace the file paths in the `if __name__ == "__main__":` block with the actual paths to your CSV files. The code assumes that the CSV files have a column named "Candidate Name" in the approved candidates file and columns "Candidate Name" and "Result" in the final results file.
