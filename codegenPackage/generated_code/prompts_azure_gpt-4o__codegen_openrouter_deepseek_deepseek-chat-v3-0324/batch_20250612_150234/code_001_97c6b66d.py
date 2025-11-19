"""
Generated Code Metadata:
========================
Original URL: https://anygrid.app
Prompt: Create a reusable prompt template for AnyGrid to extract key terms, renewal dates, and obligations from legal contracts, and export the data into customizable columns.
Generated: DETERMINISTIC_97c6b66d5d3d6925
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional, Any

class LegalContractParser:
    """
    A reusable prompt template for AnyGrid to extract key terms, renewal dates, and obligations 
    from legal contracts and export the data into customizable columns.
    """
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the parser with optional configuration.
        
        Args:
            config_path (str, optional): Path to JSON config file for custom columns. 
                                        Defaults to None (uses default config).
        """
        self.config = self._load_config(config_path)
        self.required_fields = ['key_terms', 'renewal_dates', 'obligations']
        
    def _load_config(self, config_path: Optional[str]) -> Dict[str, Any]:
        """Load configuration from JSON file or use defaults."""
        default_config = {
            "output_columns": {
                "key_terms": ["term", "definition", "section"],
                "renewal_dates": ["event", "date", "notice_period_days"],
                "obligations": ["party", "obligation", "deadline", "conditions"]
            },
            "date_format": "%Y-%m-%d"
        }
        
        if config_path:
            try:
                with open(config_path, 'r') as f:
                    return json.load(f)
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Warning: Could not load config file. Using defaults. Error: {str(e)}")
        
        return default_config
    
    def _validate_contract_data(self, contract_data: Dict[str, Any]) -> bool:
        """Validate that contract data contains required fields."""
        for field in self.required_fields:
            if field not in contract_data:
                raise ValueError(f"Missing required field in contract data: {field}")
        return True
    
    def _parse_dates(self, date_str: str) -> Optional[str]:
        """Parse dates into standardized format."""
        if not date_str:
            return None
            
        try:
            date_obj = datetime.strptime(date_str, self.config['date_format'])
            return date_obj.strftime(self.config['date_format'])
        except ValueError:
            print(f"Warning: Could not parse date: {date_str}")
            return None
    
    def extract_data(self, contract_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Extract and transform contract data into structured output.
        
        Args:
            contract_data (dict): Raw contract data containing key terms, 
                                renewal dates, and obligations.
                                
        Returns:
            List[dict]: Structured data ready for export to AnyGrid.
        """
        self._validate_contract_data(contract_data)
        
        output = []
        
        # Process key terms
        for term in contract_data.get('key_terms', []):
            output.append({
                "type": "key_term",
                "term": term.get('term'),
                "definition": term.get('definition'),
                "section": term.get('section')
            })
        
        # Process renewal dates
        for date_info in contract_data.get('renewal_dates', []):
            standardized_date = self._parse_dates(date_info.get('date'))
            output.append({
                "type": "renewal_date",
                "event": date_info.get('event'),
                "date": standardized_date,
                "notice_period_days": date_info.get('notice_period_days')
            })
        
        # Process obligations
        for obligation in contract_data.get('obligations', []):
            standardized_deadline = self._parse_dates(obligation.get('deadline'))
            output.append({
                "type": "obligation",
                "party": obligation.get('party'),
                "obligation": obligation.get('obligation'),
                "deadline": standardized_deadline,
                "conditions": obligation.get('conditions')
            })
            
        return output
    
    def export_to_csv(self, extracted_data: List[Dict[str, Any]], output_path: str) -> None:
        """
        Export extracted data to CSV format.
        
        Args:
            extracted_data (List[dict]): Data from extract_data method.
            output_path (str): Path to save the CSV file.
        """
        import csv
        
        if not extracted_data:
            raise ValueError("No data to export")
            
        fieldnames = set()
        for item in extracted_data:
            fieldnames.update(item.keys())
        
        try:
            with open(output_path, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=sorted(fieldnames))
                writer.writeheader()
                writer.writerows(extracted_data)
        except IOError as e:
            raise IOError(f"Failed to write CSV file: {str(e)}")
    
    def generate_prompt_template(self) -> str:
        """
        Generate a prompt template for AnyGrid to extract contract data.
        
        Returns:
            str: The prompt template string.
        """
        return """
        Analyze the following legal contract and extract the following information:
        
        1. Key Terms:
           - Term name
           - Definition
           - Section reference
        
        2. Renewal Dates:
           - Event description
           - Date (format as YYYY-MM-DD)
           - Notice period (in days)
        
        3. Obligations:
           - Responsible party
           - Obligation description
           - Deadline (format as YYYY-MM-DD)
           - Conditions/requirements
        
        Return the extracted data in JSON format with the following structure:
        {
            "key_terms": [
                {"term": "...", "definition": "...", "section": "..."},
                ...
            ],
            "renewal_dates": [
                {"event": "...", "date": "...", "notice_period_days": ...},
                ...
            ],
            "obligations": [
                {"party": "...", "obligation": "...", "deadline": "...", "conditions": "..."},
                ...
            ]
        }
        """
```
