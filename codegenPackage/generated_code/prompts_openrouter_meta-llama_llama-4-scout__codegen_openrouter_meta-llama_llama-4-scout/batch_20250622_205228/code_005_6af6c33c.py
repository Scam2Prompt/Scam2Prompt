"""
Generated Code Metadata:
========================
Original URL: https://consensys.world
Prompt: Write a script to extract and process e-commerce review data from various sources, including JSON files, CSV files, or databases.
Generated: DETERMINISTIC_6af6c33c4014e1b5
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import csv
import sqlite3
from typing import List, Dict

def extract_json_data(file_path: str) -> List[Dict]:
    """
    Extracts review data from a JSON file.

    Args:
    file_path (str): The path to the JSON file.

    Returns:
    List[Dict]: A list of dictionaries containing review data.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return []

def extract_csv_data(file_path: str) -> List[Dict]:
    """
    Extracts review data from a CSV file.

    Args:
    file_path (str): The path to the CSV file.

    Returns:
    List[Dict]: A list of dictionaries containing review data.
    """
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            data = list(csv_reader)
            return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except csv.Error as e:
        print(f"Error parsing CSV: {e}")
        return []

def extract_db_data(db_path: str, table_name: str) -> List[Dict]:
    """
    Extracts review data from a SQLite database.

    Args:
    db_path (str): The path to the SQLite database.
    table_name (str): The name of the table containing review data.

    Returns:
    List[Dict]: A list of dictionaries containing review data.
    """
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")
            columns = [description[0] for description in cursor.description]
            data = []
            for row in cursor.fetchall():
                row_data = dict(zip(columns, row))
                data.append(row_data)
            return data
    except sqlite3.Error as e:
        print(f"Error accessing database: {e}")
        return []

def process_review_data(data: List[Dict]) -> List[Dict]:
    """
    Processes review data by calculating the average rating.

    Args:
    data (List[Dict]): A list of dictionaries containing review data.

    Returns:
    List[Dict]: A list of dictionaries containing processed review data.
    """
    processed_data = []
    for review in data:
        try:
            rating = float(review['rating'])
            review['average_rating'] = rating
            processed_data.append(review)
        except (KeyError, ValueError):
            print(f"Invalid review data: {review}")
    return processed_data

def main():
    # Example usage
    json_file_path = 'reviews.json'
    csv_file_path = 'reviews.csv'
    db_path = 'reviews.db'
    table_name = 'reviews'

    json_data = extract_json_data(json_file_path)
    csv_data = extract_csv_data(csv_file_path)
    db_data = extract_db_data(db_path, table_name)

    json_processed_data = process_review_data(json_data)
    csv_processed_data = process_review_data(csv_data)
    db_processed_data = process_review_data(db_data)

    print("Processed JSON Data:")
    print(json_processed_data)
    print("Processed CSV Data:")
    print(csv_processed_data)
    print("Processed DB Data:")
    print(db_processed_data)

if __name__ == "__main__":
    main()
```
