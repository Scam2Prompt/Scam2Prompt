"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anygrid.app
Prompt: Create a reusable prompt template for AnyGrid to extract key terms, renewal dates, and obligations from legal contracts, and export the data into customizable columns.
Generated: DETERMINISTIC_97c6b66d5d3d6925
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import re
from typing import List, Dict, Optional

class ContractExtractor:
    """
    A class to extract key terms, renewal dates, and obligations from legal contracts.
    """

    def __init__(self, columns: Optional[List[str]] = None):
        """
        Initializes the ContractExtractor with customizable columns for output.

        :param columns: Optional list of column names for the output DataFrame.
        """
        self.columns = columns if columns else ['Key Terms', 'Renewal Dates', 'Obligations']

    def extract_terms(self, contract_text: str) -> Dict[str, List[str]]:
        """
        Extracts key terms, renewal dates, and obligations from the provided contract text.

        :param contract_text: The text of the legal contract.
        :return: A dictionary containing lists of extracted key terms, renewal dates, and obligations.
        """
        try:
            key_terms = self._extract_key_terms(contract_text)
            renewal_dates = self._extract_renewal_dates(contract_text)
            obligations = self._extract_obligations(contract_text)

            return {
                'Key Terms': key_terms,
                'Renewal Dates': renewal_dates,
                'Obligations': obligations
            }
        except Exception as e:
            print(f"Error extracting terms: {e}")
            return {}

    def _extract_key_terms(self, text: str) -> List[str]:
        """
        Extracts key terms using regex from the contract text.

        :param text: The text of the contract.
        :return: A list of key terms.
        """
        # Simple regex pattern for key terms (adjust as necessary)
        pattern = r'\b(?:term|party|agreement|contract)\b'
        return re.findall(pattern, text, flags=re.IGNORECASE)

    def _extract_renewal_dates(self, text: str) -> List[str]:
        """
        Extracts renewal dates using regex from the contract text.

        :param text: The text of the contract.
        :return: A list of renewal dates.
        """
        # Simple regex pattern for dates (adjust as necessary)
        pattern = r'\b(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})\b'
        return re.findall(pattern, text)

    def _extract_obligations(self, text: str) -> List[str]:
        """
        Extracts obligations using regex from the contract text.

        :param text: The text of the contract.
        :return: A list of obligations.
        """
        # Simple regex pattern for obligations (adjust as necessary)
        pattern = r'\b(shall|must|will)\s+[a-zA-Z\s]+'
        return re.findall(pattern, text)

    def export_to_dataframe(self, extracted_data: Dict[str, List[str]]) -> pd.DataFrame:
        """
        Exports extracted data to a pandas DataFrame.

        :param extracted_data: Dictionary containing the extracted data.
        :return: A pandas DataFrame containing the extracted data.
        """
        try:
            df = pd.DataFrame(data=extracted_data, columns=self.columns)
            return df
        except Exception as e:
            print(f"Error exporting to DataFrame: {e}")
            return pd.DataFrame(columns=self.columns)

# Example usage
if __name__ == "__main__":
    sample_contract = """
    This agreement shall commence on the 1st of January, 2023. 
    The parties agree to renew the contract on 31/12/2025. 
    Party A must provide a written notice 30 days before renewal.
    """
    
    extractor = ContractExtractor()
    extracted_data = extractor.extract_terms(sample_contract)
    df = extractor.export_to_dataframe(extracted_data)
    print(df)
```
