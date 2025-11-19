"""
Generated Code Metadata:
========================
Original URL: https://fatihinspira.com
Prompt: Develop a code example for a self-improvement chatbot that offers advice on building confidence and self-love, using natural language processing (NLP) techniques.
Generated: DETERMINISTIC_2211aedc1d4bcb29
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random
import json

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Load self-improvement advice data
with open('self_improvement_advice.json') as f:
    data = json.load(f)

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Define function to preprocess user input
def preprocess_input(input_text):
    # Tokenize input text
    tokens = word_tokenize(input_text)

    # Remove stopwords and lemmatize tokens
    filtered_tokens = []
    for token in tokens:
        token = lemmatizer.lemmatize(token.lower())
        if token not in stopwords.words('english'):
            filtered_tokens.append(token)

    return filtered_tokens

# Define function to get advice based on user input
def get_advice(input_text):
    try:
        # Preprocess user input
        input_tokens = preprocess_input(input_text)

        # Match input tokens with advice keywords
        best_match = None
        best_match_count = 0
        for advice in data['advice']:
            match_count = 0
            for keyword in advice['keywords']:
                if keyword in input_tokens:
                    match_count += 1
            if match_count > best_match_count:
                best_match = advice
                best_match_count = match_count

        # Return advice if a match is found
        if best_match:
            return random.choice(best_match['responses'])
        else:
            return "Sorry, I didn't understand that. Can you try again?"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Define chatbot function
def chatbot():
    print("Welcome to the self-improvement chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        advice = get_advice(user_input)
        print("Chatbot: ", advice)

# Run chatbot
if __name__ == "__main__":
    chatbot()
```

```json
// self_improvement_advice.json
{
    "advice": [
        {
            "keywords": ["confidence", "self-doubt"],
            "responses": [
                "Believe in yourself and your abilities. You got this!",
                "Remember that everyone has self-doubt. It's normal and temporary.",
                "Focus on your strengths and accomplishments."
            ]
        },
        {
            "keywords": ["self-love", "self-care"],
            "responses": [
                "Take care of your physical and mental health. It's essential.",
                "Practice self-compassion and be kind to yourself.",
                "Do things that make you happy and fulfilled."
            ]
        },
        {
            "keywords": ["motivation", "productivity"],
            "responses": [
                "Break down your goals into smaller, achievable tasks.",
                "Create a schedule and stick to it.",
                "Celebrate your small wins to stay motivated."
            ]
        }
    ]
}
```
