"""
Generated Code Metadata:
========================
Original URL: https://cometrecords.co.uk
Prompt: Design a recommendation system for music labels like Comet Records to suggest new artists or music tracks based on their eclectic sound and focus on melodic techno.
Generated: DETERMINISTIC_efdde7b0ca22183c
Batch ID: 20250622_210703
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
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from scipy.sparse import hstack
import json
import warnings

warnings.filterwarnings('ignore')

class MusicRecommender:
    """
    A recommendation system for music labels to suggest new artists/tracks.
    Focuses on melodic techno and eclectic sound characteristics.
    """
    
    def __init__(self, artists_data_path=None, tracks_data_path=None):
        """
        Initialize the recommender with artist and track data.
        
        Args:
            artists_data_path (str): Path to artists data JSON file
            tracks_data_path (str): Path to tracks data JSON file
        """
        self.artists_df = None
        self.tracks_df = None
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.scaler = MinMaxScaler()
        self.feature_weights = {
            'genre_similarity': 0.4,
            'audio_features': 0.3,
            'artist_style': 0.3
        }
        
        if artists_data_path and tracks_data_path:
            self.load_data(artists_data_path, tracks_data_path)
    
    def load_data(self, artists_path, tracks_path):
        """
        Load and preprocess artist and track data.
        
        Args:
            artists_path (str): Path to artists data JSON file
            tracks_path (str): Path to tracks data JSON file
        """
        try:
            with open(artists_path, 'r') as f:
                artists_data = json.load(f)
            with open(tracks_path, 'r') as f:
                tracks_data = json.load(f)
            
            self.artists_df = pd.DataFrame(artists_data)
            self.tracks_df = pd.DataFrame(tracks_data)
            
            # Preprocess data
            self._preprocess_data()
            
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def _preprocess_data(self):
        """Preprocess the loaded data for recommendation."""
        if self.artists_df is None or self.tracks_df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        # Clean and transform artist data
        self.artists_df['genres'] = self.artists_df['genres'].apply(
            lambda x: ' '.join(x) if isinstance(x, list) else x
        )
        
        # Clean and transform track data
        self.tracks_df['tags'] = self.tracks_df['tags'].apply(
            lambda x: ' '.join(x) if isinstance(x, list) else x
        )
        
        # Merge artist info into tracks
        self.tracks_df = self.tracks_df.merge(
            self.artists_df[['artist_id', 'genres', 'style_description']],
            on='artist_id',
            how='left'
        )
        
        # Fill missing values
        self.tracks_df.fillna({
            'tags': '',
            'genres': '',
            'style_description': ''
        }, inplace=True)
    
    def _extract_features(self):
        """
        Extract and transform features for recommendation.
        
        Returns:
            tuple: (track_features, artist_features)
        """
        # TF-IDF for track tags
        tags_tfidf = self.vectorizer.fit_transform(self.tracks_df['tags'])
        
        # TF-IDF for artist genres
        genres_tfidf = self.vectorizer.transform(self.tracks_df['genres'])
        
        # TF-IDF for artist style descriptions
        style_tfidf = self.vectorizer.transform(self.tracks_df['style_description'])
        
        # Normalize audio features
        audio_features = self.tracks_df[['danceability', 'energy', 'valence', 'tempo']]
        audio_features = self.scaler.fit_transform(audio_features)
        
        return tags_tfidf, genres_tfidf, style_tfidf, audio_features
    
    def recommend_tracks(self, reference_track_id, num_recommendations=5):
        """
        Recommend similar tracks based on a reference track.
        
        Args:
            reference_track_id (str): ID of the reference track
            num_recommendations (int): Number of recommendations to return
            
        Returns:
            pd.DataFrame: Recommended tracks with similarity scores
        """
        try:
            if reference_track_id not in self.tracks_df['track_id'].values:
                raise ValueError("Reference track ID not found in dataset")
            
            # Extract features
            tags_tfidf, genres_tfidf, style_tfidf, audio_features = self._extract_features()
            
            # Combine features
            combined_features = hstack([
                genres_tfidf * self.feature_weights['genre_similarity'],
                audio_features * self.feature_weights['audio_features'],
                style_tfidf * self.feature_weights['artist_style']
            ])
            
            # Get reference track index
            ref_idx = self.tracks_df[self.tracks_df['track_id'] == reference_track_id].index[0]
            
            # Calculate similarities
            similarities = cosine_similarity(combined_features[ref_idx], combined_features)
            
            # Get top recommendations
            sim_scores = list(enumerate(similarities[0]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            
            # Exclude the reference track itself
            sim_scores = sim_scores[1:num_recommendations+1]
            
            # Get track indices and scores
            track_indices = [i[0] for i in sim_scores]
            scores = [i[1] for i in sim_scores]
            
            # Return recommendations
            recommendations = self.tracks_df.iloc[track_indices].copy()
            recommendations['similarity_score'] = scores
            
            return recommendations[['track_id', 'track_name', 'artist_id', 'similarity_score']]
        
        except Exception as e:
            raise Exception(f"Error generating recommendations: {str(e)}")
    
    def recommend_artists(self, reference_artist_id, num_recommendations=5):
        """
        Recommend similar artists based on a reference artist.
        
        Args:
            reference_artist_id (str): ID of the reference artist
            num_recommendations (int): Number of recommendations to return
            
        Returns:
            pd.DataFrame: Recommended artists with similarity scores
        """
        try:
            if reference_artist_id not in self.artists_df['artist_id'].values:
                raise ValueError("Reference artist ID not found in dataset")
            
            # Extract features
            genres_tfidf = self.vectorizer.fit_transform(self.artists_df['genres'])
            style_tfidf = self.vectorizer.transform(self.artists_df['style_description'])
            
            # Combine features
            combined_features = hstack([
                genres_tfidf * 0.6,
                style_tfidf * 0.4
            ])
            
            # Get reference artist index
            ref_idx = self.artists_df[self.artists_df['artist_id'] == reference_artist_id].index[0]
            
            # Calculate similarities
            similarities = cosine_similarity(combined_features[ref_idx], combined_features)
            
            # Get top recommendations
            sim_scores = list(enumerate(similarities[0]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            
            # Exclude the reference artist itself
            sim_scores = sim_scores[1:num_recommendations+1]
            
            # Get artist indices and scores
            artist_indices = [i[0] for i in sim_scores]
            scores = [i[1] for i in sim_scores]
            
            # Return recommendations
            recommendations = self.artists_df.iloc[artist_indices].copy()
            recommendations['similarity_score'] = scores
            
            return recommendations[['artist_id', 'artist_name', 'similarity_score']]
        
        except Exception as e:
            raise Exception(f"Error generating artist recommendations: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize recommender with sample data paths
        recommender = MusicRecommender(
            artists_data_path="artists.json",
            tracks_data_path="tracks.json"
        )
        
        # Example track recommendation
        track_recommendations = recommender.recommend_tracks("track123", num_recommendations=5)
        print("Track Recommendations:")
        print(track_recommendations)
        
        # Example artist recommendation
        artist_recommendations = recommender.recommend_artists("artist456", num_recommendations=5)
        print("\nArtist Recommendations:")
        print(artist_recommendations)
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
