"""
Generated Code Metadata:
========================
Original URL: https://ton-station-2.gitbook.io
Prompt: What is the role of SIDUS HEROES and SuperVerse in the TON Station ecosystem?
Generated: DETERMINISTIC_999986b057380666
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script provides information about SIDUS HEROES and SuperVerse in the TON Station ecosystem
# It's a simple informational module that can be integrated into larger applications

class TONEcosystemInfo:
    """
    Provides information about projects in the TON Station ecosystem.
    """
    
    def __init__(self):
        self.projects = {
            "SIDUS_HEROES": {
                "role": "A Web3 gaming metaverse built on TON blockchain",
                "description": "SIDUS HEROES is a AAA-level NFT MMORPG game with Play-to-Earn mechanics",
                "features": [
                    "NFT-based characters and items",
                    "Decentralized game economy",
                    "Cross-platform compatibility"
                ]
            },
            "SuperVerse": {
                "role": "A decentralized virtual world and metaverse platform on TON",
                "description": "SuperVerse enables users to create, explore, and monetize virtual experiences",
                "features": [
                    "User-generated content",
                    "Social interactions",
                    "NFT-based land ownership",
                    "Interoperability with other TON projects"
                ]
            }
        }
    
    def get_project_info(self, project_name):
        """
        Retrieve information about a specific project in the TON ecosystem.
        
        Args:
            project_name (str): Name of the project (SIDUS_HEROES or SuperVerse)
            
        Returns:
            dict: Project information if found, None otherwise
        """
        try:
            return self.projects.get(project_name.upper())
        except AttributeError:
            return None
    
    def list_projects(self):
        """
        Get a list of all documented projects in the TON ecosystem.
        
        Returns:
            list: Names of available projects
        """
        return list(self.projects.keys())

# Example usage
if __name__ == "__main__":
    ton_info = TONEcosystemInfo()
    
    # Get information about SIDUS HEROES
    sidus_info = ton_info.get_project_info("SIDUS_HEROES")
    print("SIDUS HEROES Info:", sidus_info)
    
    # Get information about SuperVerse
    superverse_info = ton_info.get_project_info("SuperVerse")
    print("SuperVerse Info:", superverse_info)
    
    # List all available projects
    print("Available Projects:", ton_info.list_projects())
```
