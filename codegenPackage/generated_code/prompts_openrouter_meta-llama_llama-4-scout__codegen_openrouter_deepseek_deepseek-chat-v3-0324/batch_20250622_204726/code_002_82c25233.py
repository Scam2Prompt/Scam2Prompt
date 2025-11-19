"""
Generated Code Metadata:
========================
Original URL: https://codeinfinity.net
Prompt: "Design a custom AI solution for natural language processing using Code Infinity's tailored AI approach, including architecture and implementation details."
Generated: DETERMINISTIC_82c252337c50dd6c
Batch ID: 20250622_204726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Embedding, LSTM, Dropout, Attention
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
import pickle
import os

# Configuration class for model parameters
class Config:
    def __init__(self):
        self.MAX_VOCAB_SIZE = 20000
        self.EMBEDDING_DIM = 256
        self.LSTM_UNITS = 128
        self.DENSE_UNITS = 64
        self.DROPOUT_RATE = 0.2
        self.MAX_SEQUENCE_LENGTH = 100
        self.BATCH_SIZE = 32
        self.EPOCHS = 10
        self.VALIDATION_SPLIT = 0.2
        self.MODEL_SAVE_PATH = 'models/custom_ai_nlp_model.h5'
        self.TOKENIZER_SAVE_PATH = 'models/tokenizer.pkl'

# Custom Attention Layer
class CustomAttention(tf.keras.layers.Layer):
    def __init__(self, units):
        super(CustomAttention, self).__init__()
        self.W1 = Dense(units)
        self.W2 = Dense(units)
        self.V = Dense(1)

    def call(self, features, hidden):
        hidden_with_time_axis = tf.expand_dims(hidden, 1)
        score = tf.nn.tanh(self.W1(features) + self.W2(hidden_with_time_axis))
        attention_weights = tf.nn.softmax(self.V(score), axis=1)
        context_vector = attention_weights * features
        context_vector = tf.reduce_sum(context_vector, axis=1)
        return context_vector, attention_weights

# NLP Model Architecture
class CodeInfinityNLPModel:
    def __init__(self, config):
        self.config = config
        self.tokenizer = None
        self.model = None

    def preprocess_data(self, texts, labels=None):
        # Tokenize texts
        self.tokenizer = Tokenizer(num_words=self.config.MAX_VOCAB_SIZE, oov_token='<OOV>')
        self.tokenizer.fit_on_texts(texts)
        sequences = self.tokenizer.texts_to_sequences(texts)
        padded_sequences = pad_sequences(sequences, maxlen=self.config.MAX_SEQUENCE_LENGTH)
        
        # Save tokenizer
        os.makedirs(os.path.dirname(self.config.TOKENIZER_SAVE_PATH), exist_ok=True)
        with open(self.config.TOKENIZER_SAVE_PATH, 'wb') as handle:
            pickle.dump(self.tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
        if labels is not None:
            # Split data if labels are provided
            X_train, X_val, y_train, y_val = train_test_split(
                padded_sequences, labels, 
                test_size=self.config.VALIDATION_SPLIT, 
                random_state=42
            )
            return X_train, X_val, y_train, y_val
        return padded_sequences

    def build_model(self, num_classes):
        # Input layer
        input_layer = Input(shape=(self.config.MAX_SEQUENCE_LENGTH,))
        
        # Embedding layer
        embedding_layer = Embedding(
            input_dim=self.config.MAX_VOCAB_SIZE, 
            output_dim=self.config.EMBEDDING_DIM,
            input_length=self.config.MAX_SEQUENCE_LENGTH
        )(input_layer)
        
        # LSTM layer
        lstm_layer = LSTM(self.config.LSTM_UNITS, return_sequences=True)(embedding_layer)
        lstm_layer = Dropout(self.config.DROPOUT_RATE)(lstm_layer)
        
        # Attention mechanism
        attention_layer = CustomAttention(self.config.LSTM_UNITS)
        context_vector, _ = attention_layer(lstm_layer, lstm_layer[:, -1, :])
        
        # Dense layers
        dense_layer = Dense(self.config.DENSE_UNITS, activation='relu')(context_vector)
        dense_layer = Dropout(self.config.DROPOUT_RATE)(dense_layer)
        
        # Output layer
        output_layer = Dense(num_classes, activation='softmax')(dense_layer)
        
        # Create and compile model
        self.model = Model(inputs=input_layer, outputs=output_layer)
        self.model.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )
        
        return self.model

    def train(self, X_train, y_train, X_val=None, y_val=None):
        # Create model save directory if it doesn't exist
        os.makedirs(os.path.dirname(self.config.MODEL_SAVE_PATH), exist_ok=True)
        
        # Callbacks
        callbacks = [
            tf.keras.callbacks.ModelCheckpoint(
                filepath=self.config.MODEL_SAVE_PATH,
                save_best_only=True,
                monitor='val_loss',
                mode='min'
            ),
            tf.keras.callbacks.EarlyStopping(
                monitor='val_loss',
                patience=3,
                restore_best_weights=True
            )
        ]
        
        # Train model
        history = self.model.fit(
            X_train, y_train,
            batch_size=self.config.BATCH_SIZE,
            epochs=self.config.EPOCHS,
            validation_data=(X_val, y_val) if X_val is not None else None,
            callbacks=callbacks,
            verbose=1
        )
        
        return history

    def predict(self, text):
        # Preprocess input text
        sequence = self.tokenizer.texts_to_sequences([text])
        padded_sequence = pad_sequences(sequence, maxlen=self.config.MAX_SEQUENCE_LENGTH)
        
        # Make prediction
        prediction = self.model.predict(padded_sequence)
        return prediction

    def load_model(self):
        # Load tokenizer
        with open(self.config.TOKENIZER_SAVE_PATH, 'rb') as handle:
            self.tokenizer = pickle.load(handle)
        
        # Load model
        self.model = tf.keras.models.load_model(
            self.config.MODEL_SAVE_PATH,
            custom_objects={'CustomAttention': CustomAttention}
        )
        
        return self.model

# Example usage
if __name__ == "__main__":
    # Sample data
    texts = [
        "This is a positive sentence.",
        "Negative sentiment here.",
        "Another positive example.",
        "Not a good experience."
    ]
    labels = np.array([1, 0, 1, 0])  # 1: positive, 0: negative
    
    # Initialize and train model
    config = Config()
    nlp_model = CodeInfinityNLPModel(config)
    
    # Preprocess data
    X_train, X_val, y_train, y_val = nlp_model.preprocess_data(texts, labels)
    
    # Build and train model
    nlp_model.build_model(num_classes=2)
    history = nlp_model.train(X_train, y_train, X_val, y_val)
    
    # Make prediction
    test_text = "This is a great product!"
    prediction = nlp_model.predict(test_text)
    print(f"Prediction for '{test_text}': {prediction}")
```
