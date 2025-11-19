"""
Generated Code Metadata:
========================
Original URL: https://beta.metis-lab.com
Prompt: Write a script to analyze and visualize the frequency of keywords in the titles of Mêtis' resources (e.g., articles, videos, podcasts) using natural language processing techniques.
Generated: DETERMINISTIC_312edebe2200b2c9
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud
import nltk
import os

# Ensure necessary NLTK resources are downloaded
nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords

# Function to load data from a CSV file
def load_data(file_path):
    """
    Load resource data from a CSV file.

    :param file_path: Path to the CSV file containing resource titles.
    :return: DataFrame containing the titles.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Function to preprocess titles
def preprocess_titles(titles):
    """
    Preprocess the titles by converting to lowercase and removing stopwords.

    :param titles: List of titles to preprocess.
    :return: List of cleaned titles.
    """
    stop_words = set(stopwords.words('english'))
    cleaned_titles = []
    
    for title in titles:
        # Convert to lowercase and split into words
        words = title.lower().split()
        # Remove stopwords
        filtered_words = [word for word in words if word not in stop_words]
        cleaned_titles.append(' '.join(filtered_words))
    
    return cleaned_titles

# Function to analyze keyword frequency
def analyze_keyword_frequency(titles):
    """
    Analyze the frequency of keywords in the titles.

    :param titles: List of cleaned titles.
    :return: DataFrame of keyword frequencies.
    """
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(titles)
    keyword_freq = X.toarray().sum(axis=0)
    
    # Create a DataFrame for keyword frequencies
    freq_df = pd.DataFrame(keyword_freq, index=vectorizer.get_feature_names_out(), columns=['Frequency'])
    freq_df = freq_df.sort_values(by='Frequency', ascending=False)
    
    return freq_df

# Function to visualize keyword frequency
def visualize_keyword_frequency(freq_df):
    """
    Visualize the keyword frequency using a bar chart and a word cloud.

    :param freq_df: DataFrame of keyword frequencies.
    """
    # Bar chart
    plt.figure(figsize=(12, 6))
    freq_df.head(10).plot(kind='bar', legend=False)
    plt.title('Top 10 Keywords in Resource Titles')
    plt.xlabel('Keywords')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(freq_df['Frequency'])
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Keyword Frequency Word Cloud')
    plt.show()

# Main function to execute the analysis
def main():
    # Path to the CSV file containing resource titles
    file_path = 'metis_resources.csv'
    
    # Load data
    data = load_data(file_path)
    if data is None or 'title' not in data.columns:
        print("Invalid data or missing 'title' column.")
        return
    
    # Preprocess titles
    cleaned_titles = preprocess_titles(data['title'].tolist())
    
    # Analyze keyword frequency
    freq_df = analyze_keyword_frequency(cleaned_titles)
    
    # Visualize keyword frequency
    visualize_keyword_frequency(freq_df)

# Entry point of the script
if __name__ == "__main__":
    main()
```

Make sure to have the required libraries installed before running the script:
```bash
pip install pandas matplotlib scikit-learn wordcloud nltk
```
