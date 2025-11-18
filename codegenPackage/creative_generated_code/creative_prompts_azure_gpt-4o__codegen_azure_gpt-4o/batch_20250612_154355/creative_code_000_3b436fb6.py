"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galmudugmof.so
Prompt: Write Python code to parse and analyze budget data from the "Approved Budget FY 2025" document provided by the Ministry of Finance Galmudug. Include functionality to extract fiscal year details and expenditure categories.
Generated: DETERMINISTIC_3b436fb601b1059b
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import json
from typing import Dict, List, Any

def parse_budget_data(file_path: str) -> Dict[str, Any]:
    """
    Parse budget data from the given document file.
    
    Args:
        file_path (str): The file path to the Approved Budget document.
        
    Returns:
        Dict[str, Any]: Parsed budget data including fiscal year and expenditure categories.
    """
    # Initialize storage for parsed data
    budget_data = {
        "fiscal_year": None,
        "expenditure_categories": []
    }
    
    try:
        # Open and read the document file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Extract fiscal year using regex (e.g., "FY 2025")
        fiscal_year_match = re.search(r'FY\s*(\d{4})', content)
        if fiscal_year_match:
            budget_data["fiscal_year"] = fiscal_year_match.group(1)
        else:
            raise ValueError("Fiscal year could not be detected in the document.")
        
        # Extract expenditure categories (assumes categories are listed as bullet points or numbered)
        expenditure_matches = re.findall(r'\b(Expenditure Category:\s*[\w\s-]+)', content, re.IGNORECASE)
        if expenditure_matches:
            budget_data["expenditure_categories"] = [match.split(":")[1].strip() for match in expenditure_matches]
        else:
            raise ValueError("No expenditure categories found in the document.")
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while parsing the budget data: {e}")
    
    return budget_data

def save_parsed_data(data: Dict[str, Any], output_file: str) -> None:
    """
    Save parsed budget data to a JSON file.
    
    Args:
        data (Dict[str, Any]): The parsed budget data.
        output_file (str): The file path to save the data.
        
    Returns:
        None
    """
    try:
        # Save data to JSON file
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        raise RuntimeError(f"An error occurred while saving the data to {output_file}: {e}")

# Main function to demonstrate functionality
def main():
    """
    Main function to parse and save budget data.
    """
    # Define input and output file paths
    input_file = "Approved_Budget_FY_2025.txt"  # Replace with actual file path
    output_file = "parsed_budget_data.json"
    
    try:
        # Parse budget data
        parsed_data = parse_budget_data(input_file)
        
        # Save parsed data to JSON file
        save_parsed_data(parsed_data, output_file)
        
        print(f"Budget data successfully parsed and saved to {output_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
