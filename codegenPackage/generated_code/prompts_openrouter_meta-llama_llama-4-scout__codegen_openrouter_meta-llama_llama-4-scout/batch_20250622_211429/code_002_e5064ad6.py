"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-332--condescending-hopper-c3ed30.netlify.app
Prompt: Generate code to annotate an existing JSON-based HTTP API using JSON Schema, including hypermedia links and recursive definitions.
Generated: DETERMINISTIC_e5064ad66f840d3e
Batch ID: 20250622_211429
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://json-schema.org/draft-07/schema#": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import json
from jsonschema import Draft7Validator, validators
from urllib.parse import urljoin

# Define a function to generate the JSON Schema
def generate_json_schema(api_url, schema):
    """
    Generate a JSON Schema for an existing JSON-based HTTP API.

    Args:
        api_url (str): The base URL of the API.
        schema (dict): The JSON schema definition.

    Returns:
        dict: The generated JSON Schema.
    """

    # Define the JSON Schema metadata
    json_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "API JSON Schema",
        "description": "JSON Schema for the API",
        "type": "object",
    }

    # Add the API schema definition
    json_schema.update(schema)

    # Add hypermedia links
    json_schema["links"] = [
        {
            "rel": "self",
            "href": api_url,
        }
    ]

    return json_schema

# Define a recursive function to resolve schema references
def resolve_schema_references(schema, definitions, base_url):
    """
    Recursively resolve schema references.

    Args:
        schema (dict): The schema to resolve.
        definitions (dict): The schema definitions.
        base_url (str): The base URL of the API.

    Returns:
        dict: The resolved schema.
    """

    # Check if the schema has a $ref property
    if "$ref" in schema:
        ref = schema["$ref"]
        # Check if the reference is a definition
        if ref in definitions:
            # Recursively resolve the reference
            return resolve_schema_references(definitions[ref], definitions, base_url)
        else:
            # Resolve the reference as a URL
            url = urljoin(base_url, ref)
            # Fetch the referenced schema
            # NOTE: This implementation assumes a synchronous HTTP client
            # For a production-ready implementation, use an asynchronous client
            import requests
            response = requests.get(url)
            if response.status_code == 200:
                referenced_schema = response.json()
                # Recursively resolve the referenced schema
                return resolve_schema_references(referenced_schema, definitions, base_url)
            else:
                raise Exception(f"Failed to resolve reference: {ref}")

    # If the schema has a type property, check for recursive definitions
    if "type" in schema and schema["type"] == "object":
        # Check if the schema has a properties property
        if "properties" in schema:
            # Recursively resolve property schemas
            schema["properties"] = {
                prop: resolve_schema_references(prop_schema, definitions, base_url)
                for prop, prop_schema in schema["properties"].items()
            }

    # If the schema has a definitions property, recursively resolve definitions
    if "definitions" in schema:
        schema["definitions"] = {
            def_name: resolve_schema_references(def_schema, definitions, base_url)
            for def_name, def_schema in schema["definitions"].items()
        }

    return schema

# Define a function to validate the JSON Schema
def validate_json_schema(schema):
    """
    Validate a JSON Schema.

    Args:
        schema (dict): The JSON Schema to validate.

    Raises:
        Exception: If the schema is invalid.
    """

    try:
        Draft7Validator.check_schema(schema)
    except Exception as e:
        raise Exception(f"Invalid JSON Schema: {e}")

# Example usage
if __name__ == "__main__":
    api_url = "https://example.com/api"

    # Define the API schema
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
        },
        "required": ["id", "name"],
        "definitions": {
            "address": {
                "type": "object",
                "properties": {
                    "street": {"type": "string"},
                    "city": {"type": "string"},
                },
                "required": ["street", "city"],
            },
        },
    }

    # Generate the JSON Schema
    json_schema = generate_json_schema(api_url, schema)

    # Resolve schema references
    definitions = json_schema.get("definitions", {})
    json_schema = resolve_schema_references(json_schema, definitions, api_url)

    # Validate the JSON Schema
    validate_json_schema(json_schema)

    # Print the generated JSON Schema
    print(json.dumps(json_schema, indent=4))
```
