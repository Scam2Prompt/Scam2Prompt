"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2735--docusaurus-2.netlify.app
Prompt: Write a script to deploy a Docusaurus site to GitHub Pages, ensuring the static HTML files are correctly generated and served.
Generated: DETERMINISTIC_d69e973d81dfc343
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import sys


def run_command(command, description):
    """
    Runs a shell command and raises an exception if it fails.
    :param command: List of command arguments to run.
    :param description: Description of the operation being performed.
    """
    try:
        print(f"Running: {description}...")
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {description} failed!")
        print(e.stderr)
        sys.exit(1)


def main():
    """
    Main function to deploy a Docusaurus site to GitHub Pages.
    Steps:
    1. Ensure Node.js and npm are installed.
    2. Build the static site files.
    3. Deploy the site to GitHub Pages.
    """
    # Step 1: Ensure the script is run from the root of the Docusaurus project
    if not os.path.exists('docusaurus.config.js'):
        print("Error: docusaurus.config.js not found. Please run this script from the root of your Docusaurus project.")
        sys.exit(1)

    # Step 2: Verify necessary tools are installed
    try:
        subprocess.run(['node', '-v'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(['npm', '-v'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Node.js and npm are installed.")
    except FileNotFoundError:
        print("Error: Node.js and npm are required but not installed. Please install them and try again.")
        sys.exit(1)

    # Step 3: Install dependencies
    run_command(['npm', 'install'], "Installing dependencies")

    # Step 4: Build the static site files
    run_command(['npm', 'run', 'build'], "Building the static site files")

    # Step 5: Deploy the site to GitHub Pages
    # Assumes the 'deploy' field is properly configured in docusaurus.config.js
    run_command(['npm', 'run', 'deploy'], "Deploying the site to GitHub Pages")

    print("Deployment complete! Your Docusaurus site is live on GitHub Pages.")


if __name__ == "__main__":
    main()
```
