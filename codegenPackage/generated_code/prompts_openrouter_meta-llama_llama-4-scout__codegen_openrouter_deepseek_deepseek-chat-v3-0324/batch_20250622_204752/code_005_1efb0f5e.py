"""
Generated Code Metadata:
========================
Original URL: https://lineage-ai.vercel.app
Prompt: Develop a library for working with Model Cards, including functions for creating, reading, and updating model metadata.
Generated: DETERMINISTIC_1efb0f5ee42dd5b6
Batch ID: 20250622_204752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Model Cards Library

A library for creating, reading, and updating model metadata following the Model Cards specification.
"""

import json
from typing import Dict, Optional, Union
from datetime import datetime
import uuid
from enum import Enum
import jsonschema
from pathlib import Path

class ModelType(Enum):
    """Enumeration of supported model types."""
    CLASSIFICATION = "classification"
    REGRESSION = "regression"
    CLUSTERING = "clustering"
    GENERATIVE = "generative"
    EMBEDDING = "embedding"
    OTHER = "other"

class ModelCard:
    """Class representing a Model Card with metadata about a machine learning model."""
    
    SCHEMA = {
        "type": "object",
        "properties": {
            "model_id": {"type": "string"},
            "model_name": {"type": "string"},
            "model_type": {"type": "string", "enum": [t.value for t in ModelType]},
            "description": {"type": "string"},
            "version": {"type": "string"},
            "owners": {
                "type": "array",
                "items": {"type": "string"}
            },
            "license": {"type": "string"},
            "created_date": {"type": "string", "format": "date-time"},
            "last_updated": {"type": "string", "format": "date-time"},
            "performance_metrics": {"type": "object"},
            "training_data": {"type": "object"},
            "evaluation_data": {"type": "object"},
            "ethical_considerations": {"type": "object"},
            "caveats_and_recommendations": {"type": "object"},
            "references": {
                "type": "array",
                "items": {"type": "string"}
            }
        },
        "required": ["model_id", "model_name", "model_type", "version"]
    }
    
    def __init__(self, model_name: str, model_type: ModelType, version: str, **kwargs):
        """
        Initialize a ModelCard instance.
        
        Args:
            model_name: Name of the model
            model_type: Type of the model (from ModelType enum)
            version: Version string for the model
            **kwargs: Additional model card properties
        """
        self.model_id = str(uuid.uuid4())
        self.model_name = model_name
        self.model_type = model_type.value if isinstance(model_type, ModelType) else model_type
        self.version = version
        self.description = kwargs.get("description", "")
        self.owners = kwargs.get("owners", [])
        self.license = kwargs.get("license", "")
        self.created_date = datetime.utcnow().isoformat()
        self.last_updated = self.created_date
        self.performance_metrics = kwargs.get("performance_metrics", {})
        self.training_data = kwargs.get("training_data", {})
        self.evaluation_data = kwargs.get("evaluation_data", {})
        self.ethical_considerations = kwargs.get("ethical_considerations", {})
        self.caveats_and_recommendations = kwargs.get("caveats_and_recommendations", {})
        self.references = kwargs.get("references", [])
        
        self.validate()
    
    def validate(self) -> None:
        """Validate the model card against the schema."""
        card_dict = self.to_dict()
        try:
            jsonschema.validate(instance=card_dict, schema=self.SCHEMA)
        except jsonschema.ValidationError as e:
            raise ValueError(f"Model card validation failed: {e.message}")
    
    def update(self, **kwargs) -> None:
        """
        Update model card properties.
        
        Args:
            **kwargs: Key-value pairs of properties to update
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"'{key}' is not a valid ModelCard attribute")
        
        self.last_updated = datetime.utcnow().isoformat()
        self.validate()
    
    def to_dict(self) -> Dict:
        """Convert the ModelCard instance to a dictionary."""
        return {
            "model_id": self.model_id,
            "model_name": self.model_name,
            "model_type": self.model_type,
            "description": self.description,
            "version": self.version,
            "owners": self.owners,
            "license": self.license,
            "created_date": self.created_date,
            "last_updated": self.last_updated,
            "performance_metrics": self.performance_metrics,
            "training_data": self.training_data,
            "evaluation_data": self.evaluation_data,
            "ethical_considerations": self.ethical_considerations,
            "caveats_and_recommendations": self.caveats_and_recommendations,
            "references": self.references
        }
    
    def to_json(self) -> str:
        """Serialize the ModelCard to JSON string."""
        return json.dumps(self.to_dict(), indent=2)
    
    def save(self, file_path: Union[str, Path]) -> None:
        """
        Save the ModelCard to a JSON file.
        
        Args:
            file_path: Path to save the JSON file
        """
        with open(file_path, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)

    @classmethod
    def from_dict(cls, data: Dict) -> 'ModelCard':
        """
        Create a ModelCard from a dictionary.
        
        Args:
            data: Dictionary containing model card data
            
        Returns:
            ModelCard instance
        """
        model_type = ModelType(data["model_type"]) if "model_type" in data else ModelType.OTHER
        card = cls(
            model_name=data["model_name"],
            model_type=model_type,
            version=data["version"],
            description=data.get("description", ""),
            owners=data.get("owners", []),
            license=data.get("license", ""),
            performance_metrics=data.get("performance_metrics", {}),
            training_data=data.get("training_data", {}),
            evaluation_data=data.get("evaluation_data", {}),
            ethical_considerations=data.get("ethical_considerations", {}),
            caveats_and_recommendations=data.get("caveats_and_recommendations", {}),
            references=data.get("references", [])
        )
        card.model_id = data.get("model_id", str(uuid.uuid4()))
        card.created_date = data.get("created_date", datetime.utcnow().isoformat())
        card.last_updated = data.get("last_updated", card.created_date)
        return card
    
    @classmethod
    def from_json(cls, json_str: str) -> 'ModelCard':
        """
        Create a ModelCard from a JSON string.
        
        Args:
            json_str: JSON string containing model card data
            
        Returns:
            ModelCard instance
        """
        data = json.loads(json_str)
        return cls.from_dict(data)
    
    @classmethod
    def load(cls, file_path: Union[str, Path]) -> 'ModelCard':
        """
        Load a ModelCard from a JSON file.
        
        Args:
            file_path: Path to the JSON file
            
        Returns:
            ModelCard instance
        """
        with open(file_path, 'r') as f:
            data = json.load(f)
        return cls.from_dict(data)

class ModelCardManager:
    """Manager class for handling collections of ModelCards."""
    
    def __init__(self):
        self.cards: Dict[str, ModelCard] = {}
    
    def add_card(self, card: ModelCard) -> None:
        """
        Add a ModelCard to the manager.
        
        Args:
            card: ModelCard instance to add
        """
        if card.model_id in self.cards:
            raise ValueError(f"ModelCard with ID {card.model_id} already exists")
        self.cards[card.model_id] = card
    
    def get_card(self, model_id: str) -> Optional[ModelCard]:
        """
        Get a ModelCard by its ID.
        
        Args:
            model_id: ID of the ModelCard to retrieve
            
        Returns:
            ModelCard instance or None if not found
        """
        return self.cards.get(model_id)
    
    def update_card(self, model_id: str, **kwargs) -> None:
        """
        Update a ModelCard's properties.
        
        Args:
            model_id: ID of the ModelCard to update
            **kwargs: Key-value pairs of properties to update
        """
        if model_id not in self.cards:
            raise ValueError(f"ModelCard with ID {model_id} not found")
        self.cards[model_id].update(**kwargs)
    
    def remove_card(self, model_id: str) -> None:
        """
        Remove a ModelCard from the manager.
        
        Args:
            model_id: ID of the ModelCard to remove
        """
        if model_id not in self.cards:
            raise ValueError(f"ModelCard with ID {model_id} not found")
        del self.cards[model_id]
    
    def list_cards(self) -> Dict[str, Dict]:
        """
        List all ModelCards in the manager.
        
        Returns:
            Dictionary mapping model IDs to their basic info
        """
        return
