"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2728--docusaurus-2.netlify.app
Prompt: Generate a script to migrate a Docusaurus v1 project to v2, incorporating document versioning and localization features.
Generated: DETERMINISTIC_f2c42ac9c41c862b
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
including document versioning and localization features.
"""

import os
import shutil
import json
import re
from pathlib import Path
import argparse
import logging
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DocusaurusMigrator:
    def __init__(self, project_path: str):
        self.project_path = Path(project_path).resolve()
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
                            "showReadingTime": true,
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
        required_files = ["website/siteConfig.js"]

        for dir_name in required_dirs:
            if not (self.project_path / dir_name).exists():
                logger.error(f"Missing directory: {dir_name}")
                return False

        for file_name in required_files:
            if not (self.project_path / file_name).exists():
                logger.error(f"Missing file: {file_name}")
                return False

        return True

    def parse_v1_config(self) -> None:
        """Parse the Docusaurus v1 configuration from siteConfig.js."""
        config_file = self.project_path / "website" / "siteConfig.js"
        
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract the config object from the JS file
            match = re.search(r'const siteConfig = ({.*?});', content, re.DOTALL)
            if not match:
                raise ValueError("Could not find siteConfig in file")
            
            config_str = match.group(1)
            # Clean up JS-specific syntax to make it valid JSON
            config_str = re.sub(r'/\*.*?\*/', '', config_str, flags=re.DOTALL)  # Remove comments
            config_str = re.sub(r'//.*$', '', config_str, flags=re.MULTILINE)  # Remove line comments
            config_str = re.sub(r',\s*}', '}', config_str)  # Remove trailing commas
            config_str = re.sub(r',\s*]', ']', config_str)  # Remove trailing commas in arrays
            config_str = re.sub(r'(\w+):', r'"\1":', config_str)  # Add quotes to keys
            
            self.v1_config = json.loads(config_str)
            logger.info("Successfully parsed v1 configuration")
        except Exception as e:
            logger.error(f"Failed to parse v1 config: {str(e)}")
            raise

    def migrate_config(self) -> None:
        """Migrate configuration from v1 to v2 format."""
        if not self.v1_config:
            raise ValueError("v1 config not loaded")
        
        # Basic metadata
        self.v2_config["title"] = self.v1_config.get("title", "")
        self.v2_config["tagline"] = self.v1_config.get("tagline", "")
        self.v2_config["url"] = self.v1_config.get("url", "")
        self.v2_config["baseUrl"] = self.v1_config.get("baseUrl", "/")
        
        # Organization and project name
        if "organizationName" in self.v1_config:
            self.v2_config["organizationName"] = self.v1_config["organizationName"]
        if "projectName" in self.v1_config:
            self.v2_config["projectName"] = self.v1_config["projectName"]
        
        # Navbar
        if "headerLinks" in self.v1_config:
            self._migrate_header_links()
        
        # Footer
        if "footer" in self.v1_config:
            self._migrate_footer()
        
        # Versioning and localization
        if "versions" in self.v1_config:
            self._setup_versioning()
        if "languages" in self.v1_config:
            self._setup_localization()
        
        logger.info("Configuration migrated successfully")

    def _migrate_header_links(self) -> None:
        """Migrate headerLinks to navbar items."""
        navbar_items = []
        
        for link in self.v1_config["headerLinks"]:
            item = {}
            
            if link.get("doc"):
                item = {
                    "type": "doc",
                    "docId": link["doc"],
                    "position": "left",
                    "label": link.get("label", link["doc"])
                }
            elif link.get("page"):
                item = {
                    "type": "doc",
                    "docId": link["page"],
                    "position": "left",
                    "label": link.get("label", link["page"])
                }
            elif link.get("blog"):
                item = {
                    "type": "doc",
                    "docId": "blog",
                    "position": "left",
                    "label": link.get("label", "Blog")
                }
            elif link.get("href"):
                item = {
                    "type": "dropdown",
                    "label": link.get("label", "External"),
                    "items": [
                        {
                            "label": link.get("label", "External Link"),
                            "href": link["href"]
                        }
                    ]
                }
            
            if item:
                navbar_items.append(item)
        
        self.v2_config["themeConfig"]["navbar"]["items"] = navbar_items

    def _migrate_footer(self) -> None:
        """Migrate footer configuration."""
        footer = self.v1_config["footer"]
        
        if "copyright" in footer:
            self.v2_config["themeConfig"]["footer"]["copyright"] = footer["copyright"]
        
        if "links" in footer:
            migrated_links = []
            for link_group in footer["links"]:
                group = {
                    "title": link_group.get("title", ""),
                    "items": []
                }
                
                for link in link_group.get("items", []):
                    if "to" in link:
                        group["items"].append({
                            "label": link.get("label", ""),
                            "to": link["to"]
                        })
                    elif "href" in link:
                        group["items"].append({
                            "label": link.get("label", ""),
                            "href": link["href"]
                        })
                
                if group["items"]:
                    migrated_links.append(group)
            
            self.v2_config["themeConfig"]["footer"]["links"] = migrated_links

    def _setup_versioning(self) -> None:
        """Set up versioning configuration."""
        if not self.v2_config.get("presets"):
            self.v2_config["presets"] = []
        
        for preset in self.v2_config["presets"]:
            if isinstance(preset, list) and preset[0] == "@docusaurus/preset-classic":
                if "docs" not in preset[1]:
                    preset[1]["docs"] = {}
                preset[1]["docs"]["versions"] = self.v1_config["versions"]
                break

    def _setup_localization(self) -> None:
        """Set up localization configuration."""
        self.v2_config["i18n"] = {
            "defaultLocale": self.v1_config.get("defaultLanguage", "en"),
            "locales": self.v1_config.get("languages", ["en"]),
            "localeConfigs": {}
        }

    def migrate_docs(self) -> None:
        """Migrate documentation files from v1 to v2 structure."""
        docs_src = self.project_path / "docs"
        docs_dest = self.project_path / "docs"
        
        # Create versioned docs if needed
        if "versions" in self.v1_config:
            self._migrate_versioned_docs(docs_src, docs_dest)
        else:
            self._migrate_regular_docs(docs_src, docs_dest)
        
        logger.info("Documentation migration completed")

    def _migrate_regular
