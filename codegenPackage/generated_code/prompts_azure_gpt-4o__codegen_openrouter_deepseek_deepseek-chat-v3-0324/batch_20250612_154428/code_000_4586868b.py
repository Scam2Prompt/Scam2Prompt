"""
Generated Code Metadata:
========================
Original URL: https://confinance.info
Prompt: Write Python code using Jupyter Book to create a structured conservation finance guide with chapters on fire, water, barriers, and roadmaps, similar to the structure described on https://confinance.info.
Generated: DETERMINISTIC_4586868b3b8b2fbd
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
from pathlib import Path
import yaml
from myst_parser.main import to_html

# Define the structure of the Jupyter Book
def create_jupyter_book_structure(base_dir="conservation_finance_guide"):
    """
    Creates the directory structure and configuration files for a Jupyter Book.
    
    Args:
        base_dir (str): The base directory for the Jupyter Book.
    """
    # Create base directory
    Path(base_dir).mkdir(exist_ok=True)
    
    # Create _config.yml
    config = {
        "title": "Conservation Finance Guide",
        "author": "Conservation Finance Team",
        "execute": {
            "execute_notebooks": "auto",
            "timeout": 600
        },
        "html": {
            "use_issues_button": False,
            "use_repository_button": False,
            "use_edit_page_button": False
        }
    }
    
    with open(Path(base_dir) / "_config.yml", "w") as f:
        yaml.dump(config, f)
    
    # Create _toc.yml
    toc = {
        "format": "jb-book",
        "root": "intro.md",
        "chapters": [
            {
                "file": "fire/index",
                "sections": [
                    {"file": "fire/overview"},
                    {"file": "fire/financing_mechanisms"},
                    {"file": "fire/case_studies"}
                ]
            },
            {
                "file": "water/index",
                "sections": [
                    {"file": "water/overview"},
                    {"file": "water/financing_mechanisms"},
                    {"file": "water/case_studies"}
                ]
            },
            {
                "file": "barriers/index",
                "sections": [
                    {"file": "barriers/overview"},
                    {"file": "barriers/policy"},
                    {"file": "barriers/economic"}
                ]
            },
            {
                "file": "roadmaps/index",
                "sections": [
                    {"file": "roadmaps/implementation"},
                    {"file": "roadmaps/funding_strategies"},
                    {"file": "roadmaps/future_directions"}
                ]
            }
        ]
    }
    
    with open(Path(base_dir) / "_toc.yml", "w") as f:
        yaml.dump(toc, f)
    
    # Create content files
    content_files = {
        "intro.md": "# Conservation Finance Guide\n\nWelcome to the Conservation Finance Guide.",
        "fire/index.md": "# Fire Conservation Finance\n\nIntroduction to fire-related conservation finance.",
        "fire/overview.md": "## Overview\n\nOverview of fire conservation finance.",
        "fire/financing_mechanisms.md": "## Financing Mechanisms\n\nAvailable financing mechanisms for fire conservation.",
        "fire/case_studies.md": "## Case Studies\n\nReal-world examples of fire conservation finance.",
        "water/index.md": "# Water Conservation Finance\n\nIntroduction to water-related conservation finance.",
        "water/overview.md": "## Overview\n\nOverview of water conservation finance.",
        "water/financing_mechanisms.md": "## Financing Mechanisms\n\nAvailable financing mechanisms for water conservation.",
        "water/case_studies.md": "## Case Studies\n\nReal-world examples of water conservation finance.",
        "barriers/index.md": "# Barriers in Conservation Finance\n\nIntroduction to barriers in conservation finance.",
        "barriers/overview.md": "## Overview\n\nOverview of barriers in conservation finance.",
        "barriers/policy.md": "## Policy Barriers\n\nPolicy-related barriers in conservation finance.",
        "barriers/economic.md": "## Economic Barriers\n\nEconomic barriers in conservation finance.",
        "roadmaps/index.md": "# Roadmaps for Conservation Finance\n\nIntroduction to roadmaps for conservation finance.",
        "roadmaps/implementation.md": "## Implementation Roadmaps\n\nRoadmaps for implementing conservation finance strategies.",
        "roadmaps/funding_strategies.md": "## Funding Strategies\n\nStrategies for funding conservation projects.",
        "roadmaps/future_directions.md": "## Future Directions\n\nFuture trends and directions in conservation finance."
    }
    
    # Create directories and files
    for file_path, content in content_files.items():
        full_path = Path(base_dir) / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        with open(full_path, "w") as f:
            f.write(content)
    
    print(f"Jupyter Book structure created in '{base_dir}'")

# Main execution
if __name__ == "__main__":
    try:
        create_jupyter_book_structure()
    except Exception as e:
        print(f"Error creating Jupyter Book structure: {e}")
```
