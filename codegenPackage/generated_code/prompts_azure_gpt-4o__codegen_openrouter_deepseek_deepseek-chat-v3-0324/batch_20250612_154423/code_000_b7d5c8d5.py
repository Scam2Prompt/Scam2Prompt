"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Write Python code to process and extract information from the list of candidates and results provided in the IGEOG selection process documents, such as "Listagem de inscrições deferidas e indeferidas" and "Resultado Final."
Generated: DETERMINISTIC_b7d5c8d52802e2b6
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import List, Dict, Optional
import pandas as pd
from pathlib import Path

class IGEOGProcessor:
    """
    A class to process and extract information from IGEOG selection process documents.
    Handles both 'Listagem de inscrições deferidas e indeferidas' and 'Resultado Final' documents.
    """
    
    def __init__(self):
        self.candidate_data = []
        self.final_results = []
    
    def load_document(self, file_path: str, document_type: str) -> bool:
        """
        Load and parse the document based on its type.
        
        Args:
            file_path: Path to the document file
            document_type: Type of document ('registration' or 'final_result')
            
        Returns:
            bool: True if loading was successful, False otherwise
        """
        try:
            path = Path(file_path)
            if not path.exists():
                raise FileNotFoundError(f"File not found: {file_path}")
            
            if document_type == 'registration':
                return self._parse_registration_document(path)
            elif document_type == 'final_result':
                return self._parse_final_result_document(path)
            else:
                raise ValueError("Invalid document type. Must be 'registration' or 'final_result'")
                
        except Exception as e:
            print(f"Error loading document: {e}")
            return False
    
    def _parse_registration_document(self, file_path: Path) -> bool:
        """
        Parse the registration document ('Listagem de inscrições deferidas e indeferidas').
        
        Args:
            file_path: Path to the document file
            
        Returns:
            bool: True if parsing was successful
        """
        try:
            # Read the document - assuming it's a PDF that needs text extraction
            # For demonstration, we'll assume we've extracted text to a string
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            
            # Sample pattern for registration document (adjust according to actual format)
            pattern = re.compile(
                r'(?P<inscription>\d+)\s+'  # Inscription number
                r'(?P<name>[A-ZÀ-Ú\s]+)\s+'  # Name (uppercase with accents)
                r'(?P<status>DEFERIDO|INDEFERIDO)'  # Status
            )
            
            matches = pattern.finditer(text)
            self.candidate_data = [
                {
                    'inscription': match.group('inscription'),
                    'name': match.group('name').strip(),
                    'status': match.group('status')
                }
                for match in matches
            ]
            
            return True
            
        except Exception as e:
            print(f"Error parsing registration document: {e}")
            return False
    
    def _parse_final_result_document(self, file_path: Path) -> bool:
        """
        Parse the final result document ('Resultado Final').
        
        Args:
            file_path: Path to the document file
            
        Returns:
            bool: True if parsing was successful
        """
        try:
            # Read the document - assuming it's a PDF that needs text extraction
            # For demonstration, we'll assume we've extracted text to a string
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            
            # Sample pattern for final result document (adjust according to actual format)
            pattern = re.compile(
                r'(?P<position>\d+)\s+'  # Position/ranking
                r'(?P<inscription>\d+)\s+'  # Inscription number
                r'(?P<name>[A-ZÀ-Ú\s]+)\s+'  # Name (uppercase with accents)
                r'(?P<score>\d+,\d+)'  # Final score
            )
            
            matches = pattern.finditer(text)
            self.final_results = [
                {
                    'position': match.group('position'),
                    'inscription': match.group('inscription'),
                    'name': match.group('name').strip(),
                    'score': match.group('score')
                }
                for match in matches
            ]
            
            return True
            
        except Exception as e:
            print(f"Error parsing final result document: {e}")
            return False
    
    def get_candidate_data(self) -> List[Dict]:
        """
        Get the parsed candidate data from registration document.
        
        Returns:
            List[Dict]: List of candidate dictionaries
        """
        return self.candidate_data
    
    def get_final_results(self) -> List[Dict]:
        """
        Get the parsed final results.
        
        Returns:
            List[Dict]: List of final result dictionaries
        """
        return self.final_results
    
    def merge_data(self) -> pd.DataFrame:
        """
        Merge registration data with final results.
        
        Returns:
            pd.DataFrame: Merged data as a DataFrame
        """
        try:
            reg_df = pd.DataFrame(self.candidate_data)
            res_df = pd.DataFrame(self.final_results)
            
            if reg_df.empty or res_df.empty:
                raise ValueError("No data to merge. Load documents first.")
            
            merged = pd.merge(
                reg_df,
                res_df,
                on=['inscription', 'name'],
                how='outer'
            )
            
            return merged
            
        except Exception as e:
            print(f"Error merging data: {e}")
            return pd.DataFrame()
    
    def export_to_csv(self, output_path: str, data: Optional[pd.DataFrame] = None) -> bool:
        """
        Export data to CSV file.
        
        Args:
            output_path: Path to save the CSV file
            data: DataFrame to export (if None, uses merged data)
            
        Returns:
            bool: True if export was successful
        """
        try:
            if data is None:
                data = self.merge_data()
                if data.empty:
                    raise ValueError("No data to export")
            
            data.to_csv(output_path, index=False, encoding='utf-8')
            return True
            
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return False

# Example usage
if __name__ == "__main__":
    processor = IGEOGProcessor()
    
    # Load documents (replace with actual file paths)
    processor.load_document("deferidas_indefiridas.txt", "registration")
    processor.load_document("resultado_final.txt", "final_result")
    
    # Get and print data
    print("Candidate Data:")
    print(processor.get_candidate_data())
    
    print("\nFinal Results:")
    print(processor.get_final_results())
    
    # Merge and export data
    merged_data = processor.merge_data()
    if not merged_data.empty:
        processor.export_to_csv("igeog_results.csv", merged_data)
```
