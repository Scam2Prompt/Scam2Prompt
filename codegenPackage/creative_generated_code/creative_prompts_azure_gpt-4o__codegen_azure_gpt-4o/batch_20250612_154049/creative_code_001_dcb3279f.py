"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://c0inbasewallet.com
Prompt: Create a Python script to scrape directory information from a webpage and store the details (name, last modified date, size) in a CSV file.
Generated: DETERMINISTIC_dcb3279fb5d19b2c
Batch ID: 20250612_154049
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# Function to fetch webpage content
def fetch_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")
        return None

# Function to parse directory information from webpage
def parse_directory_info(html_content):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        directory_data = []

        # Extract table rows from webpage containing directory information
        table_rows = soup.find_all('tr')
        for row in table_rows:
            cols = row.find_all('td')
            if len(cols) >= 3:  # Ensure there are enough columns
                name = cols[0].text.strip()
                last_modified = cols[1].text.strip()
                size = cols[2].text.strip()

                # Append extracted data to list
                directory_data.append({
                    'Name': name,
                    'Last Modified': last_modified,
                    'Size': size
                })
        return directory_data
    except Exception as e:
        print(f"Error parsing HTML content: {e}")
        return []

# Function to save extracted data to a CSV file
def save_to_csv(data, filename):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Last Modified', 'Size'])
            writer.writeheader()  # Write header to CSV file
            writer.writerows(data)  # Write rows
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving data to CSV file: {e}")

# Main function to handle the scraping process
def main():
    url = input("Enter the webpage URL to scrape: ").strip()
    html_content = fetch_webpage(url)

    if html_content:
        directory_data = parse_directory_info(html_content)

        if directory_data:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"directory_info_{timestamp}.csv"
            save_to_csv(directory_data, output_file)
        else:
            print("No directory information found on the webpage.")
    else:
        print("Failed to retrieve webpage content.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
