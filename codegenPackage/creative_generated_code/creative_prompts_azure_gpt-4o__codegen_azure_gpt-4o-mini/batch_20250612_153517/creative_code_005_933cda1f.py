"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openweb-3ua.pages.dev
Prompt: Develop a script to query and visualize the distribution of submitted artworks for Opepen's Permanent Collection using a blockchain-based API.
Generated: DETERMINISTIC_933cda1ffbd0b30f
Batch ID: 20250612_153517
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.opepen.xyz/permanent-collection": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for seaborn
sns.set(style="whitegrid")

def fetch_artworks(api_url):
    """
    Fetch the submitted artworks from the blockchain-based API.

    Parameters:
        api_url (str): The URL of the blockchain API.

    Returns:
        list: A list of artworks if successful, otherwise raises an exception.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        return response.json()  # Assuming the API returns JSON data
    except requests.exceptions.HTTPError as err:
        raise SystemExit(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        raise SystemExit(f"Error occurred while fetching data: {err}")

def process_artworks(data):
    """
    Process the artworks data to extract necessary information for visualization.

    Parameters:
        data (list): The list of artworks.

    Returns:
        pd.DataFrame: A DataFrame containing processed artworks data.
    """
    # Create a DataFrame from the list of artworks
    df = pd.DataFrame(data)

    # Ensure necessary columns are present
    if 'artist' not in df.columns or 'submission_date' not in df.columns:
        raise ValueError("Missing required columns in the artwork data")

    # Convert submission_date to datetime
    df['submission_date'] = pd.to_datetime(df['submission_date'])

    return df

def visualize_artwork_distribution(df):
    """
    Visualize the distribution of submitted artworks by artist.

    Parameters:
        df (pd.DataFrame): DataFrame containing processed artworks data.
    """
    # Count the number of submissions by artist
    artist_counts = df['artist'].value_counts()
    
    # Create a bar plot
    plt.figure(figsize=(12, 6))
    sns.barplot(x=artist_counts.index, y=artist_counts.values, palette='viridis')
    plt.title("Distribution of Submitted Artworks by Artist")
    plt.xlabel("Artist")
    plt.ylabel("Number of Submissions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the script.
    Fetches, processes, and visualizes the artworks data.
    """
    api_url = "https://api.opepen.xyz/permanent-collection"  # Replace with the actual API URL

    # Fetch artworks data
    artworks_data = fetch_artworks(api_url)

    # Process artworks data
    processed_df = process_artworks(artworks_data)

    # Visualize the distribution of submitted artworks
    visualize_artwork_distribution(processed_df)

if __name__ == "__main__":
    main()
```
