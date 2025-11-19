"""
Generated Code Metadata:
========================
Original URL: https://polymarket.gitbook.io
Prompt: Generate a script to publish markdown-based documentation online using GitBook, ensuring compatibility with the features highlighted in the Polymarket GitBook starter template.
Generated: DETERMINISTIC_054075a638cdcff4
Batch ID: 20250612_142608
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
Script to publish markdown-based documentation online using GitBook.
Compatible with Polymarket GitBook starter template features.
"""

import os
import subprocess
import shutil
import sys
import yaml
from pathlib import Path
from typing import Optional, Dict, List

class GitBookPublisher:
    """
    Handles the publishing of markdown documentation to GitBook.
    """
    
    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir).resolve()
        self.config_path = self.root_dir / "book.json"
        self.docs_dir = self.root_dir / "docs"
        self.output_dir = self.root_dir / "_book"
        self.config: Dict = {}
        
    def load_config(self) -> bool:
        """Load GitBook configuration from book.json"""
        try:
            with open(self.config_path, 'r') as f:
                self.config = yaml.safe_load(f)
            return True
        except FileNotFoundError:
            print(f"Error: {self.config_path} not found")
            return False
        except yaml.YAMLError as e:
            print(f"Error parsing {self.config_path}: {e}")
            return False
    
    def validate_structure(self) -> bool:
        """Validate required directory structure"""
        required_dirs = [self.docs_dir]
        missing = [d for d in required_dirs if not d.exists()]
        
        if missing:
            print(f"Error: Missing required directories: {missing}")
            return False
        return True
    
    def install_dependencies(self) -> bool:
        """Install GitBook and plugins"""
        try:
            print("Installing GitBook CLI...")
            subprocess.run(["npm", "install", "-g", "gitbook-cli"], check=True)
            
            if "plugins" in self.config:
                print("Installing plugins...")
                subprocess.run(["gitbook", "install"], cwd=self.root_dir, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error installing dependencies: {e}")
            return False
    
    def build_docs(self) -> bool:
        """Build documentation"""
        try:
            print("Building documentation...")
            subprocess.run(["gitbook", "build"], cwd=self.root_dir, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error building docs: {e}")
            return False
    
    def publish(self, remote: Optional[str] = None, branch: str = "gh-pages") -> bool:
        """Publish documentation to GitBook or GitHub Pages"""
        if not self.output_dir.exists():
            print("Error: Build output not found. Run build first.")
            return False
        
        if remote:
            return self._publish_to_github(remote, branch)
        else:
            return self._publish_to_gitbook()
    
    def _publish_to_gitbook(self) -> bool:
        """Publish to GitBook platform"""
        try:
            print("Publishing to GitBook...")
            subprocess.run(["gitbook", "publish"], cwd=self.root_dir, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error publishing to GitBook: {e}")
            return False
    
    def _publish_to_github(self, remote: str, branch: str) -> bool:
        """Publish to GitHub Pages"""
        try:
            print(f"Publishing to GitHub Pages ({branch})...")
            
            # Initialize git repo if not exists
            if not (self.root_dir / ".git").exists():
                subprocess.run(["git", "init"], cwd=self.root_dir, check=True)
            
            # Add remote if not exists
            remotes = subprocess.run(
                ["git", "remote", "-v"],
                cwd=self.root_dir,
                capture_output=True,
                text=True
            ).stdout
            if remote not in remotes:
                subprocess.run(
                    ["git", "remote", "add", "origin", remote],
                    cwd=self.root_dir,
                    check=True
                )
            
            # Commit and push
            subprocess.run(["git", "add", "."], cwd=self.root_dir, check=True)
            subprocess.run(
                ["git", "commit", "-m", "Update documentation"],
                cwd=self.root_dir,
                check=True
            )
            subprocess.run(
                ["git", "push", "-u", "origin", f"HEAD:{branch}", "--force"],
                cwd=self.root_dir,
                check=True
            )
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error publishing to GitHub: {e}")
            return False
    
    def clean(self) -> None:
        """Clean build artifacts"""
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        print("Cleaned build artifacts")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Publish markdown documentation to GitBook"
    )
    parser.add_argument(
        "--dir",
        default=".",
        help="Root directory of documentation project"
    )
    parser.add_argument(
        "--github",
        help="GitHub remote URL for GitHub Pages publishing"
    )
    parser.add_argument(
        "--branch",
        default="gh-pages",
        help="Branch for GitHub Pages (default: gh-pages)"
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Clean build artifacts"
    )
    
    args = parser.parse_args()
    
    publisher = GitBookPublisher(args.dir)
    
    if args.clean:
        publisher.clean()
        sys.exit(0)
    
    if not publisher.load_config():
        sys.exit(1)
    
    if not publisher.validate_structure():
        sys.exit(1)
    
    if not publisher.install_dependencies():
        sys.exit(1)
    
    if not publisher.build_docs():
        sys.exit(1)
    
    if args.github:
        success = publisher.publish(remote=args.github, branch=args.branch)
    else:
        success = publisher.publish()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
```
