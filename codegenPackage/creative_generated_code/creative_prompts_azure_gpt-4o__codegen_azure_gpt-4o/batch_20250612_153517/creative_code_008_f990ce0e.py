"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openweb-3ua.pages.dev
Prompt: Write a Python script to analyze the metadata of submitted Opepen artworks and generate a report for token holders participating in consensus decisions.
Generated: DETERMINISTIC_f990ce0ee3908af0
Batch ID: 20250612_153517
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
from datetime import datetime

def load_metadata(file_path):
    """
    Load metadata from a JSON file.
    
    Parameters:
        file_path (str): Path to the metadata JSON file.
        
    Returns:
        dict: Parsed metadata as a dictionary.
    """
    try:
        with open(file_path, 'r') as file:
            metadata = json.load(file)
        return metadata
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        raise
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from file '{file_path}'.")
        raise

def analyze_metadata(metadata):
    """
    Analyze the metadata and generate a report for token holders.
    
    Parameters:
        metadata (dict): Metadata dictionary.
        
    Returns:
        dict: Analyzed report.
    """
    report = {
        "total_artworks": 0,
        "unique_holders": 0,
        "holder_participation": {},
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    try:
        # Extract artworks and holders
        artworks = metadata.get("artworks", [])
        holders = metadata.get("holders", {})
        
        report["total_artworks"] = len(artworks)
        report["unique_holders"] = len(holders)
        
        # Build participation report
        for holder, tokens in holders.items():
            participation_count = sum(1 for token in tokens if token in artworks)
            report["holder_participation"][holder] = {
                "token_count": len(tokens),
                "participation_count": participation_count
            }
        
        return report
    except Exception as e:
        print(f"Error during metadata analysis: {e}")
        raise

def save_report(report, output_path):
    """
    Save the report as a JSON file.
    
    Parameters:
        report (dict): Analyzed report dictionary.
        output_path (str): Path to save the report JSON file.
    """
    try:
        with open(output_path, 'w') as file:
            json.dump(report, file, indent=4)
        print(f"Report successfully saved to '{output_path}'.")
    except Exception as e:
        print(f"Error saving report: {e}")
        raise

def main():
    """
    Main function to execute the metadata analysis and report generation.
    """
    metadata_file = "opepen_metadata.json"
    report_file = "opepen_report.json"
    
    try:
        # Load metadata
        metadata = load_metadata(metadata_file)
        
        # Analyze metadata
        report = analyze_metadata(metadata)
        
        # Save the report
        save_report(report, report_file)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
