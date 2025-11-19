"""
Generated Code Metadata:
========================
Original URL: https://sautikenya.com
Prompt: "Create a Python script to analyze the impact of advocacy campaigns on peace and governance in Kenya, using metrics such as community engagement and social media reach."
Generated: DETERMINISTIC_2b285c5dc216cc87
Batch ID: 20250622_205542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Configure logging for error handling and debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_data(file_path):
    """
    Load data from a CSV file into a Pandas DataFrame.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        logging.info("Data loaded successfully.")
        return data
    except FileNotFoundError:
        logging.error("File not found. Please check the file path.")
        raise
    except pd.errors.EmptyDataError:
        logging.error("File is empty. Please provide a valid CSV file.")
        raise
    except Exception as e:
        logging.error(f"An error occurred while loading the data: {e}")
        raise

def preprocess_data(data):
    """
    Preprocess the data by handling missing values and ensuring proper data types.
    
    Args:
        data (pd.DataFrame): Raw data.
    
    Returns:
        pd.DataFrame: Preprocessed data.
    """
    try:
        # Drop rows with missing values
        data = data.dropna()
        
        # Ensure proper data types
        data['Community Engagement'] = data['Community Engagement'].astype(float)
        data['Social Media Reach'] = data['Social Media Reach'].astype(int)
        data['Advocacy Campaign'] = data['Advocacy Campaign'].astype(str)
        
        logging.info("Data preprocessing completed successfully.")
        return data
    except KeyError as e:
        logging.error(f"Missing expected column in the data: {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred during preprocessing: {e}")
        raise

def analyze_data(data):
    """
    Analyze the impact of advocacy campaigns using metrics such as community engagement and social media reach.
    
    Args:
        data (pd.DataFrame): Preprocessed data.
    
    Returns:
        None
    """
    try:
        # Group data by advocacy campaign and calculate mean metrics
        campaign_analysis = data.groupby('Advocacy Campaign').mean()
        
        logging.info("Data analysis completed successfully.")
        print("Campaign Analysis:\n", campaign_analysis)
        
        # Visualize the data
        plt.figure(figsize=(10, 6))
        sns.barplot(
            x=campaign_analysis.index,
            y=campaign_analysis['Community Engagement'],
            palette='viridis'
        )
        plt.title('Average Community Engagement by Advocacy Campaign')
        plt.xlabel('Advocacy Campaign')
        plt.ylabel('Community Engagement')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        plt.figure(figsize=(10, 6))
        sns.barplot(
            x=campaign_analysis.index,
            y=campaign_analysis['Social Media Reach'],
            palette='magma'
        )
        plt.title('Average Social Media Reach by Advocacy Campaign')
        plt.xlabel('Advocacy Campaign')
        plt.ylabel('Social Media Reach')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        logging.error(f"An error occurred during analysis: {e}")
        raise

def main():
    """
    Main function to execute the script.
    """
    try:
        # File path to the dataset
        file_path = 'advocacy_campaigns_kenya.csv'
        
        # Load, preprocess, and analyze the data
        raw_data = load_data(file_path)
        preprocessed_data = preprocess_data(raw_data)
        analyze_data(preprocessed_data)
    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
```
