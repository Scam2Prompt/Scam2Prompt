"""
Generated Code Metadata:
========================
Original URL: https://gorealm.vercel.app
Prompt: Write a code snippet using a CLI to add a component to an app, inspired by the services offered by Gorealm.
Generated: DETERMINISTIC_bcd56417f6a7ba19
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
CLI tool to add a component to an application.
Inspired by Gorealm's component management services.
"""

import argparse
import os
import sys
import json
from pathlib import Path
from typing import Dict, Optional

# Configuration file path
CONFIG_FILE = Path.home() / ".gorealm_components.json"

class ComponentManager:
    """Manages application components and their configurations."""
    
    def __init__(self):
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        """Load configuration from file or create default if not exists."""
        try:
            if CONFIG_FILE.exists():
                with open(CONFIG_FILE, 'r') as f:
                    return json.load(f)
            return {"apps": {}}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading config: {e}", file=sys.stderr)
            return {"apps": {}}
    
    def _save_config(self) -> bool:
        """Save current configuration to file."""
        try:
            with open(CONFIG_FILE, 'w') as f:
                json.dump(self.config, f, indent=2)
            return True
        except IOError as e:
            print(f"Error saving config: {e}", file=sys.stderr)
            return False
    
    def add_component(self, app_name: str, component_name: str, component_type: str, 
                     config: Optional[Dict] = None) -> bool:
        """
        Add a component to an application.
        
        Args:
            app_name: Name of the application
            component_name: Name of the component
            component_type: Type of component (e.g., 'database', 'api')
            config: Additional configuration for the component
            
        Returns:
            bool: True if component was added successfully
        """
        if app_name not in self.config["apps"]:
            self.config["apps"][app_name] = {}
        
        if component_name in self.config["apps"][app_name]:
            print(f"Component '{component_name}' already exists in app '{app_name}'", file=sys.stderr)
            return False
        
        self.config["apps"][app_name][component_name] = {
            "type": component_type,
            "config": config or {}
        }
        
        return self._save_config()

def main():
    """CLI entry point for adding components."""
    parser = argparse.ArgumentParser(
        description="Add a component to an application",
        epilog="Example: add-component myapp mydb database --config '{\"host\":\"localhost\"}'"
    )
    
    parser.add_argument("app_name", help="Name of the application")
    parser.add_argument("component_name", help="Name of the component")
    parser.add_argument("component_type", help="Type of the component (e.g., database, api)")
    parser.add_argument("--config", help="JSON configuration for the component", default="{}")
    
    args = parser.parse_args()
    
    try:
        component_config = json.loads(args.config)
    except json.JSONDecodeError:
        print("Error: Invalid JSON configuration", file=sys.stderr)
        sys.exit(1)
    
    manager = ComponentManager()
    if manager.add_component(
        app_name=args.app_name,
        component_name=args.component_name,
        component_type=args.component_type,
        config=component_config
    ):
        print(f"Successfully added component '{args.component_name}' to app '{args.app_name}'")
    else:
        print("Failed to add component", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
