"""
Generated Code Metadata:
========================
Original URL: https://highvaluestaffing.com
Prompt: Write a Python script that automates the job matching process, inspired by High Value Staffing's method of connecting candidates with organizations.
Generated: DETERMINISTIC_e3e8d60ad188b589
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class JobMatcher:
    def __init__(self, candidates_file, jobs_file):
        """
        Initializes the JobMatcher with candidate and job data.

        :param candidates_file: Path to the CSV file containing candidate data.
        :param jobs_file: Path to the CSV file containing job data.
        """
        self.candidates = self.load_data(candidates_file)
        self.jobs = self.load_data(jobs_file)

    def load_data(self, file_path):
        """
        Loads data from a CSV file into a DataFrame.

        :param file_path: Path to the CSV file.
        :return: DataFrame containing the loaded data.
        """
        try:
            data = pd.read_csv(file_path)
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {file_path} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError(f"The file {file_path} is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def preprocess_data(self):
        """
        Preprocesses candidate and job data to prepare for matching.
        This includes combining relevant fields into a single text field.
        """
        self.candidates['combined'] = self.candidates['skills'] + ' ' + self.candidates['experience']
        self.jobs['combined'] = self.jobs['requirements'] + ' ' + self.jobs['description']

    def match_jobs(self):
        """
        Matches candidates to jobs based on cosine similarity of their combined text fields.
        Returns a DataFrame with candidates and their matched jobs.
        """
        self.preprocess_data()
        
        # Vectorize the combined text fields
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(pd.concat([self.candidates['combined'], self.jobs['combined']]))
        
        # Calculate cosine similarity
        candidate_matrix = tfidf_matrix[:len(self.candidates)]
        job_matrix = tfidf_matrix[len(self.candidates):]
        similarity_matrix = cosine_similarity(candidate_matrix, job_matrix)

        # Create a DataFrame to hold matches
        matches = []
        for candidate_index, job_scores in enumerate(similarity_matrix):
            best_job_index = np.argmax(job_scores)
            matches.append({
                'candidate_id': self.candidates.iloc[candidate_index]['id'],
                'job_id': self.jobs.iloc[best_job_index]['id'],
                'similarity_score': job_scores[best_job_index]
            })

        return pd.DataFrame(matches)

    def save_matches(self, output_file):
        """
        Saves the matched candidates and jobs to a CSV file.

        :param output_file: Path to the output CSV file.
        """
        matches_df = self.match_jobs()
        matches_df.to_csv(output_file, index=False)
        print(f"Matches saved to {output_file}")

if __name__ == "__main__":
    # Example usage
    try:
        matcher = JobMatcher('candidates.csv', 'jobs.csv')
        matcher.save_matches('job_matches.csv')
    except Exception as e:
        print(f"An error occurred: {e}")
```
