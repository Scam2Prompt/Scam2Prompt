"""
Generated Code Metadata:
========================
Original URL: https://www.brothernz.com
Prompt: Write Python code to automate the selection of Brother ScanNCut machine models from a product catalog, filtering by price and features such as Disney-themed designs.
Generated: DETERMINISTIC_7d56294ee2b9baa8
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class ScanNCutModel:
    """
    Represents a Brother ScanNCut machine model with its attributes.
    """
    def __init__(
        self,
        model_id: str,
        name: str,
        price: float,
        has_disney: bool,
        features: List[str]
    ):
        self.model_id = model_id
        self.name = name
        self.price = price
        self.has_disney = has_disney
        self.features = features

    def to_dict(self) -> Dict:
        """Convert the model to a dictionary for easy serialization."""
        return {
            "model_id": self.model_id,
            "name": self.name,
            "price": self.price,
            "has_disney": self.has_disney,
            "features": self.features
        }

class ScanNCutCatalog:
    """
    Handles the catalog of ScanNCut models and provides filtering capabilities.
    """
    def __init__(self, catalog_file: Optional[str] = None):
        self.models: List[ScanNCutModel] = []
        if catalog_file:
            self.load_catalog(catalog_file)

    def load_catalog(self, file_path: str) -> None:
        """Load the catalog from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                for item in data:
                    self.models.append(
                        ScanNCutModel(
                            model_id=item["model_id"],
                            name=item["name"],
                            price=item["price"],
                            has_disney=item["has_disney"],
                            features=item["features"]
                        )
                    )
        except FileNotFoundError:
            raise FileNotFoundError(f"Catalog file not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in catalog file: {file_path}")
        except KeyError as e:
            raise KeyError(f"Missing required field in catalog: {e}")

    def filter_models(
        self,
        max_price: Optional[float] = None,
        min_price: Optional[float] = None,
        has_disney: Optional[bool] = None,
        required_features: Optional[List[str]] = None
    ) -> List[ScanNCutModel]:
        """
        Filter models based on price, Disney availability, and features.
        
        Args:
            max_price: Maximum price threshold
            min_price: Minimum price threshold
            has_disney: Whether to include only Disney-themed models
            required_features: List of features that must be present
            
        Returns:
            List of filtered ScanNCutModel objects
        """
        filtered = self.models
        
        if max_price is not None:
            filtered = [m for m in filtered if m.price <= max_price]
        
        if min_price is not None:
            filtered = [m for m in filtered if m.price >= min_price]
        
        if has_disney is not None:
            filtered = [m for m in filtered if m.has_disney == has_disney]
        
        if required_features:
            filtered = [
                m for m in filtered
                if all(feature in m.features for feature in required_features)
            ]
        
        return filtered

    def save_filtered_results(
        self,
        models: List[ScanNCutModel],
        output_file: str
    ) -> None:
        """Save filtered models to a JSON file."""
        try:
            with open(output_file, 'w') as file:
                json.dump([m.to_dict() for m in models], file, indent=2)
        except IOError as e:
            raise IOError(f"Error writing to output file: {e}")

def main():
    try:
        # Initialize catalog
        catalog = ScanNCutCatalog("scanncut_catalog.json")
        
        # Filter parameters
        filtered_models = catalog.filter_models(
            max_price=500.00,
            min_price=200.00,
            has_disney=True,
            required_features=["Wireless", "Auto Blade Detection"]
        )
        
        # Save results
        catalog.save_filtered_results(filtered_models, "filtered_results.json")
        print(f"Found {len(filtered_models)} matching models.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
