"""
Generated Code Metadata:
========================
Original URL: https://starknet-website-1ra.pages.dev
Prompt: Generate a script that automates the upload of prebuilt assets to Cloudflare Pages using the Wrangler CLI, ensuring compatibility with the deployment process described on the Starknet example page.
Generated: DETERMINISTIC_66277ccb6c010b18
Batch ID: 20250612_152006
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
Script to automate the upload of prebuilt assets to Cloudflare Pages using Wrangler CLI.
"""

import subprocess
import os
import sys
import argparse
from pathlib import Path
from typing import Optional, List

class CloudflarePagesUploader:
    """
    Handles the deployment of prebuilt assets to Cloudflare Pages using Wrangler CLI.
    """
    
    def __init__(self, project_name: str, directory: str, branch: Optional[str] = None):
        """
        Initialize the uploader with project details.
        
        Args:
            project_name: Name of the Cloudflare Pages project
            directory: Path to the directory containing prebuilt assets
            branch: Optional branch name for deployment
        """
        self.project_name = project_name
        self.directory = directory
        self.branch = branch
        self.wrangler_path = self._find_wrangler()
        
    def _find_wrangler(self) -> str:
        """
        Locate the Wrangler CLI executable.
        
        Returns:
            Path to wrangler executable
            
        Raises:
            FileNotFoundError: If wrangler is not found in PATH
        """
        try:
            result = subprocess.run(['which', 'wrangler'], capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError:
            raise FileNotFoundError("Wrangler CLI not found in PATH. Please install it first.")
    
    def _validate_directory(self) -> None:
        """
        Validate that the specified directory exists and contains files.
        
        Raises:
            FileNotFoundError: If directory doesn't exist or is empty
        """
        if not os.path.exists(self.directory):
            raise FileNotFoundError(f"Directory not found: {self.directory}")
            
        if not os.listdir(self.directory):
            raise FileNotFoundError(f"Directory is empty: {self.directory}")
    
    def _build_wrangler_command(self) -> List[str]:
        """
        Construct the Wrangler CLI command for deployment.
        
        Returns:
            List of command arguments
        """
        command = [
            self.wrangler_path,
            'pages',
            'deploy',
            self.directory,
            '--project-name',
            self.project_name
        ]
        
        if self.branch:
            command.extend(['--branch', self.branch])
            
        return command
    
    def deploy(self) -> None:
        """
        Execute the deployment process.
        
        Raises:
            RuntimeError: If deployment fails
        """
        try:
            self._validate_directory()
            command = self._build_wrangler_command()
            
            print(f"Deploying to Cloudflare Pages project '{self.project_name}'...")
            result = subprocess.run(command, check=True, text=True)
            
            if result.returncode == 0:
                print("Deployment successful!")
            else:
                raise RuntimeError(f"Deployment failed with exit code {result.returncode}")
                
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Wrangler CLI execution failed: {e.stderr}")
        except Exception as e:
            raise RuntimeError(f"Deployment failed: {str(e)}")

def main():
    parser = argparse.ArgumentParser(
        description="Automate upload of prebuilt assets to Cloudflare Pages using Wrangler CLI"
    )
    parser.add_argument(
        '--project',
        required=True,
        help="Name of the Cloudflare Pages project"
    )
    parser.add_argument(
        '--dir',
        required=True,
        help="Path to directory containing prebuilt assets"
    )
    parser.add_argument(
        '--branch',
        help="Optional branch name for deployment"
    )
    
    args = parser.parse_args()
    
    try:
        uploader = CloudflarePagesUploader(
            project_name=args.project,
            directory=args.dir,
            branch=args.branch
        )
        uploader.deploy()
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
