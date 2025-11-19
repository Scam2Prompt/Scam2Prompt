"""
Generated Code Metadata:
========================
Original URL: https://origines-decoration.com
Prompt: "Generate a list of keywords and tags for categorizing and searching luxury furniture products on a website like origines-decoration.com, using techniques like natural language processing and machine learning."
Generated: DETERMINISTIC_451e9a6afb6aafa4
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

# Ensure required NLTK data is downloaded
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

class LuxuryFurnitureKeywordGenerator:
    """
    A class to generate keywords and tags for luxury furniture products using NLP techniques.
    """
    
    def __init__(self, product_descriptions):
        """
        Initialize the keyword generator with product descriptions.
        
        Args:
            product_descriptions (list): List of product descriptions
        """
        self.product_descriptions = product_descriptions
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.vectorizer = TfidfVectorizer(max_features=1000)
        self.keywords = []
        
    def preprocess_text(self, text):
        """
        Preprocess text by removing special characters, stopwords, and lemmatizing.
        
        Args:
            text (str): Input text to preprocess
            
        Returns:
            str: Processed text
        """
        # Remove special characters and digits
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove stopwords and lemmatize
        tokens = [self.lemmatizer.lemmatize(word) for word in text.split() 
                 if word not in self.stop_words and len(word) > 2]
        
        return ' '.join(tokens)
    
    def extract_keywords(self, num_clusters=5, top_n=20):
        """
        Extract keywords using TF-IDF and K-means clustering.
        
        Args:
            num_clusters (int): Number of clusters for K-means
            top_n (int): Number of top keywords to extract per cluster
            
        Returns:
            list: List of extracted keywords
        """
        try:
            # Preprocess all descriptions
            processed_descriptions = [self.preprocess_text(desc) for desc in self.product_descriptions]
            
            # Create TF-IDF matrix
            tfidf_matrix = self.vectorizer.fit_transform(processed_descriptions)
            
            # Perform K-means clustering
            kmeans = KMeans(n_clusters=num_clusters, random_state=42)
            kmeans.fit(tfidf_matrix)
            
            # Get top features for each cluster
            feature_names = self.vectorizer.get_feature_names_out()
            self.keywords = []
            
            for i in range(num_clusters):
                # Get indices of top TF-IDF scores in cluster
                centroid = kmeans.cluster_centers_[i]
                top_indices = centroid.argsort()[-top_n:][::-1]
                
                # Get corresponding feature names
                cluster_keywords = [feature_names[index] for index in top_indices]
                self.keywords.extend(cluster_keywords)
            
            # Remove duplicates and return
            return list(set(self.keywords))
            
        except Exception as e:
            print(f"Error extracting keywords: {e}")
            return []
    
    def generate_tags(self, additional_metadata=None):
        """
        Generate product tags combining extracted keywords with additional metadata.
        
        Args:
            additional_metadata (dict): Additional product metadata like material, style, etc.
            
        Returns:
            list: List of generated tags
        """
        tags = []
        
        # Add extracted keywords
        if self.keywords:
            tags.extend(self.keywords)
        
        # Add metadata if provided
        if additional_metadata:
            try:
                for key, values in additional_metadata.items():
                    if isinstance(values, list):
                        tags.extend(values)
                    else:
                        tags.append(values)
            except Exception as e:
                print(f"Error processing metadata: {e}")
        
        # Clean and deduplicate tags
        tags = [tag.lower().strip() for tag in tags if tag and isinstance(tag, str)]
        return list(set(tags))
    
    def save_keywords_to_csv(self, filepath):
        """
        Save generated keywords to a CSV file.
        
        Args:
            filepath (str): Path to save the CSV file
        """
        try:
            df = pd.DataFrame({'keywords': self.keywords})
            df.to_csv(filepath, index=False)
        except Exception as e:
            print(f"Error saving keywords to CSV: {e}")

# Example usage
if __name__ == "__main__":
    # Sample luxury furniture product descriptions
    product_descriptions = [
        "Handcrafted mahogany dining table with intricate carvings",
        "Italian leather sofa with gold-plated accents",
        "French provincial oak armoire with antique finish",
        "Modern minimalist glass coffee table with chrome legs",
        "Art Deco velvet upholstered armchair with walnut frame",
        "Scandinavian teak sideboard with brass handles",
        "Mid-century modern credenza with rosewood veneer",
        "Louis XVI style gilded console table",
        "Contemporary sectional sofa in premium Belgian linen",
        "Vintage industrial metal and reclaimed wood desk"
    ]
    
    # Additional product metadata
    metadata = {
        'materials': ['mahogany', 'leather', 'oak', 'glass', 'velvet', 'teak', 'rosewood', 'metal', 'linen', 'walnut'],
        'styles': ['handcrafted', 'italian', 'french provincial', 'modern', 'art deco', 
                  'scandinavian', 'mid-century', 'louis xvi', 'contemporary', 'vintage'],
        'categories': ['dining table', 'sofa', 'armoire', 'coffee table', 'armchair', 
                      'sideboard', 'credenza', 'console table', 'sectional', 'desk']
    }
    
    # Initialize and process
    keyword_generator = LuxuryFurnitureKeywordGenerator(product_descriptions)
    keywords = keyword_generator.extract_keywords()
    tags = keyword_generator.generate_tags(additional_metadata=metadata)
    
    # Save results
    keyword_generator.save_keywords_to_csv('luxury_furniture_keywords.csv')
    
    print("Generated Keywords:", keywords[:20])
    print("\nGenerated Tags:", tags[:20])
```
