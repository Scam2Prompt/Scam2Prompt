"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-134--keen-roentgen-cafcb7.netlify.app
Prompt: Provide a code snippet for automatically deleting branches after merging pull requests, as mentioned by Joe Previte.
Generated: DETERMINISTIC_cfa06b218d9d62cf
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready script to automatically delete branches after merged pull requests:

```python
#!/usr/bin/env python3
"""
Automatically delete merged branches in a Git repository.
"""

import subprocess
import sys
from typing import List, Optional

def run_command(cmd: str) -> Optional[str]:
    """
    Execute a shell command and return its output.
    
    Args:
        cmd: The command to execute
        
    Returns:
        Command output as string or None if error occurs
    """
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {cmd}\nError: {e.stderr}", file=sys.stderr)
        return None

def get_merged_branches() -> List[str]:
    """
    Get list of merged branches excluding main/master and current branch.
    
    Returns:
        List of branch names that have been merged
    """
    current_branch = run_command("git branch --show-current")
    if not current_branch:
        return []
    
    # Get merged branches excluding main/master and current branch
    cmd = (
        "git branch --merged | "
        "grep -v '^*' | "
        "grep -v 'main' | "
        "grep -v 'master' | "
        "grep -v 'develop' | "
        f"grep -v '{current_branch}' | "
        "tr -d ' '"
    )
    output = run_command(cmd)
    return output.split('\n') if output else []

def delete_branches(branches: List[str]) -> None:
    """
    Delete the specified branches both locally and remotely.
    
    Args:
        branches: List of branch names to delete
    """
    if not branches:
        print("No branches to delete.")
        return
    
    for branch in branches:
        if not branch:
            continue
            
        # Delete local branch
        print(f"Deleting local branch: {branch}")
        run_command(f"git branch -d {branch}")
        
        # Delete remote branch
        print(f"Deleting remote branch: {branch}")
        run_command(f"git push origin --delete {branch}")

def main() -> None:
    """
    Main execution function.
    """
    # Verify we're in a git repository
    if not run_command("git rev-parse --is-inside-work-tree"):
        print("Error: Not in a Git repository", file=sys.stderr)
        sys.exit(1)
        
    # Fetch latest from remote
    print("Fetching latest changes from remote...")
    run_command("git fetch --prune")
    
    # Get and delete merged branches
    branches = get_merged_branches()
    delete_branches(branches)
    
    print("Cleanup complete.")

if __name__ == "__main__":
    main()
```
