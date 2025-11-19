"""
Generated Code Metadata:
========================
Original URL: https://app.ebookzone.club
Prompt: Write code to extract metadata (e.g., title, author) from ePub and FB2 files, referencing the formats supported by the webpage.
Generated: DETERMINISTIC_431dc9d2f782bd0c
Batch ID: 20250612_145245
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "http://purl.org/dc/elements/1.1/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://www.idpf.org/2007/opf": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://www.gribuser.ru/xml/fictionbook/2.0": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import os
import zipfile
import xml.etree.ElementTree as ET
from typing import Dict, Optional

def extract_epub_metadata(file_path: str) -> Optional[Dict[str, str]]:
    """
    Extract metadata from an EPUB file.
    
    Args:
        file_path: Path to the EPUB file.
    
    Returns:
        Dictionary containing metadata (title, author, etc.) or None if extraction fails.
    """
    if not os.path.isfile(file_path):
        return None

    try:
        with zipfile.ZipFile(file_path, 'r') as epub:
            # Find the container file to locate the OPF file
            with epub.open('META-INF/container.xml') as container_file:
                container = ET.parse(container_file)
                rootfile = container.find('.//{*}rootfile')
                if rootfile is None:
                    return None
                opf_path = rootfile.attrib['full-path']

            # Parse the OPF file for metadata
            with epub.open(opf_path) as opf_file:
                opf = ET.parse(opf_file)
                ns = {
                    'dc': 'http://purl.org/dc/elements/1.1/',
                    'opf': 'http://www.idpf.org/2007/opf'
                }
                
                metadata = {}
                title = opf.find('.//dc:title', ns)
                if title is not None:
                    metadata['title'] = title.text
                
                creator = opf.find('.//dc:creator', ns)
                if creator is not None:
                    metadata['author'] = creator.text
                
                return metadata if metadata else None

    except (zipfile.BadZipFile, ET.ParseError, KeyError):
        return None

def extract_fb2_metadata(file_path: str) -> Optional[Dict[str, str]]:
    """
    Extract metadata from an FB2 file.
    
    Args:
        file_path: Path to the FB2 file.
    
    Returns:
        Dictionary containing metadata (title, author, etc.) or None if extraction fails.
    """
    if not os.path.isfile(file_path):
        return None

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        # FB2 namespace
        ns = {'fb2': 'http://www.gribuser.ru/xml/fictionbook/2.0'}
        
        metadata = {}
        
        # Title
        title_info = root.find('.//fb2:title-info', ns)
        if title_info is not None:
            title = title_info.find('fb2:book-title', ns)
            if title is not None:
                metadata['title'] = title.text
            
            # Author
            author = title_info.find('fb2:author', ns)
            if author is not None:
                first_name = author.find('fb2:first-name', ns)
                last_name = author.find('fb2:last-name', ns)
                author_name = ''
                if first_name is not None:
                    author_name += first_name.text
                if last_name is not None:
                    if author_name:
                        author_name += ' '
                    author_name += last_name.text
                if author_name:
                    metadata['author'] = author_name
        
        return metadata if metadata else None

    except ET.ParseError:
        return None

def extract_ebook_metadata(file_path: str) -> Optional[Dict[str, str]]:
    """
    Extract metadata from an ebook file (EPUB or FB2).
    
    Args:
        file_path: Path to the ebook file.
    
    Returns:
        Dictionary containing metadata or None if extraction fails.
    """
    if not os.path.isfile(file_path):
        return None

    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == '.epub':
        return extract_epub_metadata(file_path)
    elif ext == '.fb2':
        return extract_fb2_metadata(file_path)
    else:
        return None
```
