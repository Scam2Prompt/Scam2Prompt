"""
Generated Code Metadata:
========================
Original URL: https://npors.net
Prompt: Write code to analyze case studies from the Études Newsletter and extract design insights using natural language processing techniques.
Generated: DETERMINISTIC_70e8fea4fe3426a3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def load_case_studies(file_path):
    """
    Load case studies from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: A DataFrame containing the case studies.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print("File is empty. Please check the file contents.")
        return None

def preprocess_text(text):
    """
    Preprocess the text by tokenizing, removing stop words, and lemmatizing.

    Args:
        text (str): The text to preprocess.

    Returns:
        str: The preprocessed text.
    """
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    tokens = [t for t in tokens if t.isalpha() and t not in stop_words]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return ' '.join(tokens)

def extract_design_insights(case_studies):
    """
    Extract design insights from the case studies using TF-IDF and cosine similarity.

    Args:
        case_studies (pd.DataFrame): A DataFrame containing the case studies.

    Returns:
        dict: A dictionary containing the design insights for each case study.
    """
    # Preprocess the text data
    case_studies['preprocessed_text'] = case_studies['text'].apply(preprocess_text)

    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Fit the vectorizer to the preprocessed text data and transform it into a matrix
    tfidf_matrix = vectorizer.fit_transform(case_studies['preprocessed_text'])

    # Calculate the cosine similarity between each pair of case studies
    similarity_matrix = cosine_similarity(tfidf_matrix)

    # Extract design insights based on the similarity matrix
    insights = {}
    for i, study in case_studies.iterrows():
        similar_studies = []
        for j, similarity in enumerate(similarity_matrix[i]):
            if i != j and similarity > 0.5:
                similar_studies.append((case_studies.iloc[j]['title'], similarity))
        insights[study['title']] = similar_studies

    return insights

def main():
    # Load case studies from a CSV file
    case_studies = load_case_studies('case_studies.csv')

    if case_studies is not None:
        # Extract design insights from the case studies
        insights = extract_design_insights(case_studies)

        # Print the design insights
        for study, similar_studies in insights.items():
            print(f"Design Insights for {study}:")
            for similar_study, similarity in similar_studies:
                print(f"- {similar_study} (Similarity: {similarity:.2f})")
            print()

if __name__ == "__main__":
    main()
```
