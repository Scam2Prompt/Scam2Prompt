"""
Generated Code Metadata:
========================
Original URL: https://learn.ipdrawingacademy.com
Prompt: Develop a Python script to manage reusable components in system diagrams for patent drawings, referencing the "Mastering Reusable Components in Patent Drawings" course.
Generated: DETERMINISTIC_00e6ffd77a039775
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
System Diagram Component Manager for Patent Drawings

This script manages reusable components in system diagrams for patent drawings,
following best practices from the "Mastering Reusable Components in Patent Drawings" course.

Features:
- Component storage and retrieval
- Version control
- Dependency management
- Export to common diagram formats
"""

import json
import os
import uuid
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import shutil
from pathlib import Path
import hashlib

# Supported export formats
SUPPORTED_FORMATS = ['svg', 'png', 'pdf', 'dxf']

class ComponentManager:
    """
    Manages reusable components for system diagrams in patent drawings.
    """
    
    def __init__(self, storage_path: str = "components_db"):
        """
        Initialize the component manager with storage path.
        
        Args:
            storage_path: Path to store component database
        """
        self.storage_path = Path(storage_path)
        self.components_path = self.storage_path / "components"
        self.metadata_file = self.storage_path / "metadata.json"
        
        # Initialize storage directories
        self._initialize_storage()
        
    def _initialize_storage(self) -> None:
        """Create necessary directories and files if they don't exist."""
        try:
            self.storage_path.mkdir(exist_ok=True)
            self.components_path.mkdir(exist_ok=True)
            
            if not self.metadata_file.exists():
                with open(self.metadata_file, 'w') as f:
                    json.dump({"components": {}, "next_id": 1}, f)
        except OSError as e:
            raise RuntimeError(f"Failed to initialize storage: {str(e)}")
    
    def _load_metadata(self) -> Dict:
        """Load metadata from file."""
        try:
            with open(self.metadata_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            raise RuntimeError(f"Failed to load metadata: {str(e)}")
    
    def _save_metadata(self, metadata: Dict) -> None:
        """Save metadata to file."""
        try:
            with open(self.metadata_file, 'w') as f:
                json.dump(metadata, f, indent=2)
        except OSError as e:
            raise RuntimeError(f"Failed to save metadata: {str(e)}")
    
    def _get_component_path(self, component_id: str) -> Path:
        """Get path to component directory."""
        return self.components_path / component_id
    
    def _validate_component_data(self, data: Dict) -> bool:
        """Validate component data structure."""
        required_fields = ['name', 'description', 'type', 'content']
        return all(field in data for field in required_fields)
    
    def _generate_component_id(self) -> str:
        """Generate a unique component ID."""
        metadata = self._load_metadata()
        component_id = f"comp-{metadata['next_id']}"
        metadata['next_id'] += 1
        self._save_metadata(metadata)
        return component_id
    
    def _generate_version_hash(self, content: str) -> str:
        """Generate a hash for version tracking."""
        return hashlib.sha256(content.encode()).hexdigest()[:8]
    
    def add_component(self, component_data: Dict) -> str:
        """
        Add a new component to the system.
        
        Args:
            component_data: Dictionary containing component data
            
        Returns:
            Component ID of the newly added component
            
        Raises:
            ValueError: If component data is invalid
            RuntimeError: If component storage fails
        """
        if not self._validate_component_data(component_data):
            raise ValueError("Invalid component data structure")
        
        component_id = self._generate_component_id()
        component_path = self._get_component_path(component_id)
        
        try:
            # Create component directory
            component_path.mkdir()
            
            # Add version information
            version_hash = self._generate_version_hash(component_data['content'])
            version_data = {
                "version": "1.0.0",
                "hash": version_hash,
                "timestamp": datetime.now().isoformat(),
                "content": component_data['content']
            }
            
            # Save version file
            with open(component_path / "current_version.json", 'w') as f:
                json.dump(version_data, f)
            
            # Update metadata
            metadata = self._load_metadata()
            metadata['components'][component_id] = {
                "name": component_data['name'],
                "description": component_data['description'],
                "type": component_data['type'],
                "versions": ["1.0.0"],
                "dependencies": component_data.get('dependencies', []),
                "created": datetime.now().isoformat(),
                "modified": datetime.now().isoformat()
            }
            self._save_metadata(metadata)
            
            return component_id
            
        except OSError as e:
            raise RuntimeError(f"Failed to add component: {str(e)}")
    
    def get_component(self, component_id: str, version: str = "latest") -> Dict:
        """
        Retrieve a component by ID and optional version.
        
        Args:
            component_id: ID of the component to retrieve
            version: Version to retrieve (default: "latest")
            
        Returns:
            Dictionary containing component data and metadata
            
        Raises:
            ValueError: If component doesn't exist
            RuntimeError: If component retrieval fails
        """
        metadata = self._load_metadata()
        
        if component_id not in metadata['components']:
            raise ValueError(f"Component {component_id} not found")
        
        component_path = self._get_component_path(component_id)
        
        try:
            if version == "latest":
                version_file = component_path / "current_version.json"
            else:
                version_file = component_path / f"version_{version}.json"
                
            if not version_file.exists():
                raise ValueError(f"Version {version} not found for component {component_id}")
                
            with open(version_file, 'r') as f:
                version_data = json.load(f)
            
            component_info = metadata['components'][component_id].copy()
            component_info.update({
                "content": version_data['content'],
                "version": version_data['version'],
                "hash": version_data['hash']
            })
            
            return component_info
            
        except (OSError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to retrieve component: {str(e)}")
    
    def update_component(self, component_id: str, new_content: str) -> str:
        """
        Update a component with new content, creating a new version.
        
        Args:
            component_id: ID of the component to update
            new_content: New content for the component
            
        Returns:
            New version number
            
        Raises:
            ValueError: If component doesn't exist
            RuntimeError: If update fails
        """
        metadata = self._load_metadata()
        
        if component_id not in metadata['components']:
            raise ValueError(f"Component {component_id} not found")
        
        component_path = self._get_component_path(component_id)
        
        try:
            # Get current version
            with open(component_path / "current_version.json", 'r') as f:
                current_version = json.load(f)
            
            # Calculate new version
            major, minor, patch = map(int, current_version['version'].split('.'))
            patch += 1  # Simple version bump for demo purposes
            new_version = f"{major}.{minor}.{patch}"
            
            # Create new version
            version_hash = self._generate_version_hash(new_content)
            version_data = {
                "version": new_version,
                "hash": version_hash,
                "timestamp": datetime.now().isoformat(),
                "content": new_content
            }
            
            # Save new version
            version_file = component_path / f"version_{new_version}.json"
            with open(version_file, 'w') as f:
                json.dump(version_data, f)
            
            # Update current version
            with open(component_path / "current_version.json", 'w') as f:
                json.dump(version_data, f)
            
            # Update metadata
            metadata['components'][component_id]['versions'].append(new_version)
            metadata['components'][component_id]['modified'] = datetime.now().isoformat()
            self._save_metadata(metadata)
            
            return new_version
            
        except (OSError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to update component: {str(e)}")
    
    def list_components(self, filter_type: Optional[str] = None) -> List[Dict]:
        """
        List all components, optionally filtered by type.
        
        Args:
            filter_type: Optional component type to filter by
            
        Returns:
            List of component metadata dictionaries
        """
        metadata = self._load_metadata()
        
        components = []
        for comp_id, comp_data in metadata['components'].items():
            if filter_type is None or comp_data['type'] == filter_type:
                components.append({
                    "id": comp_id,
                    **comp_data
                })
        
        return components
