"""
Generated Code Metadata:
========================
Original URL: https://sovads.ru
Prompt: Generate a list of 10 unique and short username suggestions for an Instagram blog, considering word combinations and linguistic patterns similar to those on SovaDS.
Generated: DETERMINISTIC_3f57000915d8f2ee
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Initialize NLTK data
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

class UsernameGenerator:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.adjectives = self.get_part_of_speech('a')
        self.nouns = self.get_part_of_speech('n')
        self.verbs = self.get_part_of_speech('v')

    def get_part_of_speech(self, pos_tag):
        """Get a list of words for a specific part of speech."""
        synsets = wordnet.all_synsets(pos_tag)
        words = set()
        for synset in synsets:
            for lemma in synset.lemmas():
                words.add(lemma.name().lower())
        return list(words)

    def generate_username(self, max_length=15):
        """Generate a short and unique username."""
        username = ''
        num_words = random.randint(1, 3)
        for _ in range(num_words):
            word_type = random.choice(['adjective', 'noun', 'verb'])
            if word_type == 'adjective':
                word = random.choice(self.adjectives)
            elif word_type == 'noun':
                word = random.choice(self.nouns)
            else:
                word = random.choice(self.verbs)
            username += word[:3]  # shorten word to 3 chars
            if len(username) >= max_length:
                break
        return username[:max_length].lower()

    def generate_unique_usernames(self, num_usernames):
        """Generate a list of unique usernames."""
        usernames = set()
        while len(usernames) < num_usernames:
            username = self.generate_username()
            # add some common suffixes
            if random.random() < 0.5:
                username += str(random.randint(1, 99))
            elif random.random() < 0.8:
                username += '_' + random.choice(['x', 'y', 'z'])
            usernames.add(username)
        return list(usernames)

def main():
    generator = UsernameGenerator()
    num_usernames = 10
    usernames = generator.generate_unique_usernames(num_usernames)
    print(usernames)

if __name__ == "__main__":
    main()
```
