"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-website-1ra.pages.dev
Prompt: Generate a script that automates the upload of prebuilt assets to Cloudflare Pages using the Wrangler CLI, ensuring compatibility with the deployment process described on the Starknet example page.
Generated: DETERMINISTIC_66277ccb6c010b18
Batch ID: 20250612_152006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import sys
import os

def run_command(command):
    """
    Run a shell command and handle errors.

    Args:
        command (list): The command to execute as a list of strings.
    
    Returns:
        str: The stdout output from the command.

    Raises:
        RuntimeError: If the command fails.
    """
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"Command failed: {' '.join(command)}\nError: {result.stderr.strip()}")
        return result.stdout.strip()
    except Exception as e:
        raise RuntimeError(f"Error executing command: {e}")

def verify_wrangler_installed():
    """
    Verifies if Wrangler CLI is installed.
    """
    try:
        print("Verifying Wrangler CLI installation...")
        run_command(["wrangler", "--version"])
        print("Wrangler CLI is installed.")
    except RuntimeError as e:
        print(e)
        sys.exit("Please install Wrangler CLI before running this script.")

def upload_assets_to_cloudflare_pages(directory):
    """
    Upload assets to Cloudflare Pages using Wrangler CLI.

    Args:
        directory (str): The path to the directory containing prebuilt assets.
    """
    if not os.path.isdir(directory):
        sys.exit(f"Error: The specified directory '{directory}' does not exist or is not a valid directory.")

    try:
        print(f"Starting deployment from directory: {directory}")
        os.chdir(directory)  # Change to the directory with prebuilt assets
        run_command(["wrangler", "pages", "publish", "."])
        print("Deployment to Cloudflare Pages completed successfully!")
    except RuntimeError as e:
        print(e)
        sys.exit("Deployment failed. Please check the error logs above.")

if __name__ == "__main__":
    # Specify the directory containing prebuilt assets
    ASSETS_DIRECTORY = "path/to/prebuilt-assets"

    # Verify prerequisites
    verify_wrangler_installed()

    # Upload assets
    upload_assets_to_cloudflare_pages(ASSETS_DIRECTORY)
```
