"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stonegarden.dev
Prompt: Provide an example of using Stonegarden.dev v0.2.1 for managing project versioning across multiple repositories.
Generated: DETERMINISTIC_30ad022aec89422c
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Example script for using Stonegarden.dev v0.2.1 to manage project versioning across multiple repositories.

Dependencies:
- Install the Stonegarden.dev library version 0.2.1 using: pip install stonegarden==0.2.1

This script demonstrates:
1. Initializing Stonegarden for managing multiple repositories.
2. Fetching and displaying version information across repositories.
3. Incrementing repository versions safely with error handling.

"""

import stonegarden
from stonegarden.exceptions import StonegardenError

def main():
    try:
        # Initialize Stonegarden with configuration for managing repositories
        manager = stonegarden.ProjectManager(config_file="stonegarden_config.yml")

        # Fetch all repositories managed by Stonegarden
        repositories = manager.get_repositories()

        # Display current version information for each repository
        print("Current versions of repositories:")
        for repo in repositories:
            print(f"{repo.name}: {repo.get_version()}")

        # Example: Increment the version for each repository
        print("\nIncrementing versions...")
        for repo in repositories:
            try:
                # Increment the version (e.g., patch update)
                repo.increment_version(part="patch")
                print(f"Updated {repo.name} to version {repo.get_version()}")
            except StonegardenError as e:
                # Handle version increment errors
                print(f"Failed to update version for {repo.name}: {e}")

        # Save the updated versions back to the configuration
        manager.save()

        print("\nVersion update completed successfully.")
    except StonegardenError as e:
        # Handle general Stonegarden errors
        print(f"Error managing project versions: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
