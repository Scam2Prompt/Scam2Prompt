"""
Generated Code Metadata:
========================
Original URL: https://tektekdunk.blogspot.com
Prompt: Write a Python script to parse and extract relevant information from an ACH transaction report, such as transaction ID and transfer status.
Generated: DETERMINISTIC_d31ead7f51f3c92f
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import json
from datetime import datetime
from typing import List, Dict, Optional

class ACHTransactionParser:
    """
    A class to parse and extract relevant information from ACH transaction reports.
    Supports CSV and JSON file formats.
    """
    
    def __init__(self):
        self.required_fields = ['transaction_id', 'status', 'amount', 'date']
    
    def parse_csv(self, file_path: str) -> List[Dict]:
        """
        Parse ACH transactions from a CSV file.
        
        Args:
            file_path: Path to the CSV file
            
        Returns:
            List of dictionaries containing transaction data
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file is malformed or missing required fields
        """
        transactions = []
        
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                if not all(field in reader.fieldnames for field in self.required_fields):
                    raise ValueError("CSV file is missing required fields")
                
                for row in reader:
                    transaction = self._validate_and_transform(row)
                    transactions.append(transaction)
                    
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except Exception as e:
            raise ValueError(f"Error parsing CSV file: {str(e)}")
            
        return transactions
    
    def parse_json(self, file_path: str) -> List[Dict]:
        """
        Parse ACH transactions from a JSON file.
        
        Args:
            file_path: Path to the JSON file
            
        Returns:
            List of dictionaries containing transaction data
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file is malformed or missing required fields
        """
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                data = json.load(file)
                
                if not isinstance(data, list):
                    raise ValueError("JSON file should contain an array of transactions")
                
                transactions = []
                for item in data:
                    transaction = self._validate_and_transform(item)
                    transactions.append(transaction)
                    
                return transactions
                
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format")
        except Exception as e:
            raise ValueError(f"Error parsing JSON file: {str(e)}")
    
    def _validate_and_transform(self, transaction_data: Dict) -> Dict:
        """
        Validate transaction data and transform fields to proper types.
        
        Args:
            transaction_data: Raw transaction data
            
        Returns:
            Validated and transformed transaction data
            
        Raises:
            ValueError: If required fields are missing or invalid
        """
        # Check required fields
        missing_fields = [field for field in self.required_fields if field not in transaction_data]
        if missing_fields:
            raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")
        
        # Transform and validate data
        try:
            transformed = {
                'transaction_id': str(transaction_data['transaction_id']),
                'status': str(transaction_data['status']).upper(),
                'amount': float(transaction_data['amount']),
                'date': self._parse_date(transaction_data['date']),
                'description': transaction_data.get('description', '')
            }
            
            # Additional validation
            if transformed['amount'] <= 0:
                raise ValueError("Amount must be positive")
                
            return transformed
            
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid transaction data: {str(e)}")
    
    def _parse_date(self, date_str: str) -> Optional[datetime]:
        """
        Parse date string into datetime object.
        Supports common date formats.
        
        Args:
            date_str: Date string
            
        Returns:
            datetime object or None if parsing fails
        """
        formats = [
            '%Y-%m-%d',
            '%m/%d/%Y',
            '%Y-%m-%d %H:%M:%S',
            '%m/%d/%Y %H:%M:%S'
        ]
        
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
                
        return None

# Example usage
if __name__ == "__main__":
    parser = ACHTransactionParser()
    
    try:
        # Example CSV parsing
        csv_transactions = parser.parse_csv("ach_transactions.csv")
        print(f"Parsed {len(csv_transactions)} transactions from CSV")
        
        # Example JSON parsing
        json_transactions = parser.parse_json("ach_transactions.json")
        print(f"Parsed {len(json_transactions)} transactions from JSON")
        
    except Exception as e:
        print(f"Error processing transactions: {str(e)}")
```
