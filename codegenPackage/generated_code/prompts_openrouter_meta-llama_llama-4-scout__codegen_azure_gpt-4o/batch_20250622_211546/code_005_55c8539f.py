"""
Generated Code Metadata:
========================
Original URL: https://readyplayai.com
Prompt: "What are some best practices for implementing dynamic, hierarchical quotas and fair-share scheduling with Run:AI, and provide an example code snippet for it."
Generated: DETERMINISTIC_55c8539f41570994
Batch ID: 20250622_211546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates best practices for implementing dynamic, hierarchical quotas 
and fair-share scheduling using Run:AI. It uses the Run:AI Python SDK to manage 
resource quotas and scheduling policies dynamically.

Prerequisites:
- Install the Run:AI Python SDK (`pip install runai-sdk`)
- Ensure proper authentication and access to the Run:AI cluster
"""

import runai.sdk as runai
import logging

# Configure logging for better visibility
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_or_update_quota(project_name, quota_limit, parent_project=None):
    """
    Create or update a quota for a project.
    
    Args:
        project_name (str): Name of the project.
        quota_limit (int): GPU quota limit for the project.
        parent_project (str, optional): Name of the parent project for hierarchical quotas.
    """
    try:
        # Check if the project already exists
        project = runai.Project.get(project_name)
        if project:
            logging.info(f"Project '{project_name}' already exists. Updating quota...")
            project.update_quota(quota_limit)
        else:
            logging.info(f"Creating new project '{project_name}' with quota {quota_limit}...")
            runai.Project.create(name=project_name, quota=quota_limit, parent=parent_project)
        logging.info(f"Quota successfully set for project '{project_name}'.")
    except Exception as e:
        logging.error(f"Failed to create or update quota for project '{project_name}': {e}")

def set_fair_share_scheduling(project_name, fair_share_ratio):
    """
    Set fair-share scheduling for a project.
    
    Args:
        project_name (str): Name of the project.
        fair_share_ratio (float): Fair-share ratio (e.g., 0.5 for 50%).
    """
    try:
        project = runai.Project.get(project_name)
        if not project:
            raise ValueError(f"Project '{project_name}' does not exist.")
        
        logging.info(f"Setting fair-share scheduling for project '{project_name}'...")
        project.set_scheduling_policy(fair_share_ratio=fair_share_ratio)
        logging.info(f"Fair-share scheduling successfully set for project '{project_name}'.")
    except Exception as e:
        logging.error(f"Failed to set fair-share scheduling for project '{project_name}': {e}")

def main():
    """
    Main function to demonstrate dynamic quota and fair-share scheduling.
    """
    # Example configuration
    projects = [
        {"name": "team-a", "quota": 4, "parent": None, "fair_share": 0.6},
        {"name": "team-b", "quota": 2, "parent": "team-a", "fair_share": 0.4},
    ]

    for project in projects:
        create_or_update_quota(
            project_name=project["name"],
            quota_limit=project["quota"],
            parent_project=project["parent"]
        )
        set_fair_share_scheduling(
            project_name=project["name"],
            fair_share_ratio=project["fair_share"]
        )

if __name__ == "__main__":
    main()
```
