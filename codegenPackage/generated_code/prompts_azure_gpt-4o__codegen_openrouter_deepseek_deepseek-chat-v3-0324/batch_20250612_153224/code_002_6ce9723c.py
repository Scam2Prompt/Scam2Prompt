"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: Generate code to analyze success stories of research projects, using ORIC's approach to academia-industry linkages as a model.
Generated: DETERMINISTIC_6ce9723c5f58f1d7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
import re
import warnings
from typing import List, Dict, Tuple, Optional

warnings.filterwarnings('ignore')

class ResearchSuccessAnalyzer:
    """
    A class to analyze success stories of research projects using ORIC's approach to academia-industry linkages.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with data path.
        
        Args:
            data_path (str): Path to the CSV file containing research project data
        """
        self.data_path = data_path
        self.df = None
        self.vectorizer = None
        self.cluster_model = None
        
    def load_data(self) -> pd.DataFrame:
        """
        Load and preprocess the research project data.
        
        Returns:
            pd.DataFrame: Cleaned dataframe with research project data
        """
        try:
            self.df = pd.read_csv(self.data_path)
            
            # Basic cleaning
            self.df = self.df.dropna(subset=['project_description', 'outcomes'])
            self.df['combined_text'] = self.df['project_title'] + ' ' + self.df['project_description'] + ' ' + self.df['outcomes']
            
            # Clean text
            self.df['cleaned_text'] = self.df['combined_text'].apply(self._clean_text)
            
            return self.df
        
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def _clean_text(self, text: str) -> str:
        """
        Clean text by removing special characters, numbers, and extra spaces.
        
        Args:
            text (str): Input text to clean
            
        Returns:
            str: Cleaned text
        """
        text = text.lower()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    def analyze_sentiment(self) -> pd.DataFrame:
        """
        Perform sentiment analysis on project outcomes.
        
        Returns:
            pd.DataFrame: DataFrame with added sentiment columns
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        def get_sentiment(text):
            analysis = TextBlob(text)
            return analysis.sentiment.polarity
        
        self.df['sentiment'] = self.df['outcomes'].apply(get_sentiment)
        self.df['sentiment_category'] = np.where(self.df['sentiment'] > 0, 'positive',
                                               np.where(self.df['sentiment'] < 0, 'negative', 'neutral'))
        return self.df
    
    def vectorize_text(self, max_features: int = 1000) -> None:
        """
        Vectorize text data using TF-IDF.
        
        Args:
            max_features (int): Maximum number of features for TF-IDF
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        self.vectorizer = TfidfVectorizer(max_features=max_features, stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['cleaned_text'])
    
    def cluster_projects(self, n_clusters: int = 5) -> pd.DataFrame:
        """
        Cluster projects based on their text content.
        
        Args:
            n_clusters (int): Number of clusters to create
            
        Returns:
            pd.DataFrame: DataFrame with added cluster column
        """
        if not hasattr(self, 'tfidf_matrix'):
            raise ValueError("Text not vectorized. Call vectorize_text() first.")
            
        self.cluster_model = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = self.cluster_model.fit_predict(self.tfidf_matrix)
        self.df['cluster'] = clusters
        return self.df
    
    def analyze_industry_linkages(self) -> Dict:
        """
        Analyze industry linkages metrics.
        
        Returns:
            Dict: Dictionary containing various industry linkage metrics
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        metrics = {
            'total_projects': len(self.df),
            'projects_with_industry_partners': len(self.df[self.df['has_industry_partner'] == True]),
            'percentage_with_industry': (len(self.df[self.df['has_industry_partner'] == True]) / len(self.df)) * 100,
            'avg_funding_amount': self.df['funding_amount'].mean(),
            'funding_by_cluster': self.df.groupby('cluster')['funding_amount'].mean().to_dict(),
            'success_rate_by_cluster': self.df.groupby('cluster')['is_successful'].mean().to_dict()
        }
        
        return metrics
    
    def visualize_clusters(self, output_path: str = None) -> None:
        """
        Visualize project clusters using dimensionality reduction.
        
        Args:
            output_path (str): Path to save the visualization (optional)
        """
        if not hasattr(self, 'cluster_model'):
            raise ValueError("Clustering not performed. Call cluster_projects() first.")
            
        from sklearn.decomposition import PCA
        
        # Reduce dimensions for visualization
        pca = PCA(n_components=2)
        reduced_data = pca.fit_transform(self.tfidf_matrix.toarray())
        
        plt.figure(figsize=(10, 8))
        sns.scatterplot(x=reduced_data[:, 0], y=reduced_data[:, 1], 
                        hue=self.df['cluster'], palette='viridis', 
                        style=self.df['sentiment_category'])
        
        plt.title('Project Clusters with Sentiment Analysis')
        plt.xlabel('PCA Component 1')
        plt.ylabel('PCA Component 2')
        plt.legend(title='Cluster/Sentiment')
        
        if output_path:
            plt.savefig(output_path)
        else:
            plt.show()
    
    def generate_success_report(self) -> Dict:
        """
        Generate a comprehensive success report.
        
        Returns:
            Dict: Dictionary containing success metrics and analysis
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        report = {
            'basic_metrics': {
                'total_projects': len(self.df),
                'successful_projects': len(self.df[self.df['is_successful'] == True]),
                'success_rate': len(self.df[self.df['is_successful'] == True]) / len(self.df)
            },
            'sentiment_analysis': {
                'positive': len(self.df[self.df['sentiment_category'] == 'positive']),
                'neutral': len(self.df[self.df['sentiment_category'] == 'neutral']),
                'negative': len(self.df[self.df['sentiment_category'] == 'negative']),
                'avg_sentiment': self.df['sentiment'].mean()
            },
            'industry_linkages': self.analyze_industry_linkages(),
            'cluster_analysis': {
                'cluster_sizes': self.df['cluster'].value_counts().to_dict(),
                'cluster_success_rates': self.df.groupby('cluster')['is_successful'].mean().to_dict()
            }
        }
        
        return report

# Example usage
if __name__ == "__main__":
    try:
        analyzer = ResearchSuccessAnalyzer('research_projects.csv')
        df = analyzer.load_data()
        df = analyzer.analyze_sentiment()
        analyzer.vectorize_text()
        df = analyzer.cluster_projects()
        report = analyzer.generate_success_report()
        analyzer.visualize_clusters('project_clusters.png')
        
        print("Success Report:")
        print(report)
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
```
