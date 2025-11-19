"""
Generated Code Metadata:
========================
Original URL: https://ejecutortecnico.github.io
Prompt: How can I apply the programming techniques from the Ejecutor Tecnico's "Presentaciones de Python" in a real-world project?
Generated: DETERMINISTIC_81da5285d62f7773
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Real-world project applying techniques from Ejecutor Tecnico's "Presentaciones de Python".
This example demonstrates a data processing pipeline with:
- Clean code structure
- Type hints
- Error handling
- Logging
- Configuration management
- Unit testing
"""

import logging
from typing import List, Dict, Optional
import json
import csv
from pathlib import Path
from dataclasses import dataclass
import unittest
from configparser import ConfigParser

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class DataRecord:
    """Data record structure using dataclass for clean representation"""
    id: int
    name: str
    value: float
    category: str

class DataProcessor:
    """Main data processing class implementing core functionality"""
    
    def __init__(self, config_path: str = 'config.ini'):
        self.config = self._load_config(config_path)
        self.data: List[DataRecord] = []
        
    def _load_config(self, config_path: str) -> ConfigParser:
        """Load configuration from file with error handling"""
        config = ConfigParser()
        try:
            if not Path(config_path).exists():
                raise FileNotFoundError(f"Config file {config_path} not found")
            config.read(config_path)
            logger.info("Configuration loaded successfully")
            return config
        except Exception as e:
            logger.error(f"Error loading config: {e}")
            raise

    def load_data(self, file_path: str) -> None:
        """Load data from JSON or CSV file based on extension"""
        try:
            path = Path(file_path)
            if path.suffix == '.json':
                self._load_json(path)
            elif path.suffix == '.csv':
                self._load_csv(path)
            else:
                raise ValueError("Unsupported file format")
            logger.info(f"Successfully loaded {len(self.data)} records from {file_path}")
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise

    def _load_json(self, file_path: Path) -> None:
        """Helper method to load JSON data"""
        with open(file_path, 'r') as f:
            raw_data = json.load(f)
            self.data = [DataRecord(**item) for item in raw_data]

    def _load_csv(self, file_path: Path) -> None:
        """Helper method to load CSV data"""
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            self.data = [DataRecord(
                id=int(row['id']),
                name=row['name'],
                value=float(row['value']),
                category=row['category']
            ) for row in reader]

    def process_data(self) -> Dict[str, float]:
        """Process data to calculate category averages"""
        if not self.data:
            raise ValueError("No data loaded to process")
            
        category_totals: Dict[str, float] = {}
        category_counts: Dict[str, int] = {}
        
        for record in self.data:
            if record.category not in category_totals:
                category_totals[record.category] = 0.0
                category_counts[record.category] = 0
            category_totals[record.category] += record.value
            category_counts[record.category] += 1
        
        return {
            category: total / category_counts[category]
            for category, total in category_totals.items()
        }

    def save_results(self, output_path: str, results: Dict[str, float]) -> None:
        """Save processing results to JSON file"""
        try:
            with open(output_path, 'w') as f:
                json.dump(results, f, indent=2)
            logger.info(f"Results saved to {output_path}")
        except Exception as e:
            logger.error(f"Error saving results: {e}")
            raise

class TestDataProcessor(unittest.TestCase):
    """Unit tests for DataProcessor class"""
    
    def setUp(self):
        self.processor = DataProcessor()
        self.test_data = [
            DataRecord(1, "Test1", 10.0, "A"),
            DataRecord(2, "Test2", 20.0, "A"),
            DataRecord(3, "Test3", 30.0, "B")
        ]
    
    def test_process_data(self):
        self.processor.data = self.test_data
        results = self.processor.process_data()
        self.assertEqual(results['A'], 15.0)
        self.assertEqual(results['B'], 30.0)
    
    def test_empty_data(self):
        with self.assertRaises(ValueError):
            self.processor.process_data()

def main():
    """Main execution function"""
    try:
        processor = DataProcessor()
        processor.load_data('input_data.json')
        results = processor.process_data()
        processor.save_results('output_results.json', results)
    except Exception as e:
        logger.error(f"Application error: {e}")
        return 1
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
```
