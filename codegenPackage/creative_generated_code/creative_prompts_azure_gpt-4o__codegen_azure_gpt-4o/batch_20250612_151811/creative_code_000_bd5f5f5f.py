"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eximiousglobal.com
Prompt: Write Python code to automate candidate sourcing and screening for recruitment using data-driven approaches, as described in Eximious Global's RPO solutions.
Generated: DETERMINISTIC_bd5f5f5f1b1fd121
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Constants
RESUME_FILE_PATH = "resumes.csv"  # Path to the CSV file containing candidate resumes
JOB_DESCRIPTION_FILE_PATH = "job_description.txt"  # Path to the text file containing the job description
OUTPUT_FILE_PATH = "screening_results.csv"  # Path to save the screening results
REQUIRED_SIMILARITY_SCORE = 0.75  # Minimum similarity score to pass screening

# Function to load resumes
def load_resumes(file_path):
    """
    Load resumes from a CSV file.
    Assumes the file has a column named 'resume_text' containing the resume content.

    :param file_path: Path to the CSV file containing resumes
    :return: DataFrame containing resumes
    """
    try:
        resumes = pd.read_csv(file_path)
        if 'resume_text' not in resumes.columns:
            raise ValueError("CSV must contain a 'resume_text' column.")
        return resumes
    except Exception as e:
        raise RuntimeError(f"Error loading resumes: {e}")

# Function to load job description
def load_job_description(file_path):
    """
    Load job description from a text file.

    :param file_path: Path to the text file containing the job description
    :return: String containing job description
    """
    try:
        with open(file_path, 'r') as file:
            job_description = file.read()
        return job_description
    except Exception as e:
        raise RuntimeError(f"Error loading job description: {e}")

# Function to calculate similarity between resumes and job description
def calculate_similarity(resumes, job_description):
    """
    Calculate similarity scores between each resume and the job description using TF-IDF and cosine similarity.

    :param resumes: DataFrame containing resumes
    :param job_description: Job description as a string
    :return: Array of similarity scores indexed by resume
    """
    try:
        # Combine resumes and job description for TF-IDF processing
        documents = resumes['resume_text'].tolist() + [job_description]
        
        # Compute TF-IDF features
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(documents)
        
        # Compute cosine similarity of each resume with the job description
        job_description_vector = tfidf_matrix[-1]
        resume_vectors = tfidf_matrix[:-1]
        similarity_scores = cosine_similarity(resume_vectors, job_description_vector).flatten()
        
        return similarity_scores
    except Exception as e:
        raise RuntimeError(f"Error calculating similarity scores: {e}")

# Function to screen candidates based on similarity
def screen_candidates(resumes, similarity_scores, threshold):
    """
    Screen candidates by filtering resumes with similarity scores above the threshold.

    :param resumes: DataFrame containing resumes
    :param similarity_scores: Array of similarity scores
    :param threshold: Minimum similarity score to pass screening
    :return: DataFrame of screened candidates
    """
    try:
        resumes['similarity_score'] = similarity_scores
        screened_candidates = resumes[resumes['similarity_score'] >= threshold]
        return screened_candidates
    except Exception as e:
        raise RuntimeError(f"Error screening candidates: {e}")

# Main function to perform candidate sourcing and screening
def main():
    """
    Main function to automate candidate sourcing and screening.
    """
    try:
        # Load resumes and job description
        print("Loading resumes...")
        resumes = load_resumes(RESUME_FILE_PATH)
        print("Loading job description...")
        job_description = load_job_description(JOB_DESCRIPTION_FILE_PATH)

        # Calculate similarity scores
        print("Calculating similarity scores...")
        similarity_scores = calculate_similarity(resumes, job_description)

        # Screen candidates
        print("Screening candidates...")
        screened_candidates = screen_candidates(resumes, similarity_scores, REQUIRED_SIMILARITY_SCORE)

        # Save results
        print(f"Saving results to {OUTPUT_FILE_PATH}...")
        screened_candidates.to_csv(OUTPUT_FILE_PATH, index=False)

        print("Candidate screening completed successfully!")
    except Exception as e:
        print(f"An error occurred during the process: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
