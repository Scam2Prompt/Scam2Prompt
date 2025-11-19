"""
Generated Code Metadata:
========================
Original URL: https://gorealm.vercel.app
Prompt: Write a CLI-based workflow for envisioning and achieving app development goals using Gorealm's tools.
Generated: DETERMINISTIC_f11d3107f4d78353
Batch ID: 20250612_153648
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
CLI-based workflow for envisioning and achieving app development goals using Gorealm's tools.
"""

import sys
import argparse
import json
from pathlib import Path
from typing import Dict, List, Optional
import subprocess
import shutil
import platform

# Constants
CONFIG_FILE = Path.home() / ".gorealm_config.json"
TEMPLATES_DIR = Path.home() / ".gorealm_templates"
LOG_FILE = Path.home() / ".gorealm_workflow.log"

class GorealmWorkflow:
    def __init__(self):
        self.config = self._load_config()
        self._setup_directories()

    def _load_config(self) -> Dict:
        """Load configuration from file or create default config."""
        try:
            if CONFIG_FILE.exists():
                with open(CONFIG_FILE, 'r') as f:
                    return json.load(f)
            return {
                "projects": {},
                "templates": {},
                "settings": {
                    "auto_update": True,
                    "default_template": "basic"
                }
            }
        except Exception as e:
            print(f"Error loading config: {e}", file=sys.stderr)
            sys.exit(1)

    def _save_config(self) -> None:
        """Save current configuration to file."""
        try:
            with open(CONFIG_FILE, 'w') as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            print(f"Error saving config: {e}", file=sys.stderr)
            sys.exit(1)

    def _setup_directories(self) -> None:
        """Ensure required directories exist."""
        try:
            TEMPLATES_DIR.mkdir(exist_ok=True)
        except Exception as e:
            print(f"Error creating templates directory: {e}", file=sys.stderr)
            sys.exit(1)

    def _log_action(self, action: str, details: str = "") -> None:
        """Log an action to the workflow log."""
        try:
            with open(LOG_FILE, 'a') as f:
                f.write(f"{action}: {details}\n")
        except Exception as e:
            print(f"Warning: Could not log action - {e}", file=sys.stderr)

    def create_project(self, name: str, template: Optional[str] = None) -> None:
        """Create a new project with optional template."""
        if name in self.config["projects"]:
            print(f"Project '{name}' already exists.", file=sys.stderr)
            sys.exit(1)

        template = template or self.config["settings"]["default_template"]
        
        try:
            project_path = Path.cwd() / name
            project_path.mkdir()
            
            # Apply template if available
            if template in self.config["templates"]:
                template_path = TEMPLATES_DIR / template
                if template_path.exists():
                    self._copy_template(template_path, project_path)
            
            self.config["projects"][name] = {
                "path": str(project_path),
                "template": template,
                "status": "created"
            }
            self._save_config()
            self._log_action("create_project", f"Created project {name} with template {template}")
            print(f"Project '{name}' created successfully.")
        except Exception as e:
            print(f"Error creating project: {e}", file=sys.stderr)
            sys.exit(1)

    def _copy_template(self, src: Path, dest: Path) -> None:
        """Copy template files to project directory."""
        try:
            for item in src.iterdir():
                if item.is_dir():
                    shutil.copytree(item, dest / item.name)
                else:
                    shutil.copy2(item, dest / item.name)
        except Exception as e:
            print(f"Error copying template: {e}", file=sys.stderr)
            raise

    def list_projects(self) -> None:
        """List all projects."""
        if not self.config["projects"]:
            print("No projects found.")
            return
        
        print("Projects:")
        for name, details in self.config["projects"].items():
            print(f"- {name}: {details['path']} ({details['status']})")

    def build_project(self, name: str) -> None:
        """Build a project."""
        if name not in self.config["projects"]:
            print(f"Project '{name}' not found.", file=sys.stderr)
            sys.exit(1)
        
        project_path = Path(self.config["projects"][name]["path"])
        
        try:
            # Check if it's a Go project
            if (project_path / "go.mod").exists():
                self._build_go_project(project_path)
            else:
                print("Project type not recognized. Only Go projects are currently supported.")
                sys.exit(1)
            
            self.config["projects"][name]["status"] = "built"
            self._save_config()
            self._log_action("build_project", f"Built project {name}")
            print(f"Project '{name}' built successfully.")
        except Exception as e:
            print(f"Error building project: {e}", file=sys.stderr)
            sys.exit(1)

    def _build_go_project(self, project_path: Path) -> None:
        """Build a Go project."""
        try:
            subprocess.run(["go", "build"], cwd=project_path, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Go build failed with exit code {e.returncode}", file=sys.stderr)
            raise
        except FileNotFoundError:
            print("Go compiler not found. Please install Go first.", file=sys.stderr)
            raise

    def run_project(self, name: str) -> None:
        """Run a project."""
        if name not in self.config["projects"]:
            print(f"Project '{name}' not found.", file=sys.stderr)
            sys.exit(1)
        
        project_path = Path(self.config["projects"][name]["path"])
        
        try:
            # Check if it's a Go project
            if (project_path / "go.mod").exists():
                self._run_go_project(project_path)
            else:
                print("Project type not recognized. Only Go projects are currently supported.")
                sys.exit(1)
            
            self.config["projects"][name]["status"] = "running"
            self._save_config()
            self._log_action("run_project", f"Ran project {name}")
        except Exception as e:
            print(f"Error running project: {e}", file=sys.stderr)
            sys.exit(1)

    def _run_go_project(self, project_path: Path) -> None:
        """Run a Go project."""
        try:
            subprocess.run(["go", "run", "."], cwd=project_path, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Go run failed with exit code {e.returncode}", file=sys.stderr)
            raise
        except FileNotFoundError:
            print("Go compiler not found. Please install Go first.", file=sys.stderr)
            raise

    def add_template(self, name: str, path: str) -> None:
        """Add a new template."""
        source_path = Path(path)
        if not source_path.exists():
            print(f"Source path '{path}' does not exist.", file=sys.stderr)
            sys.exit(1)
        
        try:
            template_path = TEMPLATES_DIR / name
            if template_path.exists():
                print(f"Template '{name}' already exists.", file=sys.stderr)
                sys.exit(1)
                
            shutil.copytree(source_path, template_path)
            self.config["templates"][name] = str(template_path)
            self._save_config()
            self._log_action("add_template", f"Added template {name} from {path}")
            print(f"Template '{name}' added successfully.")
        except Exception as e:
            print(f"Error adding template: {e}", file=sys.stderr)
            sys.exit(1)

    def list_templates(self) -> None:
        """List all available templates."""
        if not self.config["templates"]:
            print("No templates found.")
            return
        
        print("Available templates:")
        for name, path in self.config["templates"].items():
            print(f"- {name}: {path}")

def main():
    parser = argparse.ArgumentParser(
        description="Gorealm App Development Workflow CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Create project command
    create_parser = subparsers.add_parser("create", help="Create a new project")
    create_parser.add_argument("name", help="Name of the project")
    create_parser.add_argument("-t", "--template", help="Template to use")

    # List projects command
    subparsers.add_parser("list", help="List all projects")

    # Build project command
    build_parser = subparsers.add_parser("build", help="Build a project")
    build_parser.add_argument("name", help="Name of the project to build")

    # Run project command
    run
