"""
Generated Code Metadata:
========================
Original URL: https://longhuigolf.com
Prompt: Create a script to analyze customer testimonials and extract key phrases about golf grip quality, similar to the feedback showcased on the Longhui Golf website.
Generated: DETERMINISTIC_0839d511e6e2ac5b
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize

# Download required NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def preprocess_text(text):
    """
    Preprocess the input text by converting to lowercase, removing special characters and digits,
    and tokenizing into sentences.
    """
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove special characters and digits
    sentences = sent_tokenize(text)  # Tokenize into sentences
    return sentences

def extract_key_phrases(sentences):
    """
    Extract key phrases from the given sentences by removing stopwords, lemmatizing words,
    and ranking phrases based on frequency.
    """
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    key_phrases = []

    for sentence in sentences:
        words = word_tokenize(sentence)  # Tokenize into words
        words = [word for word in words if word not in stop_words]  # Remove stopwords
        words = [lemmatizer.lemmatize(word) for word in words]  # Lemmatize words
        phrases = [' '.join(words[i:i+3]) for i in range(len(words)-2)]  # Extract phrases of up to 3 words
        key_phrases.extend(phrases)

    # Rank phrases by frequency
    phrase_freq = {}
    for phrase in key_phrases:
        if phrase in phrase_freq:
            phrase_freq[phrase] += 1
        else:
            phrase_freq[phrase] = 1

    # Filter phrases related to golf grip quality
    grip_quality_phrases = [phrase for phrase, freq in phrase_freq.items() if 'grip' in phrase or 'hold' in phrase or 'feel' in phrase]
    grip_quality_phrases.sort(key=lambda x: phrase_freq[x], reverse=True)  # Sort by frequency

    return grip_quality_phrases

def analyze_testimonials(testimonials):
    """
    Analyze customer testimonials and extract key phrases about golf grip quality.
    """
    key_phrases = []
    for testimonial in testimonials:
        sentences = preprocess_text(testimonial)
        phrases = extract_key_phrases(sentences)
        key_phrases.extend(phrases)

    # Remove duplicates and return top phrases
    unique_phrases = list(set(key_phrases))
    return sorted(unique_phrases, key=lambda x: key_phrases.count(x), reverse=True)

# Example usage
testimonials = [
    "I love the grip on my new golf clubs, it feels so comfortable in my hands.",
    "The grip quality is top-notch, I can hold the club with confidence.",
    "I've never felt a better grip on a golf club, it's amazing.",
    "The feel of the grip is fantastic, it's like an extension of my hand.",
    "I'm not a big fan of the grip, it feels a bit too thick for me."
]

key_phrases = analyze_testimonials(testimonials)
print("Key Phrases:")
for phrase in key_phrases:
    print(phrase)
```
