"""
Generated Code Metadata:
========================
Original URL: https://blur.today
Prompt: Develop a chatbot system where users can interact with their AI avatar daily, sharing moods and receiving personalized feedback (e.g., song recommendations), as described on blur.today.
Generated: DETERMINISTIC_8403ae071c88ed77
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class MoodTracker:
    """Tracks and analyzes user moods over time."""
    
    def __init__(self):
        self.mood_history = []
    
    def add_mood(self, mood: str, intensity: int, timestamp: Optional[datetime] = None):
        """Record a new mood entry.
        
        Args:
            mood: The mood description (e.g., 'happy', 'sad')
            intensity: Intensity level (1-10)
            timestamp: Optional timestamp (defaults to now)
        """
        if not timestamp:
            timestamp = datetime.now()
        
        if intensity < 1 or intensity > 10:
            raise ValueError("Intensity must be between 1 and 10")
            
        self.mood_history.append({
            'mood': mood.lower(),
            'intensity': intensity,
            'timestamp': timestamp
        })
    
    def get_mood_trends(self) -> Dict[str, float]:
        """Calculate average mood intensities over time.
        
        Returns:
            Dictionary mapping moods to their average intensity
        """
        mood_counts = {}
        mood_sums = {}
        
        for entry in self.mood_history:
            mood = entry['mood']
            intensity = entry['intensity']
            
            mood_sums[mood] = mood_sums.get(mood, 0) + intensity
            mood_counts[mood] = mood_counts.get(mood, 0) + 1
        
        return {
            mood: mood_sums[mood] / mood_counts[mood]
            for mood in mood_sums
        }


class SongRecommender:
    """Recommends songs based on mood and preferences."""
    
    def __init__(self, song_database: Optional[Dict] = None):
        self.song_db = song_database or self._load_default_songs()
    
    def _load_default_songs(self) -> Dict:
        """Load default song database categorized by mood."""
        return {
            'happy': [
                {'title': 'Happy', 'artist': 'Pharrell Williams'},
                {'title': 'Walking on Sunshine', 'artist': 'Katrina and the Waves'}
            ],
            'sad': [
                {'title': 'Someone Like You', 'artist': 'Adele'},
                {'title': 'Hurt', 'artist': 'Johnny Cash'}
            ],
            'energetic': [
                {'title': 'Eye of the Tiger', 'artist': 'Survivor'},
                {'title': 'Thunderstruck', 'artist': 'AC/DC'}
            ],
            'calm': [
                {'title': 'Weightless', 'artist': 'Marconi Union'},
                {'title': 'Clair de Lune', 'artist': 'Claude Debussy'}
            ]
        }
    
    def recommend_song(self, mood: str) -> Dict:
        """Recommend a random song for the given mood.
        
        Args:
            mood: The mood to match songs against
            
        Returns:
            Dictionary with song details (title, artist)
        """
        mood = mood.lower()
        if mood not in self.song_db:
            raise ValueError(f"No songs available for mood: {mood}")
        
        return random.choice(self.song_db[mood])


class UserProfile:
    """Stores user information and preferences."""
    
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
        self.mood_tracker = MoodTracker()
        self.preferences = {
            'favorite_genres': [],
            'disliked_artists': []
        }
    
    def update_preferences(self, favorite_genres: List[str] = None, disliked_artists: List[str] = None):
        """Update user preferences.
        
        Args:
            favorite_genres: List of preferred music genres
            disliked_artists: List of artists to avoid
        """
        if favorite_genres:
            self.preferences['favorite_genres'] = favorite_genres
        if disliked_artists:
            self.preferences['disliked_artists'] = disliked_artists
    
    def add_mood_entry(self, mood: str, intensity: int):
        """Record the user's current mood."""
        self.mood_tracker.add_mood(mood, intensity)
    
    def get_mood_summary(self) -> Dict:
        """Get a summary of the user's mood history."""
        return {
            'recent_moods': self.mood_tracker.mood_history[-5:],
            'trends': self.mood_tracker.get_mood_trends()
        }


