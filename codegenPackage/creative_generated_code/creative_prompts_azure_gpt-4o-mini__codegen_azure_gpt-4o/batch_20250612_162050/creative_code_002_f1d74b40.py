"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agnedoveikaite.lt
Prompt: Write a Python script that analyzes user emotions and suggests personalized music playlists, reflecting the principles of emotional intelligence discussed by Agne Doveikaite.
Generated: DETERMINISTIC_f1d74b4045c99853
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Emotion-based Music Recommendation System
This script analyzes user emotions and suggests personalized music playlists based on emotional states.
It reflects principles of emotional intelligence discussed by Agne Doveikaite.
"""

import json
import random
import logging

# Set up logging for error handling
logging.basicConfig(
    format="%(levelname)s: %(message)s",
    level=logging.INFO
)

# Predefined playlists categorized by emotions
PLAYLISTS = {
    "happy": ["Happy Hits Playlist", "Feel-Good Songs", "Upbeat Pop"],
    "sad": ["Melancholic Tunes", "Acoustic Comfort", "Relaxing Piano"],
    "angry": ["Rock Anthem Playlist", "Heavy Metal Madness", "Distress Reliever"],
    "calm": ["Zen Chillout", "Meditation Melodies", "Nature Sounds"],
    "excited": ["Pump-Up Jams", "Dance Party Mix", "Celebration Songs"]
}

# Emotional analysis function
def analyze_emotion(user_input):
    """
    Analyze the user's input to determine their emotional state.

    :param user_input: str - Input describing the user's feelings
    :return: str - Detected emotion (key from PLAYLISTS), or None if not detected
    """
    # Keywords to detect emotions in user input
    emotion_keywords = {
        "happy": ["happy", "joyful", "excited", "content"],
        "sad": ["sad", "down", "melancholy", "heartbroken"],
        "angry": ["angry", "mad", "furious", "frustrated"],
        "calm": ["calm", "peaceful", "relaxed", "mindful"],
        "excited": ["excited", "energetic", "thrilled", "ecstatic"]
    }

    # Check keywords for each emotion
    for emotion, keywords in emotion_keywords.items():
        if any(keyword in user_input.lower() for keyword in keywords):
            return emotion

    return None  # Return None if no emotion is detected


def suggest_playlist(emotion):
    """
    Suggest a playlist based on the identified emotion.

    :param emotion: str - Emotional state detected
    :return: str - Playlist recommendation
    """
    try:
        if emotion in PLAYLISTS:
            return random.choice(PLAYLISTS[emotion])
        else:
            raise ValueError("Emotion not recognized in playlist database.")
    except ValueError as e:
        logging.error(e)
        return "We couldn't find a matching playlist. Try expressing your emotions more clearly."


def main():
    """
    Main function to run the emotion analysis and playlist recommendation system.
    """
    print("Welcome to the Emotion-Based Music Recommendation System!")
    print("Please describe how you're feeling today:")
    user_input = input("Your feelings: ")

    # Analyze user emotion
    emotion = analyze_emotion(user_input)
    if emotion:
        logging.info(f"Detected emotion: {emotion}")
        playlist = suggest_playlist(emotion)
        print(f"Based on your mood, we recommend: {playlist}")
    else:
        logging.warning("Could not detect any specific emotion.")
        print("Sorry, we couldn't detect your mood. Please try again using different words.")

    print("Thank you for using our service! Have a great day!")


# Run the script if executed directly
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
