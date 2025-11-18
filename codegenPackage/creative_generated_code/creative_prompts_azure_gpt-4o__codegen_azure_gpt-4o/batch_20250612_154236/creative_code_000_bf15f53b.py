"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://penguinbookspublishers.com
Prompt: Write Python code to optimize an eBook's metadata for Amazon listings, including strategic keywords and engaging descriptions, as described by Penguin Books Publishers' book marketing services.
Generated: DETERMINISTIC_bf15f53b78234f1a
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import re
from typing import List, Dict

def optimize_metadata(title: str, author: str, description: str, keywords: List[str]) -> Dict[str, str]:
    """
    Optimizes eBook metadata for Amazon listings.
    
    Args:
        title (str): The title of the eBook.
        author (str): The name of the author.
        description (str): Original book description.
        keywords (List[str]): List of strategic keywords.

    Returns:
        Dict[str, str]: Optimized metadata including title, author, description, and keywords.
    """
    try:
        # Validate inputs
        if not title or not author or not description or not keywords:
            raise ValueError("All metadata fields must be provided and non-empty.")
        
        # Ensure keywords are unique and non-empty
        keywords = list(set(filter(None, [keyword.strip().lower() for keyword in keywords])))
        if not keywords:
            raise ValueError("Keywords list must contain at least one valid keyword.")
        
        # Optimize title with strategic keywords (append relevant keyword to title if appropriate)
        optimized_title = title
        if keywords:
            optimized_title += f" | {keywords[0].capitalize()}"

        # Enhance description (highlight keywords and improve readability)
        optimized_description = description
        for keyword in keywords[:5]:  # Use up to 5 keywords to avoid keyword stuffing
            optimized_description = re.sub(
                fr"\b{keyword}\b",
                f"*{keyword.capitalize()}*", 
                optimized_description, 
                flags=re.IGNORECASE
            )

        # Prepare the metadata dictionary
        metadata = {
            "title": optimized_title,
            "author": author,
            "description": optimized_description,
            "keywords": ", ".join(keywords),  # Join keywords into a comma-separated string
        }
        return metadata

    except ValueError as ve:
        # Handle validation errors
        print(f"Validation Error: {ve}")
        return {}
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred while optimizing metadata: {e}")
        return {}


def save_metadata_to_file(metadata: Dict[str, str], file_path: str = "optimized_metadata.json") -> bool:
    """
    Saves optimized metadata to a JSON file.
    
    Args:
        metadata (Dict[str, str]): Metadata dictionary to save.
        file_path (str): Target file path for saving metadata.

    Returns:
        bool: True if file is saved successfully, False otherwise.
    """
    try:
        if not metadata:
            raise ValueError("Metadata cannot be empty when saving to file.")
        
        with open(file_path, 'w') as file:
            json.dump(metadata, file, indent=4)
        print(f"Metadata successfully saved to {file_path}")
        return True

    except ValueError as ve:
        print(f"Validation Error: {ve}")
        return False
    except Exception as e:
        print(f"An error occurred while saving metadata to file: {e}")
        return False


# Example usage
if __name__ == "__main__":
    # Sample input data
    sample_title = "The Art of Programming"
    sample_author = "John Doe"
    sample_description = (
        "This book provides insights into the world of programming with practical examples. "
        "Whether you are a beginner or an experienced developer, this book has something for everyone."
    )
    sample_keywords = ["programming", "developer", "coding", "software", "beginner", "examples"]

    # Optimize metadata
    optimized_metadata = optimize_metadata(
        title=sample_title,
        author=sample_author,
        description=sample_description,
        keywords=sample_keywords
    )

    # Save optimized metadata to file
    save_metadata_to_file(optimized_metadata)
```
