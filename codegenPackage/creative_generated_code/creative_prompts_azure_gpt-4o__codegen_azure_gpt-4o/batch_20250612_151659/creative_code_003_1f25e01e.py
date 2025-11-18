"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://embersft.costhentic.com
Prompt: Recommend libraries or APIs for tracking rarity tiers of Ember NFTs based on their 150+ traits and identifying rare 1/1 NFTs.
Generated: DETERMINISTIC_1f25e01ee875989a
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to use relevant libraries/APIs to analyze the rarity of Ember NFTs based on traits.
The code uses pandas for data manipulation and matplotlib for visualization. It provides modularity for working with
150+ traits and identifies rare 1/1 NFTs (unique tokens).

Requirements:
1. pandas - for data manipulation
2. matplotlib - for visualization
3. numpy - for statistical analysis
4. json - for loading NFT metadata

Install dependencies:
pip install pandas matplotlib numpy
"""

import pandas as pd
import numpy as np
import json
from matplotlib import pyplot as plt

# Function to load NFT metadata from a JSON file
def load_metadata(file_path):
    """
    Load NFT metadata from a JSON file.

    :param file_path: Path to the JSON file containing NFT metadata.
    :return: List of NFT metadata records.
    """
    try:
        with open(file_path, 'r') as file:
            metadata = json.load(file)
        return metadata
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON file.")
        return []

# Function to create a DataFrame from metadata
def create_dataframe(metadata):
    """
    Convert NFT metadata into a pandas DataFrame.

    :param metadata: List of NFT metadata records.
    :return: pandas DataFrame containing traits and other data.
    """
    try:
        return pd.DataFrame(metadata)
    except ValueError as e:
        print(f"Error: Failed to create DataFrame - {e}")
        return pd.DataFrame()

# Function to calculate rarity score based on trait frequency
def calculate_rarity_scores(df):
    """
    Calculate rarity scores for NFTs based on trait frequencies.

    :param df: pandas DataFrame containing NFT traits.
    :return: DataFrame with rarity scores added.
    """
    rarity_scores = []
    for _, row in df.iterrows():
        score = 0
        for trait, value in row.items():
            if trait != 'NFT_ID':  # Exclude NFT_ID column if present
                frequency = df[trait].value_counts().get(value, 0)
                score += 1 / frequency if frequency > 0 else 0
        rarity_scores.append(score)
    df['Rarity_Score'] = rarity_scores
    return df

# Function to identify rare 1/1 NFTs
def identify_unique_nfts(df):
    """
    Identify rare 1/1 NFTs based on trait uniqueness.

    :param df: pandas DataFrame containing NFT traits.
    :return: List of unique NFTs with rarity scores.
    """
    unique_nfts = []
    for _, row in df.iterrows():
        if df.loc[(df[1:] == row).all(axis=1)].shape[0] == 0:  # Check for uniqueness
            unique_nfts.append(row.to_dict())
    return unique_nfts

# Function to visualize rarity scores
def visualize_rarity_scores(df):
    """
    Create a histogram to visualize distributions of rarity scores.

    :param df: pandas DataFrame containing rarity scores.
    """
    plt.figure(figsize=(10, 6))
    plt.hist(df['Rarity_Score'], bins=20, color='skyblue', edgecolor='black')
    plt.title('NFT Rarity Score Distribution')
    plt.xlabel('Rarity Score')
    plt.ylabel('Frequency')
    plt.show()

# Main function to execute the rarity tracking process
def main():
    """
    Main function to execute rarity tracking for Ember NFTs.
    """
    # Load metadata from JSON file
    metadata = load_metadata('nft_metadata.json')
    if not metadata:
        return

    # Create a DataFrame from metadata
    nft_df = create_dataframe(metadata)
    if nft_df.empty:
        return

    # Calculate rarity scores for each NFT
    nft_df = calculate_rarity_scores(nft_df)
    print("Rarity scores added to DataFrame.")

    # Identify unique 1/1 NFTs
    unique_nfts = identify_unique_nfts(nft_df)
    print(f"Number of unique 1/1 NFTs identified: {len(unique_nfts)}")
    for nft in unique_nfts:
        print(nft)

    # Visualize rarity scores
    visualize_rarity_scores(nft_df)

# Entry point for the script
if __name__ == "__main__":
    main()
```
