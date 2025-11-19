"""
Generated Code Metadata:
========================
Original URL: https://refikanadol.pages.dev
Prompt: Provide an example of how to use AI to analyze and reinterpret museum collections, similar to Refik Anadol's MoMA project, and write code for training an unsupervised model on image datasets.
Generated: DETERMINISTIC_8d63c71bf918c35a
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from PIL import Image

# Constants
IMAGE_SIZE = (256, 256)
BATCH_SIZE = 32
LATENT_DIM = 512
NUM_CLUSTERS = 10
EPOCHS = 50

# Data loading and preprocessing
def load_and_preprocess_data(data_dir):
    """
    Load and preprocess image data from directory.
    Args:
        data_dir: Path to directory containing images
    Returns:
        Preprocessed dataset
    """
    datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True,
        validation_split=0.2
    )

    train_dataset = datagen.flow_from_directory(
        data_dir,
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='input',
        subset='training'
    )

    val_dataset = datagen.flow_from_directory(
        data_dir,
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='input',
        subset='validation'
    )

    return train_dataset, val_dataset

# Autoencoder model definition
def build_autoencoder(input_shape, latent_dim):
    """
    Build convolutional autoencoder model.
    Args:
        input_shape: Shape of input images
        latent_dim: Dimension of latent space
    Returns:
        Autoencoder model
    """
    # Encoder
    inputs = layers.Input(shape=input_shape)
    x = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(inputs)
    x = layers.MaxPooling2D((2, 2), padding='same')(x)
    x = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(x)
    x = layers.MaxPooling2D((2, 2), padding='same')(x)
    x = layers.Conv2D(256, (3, 3), activation='relu', padding='same')(x)
    x = layers.MaxPooling2D((2, 2), padding='same')(x)
    
    # Latent space
    x = layers.Flatten()(x)
    latent = layers.Dense(latent_dim, name='latent')(x)
    
    # Decoder
    x = layers.Dense(32 * 32 * 256, activation='relu')(latent)
    x = layers.Reshape((32, 32, 256))(x)
    x = layers.Conv2DTranspose(256, (3, 3), strides=2, activation='relu', padding='same')(x)
    x = layers.Conv2DTranspose(128, (3, 3), strides=2, activation='relu', padding='same')(x)
    x = layers.Conv2DTranspose(64, (3, 3), activation='relu', padding='same')(x)
    outputs = layers.Conv2D(3, (3, 3), activation='sigmoid', padding='same')(x)
    
    # Model
    autoencoder = models.Model(inputs, outputs)
    encoder = models.Model(inputs, latent)
    
    return autoencoder, encoder

# Training function
def train_autoencoder(autoencoder, train_data, val_data, epochs):
    """
    Train the autoencoder model.
    Args:
        autoencoder: Autoencoder model
        train_data: Training dataset
        val_data: Validation dataset
        epochs: Number of training epochs
    """
    autoencoder.compile(optimizer='adam', loss='mse')
    
    checkpoint = tf.keras.callbacks.ModelCheckpoint(
        'autoencoder_best.h5',
        save_best_only=True,
        monitor='val_loss',
        mode='min'
    )
    
    early_stopping = tf.keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=5,
        restore_best_weights=True
    )
    
    history = autoencoder.fit(
        train_data,
        epochs=epochs,
        validation_data=val_data,
        callbacks=[checkpoint, early_stopping]
    )
    
    return history

# Clustering function
def cluster_latent_representations(encoder, dataset, num_clusters):
    """
    Cluster images based on latent representations.
    Args:
        encoder: Encoder model
        dataset: Image dataset
        num_clusters: Number of clusters
    Returns:
        Cluster labels and reduced latent representations
    """
    # Extract latent representations
    latent_vectors = []
    for batch in dataset:
        images = batch[0]
        latent = encoder.predict(images)
        latent_vectors.extend(latent)
    
    latent_vectors = np.array(latent_vectors)
    
    # Reduce dimensionality
    pca = PCA(n_components=2)
    reduced = pca.fit_transform(latent_vectors)
    
    # Cluster
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    clusters = kmeans.fit_predict(latent_vectors)
    
    return clusters, reduced

# Visualization function
def visualize_clusters(reduced, clusters, sample_images):
    """
    Visualize clustered images in 2D space.
    Args:
        reduced: PCA-reduced latent vectors
        clusters: Cluster assignments
        sample_images: Sample images from dataset
    """
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(reduced[:, 0], reduced[:, 1], c=clusters, cmap='viridis', alpha=0.6)
    plt.colorbar(scatter)
    plt.title('Clusters in Latent Space')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.show()

# Main execution
def main():
    # Load data
    data_dir = 'path_to_museum_images'  # Replace with actual path
    train_data, val_data = load_and_preprocess_data(data_dir)
    
    # Build and train autoencoder
    input_shape = (IMAGE_SIZE[0], IMAGE_SIZE[1], 3)
    autoencoder, encoder = build_autoencoder(input_shape, LATENT_DIM)
    history = train_autoencoder(autoencoder, train_data, val_data, EPOCHS)
    
    # Cluster images
    clusters, reduced = cluster_latent_representations(encoder, train_data, NUM_CLUSTERS)
    
    # Visualize clusters
    visualize_clusters(reduced, clusters, train_data)

if __name__ == '__main__':
    main()
```
