"""
Generated Code Metadata:
========================
Original URL: https://agnedoveikaite.lt
Prompt: Generate a Python script that analyzes a person's emotional state through their music preferences and provides personalized recommendations for emotional well-being.
Generated: DETERMINISTIC_5d676af72386fe89
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import numpy as np
import warnings
from typing import Dict, List, Tuple, Optional

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class MusicEmotionAnalyzer:
    """
    Analyzes emotional state through music preferences and provides recommendations.
    """
    
    def __init__(self, music_data_path: str = None):
        """
        Initialize the analyzer with music data.
        
        Args:
            music_data_path (str): Path to CSV file containing music features.
                                  If None, uses default dataset.
        """
        self.music_data = self._load_music_data(music_data_path)
        self.scaler = StandardScaler()
        self.model = None
        self.emotion_clusters = None
        
    def _load_music_data(self, path: Optional[str]) -> pd.DataFrame:
        """
        Load music data from CSV file or use default dataset.
        
        Args:
            path (str): Path to CSV file. If None, uses default dataset.
            
        Returns:
            pd.DataFrame: Music data with features.
        """
        if path:
            try:
                return pd.read_csv(path)
            except Exception as e:
                raise ValueError(f"Error loading music data: {str(e)}")
        
        # Default dataset structure (mock data)
        default_data = {
            'track_id': [f'track_{i}' for i in range(100)],
            'valence': np.random.uniform(0, 1, 100),
            'energy': np.random.uniform(0, 1, 100),
            'danceability': np.random.uniform(0, 1, 100),
            'tempo': np.random.uniform(60, 200, 100),
            'loudness': np.random.uniform(-30, 0, 100),
            'mode': np.random.randint(0, 2, 100),
            'key': np.random.randint(0, 12, 100),
            'emotion_label': np.random.choice(['happy', 'sad', 'calm', 'energetic'], 100)
        }
        return pd.DataFrame(default_data)
    
    def _preprocess_data(self) -> pd.DataFrame:
        """
        Preprocess music data for clustering.
        
        Returns:
            pd.DataFrame: Processed data ready for clustering.
        """
        features = ['valence', 'energy', 'danceability', 'tempo', 'loudness']
        processed_data = self.music_data[features].copy()
        processed_data = self.scaler.fit_transform(processed_data)
        return processed_data
    
    def _determine_optimal_clusters(self, data: np.ndarray) -> int:
        """
        Determine optimal number of clusters using silhouette score.
        
        Args:
            data (np.ndarray): Processed music data.
            
        Returns:
            int: Optimal number of clusters.
        """
        silhouette_scores = []
        max_clusters = min(10, len(data) - 1)
        
        for n_clusters in range(2, max_clusters + 1):
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            cluster_labels = kmeans.fit_predict(data)
            silhouette_avg = silhouette_score(data, cluster_labels)
            silhouette_scores.append(silhouette_avg)
        
        return np.argmax(silhouette_scores) + 2
    
    def train_emotion_model(self) -> None:
        """
        Train KMeans model to cluster music by emotional features.
        """
        processed_data = self._preprocess_data()
        optimal_clusters = self._determine_optimal_clusters(processed_data)
        
        self.model = KMeans(n_clusters=optimal_clusters, random_state=42)
        self.emotion_clusters = self.model.fit_predict(processed_data)
        
        # Map clusters to emotion labels based on feature means
        self._map_clusters_to_emotions()
    
    def _map_clusters_to_emotions(self) -> None:
        """
        Map clusters to emotion labels based on feature statistics.
        """
        self.music_data['cluster'] = self.emotion_clusters
        cluster_stats = self.music_data.groupby('cluster').mean()
        
        self.cluster_emotions = {}
        for cluster in cluster_stats.index:
            stats = cluster_stats.loc[cluster]
            
            if stats['valence'] > 0.6 and stats['energy'] > 0.6:
                emotion = 'happy'
            elif stats['valence'] < 0.4 and stats['energy'] < 0.4:
                emotion = 'sad'
            elif stats['energy'] > 0.7 and stats['danceability'] > 0.7:
                emotion = 'energetic'
            else:
                emotion = 'calm'
            
            self.cluster_emotions[cluster] = emotion
    
    def analyze_user_preferences(self, user_tracks: List[str]) -> Dict[str, float]:
        """
        Analyze user's music preferences to determine emotional state.
        
        Args:
            user_tracks (List[str]): List of track IDs the user listens to.
            
        Returns:
            Dict[str, float]: Dictionary of emotion percentages.
        """
        if not self.model:
            raise ValueError("Model not trained. Call train_emotion_model() first.")
            
        user_data = self.music_data[self.music_data['track_id'].isin(user_tracks)]
        
        if user_data.empty:
            raise ValueError("No matching tracks found in the dataset.")
            
        cluster_counts = user_data['cluster'].value_counts(normalize=True)
        emotion_counts = cluster_counts.map(lambda x: self.cluster_emotions[x])
        
        return emotion_counts.value_counts(normalize=True).to_dict()
    
    def get_recommendations(self, target_emotion: str, n_recommendations: int = 5) -> List[str]:
        """
        Get music recommendations for target emotional state.
        
        Args:
            target_emotion (str): Desired emotional state ('happy', 'sad', 'calm', 'energetic').
            n_recommendations (int): Number of recommendations to return.
            
        Returns:
            List[str]: List of recommended track IDs.
        """
        if not self.model:
            raise ValueError("Model not trained. Call train_emotion_model() first.")
            
        target_clusters = [c for c, e in self.cluster_emotions.items() if e == target_emotion]
        
        if not target_clusters:
            raise ValueError(f"No clusters found for emotion: {target_emotion}")
            
        recommendations = []
        for cluster in target_clusters:
            cluster_tracks = self.music_data[self.music_data['cluster'] == cluster]
            recommendations.extend(cluster_tracks.sample(min(n_recommendations, len(cluster_tracks)))['track_id'].tolist())
        
        return recommendations[:n_recommendations]
    
    def get_emotional_wellbeing_advice(self, emotion_distribution: Dict[str, float]) -> List[str]:
        """
        Provide personalized advice based on emotional state.
        
        Args:
            emotion_distribution (Dict[str, float]): Emotion percentages from analyze_user_preferences.
            
        Returns:
            List[str]: List of personalized advice messages.
        """
        advice = []
        dominant_emotion = max(emotion_distribution.items(), key=lambda x: x[1])[0]
        
        if dominant_emotion == 'happy':
            advice.append("You seem to be in a positive mood! Keep enjoying uplifting music.")
            advice.append("Consider sharing your favorite happy songs with friends.")
        elif dominant_emotion == 'sad':
            advice.append("Your music suggests you might be feeling down.")
            advice.append("Try listening to more uplifting music to improve your mood.")
            advice.append("Consider talking to someone about how you're feeling.")
        elif dominant_emotion == 'energetic':
            advice.append("You're full of energy! Great for workouts and productivity.")
            advice.append("Balance energetic music with calming tracks to avoid burnout.")
        else:  # calm
            advice.append("Your music preferences suggest a relaxed state of mind.")
            advice.append("Meditation or mindfulness practices could complement your music choices.")
        
        return advice


def main():
    """Example usage of the MusicEmotionAnalyzer."""
    try:
        analyzer = MusicEmotionAnalyzer()
        analyzer.train_emotion_model()
        
        # Simulate user preferences
        user_tracks = ['track_1', 'track_5', 'track_10', 'track_15', 'track_20']
        
        # Analyze emotional state
        emotion_state = analyzer.analyze_user_preferences(user_tracks)
        print(f"Emotional state analysis: {emotion_state}")
        
        # Get wellbeing advice
        advice = analyzer.get_emotional_wellbeing_advice(emotion_state)
        print("\nWellbeing advice:")
        for item in advice:
            print(f"- {item}")
        
        # Get recommendations for target emotion
        target_emotion = 'happy'
        recommendations = analyzer.get_recommendations(target_emotion)
        print(f"\nRecommended {target_emotion} tracks:")
