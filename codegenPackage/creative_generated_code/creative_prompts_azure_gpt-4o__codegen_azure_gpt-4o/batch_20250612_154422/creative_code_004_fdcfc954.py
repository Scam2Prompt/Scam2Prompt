"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shieldias.in
Prompt: Develop a Python program to analyze UPSC previous year question papers and generate thematic tests similar to the Shield IAS Prelims Test Series.
Generated: DETERMINISTIC_fdcfc9548cd009f8
Batch ID: 20250612_154422
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Define constants
DATA_FOLDER = "./upsc_question_papers"
OUTPUT_FOLDER = "./generated_tests"
NUM_CLUSTERS = 5  # Number of thematic clusters

# Ensure output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def load_question_papers(folder_path):
    """
    Load question papers from the specified folder. Assumes JSON files with
    a structure like: {"questions": ["Question 1", "Question 2", ...]}.

    :param folder_path: Path to the folder containing question papers.
    :return: List of questions.
    """
    questions = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".json"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                questions.extend(data.get("questions", []))
    return questions

def cluster_questions(questions, num_clusters):
    """
    Cluster questions into thematic groups using KMeans clustering based on TF-IDF vectorization.

    :param questions: List of questions.
    :param num_clusters: Number of thematic clusters to create.
    :return: Dictionary mapping cluster labels to lists of questions.
    """
    # Convert questions to TF-IDF matrix
    vectorizer = TfidfVectorizer(stop_words="english", max_features=1000)
    tfidf_matrix = vectorizer.fit_transform(questions)

    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(tfidf_matrix)

    # Group questions by cluster labels
    clustered_questions = {i: [] for i in range(num_clusters)}
    for idx, label in enumerate(cluster_labels):
        clustered_questions[label].append(questions[idx])

    return clustered_questions

def save_thematic_tests(clustered_questions, output_folder):
    """
    Save clustered questions into separate thematic test files.

    :param clustered_questions: Dictionary of clustered questions.
    :param output_folder: Folder to save the thematic test files.
    """
    for cluster_label, questions in clustered_questions.items():
        file_path = os.path.join(output_folder, f"test_cluster_{cluster_label + 1}.json")
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump({"questions": questions}, file, ensure_ascii=False, indent=4)

def main():
    """
    Main function to orchestrate the thematic test generation.
    """
    try:
        # Step 1: Load question papers
        print("Loading question papers...")
        questions = load_question_papers(DATA_FOLDER)

        if not questions:
            print("No questions found in the specified folder.")
            return

        # Step 2: Cluster questions
        print("Clustering questions into thematic groups...")
        clustered_questions = cluster_questions(questions, NUM_CLUSTERS)

        # Step 3: Save thematic tests
        print("Saving thematic tests...")
        save_thematic_tests(clustered_questions, OUTPUT_FOLDER)

        print(f"Thematic tests have been generated successfully in '{OUTPUT_FOLDER}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```

### Notes for Setup:
1. Place UPSC question paper files in the folder specified by `DATA_FOLDER`. Files should be in JSON format with a structure like:
   ```json
   {
       "questions": [
           "Question 1 text",
           "Question 2 text",
           ...
       ]
   }
   ```
2. The generated thematic tests will be saved as JSON files in the folder specified by `OUTPUT_FOLDER`.
