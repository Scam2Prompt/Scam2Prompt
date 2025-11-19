"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.cornucopiastrategy.com
Prompt: Write a code snippet that processes the JSON response from `api_raw_response.json` to extract specific data fields.
Generated: DETERMINISTIC_26609aa33ccc9216
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

def load_json_file(file_path):
    """
    Load a JSON file and return its content as a dictionary.
    
    :param file_path: Path to the JSON file.
    :return: Dictionary containing the JSON data.
    :raises FileNotFoundError: If the file does not exist.
    :raises json.JSONDecodeError: If the file contents are not valid JSON.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError("Error decoding JSON.", str(e), e.pos)

    return data

def extract_fields(data, fields):
    """
    Extract specified fields from the JSON data.
    
    :param data: Dictionary containing the JSON data.
    :param fields: List of fields to extract from the data.
    :return: Dictionary containing the extracted fields.
    """
    extracted_data = {}
    for field in fields:
        if field in data:
            extracted_data[field] = data[field]
        else:
            extracted_data[field] = None  # Default to None if the field does not exist
    return extracted_data

def main():
    # Define the path to the JSON file
    json_file_path = 'api_raw_response.json'
    
    # Define the fields we want to extract
    fields_to_extract = ['id', 'name', 'value', 'timestamp']

    try:
        # Load the JSON file
        json_data = load_json_file(json_file_path)
        
        # Extract the desired fields
        result = extract_fields(json_data, fields_to_extract)
        
        # Output the extracted data
        print(result)

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
