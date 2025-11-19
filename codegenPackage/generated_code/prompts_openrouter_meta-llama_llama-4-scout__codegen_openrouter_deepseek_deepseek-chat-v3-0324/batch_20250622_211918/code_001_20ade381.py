"""
Generated Code Metadata:
========================
Original URL: https://support-en-metamask-cdn.groovehq.com
Prompt: Write a code snippet to implement an automated issue logging system similar to the one described on the MetaMask support page.
Generated: DETERMINISTIC_20ade3814e636c54
Batch ID: 20250622_211918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from datetime import datetime
from typing import Dict, Optional, List
import json
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class IssueLogger:
    """
    Automated issue logging system to track and manage reported issues.
    """
    
    def __init__(self, storage_path: str = "issues.json"):
        """
        Initialize the IssueLogger with a storage file path.
        
        Args:
            storage_path (str): Path to the JSON file where issues will be stored.
                               Defaults to "issues.json".
        """
        self.storage_path = storage_path
        self.issues: List[Dict] = []
        self._load_issues()
    
    def _load_issues(self) -> None:
        """
        Load existing issues from the storage file.
        Creates the file if it doesn't exist.
        """
        try:
            if os.path.exists(self.storage_path):
                with open(self.storage_path, 'r') as f:
                    self.issues = json.load(f)
            else:
                self.issues = []
                self._save_issues()
        except Exception as e:
            logger.error(f"Failed to load issues: {e}")
            self.issues = []
    
    def _save_issues(self) -> None:
        """
        Save current issues to the storage file.
        """
        try:
            with open(self.storage_path, 'w') as f:
                json.dump(self.issues, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save issues: {e}")
    
    def log_issue(
        self,
        title: str,
        description: str,
        reporter: str,
        priority: str = "medium",
        labels: Optional[List[str]] = None
    ) -> Dict:
        """
        Log a new issue with the given details.
        
        Args:
            title (str): Short title describing the issue.
            description (str): Detailed description of the issue.
            reporter (str): Identifier for who reported the issue.
            priority (str): Priority level ("low", "medium", "high").
                           Defaults to "medium".
            labels (List[str]): Optional list of labels/tags for the issue.
        
        Returns:
            Dict: The created issue record.
        """
        if labels is None:
            labels = []
        
        if priority not in ["low", "medium", "high"]:
            priority = "medium"
            logger.warning(f"Invalid priority '{priority}', defaulting to 'medium'")
        
        issue = {
            "id": len(self.issues) + 1,
            "title": title,
            "description": description,
            "reporter": reporter,
            "priority": priority,
            "labels": labels,
            "status": "open",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        
        self.issues.append(issue)
        self._save_issues()
        logger.info(f"Logged new issue: {issue['id']} - {issue['title']}")
        return issue
    
    def update_issue_status(self, issue_id: int, status: str) -> Optional[Dict]:
        """
        Update the status of an existing issue.
        
        Args:
            issue_id (int): ID of the issue to update.
            status (str): New status ("open", "in_progress", "resolved", "closed").
        
        Returns:
            Optional[Dict]: Updated issue record if found, None otherwise.
        """
        for issue in self.issues:
            if issue["id"] == issue_id:
                issue["status"] = status
                issue["updated_at"] = datetime.now().isoformat()
                self._save_issues()
                logger.info(f"Updated issue {issue_id} status to {status}")
                return issue
        logger.warning(f"Issue {issue_id} not found")
        return None
    
    def get_issues(
        self,
        status: Optional[str] = None,
        priority: Optional[str] = None,
        label: Optional[str] = None
    ) -> List[Dict]:
        """
        Get filtered list of issues based on criteria.
        
        Args:
            status (str): Filter by status.
            priority (str): Filter by priority.
            label (str): Filter by label.
        
        Returns:
            List[Dict]: List of matching issues.
        """
        filtered = self.issues
        
        if status:
            filtered = [i for i in filtered if i["status"] == status]
        if priority:
            filtered = [i for i in filtered if i["priority"] == priority]
        if label:
            filtered = [i for i in filtered if label in i["labels"]]
        
        return filtered

# Example usage
if __name__ == "__main__":
    logger = IssueLogger()
    
    # Log some example issues
    logger.log_issue(
        title="Connection Error",
        description="Unable to connect to the network",
        reporter="user123",
        priority="high",
        labels=["network", "bug"]
    )
    
    logger.log_issue(
        title="UI Glitch",
        description="Buttons overlap on mobile view",
        reporter="user456",
        priority="medium",
        labels=["ui", "mobile"]
    )
    
    # Update an issue status
    logger.update_issue_status(1, "in_progress")
    
    # Get open issues
    open_issues = logger.get_issues(status="open")
    print(f"Open issues: {len(open_issues)}")
```
