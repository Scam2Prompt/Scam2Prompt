"""
Generated Code Metadata:
========================
Original URL: https://app-chainbase.com
Prompt: Write a code snippet that demonstrates how to create a manuscript for converting various data sources into datasets using Chainbase's API.
Generated: DETERMINISTIC_ed1f26f68ab43b2f
Batch ID: 20250612_155632
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.chainbase.online/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/data": {
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
import requests
import json
from typing import Dict, List, Optional, Union
from pydantic import BaseModel, ValidationError

class DataSourceConfig(BaseModel):
    """Configuration model for a data source."""
    source_type: str  # e.g., "api", "database", "csv"
    connection_details: Dict[str, Union[str, int, bool]]
    query: Optional[str] = None
    format: Optional[str] = "json"

class DatasetConfig(BaseModel):
    """Configuration model for the output dataset."""
    name: str
    description: Optional[str] = None
    schema: Dict[str, str]  # field_name: field_type
    output_format: str = "parquet"

class ChainbaseAPIClient:
    """Client for interacting with Chainbase's API."""
    
    def __init__(self, api_key: str, base_url: str = "https://api.chainbase.online/v1"):
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        })
    
    def create_dataset(
        self,
        data_source: DataSourceConfig,
        dataset_config: DatasetConfig,
        transformations: Optional[List[Dict]] = None
    ) -> Dict:
        """
        Create a dataset from a data source using Chainbase's API.
        
        Args:
            data_source: Configuration for the data source
            dataset_config: Configuration for the output dataset
            transformations: Optional list of transformations to apply
            
        Returns:
            Response from the API
        """
        payload = {
            "data_source": data_source.dict(),
            "dataset_config": dataset_config.dict(),
            "transformations": transformations or []
        }
        
        try:
            response = self.session.post(
                f"{self.base_url}/datasets",
                data=json.dumps(payload)
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
        except json.JSONDecodeError as e:
            raise Exception(f"Failed to decode API response: {str(e)}")

def main():
    # Example configuration
    api_key = "your_chainbase_api_key"
    client = ChainbaseAPIClient(api_key)
    
    # Data source configuration (example: API source)
    data_source = DataSourceConfig(
        source_type="api",
        connection_details={
            "url": "https://api.example.com/data",
            "method": "GET",
            "headers": {"Accept": "application/json"}
        },
        query="$.items[*]"  # Example JSONPath query
    )
    
    # Dataset configuration
    dataset_config = DatasetConfig(
        name="example_dataset",
        description="Dataset created from example API",
        schema={
            "id": "string",
            "value": "number",
            "timestamp": "datetime"
        },
        output_format="parquet"
    )
    
    # Optional transformations
    transformations = [
        {
            "type": "filter",
            "condition": "value > 100"
        },
        {
            "type": "rename",
            "from": "id",
            "to": "identifier"
        }
    ]
    
    try:
        # Create the dataset
        response = client.create_dataset(data_source, dataset_config, transformations)
        print(f"Dataset created successfully: {response}")
    except ValidationError as e:
        print(f"Configuration validation error: {e}")
    except Exception as e:
        print(f"Error creating dataset: {e}")

if __name__ == "__main__":
    main()
```
