"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terminaltunja.com
Prompt: Create code to extract and visualize the "Ejecución presupuestal" data from the Terminal Tunja website using Python and Matplotlib.
Generated: DETERMINISTIC_0608a4e02a80bb71
Batch ID: 20250612_145913
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/ejecucion-presupuestal": {
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
from bs4 import BeautifulSoup

def fetch_data(url):
    """
    Fetch the HTML content from the specified URL.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        str: The HTML content of the webpage.

    Raises:
        Exception: If the request to the URL fails.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching data from {url}: {e}")

def parse_data(html):
    """
    Parse the HTML content to extract "Ejecución presupuestal" data.

    Args:
        html (str): The HTML content of the webpage.

    Returns:
        pd.DataFrame: A DataFrame containing the extracted data.
    """
    soup = BeautifulSoup(html, 'html.parser')
    
    # Assuming the data is in a table format
    table = soup.find('table')  # Modify this selector if necessary
    rows = table.find_all('tr')
    
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if cols:  # Avoid empty rows
            data.append(cols)

    # Create a DataFrame from the extracted data
    df = pd.DataFrame(data[1:], columns=data[0])  # Assuming the first row is the header
    return df

def visualize_data(df):
    """
    Visualize the "Ejecución presupuestal" data using Matplotlib.

    Args:
        df (pd.DataFrame): The DataFrame containing the data to visualize.
    """
    # Example: Assuming the DataFrame has 'Category' and 'Amount' columns
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')  # Convert to numeric
    df.dropna(subset=['Amount'], inplace=True)  # Drop rows with NaN

    # Create a bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(df['Category'], df['Amount'], color='blue')
    plt.title('Ejecución Presupuestal')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()  # Adjust layout to make room for rotated x labels
    plt.show()

def main():
    """
    Main function to execute the data extraction and visualization process.
    """
    url = 'https://example.com/ejecucion-presupuestal'  # Replace with the actual URL
    try:
        html_content = fetch_data(url)
        budget_data = parse_data(html_content)
        visualize_data(budget_data)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
