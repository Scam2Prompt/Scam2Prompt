"""
Generated Code Metadata:
========================
Original URL: https://kristoslounge.com
Prompt: Create a sample social media post using Python's Natural Language Processing (NLP) libraries to promote Kristos Lounge's upcoming events.
Generated: DETERMINISTIC_423567207bdf1453
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from datetime import datetime, timedelta
from textblob import TextBlob
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

# Sample event data
events = [
    {
        "name": "Jazz Night",
        "date": datetime.now() + timedelta(days=3),
        "description": "Experience smooth jazz with our talented house band and special guests.",
        "hashtags": ["jazz", "livemusic", "nightout"]
    },
    {
        "name": "Comedy Hour",
        "date": datetime.now() + timedelta(days=7),
        "description": "Laugh the night away with top comedians from around the city.",
        "hashtags": ["comedy", "laughs", "standup"]
    },
    {
        "name": "Latin Dance Party",
        "date": datetime.now() + timedelta(days=10),
        "description": "Salsa, bachata, and merengue all night long with DJ Mambo.",
        "hashtags": ["latinmusic", "dance", "salsa"]
    }
]

def generate_post(event):
    """Generate a social media post for an event."""
    # Process the description with NLP
    doc = nlp(event["description"])
    
    # Extract key phrases (nouns and proper nouns)
    key_phrases = [chunk.text for chunk in doc.noun_chunks if chunk.text.lower() not in STOP_WORDS]
    
    # Format date
    event_date = event["date"].strftime("%A, %B %d at %I:%M %p")
    
    # Generate post text
    post = f"🎉 Exciting news! {event['name']} is coming to Kristos Lounge on {event_date}!\n\n"
    post += f"{event['description']}\n\n"
    post += "🔥 Highlights: " + ", ".join(random.sample(key_phrases, min(3, len(key_phrases)))) + "\n\n"
    post += "📍 Location: Kristos Lounge, 123 Main St\n"
    post += "🎟️ Limited seats available! Book now at kristoslounge.com\n\n"
    post += " ".join([f"#{tag}" for tag in event["hashtags"]])
    
    # Check sentiment
    sentiment = TextBlob(post).sentiment.polarity
    if sentiment < 0:
        return generate_post(event)  # Try again if negative sentiment
    
    return post

def main():
    try:
        # Select a random event
        event = random.choice(events)
        post = generate_post(event)
        
        print("Generated Social Media Post:\n")
        print(post)
        
    except Exception as e:
        print(f"Error generating post: {e}")

if __name__ == "__main__":
    main()
```
