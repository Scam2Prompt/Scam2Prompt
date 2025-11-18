"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://epicpinterestfail.com
Prompt: Generate code to extract and summarize blog content related to "Reflective Tape for Visibility and Safety" using natural language processing techniques.
Generated: DETERMINISTIC_f1ac43ce6435c0b8
Batch ID: 20250612_152924
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com/blog/reflective-tape-visibility-safety": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import nltk
from nltk.tokenize import sent_tokenize

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')  # For sentence tokenization

def fetch_blog_content(url):
    """
    Fetch blog content from a given URL using web scraping.
    Args:
        url (str): URL of the blog page.
    Returns:
        str: Extracted text content from the blog.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTP errors if any
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract blog content (adjust class/ID based on HTML structure)
        paragraphs = soup.find_all('p')
        blog_content = ' '.join(paragraph.text for paragraph in paragraphs)
        return blog_content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching blog content: {e}")
        return ""
    except Exception as e:
        print(f"Unexpected error: {e}")
        return ""

def summarize_content(text, num_sentences=5):
    """
    Summarize the blog content using clustering and sentence extraction.
    Args:
        text (str): Full blog content text to summarize.
        num_sentences (int): Number of sentences to include in the summary.
    Returns:
        str: Summarized content.
    """
    try:
        # Tokenize content into sentences
        sentences = sent_tokenize(text)

        # Vectorize sentences using TF-IDF
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(sentences)

        # Use KMeans clustering for summarization
        num_clusters = min(num_sentences, len(sentences))  # Avoid over-clustering
        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        kmeans.fit(tfidf_matrix)

        # Extract representative sentences from clusters
        cluster_centers = kmeans.cluster_centers_.argsort(axis=1)[:, ::-1]
        summary_sentences = []
        for cluster_idx in range(num_clusters):
            representative_idx = cluster_centers[cluster_idx][0]
            summary_sentences.append(sentences[representative_idx])

        # Join the summarized sentences into a single string
        return ' '.join(summary_sentences)
    except Exception as e:
        print(f"Error during summarization: {e}")
        return "Error generating summary."

if __name__ == "__main__":
    # Example blog URL (replace with actual URL)
    blog_url = "https://www.example.com/blog/reflective-tape-visibility-safety"

    # Fetch and process blog content
    content = fetch_blog_content(blog_url)
    if content:
        print("Original Content Length:", len(content))

        # Generate summary
        summary = summarize_content(content, num_sentences=5)
        print("Summary:")
        print(summary)
    else:
        print("Failed to fetch or process the blog content.")
```
