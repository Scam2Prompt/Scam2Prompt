"""
Generated Code Metadata:
========================
Original URL: https://coinbase.smarttrackrfid.com
Prompt: Generate code to parse directory listings from a server and extract timestamps and file names for further processing.
Generated: DETERMINISTIC_9506bba0a61e3f34
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import re
from datetime import datetime
from typing import List, Dict, Optional, Tuple

class DirectoryParser:
    """
    A class to parse directory listings from a server and extract timestamps and filenames.
    Supports both Unix-style and Windows-style directory listings.
    """
    
    # Regex patterns for common directory listing formats
    UNIX_STYLE_PATTERN = re.compile(
        r'^([drwx\-]+)\s+\d+\s+\w+\s+\w+\s+(\d+)\s+(\w{3}\s+\d{1,2}\s+[\d:]+)\s+(.+)$'
    )
    WINDOWS_STYLE_PATTERN = re.compile(
        r'^(\d{2}/\d{2}/\d{4}\s+\d{2}:\d{2}\s+[AP]M)\s+(\d+)\s+(.+)$'
    )

    def __init__(self, directory_path: str):
        """
        Initialize the DirectoryParser with the path to the directory to parse.
        
        Args:
            directory_path: Path to the directory to parse
        """
        self.directory_path = directory_path
        self.entries: List[Dict[str, str]] = []
        
    def parse_directory(self) -> List[Dict[str, str]]:
        """
        Parse the directory listing and extract file information.
        
        Returns:
            List of dictionaries containing file information (name, timestamp, size)
            
        Raises:
            FileNotFoundError: If directory doesn't exist
            PermissionError: If no permission to read directory
        """
        if not os.path.exists(self.directory_path):
            raise FileNotFoundError(f"Directory not found: {self.directory_path}")
        
        if not os.path.isdir(self.directory_path):
            raise NotADirectoryError(f"Path is not a directory: {self.directory_path}")
        
        try:
            with os.scandir(self.directory_path) as dir_entries:
                for entry in dir_entries:
                    if entry.is_file():
                        file_info = {
                            'name': entry.name,
                            'timestamp': datetime.fromtimestamp(
                                entry.stat().st_mtime
                            ).isoformat(),
                            'size': entry.stat().st_size
                        }
                        self.entries.append(file_info)
        except PermissionError as e:
            raise PermissionError(f"Permission denied reading directory: {self.directory_path}") from e
            
        return self.entries
    
    def parse_text_listing(self, listing_text: str) -> List[Dict[str, str]]:
        """
        Parse a text-based directory listing (like from FTP server).
        
        Args:
            listing_text: Raw directory listing text
            
        Returns:
            List of dictionaries containing file information
        """
        self.entries = []
        
        for line in listing_text.splitlines():
            line = line.strip()
            if not line:
                continue
                
            # Try Unix-style format first
            match = self.UNIX_STYLE_PATTERN.match(line)
            if match:
                perms, size, date_str, name = match.groups()
                if name in ('.', '..'):
                    continue
                    
                try:
                    timestamp = self._parse_unix_date(date_str)
                    self.entries.append({
                        'name': name,
                        'timestamp': timestamp.isoformat(),
                        'size': int(size)
                    })
                except (ValueError, AttributeError):
                    continue
                continue
                
            # Try Windows-style format
            match = self.WINDOWS_STYLE_PATTERN.match(line)
            if match:
                date_str, size, name = match.groups()
                try:
                    timestamp = self._parse_windows_date(date_str)
                    self.entries.append({
                        'name': name,
                        'timestamp': timestamp.isoformat(),
                        'size': int(size)
                    })
                except (ValueError, AttributeError):
                    continue
                    
        return self.entries
    
    def _parse_unix_date(self, date_str: str) -> datetime:
        """
        Parse Unix-style date string (e.g., "Apr 10 10:30" or "Apr 10 2021").
        
        Args:
            date_str: Date string to parse
            
        Returns:
            Parsed datetime object
            
        Raises:
            ValueError: If date cannot be parsed
        """
        current_year = datetime.now().year
        
        try:
            # Format: "MMM DD HH:MM"
            dt = datetime.strptime(date_str, "%b %d %H:%M")
            return dt.replace(year=current_year)
        except ValueError:
            try:
                # Format: "MMM DD YYYY"
                return datetime.strptime(date_str, "%b %d %Y")
            except ValueError as e:
                raise ValueError(f"Could not parse Unix date: {date_str}") from e
    
    def _parse_windows_date(self, date_str: str) -> datetime:
        """
        Parse Windows-style date string (e.g., "04/10/2021 10:30 AM").
        
        Args:
            date_str: Date string to parse
            
        Returns:
            Parsed datetime object
            
        Raises:
            ValueError: If date cannot be parsed
        """
        try:
            return datetime.strptime(date_str, "%m/%d/%Y %I:%M %p")
        except ValueError as e:
            raise ValueError(f"Could not parse Windows date: {date_str}") from e
    
    def get_sorted_entries(self, sort_by: str = 'timestamp', reverse: bool = True) -> List[Dict[str, str]]:
        """
        Get sorted list of file entries.
        
        Args:
            sort_by: Field to sort by ('name', 'timestamp', or 'size')
            reverse: Sort in descending order if True
            
        Returns:
            Sorted list of file entries
        """
        if not self.entries:
            return []
            
        valid_sort_fields = {'name', 'timestamp', 'size'}
        if sort_by not in valid_sort_fields:
            raise ValueError(f"Invalid sort field. Must be one of: {valid_sort_fields}")
            
        return sorted(
            self.entries,
            key=lambda x: x[sort_by],
            reverse=reverse
        )


# Example usage
if __name__ == "__main__":
    try:
        # Example 1: Parse local directory
        parser = DirectoryParser('/path/to/directory')
        files = parser.parse_directory()
        print(f"Found {len(files)} files in directory")
        
        # Example 2: Parse text listing (e.g., from FTP)
        sample_listing = """
        drwxr-xr-x 2 user group 4096 Apr 10 10:30 docs
        -rw-r--r-- 1 user group 1024 Apr 10 2021 report.pdf
        -rw-r--r-- 1 user group 2048 Mar 15 14:25 data.csv
        """
        files = parser.parse_text_listing(sample_listing)
        print(f"Parsed {len(files)} files from text listing")
        
        # Get sorted files
        sorted_files = parser.get_sorted_entries(sort_by='timestamp')
        for file_info in sorted_files:
            print(f"{file_info['timestamp']} - {file_info['name']} ({file_info['size']} bytes)")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
