"""
Generated Code Metadata:
========================
Original URL: https://consultorialicitare.com.br
Prompt: Write a Python script that automates the preparation of documents for public bidding processes, incorporating best practices from Licitare's licitation services.
Generated: DETERMINISTIC_333032558e10250e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
import datetime
import json
from typing import Dict, List, Optional
from pathlib import Path

class BiddingDocumentPreparer:
    """
    A class to automate the preparation of documents for public bidding processes.
    Incorporates best practices from Licitare's licitation services.
    """

    def __init__(self, config_path: str = "config.json"):
        """
        Initialize the document preparer with configuration.

        Args:
            config_path (str): Path to the configuration file. Defaults to "config.json".
        """
        self.config = self._load_config(config_path)
        self.template_dir = Path(self.config.get("template_dir", "templates"))
        self.output_dir = Path(self.config.get("output_dir", "output"))
        self.required_documents = self.config.get("required_documents", [])
        self._validate_config()

    def _load_config(self, config_path: str) -> Dict:
        """
        Load configuration from JSON file.

        Args:
            config_path (str): Path to the configuration file.

        Returns:
            Dict: Configuration dictionary.

        Raises:
            FileNotFoundError: If config file doesn't exist.
            json.JSONDecodeError: If config file is invalid JSON.
        """
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found at {config_path}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in configuration file: {e.msg}", e.doc, e.pos)

    def _validate_config(self) -> None:
        """
        Validate the configuration.

        Raises:
            ValueError: If required configuration is missing or invalid.
        """
        if not self.template_dir.exists():
            raise ValueError(f"Template directory not found: {self.template_dir}")
        if not self.required_documents:
            raise ValueError("No required documents specified in configuration")
        
        # Check all required templates exist
        for doc in self.required_documents:
            template_path = self.template_dir / f"{doc}.docx"
            if not template_path.exists():
                raise ValueError(f"Template for {doc} not found at {template_path}")

    def prepare_documents(self, project_name: str, project_data: Dict) -> Path:
        """
        Prepare all required bidding documents for a project.

        Args:
            project_name (str): Name of the project.
            project_data (Dict): Data to populate in the documents.

        Returns:
            Path: Path to the output directory with prepared documents.

        Raises:
            ValueError: If project name is empty or project data is invalid.
        """
        if not project_name.strip():
            raise ValueError("Project name cannot be empty")
        
        if not isinstance(project_data, dict):
            raise ValueError("Project data must be a dictionary")

        # Create output directory with timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        project_dir = self.output_dir / f"{project_name}_{timestamp}"
        project_dir.mkdir(parents=True, exist_ok=True)

        # Prepare each document
        for doc in self.required_documents:
            self._prepare_document(doc, project_dir, project_name, project_data)

        return project_dir

    def _prepare_document(self, doc_name: str, project_dir: Path, project_name: str, project_data: Dict) -> None:
        """
        Prepare a single document by copying template and populating placeholders.

        Args:
            doc_name (str): Name of the document to prepare.
            project_dir (Path): Directory to save the prepared document.
            project_name (str): Name of the project.
            project_data (Dict): Data to populate in the document.
        """
        template_path = self.template_dir / f"{doc_name}.docx"
        output_path = project_dir / f"{project_name}_{doc_name}.docx"

        # Copy template to output location
        shutil.copy(template_path, output_path)

        # In a real implementation, we would use python-docx or similar to:
        # 1. Open the document
        # 2. Replace placeholders with project_data
        # 3. Save the modified document
        # This is simplified for demonstration purposes
        print(f"Prepared document: {output_path}")

    def cleanup(self, days_old: int = 30) -> None:
        """
        Clean up old output directories older than specified days.

        Args:
            days_old (int): Number of days to keep outputs. Defaults to 30.
        """
        cutoff_time = datetime.datetime.now() - datetime.timedelta(days=days_old)
        
        for item in self.output_dir.iterdir():
            if item.is_dir():
                # Extract timestamp from directory name
                try:
                    dir_time_str = item.name.split('_')[-1]
                    dir_time = datetime.datetime.strptime(dir_time_str, "%Y%m%d_%H%M%S")
                    
                    if dir_time < cutoff_time:
                        shutil.rmtree(item)
                        print(f"Removed old directory: {item}")
                except (ValueError, IndexError):
                    # Skip directories that don't match our naming pattern
                    continue

def main():
    try:
        # Example usage
        preparer = BiddingDocumentPreparer()
        
        project_data = {
            "project_title": "New City Bridge Construction",
            "project_id": "NCB-2023-001",
            "client_name": "City Municipal Government",
            "budget": "5,000,000 USD",
            "deadline": "2023-12-31"
        }
        
        output_dir = preparer.prepare_documents("NewCityBridge", project_data)
        print(f"Documents prepared in: {output_dir}")
        
        # Optional: Clean up old directories
        preparer.cleanup()
        
    except Exception as e:
        print(f"Error preparing documents: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
```
