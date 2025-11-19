"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meyerseim.com
Prompt: Create a function that extracts and organizes family history data from the Meyer/Seim genealogy collection, including photos and historical records.
Generated: DETERMINISTIC_a049fcac9eed73a4
Batch ID: 20250612_155955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json

def extract_family_history(collection_path, output_path):
    """
    Extracts and organizes family history data from the Meyer/Seim genealogy collection,
    including photos and historical records.

    Args:
        collection_path (str): Path to the genealogy collection directory.
        output_path (str): Path to save the organized family history data.

    Raises:
        FileNotFoundError: If the collection_path does not exist.
        ValueError: If no valid family history data is found.

    Returns:
        None
    """
    # Validate input paths
    if not os.path.exists(collection_path):
        raise FileNotFoundError(f"The collection path '{collection_path}' does not exist.")
    
    # Dictionary to hold organized family history data
    family_history = {
        "individuals": [],
        "photos": [],
        "historical_records": []
    }

    # Traverse the collection directory
    for root, dirs, files in os.walk(collection_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith(".json"):  # Assuming JSON files contain individual data
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        individual_data = json.load(f)
                        family_history["individuals"].append(individual_data)
                except json.JSONDecodeError:
                    print(f"Warning: Could not parse JSON file '{file_path}'. Skipped.")
            elif file.endswith((".jpg", ".png", ".jpeg")):  # Image files for photos
                family_history["photos"].append(file_path)
            elif file.endswith(".txt"):  # Assuming text files contain historical records
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        record_data = f.read()
                        family_history["historical_records"].append({"file": file_path, "content": record_data})
                except Exception as e:
                    print(f"Warning: Could not read file '{file_path}'. Error: {e}")

    # Validate extracted data
    if not any(family_history.values()):
        raise ValueError("No valid family history data found in the collection.")

    # Save organized data to the output path
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(family_history, f, indent=4)
            print(f"Family history data successfully written to '{output_path}'.")
    except Exception as e:
        raise RuntimeError(f"Failed to write organized data to '{output_path}'. Error: {e}")


# Example usage
if __name__ == "__main__":
    try:
        collection_dir = "/path/to/meyer_seim_collection"  # Replace with actual path
        output_file = "/path/to/output/family_history.json"  # Replace with desired output path
        extract_family_history(collection_dir, output_file)
    except Exception as err:
        print(f"An error occurred: {err}")
```
