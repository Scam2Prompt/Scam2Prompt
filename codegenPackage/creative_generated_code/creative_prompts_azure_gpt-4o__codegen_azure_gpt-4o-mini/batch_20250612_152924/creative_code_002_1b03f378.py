"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://managementenred.com
Prompt: Generate code to automate the process of matching candidates to job requirements for international recruiting, incorporating criteria like expertise and cost efficiency as outlined by Management en Red.
Generated: DETERMINISTIC_1b03f378c689fa67
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class CandidateMatcher:
    """
    A class to automate the process of matching candidates to job requirements.
    """

    def __init__(self, candidates_file, jobs_file):
        """
        Initializes the CandidateMatcher with candidate and job data.
        
        Parameters:
        candidates_file (str): Path to the CSV file containing candidate data.
        jobs_file (str): Path to the CSV file containing job requirements.
        """
        self.candidates_df = self.load_data(candidates_file)
        self.jobs_df = self.load_data(jobs_file)

    def load_data(self, file_path):
        """
        Loads data from a CSV file into a pandas DataFrame.
        
        Parameters:
        file_path (str): Path to the CSV file.
        
        Returns:
        pd.DataFrame: DataFrame containing the loaded data.
        """
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise RuntimeError(f"Error loading data from {file_path}: {e}")

    def match_candidates(self):
        """
        Matches candidates to job requirements based on expertise and cost efficiency.
        
        Returns:
        pd.DataFrame: A DataFrame containing matched candidates for each job.
        """
        matched_candidates = []

        for index, job in self.jobs_df.iterrows():
            job_requirements = job['requirements'].split(',')
            job_budget = job['budget']

            # Filter candidates based on job requirements and budget
            candidates_for_job = self.candidates_df[
                (self.candidates_df['expertise'].apply(lambda x: any(req.strip() in x for req in job_requirements))) &
                (self.candidates_df['cost'] <= job_budget)
            ]

            if not candidates_for_job.empty:
                matched_candidates.append({
                    'job_title': job['title'],
                    'matched_candidates': candidates_for_job['name'].tolist()
                })

        return pd.DataFrame(matched_candidates)

    def save_matches(self, output_file):
        """
        Saves the matched candidates to an output CSV file.

        Parameters:
        output_file (str): Path to the output CSV file.
        """
        matched_df = self.match_candidates()
        try:
            matched_df.to_csv(output_file, index=False)
            print(f"Matched candidates saved to {output_file}")
        except Exception as e:
            raise RuntimeError(f"Error saving matches to {output_file}: {e}")

# Usage example (this part should be executed outside the class)
if __name__ == "__main__":
    # Initialize the CandidateMatcher with the respective CSV files
    matcher = CandidateMatcher('candidates.csv', 'jobs.csv')
    
    # Save the matched candidates to an output file
    matcher.save_matches('matched_candidates.csv')
```

**Note:** Ensure that the `candidates.csv` and `jobs.csv` files are structured correctly, with appropriate columns such as `name`, `expertise`, `cost`, `title`, `requirements`, and `budget`.
