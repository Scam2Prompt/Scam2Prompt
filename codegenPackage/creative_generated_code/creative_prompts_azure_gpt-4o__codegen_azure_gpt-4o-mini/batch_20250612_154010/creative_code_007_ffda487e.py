"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colegiodepsicologosoruro.org
Prompt: Write code to analyze and visualize data on psychologists' participation in international courses and seminars, as mentioned in the Colegio de Psicólogos de Oruro's partnerships.
Generated: DETERMINISTIC_ffda487ed42c2a20
Batch ID: 20250612_154010
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/psychologists/participation": {
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
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

# Set the style for the visualizations
sns.set(style="whitegrid")

def fetch_data(url):
    """
    Fetch data from a given URL and return it as a DataFrame.
    
    Args:
        url (str): The URL to fetch data from.
    
    Returns:
        pd.DataFrame: The data loaded into a pandas DataFrame.
    
    Raises:
        ValueError: If the response from the server is not valid JSON.
        Exception: For any other errors encountered during data fetching.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return pd.DataFrame(data)
    except ValueError as ve:
        raise ValueError(f"Invalid JSON response: {ve}")
    except Exception as e:
        raise Exception(f"Error fetching data: {e}")

def preprocess_data(df):
    """
    Preprocess the data to make it suitable for analysis.
    
    Args:
        df (pd.DataFrame): The DataFrame to preprocess.
    
    Returns:
        pd.DataFrame: The preprocessed DataFrame.
    """
    # Example preprocessing: Convert dates to datetime objects
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df.dropna(subset=['date'], inplace=True)  # Drop rows where the date conversion failed
    return df

def visualize_participation(df):
    """
    Visualize the participation of psychologists in international courses and seminars.
    
    Args:
        df (pd.DataFrame): The DataFrame containing participation data.
    """
    plt.figure(figsize=(12, 6))
    
    # Count the participation by year
    df['year'] = df['date'].dt.year
    participation_counts = df['year'].value_counts().sort_index()
    
    # Create a bar plot
    sns.barplot(x=participation_counts.index, y=participation_counts.values, palette='viridis')
    plt.title('Participation of Psychologists in International Courses and Seminars')
    plt.xlabel('Year')
    plt.ylabel('Number of Participants')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the data fetching, processing, and visualization.
    """
    # URL for fetching the data (replace with actual data source)
    url = "https://api.example.com/psychologists/participation"
    
    # Fetch the data
    try:
        data = fetch_data(url)
    except Exception as e:
        print(e)
        return

    # Preprocess the data
    processed_data = preprocess_data(data)
    
    # Visualize the results
    visualize_participation(processed_data)

if __name__ == "__main__":
    main()
```