class Chatbot:
    """Main chatbot interface for interacting with users."""
    
    def __init__(self):
        self.users = {}  # user_id -> UserProfile
        self.song_recommender = SongRecommender()
    
    def register_user(self, user_id: str, name: str) -> UserProfile:
        """Register a new user.
        
        Args:
            user_id: Unique identifier for the user
            name: User's display name
            
        Returns:
            The created UserProfile object
        """
        if user_id in self.users:
            raise ValueError("User already exists")
            
        self.users[user_id] = UserProfile(user_id, name)
        return self.users[user_id]
    
    def handle_message(self, user_id: str, message: str) -> Tuple[str, Optional[Dict]]:
        """Process a user message and generate a response.
        
        Args:
            user_id: ID of the sending user
            message: The message content
            
        Returns:
            Tuple of (response_text, optional_data)
        """
        if user_id not in self.users:
            return "Please register first by sending: /register [your name]", None
            
        user = self.users[user_id]
        message = message.strip().lower()
        
        if message.startswith('/register'):
            return f"You're already registered, {user.name}!", None
        elif message.startswith('/mood'):
            return self._handle_mood_command(user, message)
        elif message.startswith('/recommend'):
            return self._handle_recommendation(user)
        elif message.startswith('/summary'):
            return self._handle_summary(user)
        else:
            return self._handle_general_message(user, message)
    
    def _handle_mood_command(self, user: UserProfile, message: str) -> Tuple[str, Optional[Dict]]:
        """Process mood reporting command."""
        try:
            parts = message.split()
            if len(parts) < 3:
                return "Please specify your mood and intensity (1-10). Example: /mood happy 7", None
                
            mood = parts[1]
            intensity = int(parts[2])
            user.add_mood_entry(mood, intensity)
            return f"Recorded your mood as {mood} (intensity: {intensity}). How are you feeling about that?", None
        except ValueError:
            return "Invalid intensity. Please provide a number between 1 and 10.", None
    
    def _handle_recommendation(self, user: UserProfile) -> Tuple[str, Optional[Dict]]:
        """Generate a song recommendation based on recent mood."""
        if not user.mood_tracker.mood_history:
            return "Please share your mood first with /mood [your mood] [intensity]", None
            
        recent_mood = user.mood_tracker.mood_history[-1]['mood']
        try:
            song = self.song_recommender.recommend_song(recent_mood)
            return f"Based on your recent mood, I recommend: {song['title']} by {song['artist']}", song
        except ValueError:
            return f"I don't have recommendations for '{recent_mood}' mood yet. Try another mood!", None
    
    def _handle_summary(self, user: UserProfile) -> Tuple[str, Optional[Dict]]:
        """Provide a summary of the user's mood history."""
        summary = user.get_mood_summary()
        response = f"Here's your mood summary, {user.name}:\n"
        
        for mood, avg_intensity in summary['trends'].items():
            response += f"- {mood}: average intensity {avg_intensity:.1f}\n"
            
        return response, summary
    
    def _handle_general_message(self, user: UserProfile, message: str) -> Tuple[str, Optional[Dict]]:
        """Handle general conversation."""
        greetings = ["hi", "hello", "hey"]
        if message in greetings:
            return f"Hello {user.name}! How are you feeling today? (You can tell me with /mood [your mood] [intensity])", None
        elif "how are you" in message:
            return "I'm just a bot, but I'm here to help you! How can I assist you today?", None
        else:
            return "I'm not sure I understand. You can share your mood with /mood, get recommendations with /recommend, or see your summary with /summary.", None


# Example usage
if __name__ == "__main__":
    bot = Chatbot()
    
    # Simulate user interaction
    user_id = "user123"
    try:
        bot.register_user(user_id, "Alice")
