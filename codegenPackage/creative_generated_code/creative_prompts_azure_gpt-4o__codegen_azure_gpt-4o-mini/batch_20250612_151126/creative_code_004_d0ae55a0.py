"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web66.com.tw
Prompt: Write a script to filter and categorize inquiry data from 台灣黃頁詢價平台 based on industries such as "食品飲品批發" or "自動化設備製造代理."
Generated: DETERMINISTIC_d0ae55a0e5e57d23
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict, Any

# Set up logging to capture errors and information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define a function to filter and categorize inquiries
def filter_and_categorize_inquiries(inquiries: List[Dict[str, Any]], categories: List[str]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Filters and categorizes inquiry data based on specified categories.

    :param inquiries: List of inquiry data as dictionaries.
    :param categories: List of categories to filter by.
    :return: A dictionary with categories as keys and lists of inquiries as values.
    """
    categorized_data = {category: [] for category in categories}

    for inquiry in inquiries:
        try:
            # Check if the inquiry's industry is in the specified categories
            industry = inquiry.get("industry")
            if industry in categories:
                categorized_data[industry].append(inquiry)
        except Exception as e:
            logging.error(f"Error processing inquiry {inquiry}: {e}")

    return categorized_data

def main():
    # Sample inquiry data (This should be replaced with actual data fetching logic)
    inquiries = [
        {"id": 1, "industry": "食品飲品批發", "details": "Inquiry about bulk tea."},
        {"id": 2, "industry": "自動化設備製造代理", "details": "Request for automation tools."},
        {"id": 3, "industry": "食品飲品批發", "details": "Inquiry about coffee suppliers."},
        {"id": 4, "industry": "其他", "details": "General inquiry."}
    ]

    # Define categories to filter inquiries
    categories = ["食品飲品批發", "自動化設備製造代理"]

    # Filter and categorize inquiries
    categorized_inquiries = filter_and_categorize_inquiries(inquiries, categories)

    # Output the categorized inquiries
    try:
        print(json.dumps(categorized_inquiries, ensure_ascii=False, indent=2))
    except Exception as e:
        logging.error(f"Error converting categorized inquiries to JSON: {e}")

if __name__ == "__main__":
    main()
```
