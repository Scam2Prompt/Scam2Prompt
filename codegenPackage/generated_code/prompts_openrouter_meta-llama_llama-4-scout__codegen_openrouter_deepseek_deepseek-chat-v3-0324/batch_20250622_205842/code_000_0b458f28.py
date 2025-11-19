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
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from transformers import BertModel, BertTokenizer
from torchvision import models, transforms
import numpy as np
from sklearn.metrics import accuracy_score, f1_score
import pandas as pd
from torch_geometric.nn import GCNConv
from torch_geometric.data import Data
import warnings
warnings.filterwarnings('ignore')

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Constants
MAX_LEN = 128
BATCH_SIZE = 32
EMBEDDING_DIM = 768
IMAGE_EMBEDDING_DIM = 2048
NUM_EPOCHS = 10
LEARNING_RATE = 1e-4

# Product Matching Dataset
class ProductMatchingDataset(Dataset):
    def __init__(self, queries, images, reviews, labels, tokenizer, image_transform):
        self.queries = queries
        self.images = images
        self.reviews = reviews
        self.labels = labels
        self.tokenizer = tokenizer
        self.image_transform = image_transform

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        query = self.queries[idx]
        review = self.reviews[idx]
        image = self.images[idx]
        label = self.labels[idx]

        # Process text with BERT tokenizer
        encoded_query = self.tokenizer.encode_plus(
            query,
            add_special_tokens=True,
            max_length=MAX_LEN,
            padding='max_length',
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt'
        )

        encoded_review = self.tokenizer.encode_plus(
            review,
            add_special_tokens=True,
            max_length=MAX_LEN,
            padding='max_length',
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt'
        )

        # Process image
        image = self.image_transform(image)

        return {
            'query_input_ids': encoded_query['input_ids'].squeeze(0),
            'query_attention_mask': encoded_query['attention_mask'].squeeze(0),
            'review_input_ids': encoded_review['input_ids'].squeeze(0),
            'review_attention_mask': encoded_review['attention_mask'].squeeze(0),
            'image': image,
            'label': torch.tensor(label, dtype=torch.long)
        }

# Text Encoder (BERT)
class TextEncoder(nn.Module):
    def __init__(self):
        super(TextEncoder, self).__init__()
        self.bert = BertModel.from_pretrained('bert-base-uncased')
        for param in self.bert.parameters():
            param.requires_grad = False

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = outputs.pooler_output
        return pooled_output

# Image Encoder (CNN)
class ImageEncoder(nn.Module):
    def __init__(self):
        super(ImageEncoder, self).__init__()
        self.cnn = models.resnet50(pretrained=True)
        for param in self.cnn.parameters():
            param.requires_grad = False
        self.cnn.fc = nn.Identity()

    def forward(self, x):
        return self.cnn(x)

# Review Encoder (RNN)
class ReviewEncoder(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_layers=1):
        super(ReviewEncoder, self).__init__()
        self.rnn = nn.GRU(input_dim, hidden_dim, num_layers, batch_first=True)
        
    def forward(self, x):
        _, hidden = self.rnn(x)
        return hidden.squeeze(0)

# Graph Neural Network for product relationships
class GNN(nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super(GNN, self).__init__()
        self.conv1 = GCNConv(input_dim, hidden_dim)
        self.conv2 = GCNConv(hidden_dim, hidden_dim)
        
    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = torch.relu(x)
        x = self.conv2(x, edge_index)
        return x

# Siamese Network for product matching
class SiameseNetwork(nn.Module):
    def __init__(self):
        super(SiameseNetwork, self).__init__()
        self.text_encoder = TextEncoder()
        self.image_encoder = ImageEncoder()
        self.review_encoder = ReviewEncoder(EMBEDDING_DIM, EMBEDDING_DIM)
        self.gnn = GNN(EMBEDDING_DIM, EMBEDDING_DIM)
        
        # Fusion layers
        self.fusion = nn.Sequential(
            nn.Linear(EMBEDDING_DIM * 2 + IMAGE_EMBEDDING_DIM, EMBEDDING_DIM),
            nn.ReLU(),
            nn.Dropout(0.2)
        )
        
        # Classifier
        self.classifier = nn.Sequential(
            nn.Linear(EMBEDDING_DIM, 256),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(256, 1),
            nn.Sigmoid()
        )

    def forward(self, query_input_ids, query_attention_mask, 
                review_input_ids, review_attention_mask, 
                image, edge_index=None, x=None):
        # Encode text
        query_embed = self.text_encoder(query_input_ids, query_attention_mask)
        review_embed = self.text_encoder(review_input_ids, review_attention_mask)
        
        # Encode image
        image_embed = self.image_encoder(image)
        
        # Encode reviews with RNN
        review_rnn_embed = self.review_encoder(review_embed.unsqueeze(1))
        
        # Optional GNN processing
        if edge_index is not None and x is not None:
            gnn_embed = self.gnn(x, edge_index)
            combined_embed = torch.cat([query_embed, review_rnn_embed, image_embed, gnn_embed], dim=1)
        else:
            combined_embed = torch.cat([query_embed, review_rnn_embed, image_embed], dim=1)
        
        # Fusion
        fused = self.fusion(combined_embed)
        
        # Classification
        output = self.classifier(fused)
        return output

# Training function
def train_model(model, dataloader, criterion, optimizer, device):
    model.train()
    total_loss = 0.0
    all_preds = []
    all_labels = []
    
    for batch in dataloader:
        query_input_ids = batch['query_input_ids'].to(device)
        query_attention_mask = batch['query_attention_mask'].to(device)
        review_input_ids = batch['review_input_ids'].to(device)
        review_attention_mask = batch['review_attention_mask'].to(device)
        image = batch['image'].to(device)
        labels = batch['label'].float().to(device)
        
        optimizer.zero_grad()
        
        outputs = model(
            query_input_ids, query_attention_mask,
            review_input_ids, review_attention_mask,
            image
        ).squeeze()
        
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
        preds = (outputs > 0.5).float()
        all_preds.extend(preds.cpu().detach().numpy())
        all_labels.extend(labels.cpu().detach().numpy())
    
    accuracy = accuracy_score(all_labels, all_preds)
    f1 = f1_score(all_labels, all_preds)
    avg_loss = total_loss / len(dataloader)
    
    return avg_loss, accuracy, f1

# Evaluation function
def evaluate_model(model, dataloader, criterion, device):
    model.eval()
    total_loss = 0.0
    all_preds = []
    all_labels = []
    
    with torch.no_grad():
        for batch in dataloader:
            query_input_ids = batch['query_input_ids'].to(device)
            query_attention_mask = batch['query_attention_mask'].to(device)
            review_input_ids = batch['review_input_ids'].to(device)
            review_attention_mask = batch['review_attention_mask'].to(device)
            image = batch['image'].to(device)
            labels = batch['label'].float().to(device)
            
            outputs = model(
                query_input_ids, query_attention_mask,
                review_input_ids, review_attention_mask,
                image
            ).squeeze()
            
            loss = criterion(outputs, labels)
            total_loss += loss.item()
            preds = (outputs > 0.
