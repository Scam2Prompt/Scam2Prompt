"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.gitbook.io
Prompt: Generate a script to publish markdown-based documentation online using GitBook, ensuring compatibility with the features highlighted in the Polymarket GitBook starter template.
Generated: DETERMINISTIC_054075a638cdcff4
Batch ID: 20250612_142608
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
import shutil

def install_gitbook_and_plugins():
    """
    Installs GitBook CLI and necessary plugins if not already installed.
    """
    try:
        # Check if GitBook CLI is installed
        if shutil.which("gitbook") is None:
            print("GitBook CLI not found. Installing GitBook CLI...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "gitbook-cli"])
            subprocess.check_call(["gitbook", "install"])  # Install required plugins
        else:
            print("GitBook CLI is already installed.")
        
    except subprocess.CalledProcessError as e:
    
    
`
