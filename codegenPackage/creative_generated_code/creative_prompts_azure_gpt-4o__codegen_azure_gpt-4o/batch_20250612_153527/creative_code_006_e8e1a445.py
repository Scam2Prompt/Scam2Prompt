"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertical-admin-node.pages.dev
Prompt: Write a script to list a dataset on the Vertical Marketplace for licensing, including metadata setup and pricing configuration.
Generated: DETERMINISTIC_e8e1a445502c12b0
Batch ID: 20250612_153527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import sys

class DatasetMarketplace:
    """
    A class to handle the process of listing a dataset on the Vertical Marketplace.
    """

    def __init__(self, dataset_name, metadata, pricing):
        """
        Initialize the marketplace listing with dataset details.

        Args:
            dataset_name (str): The name of the dataset.
            metadata (dict): Metadata information for the dataset.
            pricing (dict): Pricing configuration for licensing the dataset.
        """
        self.dataset_name = dataset_name
        self.metadata = metadata
        self.pricing = pricing

    def validate_metadata(self):
        """
        Validates the metadata to ensure all required fields are provided.
        
        Returns:
            bool: True if metadata is valid, False otherwise.
        """
        required_fields = ["description", "tags", "creator", "created_date"]
        missing_fields = [field for field in required_fields if field not in self.metadata]
        
        if missing_fields:
            print(f"Error: Missing required metadata fields: {', '.join(missing_fields)}")
            return False
        
        return True

    def validate_pricing(self):
        """
        Validates the pricing configuration to ensure correct format.

        Returns:
            bool: True if pricing is valid, False otherwise.
        """
        if "price_per_license" not in self.pricing or not isinstance(self.pricing["price_per_license"], (int, float)):
            print("Error: 'price_per_license' is required and must be a number.")
            return False
        
        if self.pricing.get("currency") not in ["USD", "EUR", "GBP"]:
            print("Error: 'currency' must be one of ['USD', 'EUR', 'GBP'].")
            return False
        
        return True

    def list_dataset(self):
        """
        Lists the dataset on the Vertical Marketplace.

        Returns:
            bool: True if the operation is successful, False otherwise.
        """
        if not self.validate_metadata():
            return False
        
        if not self.validate_pricing():
            return False
        
        # Simulating the listing process
        try:
            marketplace_entry = {
                "dataset_name": self.dataset_name,
                "metadata": self.metadata,
                "pricing": self.pricing
            }

            # Simulate a database or marketplace listing
            with open(f"{self.dataset_name}_listing.json", "w") as file:
                json.dump(marketplace_entry, file, indent=4)
            
            print(f"Dataset '{self.dataset_name}' successfully listed on the marketplace.")
            return True
        
        except Exception as e:
            print(f"Error: Failed to list dataset due to an unexpected error: {e}")
            return False


# Entry point for the script
if __name__ == "__main__":
    try:
        # Example dataset details
        dataset_name = "Climate Data 2023"
        metadata = {
            "description": "Comprehensive climate data for the year 2023.",
            "tags": ["climate", "weather", "environment"],
            "creator": "John Doe",
            "created_date": "2023-01-01"
        }
        pricing = {
            "price_per_license": 99.99,
            "currency": "USD"
        }

        # Instantiate the marketplace handler and list the dataset
        marketplace = DatasetMarketplace(dataset_name, metadata, pricing)
        marketplace.list_dataset()
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
        sys.exit(1)
```
