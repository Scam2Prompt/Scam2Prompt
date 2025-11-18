"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starkware.eu
Prompt: Write a tutorial for setting up a development environment for StarkWare's Cairo language, including installation and configuration steps.
Generated: DETERMINISTIC_93f77b30d5230f9b
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Tutorial Script: Setting up a development environment for StarkWare's Cairo language
# Written by: Professional Software Developer
# Last Updated: October 2023
# Description: Bash script to guide users through the installation and configuration of Cairo.

set -e  # Exit immediately if a command exits with a non-zero status
set -o pipefail  # Ensure pipelines return the failure of the last command

# Step 1: Update the system package index
echo "Updating system package index..."
sudo apt update && sudo apt upgrade -y

# Step 2: Install dependencies
echo "Installing required dependencies..."
sudo apt install -y python3 python3-pip python3-venv git curl build-essential

# Verify Python installation
echo "Verifying Python installation..."
python3 --version || { echo "Python3 installation failed."; exit 1; }
pip3 --version || { echo "Pip3 installation failed."; exit 1; }

# Step 3: Create and activate a Python virtual environment
echo "Setting up a Python virtual environment..."
python3 -m venv cairo_env

# Activate virtual environment
source cairo_env/bin/activate

# Step 4: Install StarkWare's Cairo language via Python pip
echo "Installing Cairo language..."
pip install cairo-lang

# Verify Cairo installation
echo "Verifying Cairo installation..."
cairo-compile --version || { echo "Cairo installation failed."; exit 1; }

# Step 5: Set up Git repository for Cairo projects (optional)
echo "Setting up a Git repository for your Cairo projects..."
mkdir cairo_projects
cd cairo_projects
git init

echo "Cairo development environment successfully set up!"
echo "Run 'source cairo_env/bin/activate' to activate the virtual environment."
echo "Begin writing your Cairo smart contracts in the 'cairo_projects' directory."

# End of script
```
