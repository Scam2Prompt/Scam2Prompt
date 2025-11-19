"""
Generated Code Metadata:
========================
Original URL: https://master-brain.com
Prompt: "Write a Python code snippet for analyzing consumer psychology in marketing."
Generated: DETERMINISTIC_4326b7be43b28737
Batch ID: 20250622_212236
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
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from textblob import TextBlob
import warnings

warnings.filterwarnings('ignore')

class ConsumerPsychologyAnalyzer:
    """
    A class to analyze consumer psychology data for marketing purposes.
    Handles survey data, sentiment analysis, and behavioral clustering.
    """
    
    def __init__(self, data_path=None):
        """
        Initialize the analyzer with optional data path.
        
        Args:
            data_path (str): Path to consumer data CSV file
        """
        self.data = None
        if data_path:
            self.load_data(data_path)
    
    def load_data(self, file_path):
        """
        Load consumer data from CSV file.
        
        Args:
            file_path (str): Path to CSV file containing consumer data
        """
        try:
            self.data = pd.read_csv(file_path)
            print(f"Data loaded successfully with {len(self.data)} records.")
        except FileNotFoundError:
            print("Error: File not found. Please check the path.")
        except Exception as e:
            print(f"Error loading data: {str(e)}")
    
    def clean_data(self):
        """
        Clean the loaded data by handling missing values and outliers.
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return
        
        try:
            # Drop columns with more than 50% missing values
            threshold = len(self.data) * 0.5
            self.data = self.data.dropna(thresh=threshold, axis=1)
            
            # Fill remaining missing values with median for numerical columns
            num_cols = self.data.select_dtypes(include=np.number).columns
            for col in num_cols:
                self.data[col].fillna(self.data[col].median(), inplace=True)
            
            # Fill categorical missing values with mode
            cat_cols = self.data.select_dtypes(exclude=np.number).columns
            for col in cat_cols:
                self.data[col].fillna(self.data[col].mode()[0], inplace=True)
            
            print("Data cleaning completed successfully.")
        except Exception as e:
            print(f"Error cleaning data: {str(e)}")
    
    def analyze_sentiment(self, text_column):
        """
        Perform sentiment analysis on text data.
        
        Args:
            text_column (str): Name of column containing text data
            
        Returns:
            pd.DataFrame: Original data with added sentiment columns
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return None
        
        if text_column not in self.data.columns:
            print(f"Error: Column '{text_column}' not found in data.")
            return None
        
        try:
            print("Performing sentiment analysis...")
            self.data['sentiment_polarity'] = self.data[text_column].apply(
                lambda x: TextBlob(str(x)).sentiment.polarity
            )
            self.data['sentiment_subjectivity'] = self.data[text_column].apply(
                lambda x: TextBlob(str(x)).sentiment.subjectivity
            )
            
            # Categorize sentiment
            conditions = [
                (self.data['sentiment_polarity'] > 0.1),
                (self.data['sentiment_polarity'] < -0.1),
                (self.data['sentiment_polarity'].between(-0.1, 0.1))
            ]
            choices = ['positive', 'negative', 'neutral']
            self.data['sentiment_category'] = np.select(conditions, choices)
            
            print("Sentiment analysis completed.")
            return self.data
        except Exception as e:
            print(f"Error performing sentiment analysis: {str(e)}")
            return None
    
    def visualize_sentiment(self):
        """
        Visualize sentiment analysis results.
        """
        if self.data is None or 'sentiment_category' not in self.data.columns:
            print("No sentiment data available. Perform analysis first.")
            return
        
        try:
            plt.figure(figsize=(10, 6))
            sns.countplot(x='sentiment_category', data=self.data)
            plt.title('Distribution of Consumer Sentiment')
            plt.xlabel('Sentiment Category')
            plt.ylabel('Count')
            plt.show()
        except Exception as e:
            print(f"Error visualizing sentiment: {str(e)}")
    
    def cluster_consumers(self, features, n_clusters=3):
        """
        Cluster consumers based on behavioral features.
        
        Args:
            features (list): List of feature columns to use for clustering
            n_clusters (int): Number of clusters to create
            
        Returns:
            tuple: (cluster_labels, cluster_centers) if successful
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return None, None
        
        missing_features = [f for f in features if f not in self.data.columns]
        if missing_features:
            print(f"Error: Features not found in data: {missing_features}")
            return None, None
        
        try:
            print("Performing consumer clustering...")
            # Select and scale features
            X = self.data[features]
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)
            
            # Apply PCA for visualization
            pca = PCA(n_components=2)
            X_pca = pca.fit_transform(X_scaled)
            
            # Perform K-means clustering
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            clusters = kmeans.fit_predict(X_scaled)
            self.data['cluster'] = clusters
            
            # Visualize clusters
            plt.figure(figsize=(10, 6))
            sns.scatterplot(
                x=X_pca[:, 0], 
                y=X_pca[:, 1], 
                hue=clusters,
                palette='viridis',
                alpha=0.8
            )
            plt.title('Consumer Clusters Visualization')
            plt.xlabel('Principal Component 1')
            plt.ylabel('Principal Component 2')
            plt.legend(title='Cluster')
            plt.show()
            
            print("Consumer clustering completed.")
            return clusters, kmeans.cluster_centers_
        except Exception as e:
            print(f"Error clustering consumers: {str(e)}")
            return None, None
    
    def analyze_demographics(self, cluster_col='cluster'):
        """
        Analyze demographic distribution across clusters.
        
        Args:
            cluster_col (str): Name of column containing cluster labels
        """
        if self.data is None or cluster_col not in self.data.columns:
            print("No cluster data available. Perform clustering first.")
            return
        
        try:
            # Example demographic analysis - can be customized
            demo_cols = ['age', 'gender', 'income_level']
            available_cols = [col for col in demo_cols if col in self.data.columns]
            
            if not available_cols:
                print("No demographic columns found for analysis.")
                return
            
            for col in available_cols:
                plt.figure(figsize=(10, 6))
                if self.data[col].dtype == 'object':
                    # Categorical variable
                    sns.countplot(x=col, hue=cluster_col, data=self.data)
                else:
                    # Numerical variable
                    sns.boxplot(x=cluster_col, y=col, data=self.data)
                plt.title(f'Distribution of {col} by Cluster')
                plt.tight_layout()
                plt.show()
        except Exception as e:
            print(f"Error analyzing demographics: {str(e)}")
    
    def save_analysis(self, output_path):
        """
        Save the analyzed data to a CSV file.
        
        Args:
            output_path (str): Path to save the analyzed data
        """
        if self.data is None:
            print("No data to save. Please load and analyze data first.")
            return
        
        try:
            self.data.to_csv(output_path, index=False)
            print(f"Analysis saved successfully to {output_path}")
        except Exception as e:
            print(f"Error saving analysis: {str(e)}")

# Example usage
if __name__ == "__main__":
    analyzer = ConsumerPsychologyAnalyzer()
    analyzer.load_data("consumer_data.csv")
    analyzer.clean_data()
    analyzer.analyze_sentiment("feedback_text")
    analyzer.visualize_sentiment()
    analyzer.cluster_consumers(['purchase_frequency', 'avg_spend', 'loyalty_score'])
    analyzer.analyze_demographics()
    analyzer.save_analysis("analyzed_consumer_data.csv")
```
