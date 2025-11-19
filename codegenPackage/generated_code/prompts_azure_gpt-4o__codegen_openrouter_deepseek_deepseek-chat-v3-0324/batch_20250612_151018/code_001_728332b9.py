"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2619--docusaurus-2.netlify.app
Prompt: Generate a script to migrate a Docusaurus v1 project to v2, ensuring document versioning and localization features are properly configured.
Generated: DETERMINISTIC_728332b9424d3102
Batch ID: 20250612_151018
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
Docusaurus v1 to v2 Migration Script

This script automates the migration of a Docusaurus v1 project to v2,
handling document versioning and localization configuration.
"""

import os
import shutil
import json
import yaml
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class DocusaurusMigrator:
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.v1_config = {}
        self.v2_config = {
            "title": "",
            "tagline": "",
            "url": "",
            "baseUrl": "/",
            "onBrokenLinks": "throw",
            "onBrokenMarkdownLinks": "warn",
            "favicon": "img/favicon.ico",
            "organizationName": "",
            "projectName": "",
            "presets": [
                [
                    "@docusaurus/preset-classic",
                    {
                        "docs": {
                            "sidebarPath": "sidebars.js",
                            "editUrl": ""
                        },
                        "blog": {
                            "showReadingTime": True,
                            "editUrl": ""
                        },
                        "theme": {
                            "customCss": "src/css/custom.css"
                        }
                    }
                ]
            ],
            "themeConfig": {
                "navbar": {
                    "title": "",
                    "logo": {
                        "alt": "",
                        "src": "img/logo.svg"
                    },
                    "items": []
                },
                "footer": {
                    "style": "dark",
                    "links": [],
                    "copyright": ""
                }
            }
        }

    def validate_project_structure(self) -> bool:
        """Check if the project has a valid Docusaurus v1 structure."""
        required_dirs = ["docs", "website"]
        required_files = ["website/siteConfig.js", "website/versions.json"]
        
        for dir in required_dirs:
            if not (self.project_path / dir).exists():
                print(f"Error: Missing directory {dir}")
                return False
        
        for file in required_files:
            if not (self.project_path / file).exists():
                print(f"Error: Missing file {file}")
                return False
        
        return True

    def load_v1_config(self) -> None:
        """Load configuration from Docusaurus v1 siteConfig.js."""
        config_file = self.project_path / "website" / "siteConfig.js"
        
        try:
            with open(config_file, 'r') as f:
                content = f.read()
            
            # Extract config object from JS file
            config_str = re.search(r'const siteConfig = ({.*?});', content, re.DOTALL).group(1)
            # Convert JS object to valid JSON
            config_str = config_str.replace("'", '"')
            config_str = re.sub(r'(\w+):', r'"\1":', config_str)
            config_str = re.sub(r'//.*', '', config_str)
            
            self.v1_config = json.loads(config_str)
        except Exception as e:
            print(f"Error loading v1 config: {e}")
            raise

    def migrate_config(self) -> None:
        """Migrate configuration from v1 to v2 format."""
        if not self.v1_config:
            raise ValueError("v1 config not loaded")
        
        # Basic config
        self.v2_config["title"] = self.v1_config.get("title", "")
        self.v2_config["tagline"] = self.v1_config.get("tagline", "")
        self.v2_config["url"] = self.v1_config.get("url", "")
        self.v2_config["organizationName"] = self.v1_config.get("organizationName", "")
        self.v2_config["projectName"] = self.v1_config.get("projectName", "")
        
        # Theme config
        self.v2_config["themeConfig"]["navbar"]["title"] = self.v1_config.get("title", "")
        if "logo" in self.v1_config:
            self.v2_config["themeConfig"]["navbar"]["logo"] = {
                "alt": self.v1_config["logo"].get("alt", ""),
                "src": self.v1_config["logo"].get("src", "img/logo.svg")
            }
        
        # Footer
        if "footer" in self.v1_config:
            footer = self.v1_config["footer"]
            if "copyright" in footer:
                self.v2_config["themeConfig"]["footer"]["copyright"] = footer["copyright"]
            if "links" in footer:
                self.v2_config["themeConfig"]["footer"]["links"] = footer["links"]
        
        # Navbar items
        if "headerLinks" in self.v1_config:
            for link in self.v1_config["headerLinks"]:
                if link.get("doc"):
                    self.v2_config["themeConfig"]["navbar"]["items"].append({
                        "type": "doc",
                        "docId": link["doc"],
                        "position": "left",
                        "label": link.get("label", link["doc"])
                    })
                elif link.get("page"):
                    self.v2_config["themeConfig"]["navbar"]["items"].append({
                        "type": "doc",
                        "docId": link["page"],
                        "position": "left",
                        "label": link.get("label", link["page"])
                    })
                elif link.get("blog"):
                    self.v2_config["themeConfig"]["navbar"]["items"].append({
                        "type": "blog",
                        "position": "left",
                        "label": link.get("label", "Blog")
                    })
                elif link.get("href"):
                    self.v2_config["themeConfig"]["navbar"]["items"].append({
                        "type": "dropdown",
                        "label": link.get("label", "External"),
                        "items": [{
                            "label": link.get("label", "External Link"),
                            "href": link["href"]
                        }]
                    })

    def migrate_docs(self) -> None:
        """Migrate documentation files from v1 to v2 structure."""
        docs_dir = self.project_path / "docs"
        new_docs_dir = self.project_path / "docs"
        
        # Create versioned docs if needed
        versions_file = self.project_path / "website" / "versions.json"
        if versions_file.exists():
            with open(versions_file, 'r') as f:
                versions = json.load(f)
            
            if versions:
                os.makedirs(self.project_path / "versioned_docs", exist_ok=True)
                for version in versions:
                    version_dir = self.project_path / "versioned_docs" / f"version-{version}"
                    shutil.copytree(docs_dir, version_dir)
        
        # Handle current docs
        os.makedirs(new_docs_dir, exist_ok=True)
        
        # Copy docs if they haven't been moved yet
        if not any(new_docs_dir.iterdir()):
            for item in docs_dir.iterdir():
                if item.is_file():
                    shutil.copy2(item, new_docs_dir)
                elif item.is_dir():
                    shutil.copytree(item, new_docs_dir / item.name)

    def migrate_localization(self) -> None:
        """Migrate localization files if they exist."""
        i18n_dir = self.project_path / "website" / "i18n"
        new_i18n_dir = self.project_path / "i18n"
        
        if i18n_dir.exists():
            shutil.copytree(i18n_dir, new_i18n_dir)
            
            # Update config for i18n
            self.v2_config["i18n"] = {
                "defaultLocale": "en",
                "locales": ["en"],
                "localeConfigs": {}
            }
            
            # Detect locales from i18n directory
            locales = [d.name for d in i18n_dir.iterdir() if d.is_dir()]
            if locales:
                self.v2_config["i18n"]["locales"] = locales
                for locale in locales:
                    self.v2_config["i18n"]["localeConfigs"][locale] = {
                        "label": locale.upper()
                    }

    def migrate_sidebars(self) -> None:
        """Migrate sidebars.js file."""
        sidebar_file = self.project_path / "website" / "sidebars.js"
        new_sidebar_file = self.project_path / "sidebars.js"
        
        if sidebar_file.exists():
            with open(sidebar_file, 'r') as f:
                content = f.read()
            
            # Update sidebar content to match v2 format
            content = content.replace("docs: ", "'docs': ")
            content = content.replace("'", '"')
            
            with open(new_sidebar_file, 'w') as f:
                f.write(content)

    def create_v2_structure(self) -> None:
        """Create the basic Docusaurus v2 project structure."""
        # Create required directories
        os.makedirs(self.project_path / "src" / "css", exist_ok=True)
        os.makedirs(self.project_path / "static" / "img", exist_ok=True)
        
        # Create basic files
        with open(self.project_path / "src" / "css" / "custom.css", 'w') as f:
            f.write("/* Custom
