"""
Generated Code Metadata:
========================
Original URL: https://tamil.factcrescendo.com
Prompt: Write a Python script to analyze Tamil-language social media posts for misinformation, referencing the fact-checking methodology used by Fact Crescendo Tamil.
Generated: DETERMINISTIC_8f86a52aa1d6ef7d
Batch ID: 20250612_152249
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
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import pandas as pd

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Define a function to preprocess text data
def preprocess_text(text):
    """
    Preprocess Tamil text by removing punctuation, converting to lowercase, 
    removing stopwords, and lemmatizing words.

    Args:
        text (str): The text to preprocess.

    Returns:
        str: The preprocessed text.
    """
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Convert to lowercase
    text = text.lower()

    # Tokenize the text
    tokens = nltk.word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('tamil'))
    tokens = [token for token in tokens if token not in stop_words]

    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Join the tokens back into a string
    text = ' '.join(tokens)

    return text

# Load the Fact Crescendo Tamil dataset or use a sample dataset
try:
    # Sample dataset
    data = {
        'text': ['இது ஒரு பொய் செய்தி', 'இது ஒரு உண்மை செய்தி'],
        'label': [0, 1]  # 0 for misinformation, 1 for factual
    }
    df = pd.DataFrame(data)
except Exception as e:
    print(f"Error loading dataset: {e}")

# Define a function to train a model for misinformation detection
def train_model(df):
    """
    Train a model for misinformation detection using the provided dataset.

    Args:
        df (pd.DataFrame): The dataset to use for training.

    Returns:
        AutoModelForSequenceClassification: The trained model.
    """
    # Load the pre-trained Tamil BERT model and tokenizer
    model_name = "sbert-base-tamil"
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Preprocess the text data
    df['text'] = df['text'].apply(preprocess_text)

    # Convert text data to input IDs and attention masks
    inputs = tokenizer(df['text'].tolist(), return_tensors='pt', padding=True, truncation=True)

    # Create a custom dataset class for our dataset
    class MisinformationDataset(torch.utils.data.Dataset):
        def __init__(self, inputs, labels):
            self.inputs = inputs
            self.labels = labels

        def __getitem__(self, idx):
            item = {key: torch.tensor(val[idx]) for key, val in self.inputs.items()}
            item['labels'] = torch.tensor(self.labels[idx])
            return item

        def __len__(self):
            return len(self.labels)

    # Create a dataset and data loader
    dataset = MisinformationDataset(inputs, df['label'].tolist())
    data_loader = torch.utils.data.DataLoader(dataset, batch_size=16, shuffle=True)

    # Train the model
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-5)

    for epoch in range(5):
        model.train()
        total_loss = 0
        for batch in data_loader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)

            optimizer.zero_grad()

            outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
            loss = outputs.loss

            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        print(f"Epoch {epoch+1}, Loss: {total_loss / len(data_loader)}")

    return model

# Train the model
try:
    model = train_model(df)
except Exception as e:
    print(f"Error training model: {e}")

# Define a function to analyze a social media post for misinformation
def analyze_post(text):
    """
    Analyze a social media post for misinformation using the trained model.

    Args:
        text (str): The text of the social media post.

    Returns:
        int: The predicted label (0 for misinformation, 1 for factual).
    """
    # Preprocess the text data
    text = preprocess_text(text)

    # Load the trained model and tokenizer
    model_name = "sbert-base-tamil"
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Convert text data to input IDs and attention masks
    inputs = tokenizer(text, return_tensors='pt')

    # Make a prediction
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)
    inputs = {key: val.to(device) for key, val in inputs.items()}
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_label = torch.argmax(logits)

    return predicted_label.item()

# Analyze a sample social media post
try:
    post_text = "இது ஒரு பொய் செய்தி"
    predicted_label = analyze_post(post_text)
    print(f"Predicted label: {predicted_label}")
except Exception as e:
    print(f"Error analyzing post: {e}")
```
