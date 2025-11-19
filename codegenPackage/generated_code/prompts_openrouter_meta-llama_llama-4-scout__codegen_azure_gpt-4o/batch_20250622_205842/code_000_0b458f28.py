"""
Generated Code Metadata:
========================
Original URL: https://threeprotocol-claimreward.pages.dev
Prompt: "Write a Python code snippet using Neural Network AI (specifically BERT, CNNs, RNNs, Siamese networks, and GNNs) for product matching in an eCommerce marketplace, considering user queries, product images, and reviews."
Generated: DETERMINISTIC_0b458f281e9c46b1
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import torch
from transformers import BertTokenizer, BertModel
from torch import nn
from torchvision import models, transforms
from torch_geometric.nn import GCNConv
from torch_geometric.data import Data
from sklearn.metrics.pairwise import cosine_similarity

# Define constants
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
MAX_SEQ_LENGTH = 128

# Load BERT model and tokenizer for text embeddings
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
bert_model = BertModel.from_pretrained("bert-base-uncased").to(DEVICE)

# Define CNN for image embeddings
class ImageCNN(nn.Module):
    def __init__(self):
        super(ImageCNN, self).__init__()
        self.model = models.resnet50(pretrained=True)
        self.model.fc = nn.Identity()  # Remove the classification layer

    def forward(self, x):
        return self.model(x)

image_cnn = ImageCNN().to(DEVICE)

# Define RNN for review embeddings
class ReviewRNN(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_layers):
        super(ReviewRNN, self).__init__()
        self.rnn = nn.LSTM(input_dim, hidden_dim, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_dim, hidden_dim)

    def forward(self, x):
        _, (hidden, _) = self.rnn(x)
        return self.fc(hidden[-1])

review_rnn = ReviewRNN(input_dim=768, hidden_dim=256, num_layers=2).to(DEVICE)

# Define Siamese network for product matching
class SiameseNetwork(nn.Module):
    def __init__(self, embedding_dim):
        super(SiameseNetwork, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(embedding_dim * 2, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, 1),
            nn.Sigmoid()
        )

    def forward(self, embedding1, embedding2):
        combined = torch.cat((embedding1, embedding2), dim=1)
        return self.fc(combined)

siamese_network = SiameseNetwork(embedding_dim=256).to(DEVICE)

# Define GNN for graph-based product relationships
class ProductGNN(nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super(ProductGNN, self).__init__()
        self.conv1 = GCNConv(input_dim, hidden_dim)
        self.conv2 = GCNConv(hidden_dim, hidden_dim)

    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index).relu()
        x = self.conv2(x, edge_index).relu()
        return x

product_gnn = ProductGNN(input_dim=256, hidden_dim=128).to(DEVICE)

# Preprocessing functions
def preprocess_text(text):
    """Tokenize and encode text for BERT."""
    tokens = tokenizer(text, max_length=MAX_SEQ_LENGTH, padding="max_length", truncation=True, return_tensors="pt")
    return tokens["input_ids"].to(DEVICE), tokens["attention_mask"].to(DEVICE)

def preprocess_image(image):
    """Transform image for CNN."""
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    return transform(image).unsqueeze(0).to(DEVICE)

def preprocess_reviews(reviews):
    """Generate embeddings for reviews using BERT."""
    embeddings = []
    for review in reviews:
        input_ids, attention_mask = preprocess_text(review)
        with torch.no_grad():
            output = bert_model(input_ids, attention_mask=attention_mask)
        embeddings.append(output.last_hidden_state.mean(dim=1))
    return torch.stack(embeddings).to(DEVICE)

# Product matching function
def match_products(user_query, product_image, product_reviews, product_graph):
    """
    Match products based on user query, product image, reviews, and graph relationships.
    """
    # Text embedding from BERT
    input_ids, attention_mask = preprocess_text(user_query)
    with torch.no_grad():
        query_embedding = bert_model(input_ids, attention_mask=attention_mask).last_hidden_state.mean(dim=1)

    # Image embedding from CNN
    image_embedding = image_cnn(preprocess_image(product_image))

    # Review embedding from RNN
    review_embeddings = preprocess_reviews(product_reviews)
    review_embedding = review_rnn(review_embeddings)

    # Graph embedding from GNN
    graph_embedding = product_gnn(product_graph.x.to(DEVICE), product_graph.edge_index.to(DEVICE))

    # Combine embeddings
    combined_embedding = torch.cat((query_embedding, image_embedding, review_embedding, graph_embedding.mean(dim=0).unsqueeze(0)), dim=1)

    # Match products using Siamese network
    similarity_score = siamese_network(combined_embedding, combined_embedding)  # Example: comparing with itself
    return similarity_score.item()

# Example usage
if __name__ == "__main__":
    # Example data
    user_query = "Affordable smartphone with good camera"
    product_image = torch.zeros((3, 224, 224))  # Placeholder image tensor
    product_reviews = ["Great camera quality!", "Affordable price.", "Battery life could be better."]
    product_graph = Data(
        x=torch.rand((10, 256)),  # Node features
        edge_index=torch.tensor([[0, 1, 2, 3], [1, 2, 3, 4]])  # Edge list
    )

    # Match products
    score = match_products(user_query, product_image, product_reviews, product_graph)
    print(f"Product match score: {score}")
```
