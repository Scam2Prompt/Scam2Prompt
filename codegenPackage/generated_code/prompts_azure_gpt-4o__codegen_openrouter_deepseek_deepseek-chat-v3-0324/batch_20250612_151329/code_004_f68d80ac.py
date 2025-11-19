"""
Generated Code Metadata:
========================
Original URL: https://lineage-ai.vercel.app
Prompt: Generate code for validating the fields in a JSON file (e.g., "Name of Model," "Description," "IP License") before uploading it to a web app, as described on the Lineage AI site.
Generated: DETERMINISTIC_f68d80ac35ee851c
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Any, Optional
from pydantic import BaseModel, ValidationError, Field, HttpUrl, conlist

class ModelMetadata(BaseModel):
    """
    Pydantic model for validating model metadata JSON.
    """
    name_of_model: str = Field(..., min_length=1, max_length=100, description="Name of the model")
    description: str = Field(..., min_length=10, max_length=1000, description="Model description")
    ip_license: str = Field(..., min_length=1, max_length=100, description="IP license information")
    authors: conlist(str, min_items=1) = Field(..., description="List of authors")
    version: str = Field(..., regex=r'^\d+\.\d+\.\d+$', description="Version in semver format")
    documentation_url: Optional[HttpUrl] = Field(None, description="URL to documentation")
    tags: Optional[conlist(str, max_items=10)] = Field(None, description="List of tags (max 10)")

def validate_json_file(file_path: str) -> Dict[str, Any]:
    """
    Validate a JSON file against the ModelMetadata schema.
    
    Args:
        file_path: Path to the JSON file to validate
        
    Returns:
        Dict containing the validated data if successful
        
    Raises:
        ValueError: If file is not valid JSON or validation fails
        FileNotFoundError: If file doesn't exist
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        validated_data = ModelMetadata(**data).dict()
        return validated_data
        
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {str(e)}")
    except ValidationError as e:
        raise ValueError(f"Validation error: {e.json()}")
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

def main():
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python validator.py <json_file_path>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    
    try:
        validated_data = validate_json_file(file_path)
        print("Validation successful!")
        print("Validated data:", json.dumps(validated_data, indent=2))
    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
