"""
Generated Code Metadata:
========================
Original URL: https://vertical-admin-node.pages.dev
Prompt: "Design a marketplace listing for a customized AI model, using Vertical's monetization features and licensing options for passive revenue generation."
Generated: DETERMINISTIC_f9bcab3614e7dbb4
Batch ID: 20250622_210909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Marketplace listing for a customized AI model with Vertical's monetization and licensing features.
This module handles the creation, management, and monetization of AI model listings.
"""

from typing import Optional, Dict, List
from enum import Enum
import datetime
import uuid
from dataclasses import dataclass


class LicenseType(Enum):
    """Enum representing different licensing options for the AI model."""
    SINGLE_USE = "SINGLE_USE"
    SUBSCRIPTION = "SUBSCRIPTION"
    ENTERPRISE = "ENTERPRISE"
    OPEN_SOURCE = "OPEN_SOURCE"


class PricingModel(Enum):
    """Enum representing different pricing models for the AI model."""
    ONE_TIME = "ONE_TIME"
    RECURRING = "RECURRING"
    USAGE_BASED = "USAGE_BASED"


@dataclass
class License:
    """Data class representing a license for the AI model."""
    license_id: str
    license_type: LicenseType
    price: float
    currency: str = "USD"
    description: Optional[str] = None
    terms_and_conditions: Optional[str] = None


@dataclass
class AIModel:
    """Data class representing an AI model listing."""
    model_id: str
    name: str
    description: str
    version: str
    creator_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    licenses: List[License]
    pricing_model: PricingModel
    is_active: bool = True
    tags: Optional[List[str]] = None


class MarketplaceListing:
    """Class to manage AI model listings in the marketplace."""

    def __init__(self):
        self.listings: Dict[str, AIModel] = {}

    def create_listing(
        self,
        name: str,
        description: str,
        version: str,
        creator_id: str,
        licenses: List[License],
        pricing_model: PricingModel,
        tags: Optional[List[str]] = None
    ) -> AIModel:
        """
        Create a new AI model listing.
        
        Args:
            name: Name of the AI model.
            description: Description of the AI model.
            version: Version of the AI model.
            creator_id: ID of the creator.
            licenses: List of licenses available for the model.
            pricing_model: Pricing model for the model.
            tags: Optional list of tags for the model.
            
        Returns:
            The created AI model listing.
            
        Raises:
            ValueError: If required fields are missing or invalid.
        """
        if not name or not description or not version or not creator_id or not licenses:
            raise ValueError("Missing required fields for listing creation.")

        model_id = str(uuid.uuid4())
        now = datetime.datetime.utcnow()
        
        model = AIModel(
            model_id=model_id,
            name=name,
            description=description,
            version=version,
            creator_id=creator_id,
            created_at=now,
            updated_at=now,
            licenses=licenses,
            pricing_model=pricing_model,
            tags=tags
        )
        
        self.listings[model_id] = model
        return model

    def update_listing(
        self,
        model_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        version: Optional[str] = None,
        licenses: Optional[List[License]] = None,
        pricing_model: Optional[PricingModel] = None,
        tags: Optional[List[str]] = None,
        is_active: Optional[bool] = None
    ) -> AIModel:
        """
        Update an existing AI model listing.
        
        Args:
            model_id: ID of the model to update.
            name: Updated name of the model.
            description: Updated description of the model.
            version: Updated version of the model.
            licenses: Updated list of licenses.
            pricing_model: Updated pricing model.
            tags: Updated list of tags.
            is_active: Updated active status.
            
        Returns:
            The updated AI model listing.
            
        Raises:
            ValueError: If model_id is invalid or required fields are missing.
        """
        if model_id not in self.listings:
            raise ValueError("Model ID not found.")
            
        model = self.listings[model_id]
        
        if name is not None:
            model.name = name
        if description is not None:
            model.description = description
        if version is not None:
            model.version = version
        if licenses is not None:
            model.licenses = licenses
        if pricing_model is not None:
            model.pricing_model = pricing_model
        if tags is not None:
            model.tags = tags
        if is_active is not None:
            model.is_active = is_active
            
        model.updated_at = datetime.datetime.utcnow()
        
        return model

    def get_listing(self, model_id: str) -> AIModel:
        """
        Retrieve an AI model listing by ID.
        
        Args:
            model_id: ID of the model to retrieve.
            
        Returns:
            The requested AI model listing.
            
        Raises:
            ValueError: If model_id is invalid.
        """
        if model_id not in self.listings:
            raise ValueError("Model ID not found.")
            
        return self.listings[model_id]

    def deactivate_listing(self, model_id: str) -> AIModel:
        """
        Deactivate an AI model listing.
        
        Args:
            model_id: ID of the model to deactivate.
            
        Returns:
            The deactivated AI model listing.
            
        Raises:
            ValueError: If model_id is invalid.
        """
        return self.update_listing(model_id, is_active=False)

    def activate_listing(self, model_id: str) -> AIModel:
        """
        Activate an AI model listing.
        
        Args:
            model_id: ID of the model to activate.
            
        Returns:
            The activated AI model listing.
            
        Raises:
            ValueError: If model_id is invalid.
        """
        return self.update_listing(model_id, is_active=True)


# Example usage
if __name__ == "__main__":
    marketplace = MarketplaceListing()
    
    # Create licenses
    single_use_license = License(
        license_id=str(uuid.uuid4()),
        license_type=LicenseType.SINGLE_USE,
        price=99.99,
        description="Single use license for the AI model."
    )
    
    subscription_license = License(
        license_id=str(uuid.uuid4()),
        license_type=LicenseType.SUBSCRIPTION,
        price=29.99,
        description="Monthly subscription license for the AI model."
    )
    
    # Create a listing
    model = marketplace.create_listing(
        name="Sentiment Analysis Pro",
        description="Advanced sentiment analysis model with 95% accuracy.",
        version="1.0.0",
        creator_id="user_123",
        licenses=[single_use_license, subscription_license],
        pricing_model=PricingModel.RECURRING,
        tags=["NLP", "Sentiment Analysis", "Machine Learning"]
    )
    
    print(f"Created model: {model.name} (ID: {model.model_id})")
```
