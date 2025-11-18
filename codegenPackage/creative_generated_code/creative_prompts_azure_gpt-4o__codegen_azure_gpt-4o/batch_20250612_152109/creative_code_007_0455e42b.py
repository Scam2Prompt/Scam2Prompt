"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpkad.lamongankab.go.id
Prompt: Write a script to calculate and visualize the Indeks Pengelolaan Keuangan Daerah (IPKD) based on the transparency documents mentioned on the BPKAD Lamongan website.
Generated: DETERMINISTIC_0455e42b6103d2d1
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import os

# Function to calculate IPKD based on transparency documents
def calculate_ipkd(data):
    """
    Calculates the IPKD (Indeks Pengelolaan Keuangan Daerah) based on input data.
    
    Arguments:
        data (pd.DataFrame): DataFrame containing transparency documents and their scores.
    
    Returns:
        pd.DataFrame: DataFrame with calculated IPKD for each region.
    """
    try:
        # Validate required columns exist
        required_columns = ['Region', 'Document Type', 'Score']
        for col in required_columns:
            if col not in data.columns:
                raise ValueError(f"Missing required column in data: {col}")

        # Group by region and calculate the average score
        ipkd_results = data.groupby('Region')['Score'].mean().reset_index()
        ipkd_results.rename(columns={'Score': 'IPKD Score'}, inplace=True)
        
        return ipkd_results
    except Exception as e:
        print(f"Error calculating IPKD: {str(e)}")
        return None


# Function to visualize IPKD scores
def visualize_ipkd(ipkd_data):
    """
    Visualizes the IPKD scores for each region using a bar chart.
    
    Arguments:
        ipkd_data (pd.DataFrame): DataFrame containing regions and their IPKD scores.
    """
    try:
        if 'Region' not in ipkd_data.columns or 'IPKD Score' not in ipkd_data.columns:
            raise ValueError("IPKD data must contain 'Region' and 'IPKD Score' columns.")
        
        # Plot a bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(ipkd_data['Region'], ipkd_data['IPKD Score'], color='skyblue')
        plt.xlabel('Region')
        plt.ylabel('IPKD Score')
        plt.title('Indeks Pengelolaan Keuangan Daerah (IPKD)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error visualizing IPKD: {str(e)}")


# Main function to handle data input and processing
def main():
    """
    Main function to calculate and visualize IPKD based on input data.
    """
    try:
        # File path to the example CSV file
        file_path = "transparency_documents.csv"
        
        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Load data from CSV
        data = pd.read_csv(file_path)
        
        # Calculate IPKD
        ipkd_data = calculate_ipkd(data)
        if ipkd_data is not None:
            print("IPKD Calculation Results:")
            print(ipkd_data)
            
            # Visualize IPKD
            visualize_ipkd(ipkd_data)
        else:
            print("Failed to calculate IPKD.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
