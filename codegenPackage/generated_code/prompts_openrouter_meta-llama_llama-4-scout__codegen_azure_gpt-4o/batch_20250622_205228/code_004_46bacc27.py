"""
Generated Code Metadata:
========================
Original URL: https://consensys.world
Prompt: Create a data visualization dashboard to display e-commerce review data, including metrics such as review ratings, sentiment, and topic distribution.
Generated: DETERMINISTIC_46bacc2753ba427d
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud
import streamlit as st

# Function to calculate sentiment polarity
def calculate_sentiment(text):
    try:
        return TextBlob(text).sentiment.polarity
    except Exception as e:
        return np.nan

# Function to extract topics using CountVectorizer
def extract_topics(reviews, num_topics=10):
    try:
        vectorizer = CountVectorizer(stop_words='english', max_features=1000)
        word_counts = vectorizer.fit_transform(reviews)
        word_freq = pd.DataFrame(word_counts.toarray(), columns=vectorizer.get_feature_names_out())
        top_words = word_freq.sum().sort_values(ascending=False).head(num_topics)
        return top_words
    except Exception as e:
        return pd.Series()

# Load e-commerce review data
@st.cache
def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

# Main function to create the dashboard
def main():
    # Set up Streamlit app
    st.title("E-commerce Review Data Dashboard")
    st.sidebar.title("Dashboard Settings")
    
    # File upload
    uploaded_file = st.sidebar.file_uploader("Upload Review Data (CSV)", type=["csv"])
    if uploaded_file is not None:
        data = load_data(uploaded_file)
        
        # Display raw data
        st.subheader("Raw Data")
        st.write(data.head())
        
        # Check if required columns exist
        if 'review_text' in data.columns and 'review_rating' in data.columns:
            # Calculate sentiment
            st.subheader("Sentiment Analysis")
            data['sentiment'] = data['review_text'].apply(calculate_sentiment)
            st.write("Sentiment Polarity Distribution")
            fig, ax = plt.subplots()
            sns.histplot(data['sentiment'], bins=20, kde=True, ax=ax)
            st.pyplot(fig)
            
            # Display average sentiment
            avg_sentiment = data['sentiment'].mean()
            st.write(f"Average Sentiment Polarity: {avg_sentiment:.2f}")
            
            # Display review ratings distribution
            st.subheader("Review Ratings Distribution")
            fig, ax = plt.subplots()
            sns.countplot(x='review_rating', data=data, ax=ax)
            st.pyplot(fig)
            
            # Extract and display topics
            st.subheader("Topic Distribution")
            topics = extract_topics(data['review_text'])
            st.write("Top Topics")
            st.bar_chart(topics)
            
            # Generate and display word cloud
            st.subheader("Word Cloud")
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(data['review_text']))
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis('off')
            st.pyplot(fig)
        else:
            st.error("Uploaded data must contain 'review_text' and 'review_rating' columns.")
    else:
        st.info("Please upload a CSV file to begin.")

# Run the app
if __name__ == "__main__":
    main()
```
