"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beta.metis-lab.com
Prompt: Create a script to analyze the themes of roundtable discussions, such as "La sobriété" or "L’accélération muséale," using the content structure provided by Mêtis Lab.
Generated: DETERMINISTIC_c96fc85bf39da299
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Theme Analysis Script for Roundtable Discussions
=================================================

This script analyzes the themes of roundtable discussions using content provided
by Mêtis Lab. The analysis identifies recurring keywords, sentiment, and overall
theme prevalence from textual data (e.g., transcripts or notes).

Requirements:
- Python >= 3.7
- Install required dependencies using `pip install -r requirements.txt`

Dependencies:
- pandas: For structured data management.
- nltk: For text processing and analysis.
- sklearn: For text vectorization and classification.
- spacy: For advanced NLP tasks (ensure language model installation).
"""

import os
import pandas as pd
import spacy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.exceptions import NotFittedError

# Initialize Spacy NLP model (French language for this example)
try:
    nlp = spacy.load("fr_core_news_md")  # Ensure French language model is installed
except OSError as e:
    raise RuntimeError(
        "French language model not installed for Spacy. Run `python -m spacy download fr_core_news_md`."
    ) from e

# Stopwords for French (using nltk)
try:
    stop_words = set(stopwords.words("french"))
except LookupError:
    import nltk
    nltk.download("stopwords")
    stop_words = set(stopwords.words("french"))

# Global constants
INPUT_FILE = "roundtable_discussions.csv"  # Input file (CSV format)
OUTPUT_FILE = "theme_analysis_results.csv"  # Output file for analysis results

def load_data(file_path):
    """
    Loads data from a CSV file containing roundtable discussion content.

    Args:
        file_path (str): Path to the input CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the loaded content.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file '{file_path}' not found.")
    except pd.errors.ParserError:
        raise ValueError("Error parsing the input file. Ensure the CSV format is correct.")

def preprocess_text(text):
    """
    Preprocesses text by tokenizing, removing stopwords, and lemmatizing.

    Args:
        text (str): Raw text to preprocess.

    Returns:
        str: Preprocessed text.
    """
    doc = nlp(text.lower())  # Convert to lowercase and tokenize using Spacy
    tokens = [
        token.lemma_
        for token in doc
        if token.is_alpha and token.lemma_ not in stop_words
    ]  # Lemmatize and remove stopwords
    return " ".join(tokens)

def analyze_themes(data):
    """
    Analyzes themes using TF-IDF and Latent Dirichlet Allocation for topic modeling.

    Args:
        data (pd.DataFrame): DataFrame containing preprocessed discussion content.

    Returns:
        pd.DataFrame: DataFrame with identified themes and prevalence.
    """
    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer(max_features=1000)
    try:
        tfidf_matrix = vectorizer.fit_transform(data["content"])
    except ValueError:
        raise ValueError("No valid data available for theme analysis.")

    # Latent Dirichlet Allocation (LDA) for topic modeling
    lda_model = LatentDirichletAllocation(n_components=5, random_state=42)
    try:
        lda_topics = lda_model.fit_transform(tfidf_matrix)
    except NotFittedError:
        raise RuntimeError("LDA model fitting failed. Ensure valid TF-IDF input.")

    # Extract top keywords for each topic
    keywords = []
    for topic_idx, topic in enumerate(lda_model.components_):
        top_keywords = [
            vectorizer.get_feature_names_out()[i]
            for i in topic.argsort()[:-11:-1]
        ]  # Top 10 keywords per topic
        keywords.append(", ".join(top_keywords))

    # Add topic keywords to DataFrame
    theme_df = pd.DataFrame({"Topic": range(1, len(keywords) + 1), "Keywords": keywords})
    return theme_df

def main():
    """
    Main function to load data, preprocess content, and analyze themes.
    """
    print("Loading data...")
    try:
        data = load_data(INPUT_FILE)
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    if "content" not in data.columns:
        print("Error: Input file must contain a 'content' column.")
        return

    print("Preprocessing text data...")
    data["content"] = data["content"].apply(preprocess_text)

    print("Analyzing themes...")
    try:
        theme_results = analyze_themes(data)
    except Exception as e:
        print(f"Error during theme analysis: {e}")
        return

    print(f"Saving results to '{OUTPUT_FILE}'...")
    try:
        theme_results.to_csv(OUTPUT_FILE, index=False)
        print("Theme analysis completed successfully.")
    except Exception as e:
        print(f"Error saving results: {e}")

if __name__ == "__main__":
    main()
```
