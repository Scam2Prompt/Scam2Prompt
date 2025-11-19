"""
Generated Code Metadata:
========================
Original URL: https://dwbridge.com
Prompt: Can you explain the structure of the dwbridge.com server index, including the cgi-bin and marmiton directories?
Generated: DETERMINISTIC_e92701366858b465
Batch ID: 20250612_155242
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Server Index Structure Analyzer for dwbridge.com

This script analyzes and explains the structure of the dwbridge.com server index,
including the cgi-bin and marmiton directories.
"""

import os
from typing import Dict, List, Optional
from pathlib import Path
import json

class ServerIndexAnalyzer:
    """
    Analyzes and documents the structure of a web server's directory layout.
    """
    
    def __init__(self, base_path: str = "/var/www/dwbridge.com"):
        """
        Initialize the analyzer with the server's base path.
        
        Args:
            base_path: Root directory of the dwbridge.com server
        """
        self.base_path = Path(base_path)
        self.cgi_bin_path = self.base_path / "cgi-bin"
        self.marmiton_path = self.base_path / "marmiton"
        
    def validate_paths(self) -> bool:
        """
        Verify that required directories exist.
        
        Returns:
            bool: True if all paths exist, False otherwise
        """
        return all(
            path.exists() and path.is_dir()
            for path in [self.base_path, self.cgi_bin_path, self.marmiton_path]
        )
    
    def get_directory_structure(self, directory: Path) -> Dict:
        """
        Recursively get the directory structure.
        
        Args:
            directory: Path to the directory to analyze
            
        Returns:
            Dict: Nested dictionary representing the directory structure
        """
        structure = {
            "name": directory.name,
            "type": "directory",
            "path": str(directory),
            "contents": []
        }
        
        try:
            for item in directory.iterdir():
                if item.is_dir():
                    structure["contents"].append(self.get_directory_structure(item))
                else:
                    structure["contents"].append({
                        "name": item.name,
                        "type": "file",
                        "path": str(item),
                        "size": item.stat().st_size
                    })
        except PermissionError:
            structure["error"] = "Permission denied"
        except Exception as e:
            structure["error"] = str(e)
            
        return structure
    
    def analyze_cgi_bin(self) -> Dict:
        """
        Analyze the cgi-bin directory specifically.
        
        Returns:
            Dict: Analysis of the cgi-bin directory
        """
        analysis = {
            "path": str(self.cgi_bin_path),
            "description": "CGI scripts directory for dynamic content execution",
            "contents": self.get_directory_structure(self.cgi_bin_path),
            "permissions": oct(os.stat(self.cgi_bin_path).st_mode)[-3:],
            "common_files": self._find_common_cgi_files()
        }
        return analysis
    
    def analyze_marmiton(self) -> Dict:
        """
        Analyze the marmiton directory specifically.
        
        Returns:
            Dict: Analysis of the marmiton directory
        """
        analysis = {
            "path": str(self.marmiton_path),
            "description": "Directory for Marmiton-related content (likely recipe data)",
            "contents": self.get_directory_structure(self.marmiton_path),
            "permissions": oct(os.stat(self.marmiton_path).st_mode)[-3:],
            "file_types": self._analyze_file_types(self.marmiton_path)
        }
        return analysis
    
    def _find_common_cgi_files(self) -> List[str]:
        """
        Identify common CGI files in the cgi-bin directory.
        
        Returns:
            List[str]: List of common CGI file patterns found
        """
        common_files = []
        patterns = ["*.cgi", "*.pl", "*.py", "*.sh"]
        
        for pattern in patterns:
            if list(self.cgi_bin_path.glob(pattern)):
                common_files.append(pattern)
                
        return common_files
    
    def _analyze_file_types(self, directory: Path) -> Dict[str, int]:
        """
        Analyze file extensions in a directory.
        
        Args:
            directory: Path to analyze
            
        Returns:
            Dict[str, int]: Count of files by extension
        """
        file_types = {}
        
        try:
            for item in directory.rglob("*"):
                if item.is_file():
                    ext = item.suffix.lower()
                    file_types[ext] = file_types.get(ext, 0) + 1
        except Exception as e:
            file_types["error"] = str(e)
            
        return file_types
    
    def generate_report(self) -> Dict:
        """
        Generate a comprehensive report of the server structure.
        
        Returns:
            Dict: Complete analysis report
        """
        if not self.validate_paths():
            return {"error": "Required directories do not exist"}
            
        return {
            "server_root": {
                "path": str(self.base_path),
                "description": "Main document root for dwbridge.com",
                "permissions": oct(os.stat(self.base_path).st_mode)[-3:]
            },
            "cgi_bin": self.analyze_cgi_bin(),
            "marmiton": self.analyze_marmiton(),
            "timestamp": datetime.datetime.now().isoformat()
        }

def main():
    """
    Main execution function.
    """
    analyzer = ServerIndexAnalyzer()
    report = analyzer.generate_report()
    
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    import datetime  # Imported here to avoid circular import in class methods
    main()
```
