"""
Generated Code Metadata:
========================
Original URL: https://hnalkhedmad.com
Prompt: Design a Python API to query and compare features of different iPhone models, specifically focusing on screen size and MagSafe support.
Generated: DETERMINISTIC_5e3dec73eea2573e
Batch ID: 20250622_205436
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
from enum import Enum
from dataclasses import dataclass
import requests
from requests.exceptions import RequestException

class MagSafeSupport(Enum):
    """Enum representing MagSafe support status."""
    SUPPORTED = "Supported"
    NOT_SUPPORTED = "Not Supported"

@dataclass
class IPhoneModel:
    """Dataclass representing an iPhone model with its features."""
    model_name: str
    screen_size: float  # in inches
    magsafe_support: MagSafeSupport

class IPhoneAPI:
    """API to query and compare iPhone models."""
    
    def __init__(self, models_data: Optional[List[Dict]] = None):
        """
        Initialize the API with iPhone models data.
        
        Args:
            models_data: Optional list of dictionaries containing iPhone models data.
                        If not provided, defaults to built-in data.
        """
        self.models = self._load_models(models_data)
    
    def _load_models(self, models_data: Optional[List[Dict]]) -> List[IPhoneModel]:
        """
        Load iPhone models from provided data or default to built-in data.
        
        Args:
            models_data: Optional list of dictionaries containing iPhone models data.
        
        Returns:
            List of IPhoneModel objects.
        """
        if models_data is None:
            models_data = [
                {"model_name": "iPhone 12", "screen_size": 6.1, "magsafe_support": MagSafeSupport.SUPPORTED.value},
                {"model_name": "iPhone 12 Pro", "screen_size": 6.1, "magsafe_support": MagSafeSupport.SUPPORTED.value},
                {"model_name": "iPhone 13", "screen_size": 6.1, "magsafe_support": MagSafeSupport.SUPPORTED.value},
                {"model_name": "iPhone SE (2020)", "screen_size": 4.7, "magsafe_support": MagSafeSupport.NOT_SUPPORTED.value},
                {"model_name": "iPhone 14 Pro", "screen_size": 6.1, "magsafe_support": MagSafeSupport.SUPPORTED.value},
            ]
        
        models = []
        for model in models_data:
            try:
                models.append(IPhoneModel(
                    model_name=model["model_name"],
                    screen_size=float(model["screen_size"]),
                    magsafe_support=MagSafeSupport(model["magsafe_support"])
                ))
            except (KeyError, ValueError) as e:
                raise ValueError(f"Invalid model data: {e}")
        return models
    
    def get_models_by_screen_size(self, min_size: float, max_size: float) -> List[IPhoneModel]:
        """
        Get iPhone models with screen size within the specified range.
        
        Args:
            min_size: Minimum screen size in inches.
            max_size: Maximum screen size in inches.
        
        Returns:
            List of IPhoneModel objects matching the criteria.
        
        Raises:
            ValueError: If min_size is greater than max_size.
        """
        if min_size > max_size:
            raise ValueError("min_size must be less than or equal to max_size")
        
        return [model for model in self.models if min_size <= model.screen_size <= max_size]
    
    def get_models_with_magsafe(self) -> List[IPhoneModel]:
        """
        Get iPhone models that support MagSafe.
        
        Returns:
            List of IPhoneModel objects with MagSafe support.
        """
        return [model for model in self.models if model.magsafe_support == MagSafeSupport.SUPPORTED]
    
    def compare_models(self, model1_name: str, model2_name: str) -> Dict:
        """
        Compare features of two iPhone models.
        
        Args:
            model1_name: Name of the first model to compare.
            model2_name: Name of the second model to compare.
        
        Returns:
            Dictionary with comparison results.
        
        Raises:
            ValueError: If either model is not found.
        """
        model1 = self._get_model_by_name(model1_name)
        model2 = self._get_model_by_name(model2_name)
        
        return {
            "models": [model1_name, model2_name],
            "screen_size_diff": abs(model1.screen_size - model2.screen_size),
            "magsafe_diff": model1.magsafe_support.value != model2.magsafe_support.value
        }
    
    def _get_model_by_name(self, model_name: str) -> IPhoneModel:
        """
        Get an iPhone model by its name.
        
        Args:
            model_name: Name of the model to find.
        
        Returns:
            IPhoneModel object.
        
        Raises:
            ValueError: If model is not found.
        """
        for model in self.models:
            if model.model_name.lower() == model_name.lower():
                return model
        raise ValueError(f"Model '{model_name}' not found")
    
    @classmethod
    def from_json_url(cls, url: str) -> 'IPhoneAPI':
        """
        Create an IPhoneAPI instance by loading models data from a JSON URL.
        
        Args:
            url: URL pointing to JSON data.
        
        Returns:
            IPhoneAPI instance.
        
        Raises:
            RequestException: If there's an error fetching the data.
            ValueError: If the data is invalid.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            models_data = response.json()
            return cls(models_data)
        except RequestException as e:
            raise RequestException(f"Error fetching data from URL: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data: {e}")
```
