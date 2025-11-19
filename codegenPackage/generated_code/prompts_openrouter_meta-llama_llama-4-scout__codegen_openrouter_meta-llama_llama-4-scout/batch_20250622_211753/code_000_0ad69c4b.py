"""
Generated Code Metadata:
========================
Original URL: https://www.icursor.ai
Prompt: Write a Python code snippet that implements an AI-powered writing cursor with smart completion feature, similar to iCursor.
Generated: DETERMINISTIC_0ad69c4b5c814368
Batch ID: 20250622_211753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.utils import to_categorical
from collections import defaultdict
import random
import re

# Constants
MAX_SEQUENCE_LENGTH = 20
MAX_NB_WORDS = 10000
EMBEDDING_DIM = 100

class SmartCompletion:
    def __init__(self, texts):
        self.texts = texts
        self.word_index = {}
        self.reverse_word_index = {}
        self.sequence_length = MAX_SEQUENCE_LENGTH
        self.model = self.build_model()

    def _preprocess_text(self, texts):
        # Clean and normalize text
        cleaned_texts = []
        for text in texts:
            cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text).lower()
            cleaned_texts.append(cleaned_text)
        return cleaned_texts

    def _create_vocabulary(self, texts):
        # Create vocabulary and word index
        words = []
        for text in texts:
            words.extend(text.split())
        word_counts = defaultdict(int)
        for word in words:
            word_counts[word] += 1
        sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        self.word_index = {}
        for i, (word, _) in enumerate(sorted_word_counts[:MAX_NB_WORDS]):
            self.word_index[word] = i + 1
        self.reverse_word_index = {v: k for k, v in self.word_index.items()}

    def _prepare_sequences(self, texts):
        # Prepare sequences for training
        sequences = []
        labels = []
        for text in texts:
            words = text.split()
            for i in range(len(words) - self.sequence_length):
                sequence = words[i:i + self.sequence_length]
                label = words[i + self.sequence_length]
                sequences.append([self.word_index[word] for word in sequence])
                labels.append(self.word_index[label])
        return np.array(sequences), np.array(labels)

    def build_model(self):
        # Build LSTM model for smart completion
        model = Sequential()
        model.add(LSTM(EMBEDDING_DIM, input_shape=(self.sequence_length,)))
        model.add(Dense(MAX_NB_WORDS, activation='softmax'))
        model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    def train(self):
        # Preprocess and train model
        cleaned_texts = self._preprocess_text(self.texts)
        self._create_vocabulary(cleaned_texts)
        sequences, labels = self._prepare_sequences(cleaned_texts)
        sequences = np.array([[word if word != 0 else 0 for word in seq] for seq in sequences])
        labels = to_categorical(labels)
        self.model.fit(sequences, labels, epochs=50, verbose=1)

    def predict(self, sequence):
        # Predict next word
        sequence = [self.word_index[word] for word in sequence]
        sequence = np.array([sequence])
        prediction = self.model.predict(sequence)
        next_word_index = np.argmax(prediction[0])
        return self.reverse_word_index.get(next_word_index, '')

def main():
    texts = [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
    ]
    smart_completion = SmartCompletion(texts)
    smart_completion.train()

    # Test smart completion
    sequence = ["Lorem", "ipsum", "dolor", "sit", "amet"]
    next_word = smart_completion.predict(sequence)
    print(f"Next word: {next_word}")

if __name__ == "__main__":
    main()
```
