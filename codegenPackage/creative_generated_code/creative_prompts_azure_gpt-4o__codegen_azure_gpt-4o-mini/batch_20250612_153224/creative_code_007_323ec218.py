"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prgmea.pk
Prompt: Develop a recommendation system using machine learning to match buyers with suppliers listed on PRGMEA’s platform based on product categories and certifications.
Generated: DETERMINISTIC_323ec218fb11d5db
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import numpy as np
import joblib

# Load the dataset containing buyers and suppliers
def load_data(buyer_data_path, supplier_data_path):
    """
    Load buyer and supplier datasets from the specified CSV files.
    
    Parameters:
    buyer_data_path (str): Path to the buyer dataset CSV.
    supplier_data_path (str): Path to the supplier dataset CSV.
    
    Returns:
    pd.DataFrame, pd.DataFrame: DataFrames containing buyer and supplier data.
    """
    try:
        buyers = pd.read_csv(buyer_data_path)
        suppliers = pd.read_csv(supplier_data_path)
    except Exception as e:
        raise ValueError(f"Error loading data: {e}")
    
    return buyers, suppliers

# Preprocess the data
def preprocess_data(buyers, suppliers):
    """
    Preprocess the input data by handling missing values and encoding categorical variables.
    
    Parameters:
    buyers (pd.DataFrame): DataFrame containing buyer data.
    suppliers (pd.DataFrame): DataFrame containing supplier data.
    
    Returns:
    pd.DataFrame, pd.DataFrame: Preprocessed buyer and supplier DataFrames.
    """
    cat_features = ['product_category', 'certifications']
    
    # Imputer for handling missing values
    imputer = SimpleImputer(strategy='most_frequent')

    # OneHotEncoder for categorical features
    encoder = OneHotEncoder(handle_unknown='ignore')

    # Column transformer for preprocessing
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', Pipeline(steps=[
                ('imputer', imputer),
                ('encoder', encoder)
            ]), cat_features)
        ]
    )
    
    buyers_processed = preprocessor.fit_transform(buyers)
    suppliers_processed = preprocessor.fit_transform(suppliers)
    
    return buyers_processed, suppliers_processed

# Train the recommendation model
def train_model(buyers_data, suppliers_data):
    """
    Train a Nearest Neighbors model to recommend suppliers based on buyers' preferences.
    
    Parameters:
    buyers_data (np.ndarray): Preprocessed buyer data.
    suppliers_data (np.ndarray): Preprocessed supplier data.
    
    Returns:
    NearestNeighbors: Trained Nearest Neighbors model.
    """
    model = NearestNeighbors(n_neighbors=5, algorithm='auto')
    model.fit(suppliers_data)
    
    return model

# Make recommendations for a buyer
def recommend_suppliers(buyer_data, model, suppliers):
    """
    Recommend suppliers for a given buyer based on nearest neighbors.
    
    Parameters:
    buyer_data (np.ndarray): Preprocessed data for a specific buyer.
    model (NearestNeighbors): Trained recommendation model.
    suppliers (pd.DataFrame): DataFrame containing supplier data.
    
    Returns:
    pd.DataFrame: DataFrame of recommended suppliers.
    """
    distances, indices = model.kneighbors([buyer_data])
    recommended_indices = indices.flatten()
    
    return suppliers.iloc[recommended_indices]

# Save the model to disk
def save_model(model, model_path):
    """
    Save the trained model to disk for future use.
    
    Parameters:
    model: Trained model to save.
    model_path (str): Path where the model will be saved.
    """
    try:
        joblib.dump(model, model_path)
    except Exception as e:
        raise IOError(f"Error saving model: {e}")

# Load data files (assumed to be provided)
buyers, suppliers = load_data('buyers.csv', 'suppliers.csv')

# Preprocess the data
buyers_processed, suppliers_processed = preprocess_data(buyers, suppliers)

# Train the recommendation system model
model = train_model(buyers_processed, suppliers_processed)

# Save the trained model
save_model(model, 'supplier_recommendation_model.pkl')

# Example of making a recommendation for a new buyer
new_buyer_data = buyers_processed[0]  # Replace with actual new buyer data for real use
recommended_suppliers = recommend_suppliers(new_buyer_data, model, suppliers)

# Display recommended suppliers
print(recommended_suppliers)
```
