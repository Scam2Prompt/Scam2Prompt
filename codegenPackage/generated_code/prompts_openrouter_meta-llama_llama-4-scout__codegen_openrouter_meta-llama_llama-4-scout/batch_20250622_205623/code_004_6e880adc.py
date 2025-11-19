"""
Generated Code Metadata:
========================
Original URL: https://refikanadol.pages.dev
Prompt: Create a digital art piece using unsupervised machine learning, inspired by Refik Anadol's MoMA project, and describe the process in detail.
Generated: DETERMINISTIC_6e880adc9e1781a9
Batch ID: 20250622_205623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from PIL import Image
import os
import warnings
warnings.filterwarnings("ignore")

# Define constants
IMG_WIDTH, IMG_HEIGHT = 224, 224
LATENT_DIM = 128
EPOCHS = 100

# Load and preprocess dataset
def load_dataset(dataset_path):
    """Loads dataset from given path and preprocesses images"""
    img_datagen = ImageDataGenerator(preprocessing_function=preprocess_input,
                                     shear_range=0.2,
                                     zoom_range=0.2,
                                     horizontal_flip=True)
    img_generator = img_datagen.flow_from_directory(dataset_path,
                                                    target_size=(IMG_WIDTH, IMG_HEIGHT),
                                                    batch_size=32,
                                                    class_mode=None)
    return img_generator

# Create VGG16 model and extract features
def create_vgg16_model():
    """Creates VGG16 model and freezes its weights"""
    vgg16 = VGG16(weights='imagenet', include_top=False, input_shape=(IMG_WIDTH, IMG_HEIGHT, 3))
    vgg16.trainable = False
    return vgg16

def extract_features(vgg16, img_generator):
    """Extracts features from images using VGG16 model"""
    features = []
    for batch in img_generator:
        batch_features = vgg16.predict(batch[0])
        features.append(batch_features)
    features = np.concatenate(features, axis=0)
    return features

# Apply dimensionality reduction
def apply_pca(features, n_components):
    """Applies PCA to reduce dimensionality of features"""
    pca = PCA(n_components=n_components)
    reduced_features = pca.fit_transform(features)
    return reduced_features

def apply_tsne(features, n_components):
    """Applies t-SNE to reduce dimensionality of features"""
    tsne = TSNE(n_components=n_components, random_state=42)
    reduced_features = tsne.fit_transform(features)
    return reduced_features

# Generate digital art piece
def generate_art(reduced_features, output_path):
    """Generates digital art piece using reduced features"""
    plt.figure(figsize=(10, 10))
    plt.scatter(reduced_features[:, 0], reduced_features[:, 1], s=10, color='blue', alpha=0.5)
    plt.axis('off')
    plt.savefig(output_path, dpi=300)

# Main function
def main():
    dataset_path = 'path_to_your_dataset'
    output_path = 'art_piece.png'

    img_generator = load_dataset(dataset_path)
    vgg16 = create_vgg16_model()
    features = extract_features(vgg16, img_generator)

    pca_features = apply_pca(features, LATENT_DIM)
    tsne_features = apply_tsne(features, LATENT_DIM)

    generate_art(pca_features, 'pca_' + output_path)
    generate_art(tsne_features, 'tsne_' + output_path)

if __name__ == "__main__":
    main()
```
