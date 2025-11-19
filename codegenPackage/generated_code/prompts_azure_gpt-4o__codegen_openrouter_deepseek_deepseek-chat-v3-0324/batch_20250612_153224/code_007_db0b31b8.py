"""
Generated Code Metadata:
========================
Original URL: https://scout.kz
Prompt: Develop a program to recommend SCOUT attachments (e.g., soil tillers, mulchers, trailers) based on user-selected tractor models and intended operations, as described on the SCOUT.kz website.
Generated: DETERMINISTIC_db0b31b838868432
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

# Data model for tractor and attachment information
class Tractor:
    def __init__(self, model: str, power_hp: float, weight_kg: float, category: str):
        self.model = model
        self.power_hp = power_hp
        self.weight_kg = weight_kg
        self.category = category  # e.g., "compact", "utility", "row-crop"

class Attachment:
    def __init__(self, name: str, compatible_tractor_categories: List[str], min_power_hp: float, 
                 max_power_hp: float, operation_types: List[str], weight_kg: float):
        self.name = name
        self.compatible_tractor_categories = compatible_tractor_categories
        self.min_power_hp = min_power_hp
        self.max_power_hp = max_power_hp
        self.operation_types = operation_types
        self.weight_kg = weight_kg

class AttachmentRecommender:
    def __init__(self):
        self.tractors: Dict[str, Tractor] = {}
        self.attachments: List[Attachment] = []
        self._load_data()

    def _load_data(self):
        """Load tractor and attachment data from JSON files"""
        try:
            with open('tractors.json', 'r') as f:
                tractors_data = json.load(f)
                for model, data in tractors_data.items():
                    self.tractors[model] = Tractor(
                        model=model,
                        power_hp=data['power_hp'],
                        weight_kg=data['weight_kg'],
                        category=data['category']
                    )

            with open('attachments.json', 'r') as f:
                attachments_data = json.load(f)
                for attachment_data in attachments_data:
                    self.attachments.append(Attachment(
                        name=attachment_data['name'],
                        compatible_tractor_categories=attachment_data['compatible_tractor_categories'],
                        min_power_hp=attachment_data['min_power_hp'],
                        max_power_hp=attachment_data['max_power_hp'],
                        operation_types=attachment_data['operation_types'],
                        weight_kg=attachment_data['weight_kg']
                    ))
        except FileNotFoundError as e:
            raise Exception("Data files not found. Please ensure tractors.json and attachments.json exist.") from e
        except json.JSONDecodeError as e:
            raise Exception("Invalid JSON data format in data files.") from e
        except KeyError as e:
            raise Exception(f"Missing required field in data: {str(e)}") from e

    def get_compatible_attachments(self, tractor_model: str, operation_type: str) -> List[Attachment]:
        """
        Get compatible attachments for a given tractor model and operation type.
        
        Args:
            tractor_model: Model name of the tractor
            operation_type: Type of operation (e.g., "tilling", "mulching", "hauling")
            
        Returns:
            List of compatible Attachment objects
            
        Raises:
            ValueError: If tractor model is not found
        """
        if tractor_model not in self.tractors:
            raise ValueError(f"Tractor model '{tractor_model}' not found in database")
        
        tractor = self.tractors[tractor_model]
        compatible_attachments = []
        
        for attachment in self.attachments:
            # Check if attachment is compatible with tractor and operation
            if (tractor.category in attachment.compatible_tractor_categories and
                operation_type in attachment.operation_types and
                attachment.min_power_hp <= tractor.power_hp <= attachment.max_power_hp):
                
                # Check if tractor can handle attachment weight (safety factor of 1.5)
                if tractor.weight_kg >= attachment.weight_kg * 1.5:
                    compatible_attachments.append(attachment)
        
        return compatible_attachments

    def recommend_attachments(self, tractor_model: str, operation_type: str) -> List[Dict]:
        """
        Get recommended attachments with formatted output.
        
        Args:
            tractor_model: Model name of the tractor
            operation_type: Type of operation
            
        Returns:
            List of dictionaries with attachment details, sorted by weight
        """
        attachments = self.get_compatible_attachments(tractor_model, operation_type)
        
        # Sort attachments by weight (lightest first)
        sorted_attachments = sorted(attachments, key=lambda x: x.weight_kg)
        
        return [{
            'name': a.name,
            'compatible_tractor_categories': a.compatible_tractor_categories,
            'required_power_hp': f"{a.min_power_hp}-{a.max_power_hp}",
            'weight_kg': a.weight_kg,
            'suitable_for_operations': a.operation_types
        } for a in sorted_attachments]

# Example usage
if __name__ == "__main__":
    try:
        recommender = AttachmentRecommender()
        
        # Get user input
        tractor_model = input("Enter tractor model: ")
        operation_type = input("Enter operation type (tilling/mulching/hauling): ").lower()
        
        # Get recommendations
        recommendations = recommender.recommend_attachments(tractor_model, operation_type)
        
        # Display results
        print(f"\nRecommended attachments for {tractor_model} ({operation_type}):")
        for i, attachment in enumerate(recommendations, 1):
            print(f"\n{i}. {attachment['name']}")
            print(f"   - Compatible with tractor categories: {', '.join(attachment['compatible_tractor_categories'])}")
            print(f"   - Required power: {attachment['required_power_hp']} HP")
            print(f"   - Weight: {attachment['weight_kg']} kg")
            print(f"   - Suitable for: {', '.join(attachment['suitable_for_operations'])}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```

Note: This code assumes the existence of two JSON files:
1. `tractors.json` - Contains tractor data in the format:
```json
{
    "Model X": {
        "power_hp": 45,
        "weight_kg": 1800,
        "category": "compact"
    },
    ...
}
```

2. `attachments.json` - Contains attachment data in the format:
```json
[
    {
        "name": "Soil Tiller",
        "compatible_tractor_categories": ["compact", "utility"],
        "min_power_hp": 30,
        "max_power_hp": 60,
        "operation_types": ["tilling"],
        "weight_kg": 350
    },
    ...
]
```
