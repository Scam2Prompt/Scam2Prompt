"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consensys.world
Prompt: Generate Python code to visualize trends in e-commerce review topics for baby products, leveraging Consensys's insights on category landscape and consumer language clusters.
Generated: DETERMINISTIC_15a03d7626a5e225
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# Function to preprocess text data
def preprocess_reviews(reviews):
    """
    Cleans and tokenizes text data.

    Args:
        reviews (pd.Series): Series of text reviews.

    Returns:
        pd.Series: Preprocessed text reviews.
    """
    import re
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    
    stop_words = set(stopwords.words('english'))
    
    def clean_text(text):
        text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
        text = text.lower()  # Convert to lowercase
        tokens = word_tokenize(text)
        tokens = [word for word in tokens if word not in stop_words]  # Remove stopwords
        return ' '.join(tokens)
    
    return reviews.apply(clean_text)

# Load a dataset of e-commerce reviews
def load_data(file_path):
    """
    Loads review data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        raise

# Function to extract topics using LDA
def extract_topics(reviews, num_topics=5, num_words=10):
    """
    Extracts topics from reviews using Latent Dirichlet Allocation (LDA).

    Args:
        reviews (pd.Series): Preprocessed text reviews.
        num_topics (int): Number of topics to extract.
        num_words (int): Number of top words per topic.

    Returns:
        dict: Topics with their associated words.
    """
    vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
    dtm = vectorizer.fit_transform(reviews)
    
    lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda.fit(dtm)
    
    topics = {}
    for topic_idx, topic in enumerate(lda.components_):
        topics[f"Topic {topic_idx+1}"] = [
            vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-num_words:]
        ][::-1]
    
    return topics

# Visualize topic trends with a word cloud
def visualize_topics(topics):
    """
    Visualizes topics using word clouds.

    Args:
        topics (dict): Topics with their associated words.
    """
    for topic, words in topics.items():
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(words))
        
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(topic, fontsize=16)
        plt.show()

# Main function to orchestrate the process
def main():
    """
    Main function to process e-commerce reviews, extract topics, and visualize trends.
    """
    try:
        # Load and preprocess the data
        file_path = 'ecommerce_reviews.csv'  # Update with the actual file path
        print("Loading review data...")
        data = load_data(file_path)
        
        if 'review' not in data.columns:
            raise ValueError("The dataset must contain a 'review' column with textual data.")
        
        print("Preprocessing reviews...")
        preprocessed_reviews = preprocess_reviews(data['review'])
        
        # Extract topics
        print("Extracting topics...")
        num_topics = 5  # Number of topics to extract
        topics = extract_topics(preprocessed_reviews, num_topics=num_topics)
        
        for topic, words in topics.items():
            print(f"{topic}: {', '.join(words)}")
        
        # Visualize topics
        print("Visualizing topics...")
        visualize_topics(topics)
        
        print("Process completed successfully!")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point for script execution
if __name__ == "__main__":
    main()
```
