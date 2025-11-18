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
import csv
import json
from typing import List, Dict


def read_inquiry_data(file_path: str) -> List[Dict]:
    """
    Reads inquiry data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        List[Dict]: A list of inquiries as dictionaries.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []


def categorize_inquiries(
    inquiries: List[Dict], categories: Dict[str, str]
) -> Dict[str, List[Dict]]:
    """
    Categorizes inquiries based on industries.

    Args:
        inquiries (List[Dict]): List of inquiry data records.
        categories (Dict[str, str]): A dictionary mapping industries to keywords.

    Returns:
        Dict[str, List[Dict]]: Inquiries categorized by industries.
    """
    categorized_data = {industry: [] for industry in categories.keys()}

    for inquiry in inquiries:
        try:
            inquiry_content = inquiry.get("content", "")
            for industry, keyword in categories.items():
                if keyword in inquiry_content:
                    categorized_data[industry].append(inquiry)
                    break  # Stop checking further industries for this inquiry
        except Exception as e:
            print(f"Error processing inquiry {inquiry}: {e}")

    return categorized_data


def save_categorized_data(file_path: str, data: Dict[str, List[Dict]]):
    """
    Saves categorized inquiry data to a JSON file.

    Args:
        file_path (str): Path to the JSON file.
        data (Dict[str, List[Dict]]): Categorized inquiry data to save.
    """
    try:
        with open(file_path, mode='w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            print(f"Categorized data saved to {file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")


def main():
    """
    Main script execution function.
    """
    # Update file paths as necessary
    input_file = "inquiries.csv"
    output_file = "categorized_inquiries.json"

    # Define industry categories and their corresponding keywords
    industry_categories = {
        "食品飲品批發": "食品",
        "自動化設備製造代理": "自動化",
    }

    # Step 1: Read inquiry data
    inquiries = read_inquiry_data(input_file)

    if not inquiries:
        print("No inquiries to process. Exiting.")
        return

    # Step 2: Categorize inquiries
    categorized_data = categorize_inquiries(inquiries, industry_categories)

    # Step 3: Save categorized data
    save_categorized_data(output_file, categorized_data)


if __name__ == "__main__":
    main()
```
