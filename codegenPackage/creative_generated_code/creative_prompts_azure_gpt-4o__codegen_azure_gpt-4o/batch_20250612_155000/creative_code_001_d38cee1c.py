"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crxsoso.com
Prompt: Develop a Python script to parse and categorize extensions from Crx搜搜 based on tags like "工具," "教育," and "开发者工具."
Generated: DETERMINISTIC_d38cee1c3963c05d
Batch ID: 20250612_155000
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

def load_data(file_path):
    """
    Load JSON data from a file.

    :param file_path: Path to the JSON file.
    :return: Parsed JSON data (list or dict).
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON file: {e}")
    except Exception as e:
        raise RuntimeError(f"An error occurred while reading the file: {e}")


def categorize_extensions(data, tags):
    """
    Categorize extensions based on tags.

    :param data: List of extensions (dicts) loaded from JSON.
    :param tags: Dictionary of categories and their corresponding tags.
    :return: Dictionary with extensions categorized by tags.
    """
    categorized = {category: [] for category in tags}
    categorized['Uncategorized'] = []  # Bucket for extensions not matching any tags

    for extension in data:
        matched = False
        for category, category_tags in tags.items():
            if any(tag in extension.get('tags', []) for tag in category_tags):
                categorized[category].append(extension)
                matched = True
                break

        if not matched:
            categorized['Uncategorized'].append(extension)

    return categorized


def save_categorized_extensions(categorized_data, output_dir):
    """
    Save categorized extensions to separate JSON files.

    :param categorized_data: Dictionary with extensions categorized by tags.
    :param output_dir: Directory to save the categorized JSON files.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        for category, extensions in categorized_data.items():
            output_path = os.path.join(output_dir, f"{category}.json")
            with open(output_path, 'w', encoding='utf-8') as file:
                json.dump(extensions, file, ensure_ascii=False, indent=4)
    except Exception as e:
        raise RuntimeError(f"An error occurred while saving files: {e}")


def main():
    """
    Main function to parse and categorize extensions from Crx搜搜.
    """
    # Path to the input JSON file (replace with actual file path)
    input_file = "crx_data.json"

    # Directory to save categorized files (replace with your desired output directory)
    output_directory = "categorized_extensions"

    # Tags for categorization
    tags = {
        "工具": ["工具"],
        "教育": ["教育"],
        "开发者工具": ["开发者工具"]
    }

    try:
        # Step 1: Load extension data
        extensions = load_data(input_file)

        # Step 2: Categorize extensions based on tags
        categorized_extensions = categorize_extensions(extensions, tags)

        # Step 3: Save categorized extensions to JSON files
        save_categorized_extensions(categorized_extensions, output_directory)

        print(f"Categorized extensions saved to: {output_directory}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
