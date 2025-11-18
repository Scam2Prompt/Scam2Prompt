"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getgrass-claim.pages.dev
Prompt: Write a Python program to clean and prepare structured datasets collected through a Grass-like network for AI model training purposes.
Generated: DETERMINISTIC_aa89e1751b185722
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import os


def load_dataset(file_path):
    """
    Load the dataset from the given file path. Supports CSV format.

    :param file_path: Path to the dataset file
    :return: DataFrame containing the dataset
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Load the dataset using pandas
    try:
        dataset = pd.read_csv(file_path)
    except Exception as e:
        raise ValueError(f"Error loading dataset: {e}")

    return dataset


def clean_dataset(df):
    """
    Clean the given DataFrame by handling missing values and 
    removing duplicates.

    :param df: Raw dataset as a DataFrame
    :return: Cleaned DataFrame
    """
    # Handle missing values: fill numeric columns with their mean and 
    # categorical columns with the mode
    for column in df.columns:
        if df[column].dtype in [np.float64, np.int64]:
            df[column].fillna(df[column].mean(), inplace=True)
        else:
            df[column].fillna(df[column].mode()[0], inplace=True)

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    return df


def encode_categorical_features(df):
    """
    Encode categorical features using one-hot encoding to prepare
    the dataset for AI training.

    :param df: Dataset containing categorical features
    :return: DataFrame with categorical features encoded
    """
    # Perform one-hot encoding for categorical columns
    df_encoded = pd.get_dummies(df, drop_first=True)
    return df_encoded


def scale_numeric_features(df):
    """
    Scale numeric features using Min-Max scaling for uniformity.

    :param df: Dataset containing numeric features
    :return: DataFrame with scaled numeric features
    """
    from sklearn.preprocessing import MinMaxScaler

    scaler = MinMaxScaler()
    numeric_columns = df.select_dtypes(include=[np.float64, np.int64]).columns
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

    return df


def prepare_dataset(file_path):
    """
    Complete pipeline to load, clean, encode, and scale dataset.

    :param file_path: Path to the dataset file
    :return: Prepared DataFrame ready for AI model training
    """
    try:
        # Load the dataset
        raw_data = load_dataset(file_path)

        # Clean the dataset
        cleaned_data = clean_dataset(raw_data)

        # Encode categorical features
        encoded_data = encode_categorical_features(cleaned_data)

        # Scale numeric features
        final_data = scale_numeric_features(encoded_data)

        return final_data
    except Exception as e:
        print(f"An error occurred while preparing the dataset: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    file_path = "example_dataset.csv"  # Replace with your dataset file path

    # Prepare the dataset for AI model training
    prepared_data = prepare_dataset(file_path)

    if prepared_data is not None:
        print("Dataset prepared successfully. Here are the first 5 rows:")
        print(prepared_data.head())
```
