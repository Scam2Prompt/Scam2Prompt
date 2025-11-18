"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-starknet-project.vercel.app
Prompt: Suggest tools or frameworks for building StarkNet applications and provide example code for initializing a StarkNet project.
Generated: DETERMINISTIC_3c6a22228e20feca
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import subprocess
import os
import sys

def initialize_starknet_project(project_name):
    """
    Initializes a new StarkNet project using the StarkNet CLI.
    
    Args:
        project_name (str): The name of the project to be created.
    
    Raises:
        Exception: If the project initialization fails.
    """
    try:
        # Check if the project directory already exists
        if os.path.exists(project_name):
            raise Exception(f"The project directory '{project_name}' already exists. Please choose a different name.")
        
        # Run the StarkNet CLI command to create a new project
        subprocess.run(["starknet", "init", project_name], check=True)
        print(f"StarkNet project '{project_name}' has been successfully initialized.")
    
    except subprocess.CalledProcessError as e:
        print("Error occurred while initializing the project:", e)
        sys.exit(1)
    except Exception as e:
        print("An error occurred:", e)
        sys.exit(1)

# Example usage
if __name__ == "__main__":
    # Ensure the user provides a project name
    if len(sys.argv) != 2:
        print("Usage: python initialize_starknet.py <project_name>")
        sys.exit(1)

    project_name = sys.argv[1]
    initialize_starknet_project(project_name)
```

### Required Tools/Frameworks for StarkNet Applications:
1. **Cairo**: The programming language for StarkNet smart contracts.
2. **StarkNet CLI**: Command-line interface for managing StarkNet projects.
3. **StarkNet.js**: Library for interacting with StarkNet from JavaScript/TypeScript applications.
4. **Hardhat**: A development environment for Ethereum-compatible blockchains, which can be extended to support StarkNet.

Please ensure you have the StarkNet CLI installed and available in your environment to run the initialization script.
