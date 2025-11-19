"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.web.app
Prompt: Create a developer tool for the Sui ecosystem that simplifies the process of building decentralized applications, and explain its potential impact.
Generated: DETERMINISTIC_609af31dfedb5ef2
Batch ID: 20250612_155015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import subprocess
from pathlib import Path
from typing import Optional, Dict, Any, List
import click
import requests
from sui_python_sdk import SuiClient

class SuiDevTool:
    """
    A developer tool for the Sui ecosystem to simplify building decentralized applications.
    Features:
    - Project scaffolding
    - Smart contract compilation
    - Deployment automation
    - Testing utilities
    - Integration with Sui blockchain
    """
    
    def __init__(self, sui_client: Optional[SuiClient] = None):
        self.sui_client = sui_client or SuiClient()
        self.project_config = {}
        self.current_dir = Path.cwd()
        
    def initialize_project(self, project_name: str, template: str = "basic") -> None:
        """
        Initialize a new Sui project with the specified template.
        
        Args:
            project_name: Name of the project
            template: Project template to use (basic, nft, defi)
        """
        try:
            # Create project directory
            project_path = self.current_dir / project_name
            project_path.mkdir(exist_ok=False)
            
            # Initialize project structure
            (project_path / "contracts").mkdir()
            (project_path / "scripts").mkdir()
            (project_path / "tests").mkdir()
            (project_path / "frontend").mkdir()
            
            # Add template files
            self._copy_template_files(template, project_path)
            
            # Create config file
            self.project_config = {
                "name": project_name,
                "version": "0.1.0",
                "template": template,
                "contracts": [],
                "dependencies": {}
            }
            self._save_config(project_path)
            
            click.echo(f"✅ Project {project_name} initialized successfully!")
            
        except FileExistsError:
            click.echo(f"❌ Error: Project directory {project_name} already exists")
        except Exception as e:
            click.echo(f"❌ Error initializing project: {str(e)}")
    
    def compile_contract(self, contract_path: str) -> None:
        """
        Compile a Move smart contract.
        
        Args:
            contract_path: Path to the Move contract directory
        """
        try:
            contract_dir = self.current_dir / contract_path
            if not contract_dir.exists():
                raise FileNotFoundError(f"Contract directory {contract_path} not found")
                
            result = subprocess.run(
                ["sui-move", "build"],
                cwd=contract_dir,
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                raise RuntimeError(f"Compilation failed: {result.stderr}")
                
            click.echo("✅ Contract compiled successfully!")
            click.echo(result.stdout)
            
        except Exception as e:
            click.echo(f"❌ Error compiling contract: {str(e)}")
    
    def deploy_contract(self, contract_path: str) -> Optional[str]:
        """
        Deploy a compiled Move contract to the Sui blockchain.
        
        Args:
            contract_path: Path to the compiled contract
            
        Returns:
            Transaction digest if successful
        """
        try:
            if not self.sui_client:
                raise RuntimeError("Sui client not initialized")
                
            compiled_contract = self.current_dir / contract_path
            if not compiled_contract.exists():
                raise FileNotFoundError(f"Compiled contract {contract_path} not found")
                
            # Read the compiled package
            with open(compiled_contract / "build" / "Move.toml", "r") as f:
                package_config = f.read()
                
            # Deploy the contract
            tx_digest = self.sui_client.publish(
                compiled_contract,
                gas_budget=10000
            )
            
            click.echo(f"✅ Contract deployed successfully! TX Digest: {tx_digest}")
            return tx_digest
            
        except Exception as e:
            click.echo(f"❌ Error deploying contract: {str(e)}")
            return None
    
    def test_contract(self, contract_path: str) -> bool:
        """
        Run tests for a Move contract.
        
        Args:
            contract_path: Path to the contract directory
            
        Returns:
            True if all tests pass, False otherwise
        """
        try:
            contract_dir = self.current_dir / contract_path
            if not contract_dir.exists():
                raise FileNotFoundError(f"Contract directory {contract_path} not found")
                
            result = subprocess.run(
                ["sui-move", "test"],
                cwd=contract_dir,
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                click.echo("❌ Some tests failed:")
                click.echo(result.stderr)
                return False
                
            click.echo("✅ All tests passed!")
            click.echo(result.stdout)
            return True
            
        except Exception as e:
            click.echo(f"❌ Error running tests: {str(e)}")
            return False
    
    def _copy_template_files(self, template: str, project_path: Path) -> None:
        """Copy template files to the new project directory."""
        templates = {
            "basic": ["counter.move", "tests/test_counter.move"],
            "nft": ["nft.move", "tests/test_nft.move"],
            "defi": ["token.move", "amm.move", "tests/test_token.move"]
        }
        
        if template not in templates:
            raise ValueError(f"Unknown template: {template}")
            
        # Copy contract files
        for file in templates[template]:
            src = Path(__file__).parent / "templates" / template / file
            dst = project_path / "contracts" / Path(file).name
            dst.write_text(src.read_text())
    
    def _save_config(self, project_path: Path) -> None:
        """Save project configuration to sui-dev.json."""
        config_path = project_path / "sui-dev.json"
        with open(config_path, "w") as f:
            json.dump(self.project_config, f, indent=2)

@click.group()
def cli():
    """Sui Developer Tool - Simplify building decentralized applications on Sui."""
    pass

@cli.command()
@click.argument("project_name")
@click.option("--template", default="basic", help="Project template to use")
def init(project_name, template):
    """Initialize a new Sui project."""
    tool = SuiDevTool()
    tool.initialize_project(project_name, template)

@cli.command()
@click.argument("contract_path", default="contracts")
def compile(contract_path):
    """Compile a Move smart contract."""
    tool = SuiDevTool()
    tool.compile_contract(contract_path)

@cli.command()
@click.argument("contract_path", default="contracts")
def deploy(contract_path):
    """Deploy a compiled Move contract to Sui."""
    tool = SuiDevTool()
    tool.deploy_contract(contract_path)

@cli.command()
@click.argument("contract_path", default="contracts")
def test(contract_path):
    """Run tests for a Move contract."""
    tool = SuiDevTool()
    tool.test_contract(contract_path)

if __name__ == "__main__":
    cli()
```
