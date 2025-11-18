"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chiliz-token.com
Prompt: Generate code to search billions of historical records, including obituaries and vital records, and display results in a user-friendly format. Reference features like those on Ancestry.com.
Generated: DETERMINISTIC_ee712e3b776a6512
Batch ID: 20250612_145718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any, Optional

class RecordSearcher:
    def __init__(self, data_source: str):
        """
        Initialize the RecordSearcher with a path to the data source.

        :param data_source: Path to the JSON file containing historical records.
        """
        self.data_source = data_source
        self.records = self.load_records()

    def load_records(self) -> List[Dict[str, Any]]:
        """
        Load historical records from the specified JSON file.

        :return: A list of records loaded from the data source.
        """
        try:
            with open(self.data_source, 'r', encoding='utf-8') as file:
                records = json.load(file)
                return records
        except FileNotFoundError:
            raise Exception(f"Data source '{self.data_source}' not found.")
        except json.JSONDecodeError:
            raise Exception(f"Data source '{self.data_source}' is not a valid JSON file.")
        except Exception as e:
            raise Exception(f"An error occurred while loading records: {str(e)}")

    def search(self, query: str) -> List[Dict[str, Any]]:
        """
        Search for records containing the specified query.

        :param query: A string to search for within the records.
        :return: A list of matching records.
        """
        results = []
        for record in self.records:
            if self.match_query(record, query):
                results.append(record)
        return results

    def match_query(self, record: Dict[str, Any], query: str) -> bool:
        """
        Check if the record matches the query.

        :param record: A single record to check.
        :param query: The query string to match against the record.
        :return: True if the record matches, False otherwise.
        """
        query_lower = query.lower()
        # Check for a match in the relevant fields
        return any(query_lower in str(value).lower() for value in record.values())

    def display_results(self, results: List[Dict[str, Any]]) -> None:
        """
        Display the search results in a user-friendly format.

        :param results: A list of records to display.
        """
        if not results:
            print("No results found.")
            return
        
        print(f"Found {len(results)} record(s):")
        for idx, record in enumerate(results, start=1):
            print(f"{idx}. {self.format_record(record)}")

    def format_record(self, record: Dict[str, Any]) -> str:
        """
        Format a single record for display.

        :param record: The record to format.
        :return: A formatted string representation of the record.
        """
        # Customize formatting as needed
        return f"{record.get('name', 'Unknown')} - {record.get('date', 'Unknown')}"

def main():
    """
    Main function to execute the record search.
    """
    data_source = 'historical_records.json'
    searcher = RecordSearcher(data_source)

    # Example user query; in a real application, this would come from user input
    query = input("Enter search query: ")
    results = searcher.search(query)
    searcher.display_results(results)

if __name__ == '__main__':
    main()
```
