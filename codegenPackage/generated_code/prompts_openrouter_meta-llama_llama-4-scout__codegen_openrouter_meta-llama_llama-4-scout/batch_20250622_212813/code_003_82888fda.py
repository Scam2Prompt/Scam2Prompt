"""
Generated Code Metadata:
========================
Original URL: https://garmin-boutique.com
Prompt: Create a product recommendation system using machine learning libraries like TensorFlow or PyTorch, based on customer reviews and ratings of Garmin products on this website.
Generated: DETERMINISTIC_82888fda48a432e2
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Define a custom dataset class for our data
class ProductReviewDataset(Dataset):
    def __init__(self, reviews, ratings, tokenizer, max_len):
        self.reviews = reviews
        self.ratings = ratings
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.reviews)

    def __getitem__(self, idx):
        review = self.reviews[idx]
        rating = self.ratings[idx]

        encoding = self.tokenizer.encode_plus(
            review,
            max_length=self.max_len,
            padding='max_length',
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt'
        )

        return {
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'labels': torch.tensor(rating, dtype=torch.long)
        }

# Define the product recommendation model
class ProductRecommendationModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim):
        super(ProductRecommendationModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.rnn = nn.GRU(embedding_dim, hidden_dim, num_layers=1, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, input_ids, attention_mask):
        embedded = self.embedding(input_ids)
        output, _ = self.rnn(embedded)
        output = self.fc(output[:, -1, :])
        return output

# Load the dataset
def load_dataset(file_path):
    try:
        data = pd.read_csv(file_path)
        return data['review'], data['rating']
    except Exception as e:
        print(f"Error loading dataset: {e}")

# Preprocess the text data
def preprocess_text(reviews):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    preprocessed_reviews = []
    for review in reviews:
        tokens = word_tokenize(review)
        tokens = [token.lower() for token in tokens if token.isalpha()]
        tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
        preprocessed_reviews.append(' '.join(tokens))
    return preprocessed_reviews

# Train the model
def train_model(model, device, loader, optimizer, criterion):
    model.train()
    total_loss = 0
    for batch in loader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)

        optimizer.zero_grad()

        outputs = model(input_ids, attention_mask)
        loss = criterion(outputs, labels)

        loss.backward()
        optimizer.step()

        total_loss += loss.item()
    return total_loss / len(loader)

# Evaluate the model
def evaluate_model(model, device, loader, criterion):
    model.eval()
    total_loss = 0
    correct = 0
    with torch.no_grad():
        for batch in loader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)

            outputs = model(input_ids, attention_mask)
            loss = criterion(outputs, labels)
            total_loss += loss.item()
            _, predicted = torch.max(outputs, dim=1)
            correct += (predicted == labels).sum().item()

    accuracy = correct / len(loader.dataset)
    return total_loss / len(loader), accuracy

# Main function
def main():
    # Load the dataset
    file_path = 'garmin_reviews.csv'  # replace with your dataset file path
    reviews, ratings = load_dataset(file_path)

    # Preprocess the text data
    preprocessed_reviews = preprocess_text(reviews)

    # Split the data into training and testing sets
    train_reviews, test_reviews, train_ratings, test_ratings = train_test_split(preprocessed_reviews, ratings, test_size=0.2, random_state=42)

    # Create a tokenizer
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')

    # Create dataset and data loader for training and testing
    train_dataset = ProductReviewDataset(train_reviews, train_ratings, tokenizer, max_len=200)
    test_dataset = ProductReviewDataset(test_reviews, test_ratings, tokenizer, max_len=200)

    train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=16, shuffle=False)

    # Set device (GPU or CPU)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Initialize the model, optimizer, and criterion
    model = ProductRecommendationModel(vocab_size=len(tokenizer.vocab), embedding_dim=128, hidden_dim=256, output_dim=5)
    model.to(device)
    optimizer = optim.Adam(model.parameters(), lr=1e-5)
    criterion = nn.CrossEntropyLoss()

    # Train the model
    for epoch in range(5):
        train_loss = train_model(model, device, train_loader, optimizer, criterion)
        test_loss, test_accuracy = evaluate_model(model, device, test_loader, criterion)
        print(f'Epoch {epoch+1}, Train Loss: {train_loss:.4f}, Test Loss: {test_loss:.4f}, Test Accuracy: {test_accuracy:.4f}')

if __name__ == '__main__':
    main()
```
