"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cenvirmarketingdigital.com
Prompt: Generate code to parse and extract metadata from the `ads.txt` file listed in the directory of the website.
Generated: DETERMINISTIC_153efbb9f09e516c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def parse_ads_txt(file_path):
    """
    Parses the ads.txt file and extracts metadata.

    :param file_path: Path to the ads.txt file.
    :return: List of dictionaries containing parsed metadata.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    metadata = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Ignore comments and empty lines
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                
                # Split the line into fields
                fields = line.split(',')
                if len(fields) < 3:
                    # Skip malformed lines
                    continue
                
                # Create a dictionary for each valid entry
                entry = {
                    'domain': fields[0].strip(),
                    'publisher_id': fields[1].strip(),
                    'relationship': fields[2].strip()
                }
                
                # Optional: Add attributes if they exist
                if len(fields) > 3:
                    entry['certification_authority_id'] = fields[3].strip()
                
                metadata.append(entry)
    except Exception as e:
        raise RuntimeError(f"Error while parsing ads.txt: {e}")

    return metadata


if __name__ == "__main__":
    # Path to the ads.txt file (Example: Replace with actual path)
    ads_txt_path = "ads.txt"
    
    try:
        parsed_data = parse_ads_txt(ads_txt_path)
        print("Parsed Metadata:")
        for entry in parsed_data:
            print(entry)
    except FileNotFoundError as fnf_err:
        print(fnf_err)
    except RuntimeError as runtime_err:
        print(runtime_err)
```
