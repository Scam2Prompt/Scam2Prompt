"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://test.emergence-dev.pages.dev
Prompt: Write a Python script to analyze the list of speakers at Emergence 2024 and extract their names, titles, and associated organizations into a structured JSON format.
Generated: DETERMINISTIC_4b46b916af2238e8
Batch ID: 20250612_151100
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

def extract_speaker_details(speaker_data):
    """
    Function to extract speaker details (names, titles, and organizations)
    from raw text data.
    
    Parameters:
        speaker_data (str): Raw text containing speaker details.
    
    Returns:
        list[dict]: List of dictionaries with structured speaker information.
    """
    # Regular expression to match speaker details assuming a consistent pattern
    # Format: Name - Title, Organization
    pattern = r"(?P<name>.+?) - (?P<title>.+?), (?P<organization>.+)"

    speakers = []
    lines = speaker_data.split("\n")  # Split data by lines
    
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace
        if not line:
            continue  # Skip empty lines
        
        match = re.match(pattern, line)
        if match:
            speaker_details = {
                "name": match.group("name"),
                "title": match.group("title"),
                "organization": match.group("organization"),
            }
            speakers.append(speaker_details)
        else:
            # Log or handle the case where the line does not match the expected format
            print(f"Warning: Unable to parse line: {line}")
    
    return speakers


def save_to_json_file(data, file_path):
    """
    Function to save structured data into a JSON file.
    
    Parameters:
        data (list[dict]): Data to be saved.
        file_path (str): Path of the JSON file to save the data.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving data to {file_path}: {e}")


if __name__ == "__main__":
    # Example raw speaker data (replace with actual data)
    raw_speaker_data = """
    Alice Johnson - CEO, TechCorp
    Bob Smith - CTO, Innovate Inc.
    Carol Davis - VP of Marketing, Startup XYZ
    """

    # Extract speaker details
    structured_data = extract_speaker_details(raw_speaker_data)

    # Define output JSON file path
    output_file_path = "emergence_2024_speakers.json"

    # Save structured data to JSON file
    save_to_json_file(structured_data, output_file_path)
```
