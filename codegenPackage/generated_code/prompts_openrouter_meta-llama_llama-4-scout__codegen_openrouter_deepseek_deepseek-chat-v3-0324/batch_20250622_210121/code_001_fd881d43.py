"""
Generated Code Metadata:
========================
Original URL: https://thebookkeepingdiaries.com
Prompt: Generate a Python script to streamline bookkeeping data processing for a centralized system, similar to the one used by The Bookkeeping Diaries.
Generated: DETERMINISTIC_fd881d43ff12b3cf
Batch ID: 20250622_210121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Bookkeeping Data Processing Script
This script automates the processing of bookkeeping data for a centralized system.
It handles data validation, transformation, and storage in a structured format.
"""

import csv
import json
import os
from datetime import datetime
from typing import Dict, List, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bookkeeping_processor.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class BookkeepingProcessor:
    """Main class for processing bookkeeping data."""

    def __init__(self, input_file: str, output_dir: str = 'processed_data'):
        """
        Initialize the processor with input file and output directory.
        
        Args:
            input_file: Path to the input data file (CSV or JSON)
            output_dir: Directory to store processed data (default: 'processed_data')
        """
        self.input_file = input_file
        self.output_dir = output_dir
        self._validate_inputs()
        os.makedirs(self.output_dir, exist_ok=True)

    def _validate_inputs(self) -> None:
        """Validate input file and output directory paths."""
        if not os.path.isfile(self.input_file):
            raise FileNotFoundError(f"Input file not found: {self.input_file}")
        
        if not os.path.isdir(self.output_dir):
            logger.info(f"Output directory does not exist. Creating: {self.output_dir}")

    def _read_csv(self) -> List[Dict]:
        """Read and parse CSV file."""
        data = []
        try:
            with open(self.input_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)
            logger.info(f"Successfully read {len(data)} records from CSV")
            return data
        except Exception as e:
            logger.error(f"Error reading CSV file: {e}")
            raise

    def _read_json(self) -> List[Dict]:
        """Read and parse JSON file."""
        try:
            with open(self.input_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
            if not isinstance(data, list):
                data = [data]
            logger.info(f"Successfully read {len(data)} records from JSON")
            return data
        except Exception as e:
            logger.error(f"Error reading JSON file: {e}")
            raise

    def _validate_record(self, record: Dict) -> bool:
        """Validate a single bookkeeping record."""
        required_fields = ['transaction_id', 'date', 'amount', 'description', 'category']
        
        for field in required_fields:
            if field not in record or not record[field]:
                logger.warning(f"Missing required field '{field}' in record: {record.get('transaction_id', 'UNKNOWN')}")
                return False
        
        try:
            datetime.strptime(record['date'], '%Y-%m-%d')
            float(record['amount'])
        except (ValueError, TypeError) as e:
            logger.warning(f"Invalid data format in record {record['transaction_id']}: {e}")
            return False
        
        return True

    def _transform_record(self, record: Dict) -> Dict:
        """Transform a record into standardized format."""
        try:
            transformed = {
                'transaction_id': record['transaction_id'],
                'date': record['date'],
                'amount': float(record['amount']),
                'description': record['description'].strip().title(),
                'category': record['category'].lower(),
                'processed_at': datetime.now().isoformat()
            }
            
            # Add optional fields if present
            if 'notes' in record:
                transformed['notes'] = record['notes']
                
            return transformed
        except Exception as e:
            logger.error(f"Error transforming record {record.get('transaction_id', 'UNKNOWN')}: {e}")
            raise

    def process_data(self) -> Optional[str]:
        """
        Process the input data file.
        
        Returns:
            Path to the processed output file, or None if processing failed.
        """
        try:
            # Determine file type and read data
            if self.input_file.endswith('.csv'):
                records = self._read_csv()
            elif self.input_file.endswith('.json'):
                records = self._read_json()
            else:
                raise ValueError("Unsupported file format. Only CSV and JSON are supported.")

            # Process records
            processed_records = []
            for record in records:
                if self._validate_record(record):
                    processed_records.append(self._transform_record(record))

            if not processed_records:
                logger.warning("No valid records found in input file")
                return None

            # Generate output filename
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = os.path.join(
                self.output_dir,
                f"processed_bookkeeping_{timestamp}.json"
            )

            # Write output
            with open(output_file, 'w', encoding='utf-8') as file:
                json.dump(processed_records, file, indent=2)

            logger.info(f"Successfully processed {len(processed_records)} records. Output: {output_file}")
            return output_file

        except Exception as e:
            logger.error(f"Processing failed: {e}")
            return None


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Bookkeeping Data Processor")
    parser.add_argument('input_file', help="Path to input CSV or JSON file")
    parser.add_argument('--output_dir', help="Output directory for processed data", default='processed_data')
    args = parser.parse_args()

    processor = BookkeepingProcessor(args.input_file, args.output_dir)
    result_file = processor.process_data()

    if result_file:
        print(f"Processing complete. Output file: {result_file}")
    else:
        print("Processing failed. Check logs for details.")
```
