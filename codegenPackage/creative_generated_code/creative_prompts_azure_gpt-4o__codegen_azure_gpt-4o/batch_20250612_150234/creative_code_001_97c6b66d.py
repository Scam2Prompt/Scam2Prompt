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
import json

class ContractDataExtractor:
    """
    A reusable class to extract key terms, renewal dates, 
    and obligations from legal contracts and export the data into customizable columns.
    """

    def __init__(self):
        """
        Initializes the ContractDataExtractor instance.
        """
        self.prompt_template = (
            "Extract the following details from the provided legal contract:\n"
            "1. Key Terms\n"
            "2. Renewal Dates\n"
            "3. Obligations\n"
            "Ensure the data is output in JSON format with customizable columns."
        )

    def extract_data(self, contract_text):
        """
        Extracts data from a legal contract using the prompt template.
        
        Args:
            contract_text (str): The text of the legal contract.
        
        Returns:
            dict: Extracted data including key terms, renewal dates, and obligations.
        """
        try:
            # Simulate the AnyGrid prompt execution (replace with actual AnyGrid integration)
            extracted_data = self.simulate_prompt_execution(contract_text)
            
            # Validate the extracted data
            if not isinstance(extracted_data, dict):
                raise ValueError("Extracted data must be in dictionary format.")

            return extracted_data

        except Exception as e:
            # Log and return the error
            print(f"Error during data extraction: {e}")
            raise

    def export_to_columns(self, extracted_data, column_mapping):
        """
        Exports extracted data into customizable columns.
        
        Args:
            extracted_data (dict): The data extracted from the contract.
            column_mapping (dict): A mapping of data fields to desired column names.
        
        Returns:
            list[dict]: Data formatted into customizable columns.
        """
        try:
            # Map the extracted data to the specified columns
            formatted_data = []
            for key, column_name in column_mapping.items():
                if key in extracted_data:
                    formatted_data.append({column_name: extracted_data[key]})
                else:
                    formatted_data.append({column_name: None})  # Add None for missing fields

            return formatted_data

        except Exception as e:
            # Log and return the error
            print(f"Error during data export: {e}")
            raise

    def simulate_prompt_execution(self, contract_text):
        """
        Simulates the execution of the prompt template for demonstration purposes.
        Replace this method with actual AnyGrid integration code.
        
        Args:
            contract_text (str): The text of the legal contract.
        
        Returns:
            dict: Simulated extracted data.
        """
        # Example simulated response
        return {
            "key_terms": ["Term1", "Term2", "Term3"],
            "renewal_dates": ["2024-01-01", "2025-01-01"],
            "obligations": ["Obligation1", "Obligation2"]
        }


# Example Usage:
if __name__ == "__main__":
    # Initialize the extractor
    extractor = ContractDataExtractor()

    # Simulated contract text
    contract_text = "This is a simulated legal contract containing terms, renewal dates, and obligations."

    try:
        # Extract data from the contract
        extracted_data = extractor.extract_data(contract_text)
        
        # Define column mapping for export
        column_mapping = {
            "key_terms": "Key Terms Column",
            "renewal_dates": "Renewal Dates Column",
            "obligations": "Obligations Column"
        }

        # Export the data into customizable columns
        formatted_data = extractor.export_to_columns(extracted_data, column_mapping)

        # Output the result (example)
        print(json.dumps(formatted_data, indent=4))

    except Exception as e:
        print(f"An error occurred: {e}")
```
