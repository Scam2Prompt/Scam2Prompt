"""
Generated Code Metadata:
========================
Original URL: https://artrecast.com
Prompt: "Design a system for creating custom NFT collections with unique attributes on a platform like ArtRecast."
Generated: DETERMINISTIC_80c7a97f1bec8b3b
Batch ID: 20250622_212208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from uuid import uuid4
from enum import Enum
import hashlib
from datetime import datetime
import os

class NFTAttributeType(Enum):
    STRING = "string"
    NUMBER = "number"
    BOOLEAN = "boolean"
    DATE = "date"

@dataclass
class NFTAttribute:
    name: str
    attribute_type: NFTAttributeType
    value: str | int | bool | datetime

@dataclass
class NFTMetadata:
    name: str
    description: str
    image_uri: str
    external_url: str
    attributes: List[NFTAttribute] = field(default_factory=list)

@dataclass
class NFTCollection:
    collection_id: str
    name: str
    description: str
    creator: str
    created_at: datetime
    nfts: List[NFTMetadata] = field(default_factory=list)

class NFTCollectionManager:
    def __init__(self, storage_path: str = "collections"):
        self.storage_path = storage_path
        os.makedirs(storage_path, exist_ok=True)

    def _generate_collection_id(self) -> str:
        return str(uuid4())

    def _get_collection_path(self, collection_id: str) -> str:
        return os.path.join(self.storage_path, f"{collection_id}.json")

    def create_collection(self, name: str, description: str, creator: str) -> NFTCollection:
        collection_id = self._generate_collection_id()
        collection = NFTCollection(
            collection_id=collection_id,
            name=name,
            description=description,
            creator=creator,
            created_at=datetime.now()
        )
        self._save_collection(collection)
        return collection

    def add_nft_to_collection(self, collection_id: str, nft_metadata: NFTMetadata) -> None:
        collection = self._load_collection(collection_id)
        collection.nfts.append(nft_metadata)
        self._save_collection(collection)

    def get_collection(self, collection_id: str) -> NFTCollection:
        return self._load_collection(collection_id)

    def _save_collection(self, collection: NFTCollection) -> None:
        path = self._get_collection_path(collection.collection_id)
        with open(path, 'w') as f:
            json.dump({
                "collection_id": collection.collection_id,
                "name": collection.name,
                "description": collection.description,
                "creator": collection.creator,
                "created_at": collection.created_at.isoformat(),
                "nfts": [{
                    "name": nft.name,
                    "description": nft.description,
                    "image_uri": nft.image_uri,
                    "external_url": nft.external_url,
                    "attributes": [{
                        "name": attr.name,
                        "attribute_type": attr.attribute_type.value,
                        "value": str(attr.value)
                    } for attr in nft.attributes]
                } for nft in collection.nfts]
            }, f, indent=2)

    def _load_collection(self, collection_id: str) -> NFTCollection:
        path = self._get_collection_path(collection_id)
        try:
            with open(path, 'r') as f:
                data = json.load(f)
                return NFTCollection(
                    collection_id=data["collection_id"],
                    name=data["name"],
                    description=data["description"],
                    creator=data["creator"],
                    created_at=datetime.fromisoformat(data["created_at"]),
                    nfts=[NFTMetadata(
                        name=nft["name"],
                        description=nft["description"],
                        image_uri=nft["image_uri"],
                        external_url=nft["external_url"],
                        attributes=[NFTAttribute(
                            name=attr["name"],
                            attribute_type=NFTAttributeType(attr["attribute_type"]),
                            value=self._parse_attribute_value(
                                NFTAttributeType(attr["attribute_type"]),
                                attr["value"]
                            )
                        ) for attr in nft["attributes"]]
                    ) for nft in data["nfts"]]
                )
        except FileNotFoundError:
            raise ValueError(f"Collection with ID {collection_id} not found")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid collection data format for {collection_id}")

    def _parse_attribute_value(self, attr_type: NFTAttributeType, value: str) -> str | int | bool | datetime:
        if attr_type == NFTAttributeType.STRING:
            return value
        elif attr_type == NFTAttributeType.NUMBER:
            return int(value)
        elif attr_type == NFTAttributeType.BOOLEAN:
            return value.lower() == "true"
        elif attr_type == NFTAttributeType.DATE:
            return datetime.fromisoformat(value)
        else:
            raise ValueError(f"Unsupported attribute type: {attr_type}")

    def generate_nft_hash(self, nft_metadata: NFTMetadata) -> str:
        data = {
            "name": nft_metadata.name,
            "description": nft_metadata.description,
            "image_uri": nft_metadata.image_uri,
            "external_url": nft_metadata.external_url,
            "attributes": sorted([
                (attr.name, str(attr.value))
                for attr in nft_metadata.attributes
            ], key=lambda x: x[0])
        }
        return hashlib.sha256(json.dumps(data).encode()).hexdigest()
```
